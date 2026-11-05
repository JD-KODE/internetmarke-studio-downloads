"""Publish two verified binary release assets. Never publish the private application sources."""
import hashlib,io,json,os,re,subprocess,urllib.request,urllib.parse,zipfile
from pathlib import Path

def gh(*args):return subprocess.run(['gh',*args],check=True,capture_output=True,text=True).stdout

def main():
    delivery=Path('delivery.json')
    if not delivery.exists():print('No pending delivery.');return
    obj=json.loads(delivery.read_text())
    version=obj['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+',version):raise ValueError('Invalid version')
    for field in ('archive_sha256','installer_sha256'):
        if not re.fullmatch(r'[a-f0-9]{64}',obj[field]):raise ValueError('Invalid checksum')
    url=urllib.parse.urlsplit(obj['download_url'])
    if url.scheme!='https' or not url.hostname.endswith('.oaiusercontent.com') or url.username or url.password:raise ValueError('Invalid delivery source')
    with urllib.request.urlopen(obj['download_url'],timeout=60) as r:data=r.read(150*1024*1024+1)
    if len(data)>150*1024*1024 or hashlib.sha256(data).hexdigest()!=obj['archive_sha256']:raise ValueError('Artifact checksum mismatch')
    name='Internetmarke-Studio-Setup-'+version+'.exe'
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        executable=archive.read(name);checksum=archive.read('SHA256.txt')
        smoke=json.loads(archive.read('studio-smoke.json'))
    if not smoke.get('ok') or smoke.get('version')!=version:raise ValueError('Build test record missing')
    if hashlib.sha256(executable).hexdigest()!=obj['installer_sha256']:raise ValueError('Installer checksum mismatch')
    if checksum.decode('utf-8-sig').strip().lower()!=obj['installer_sha256']+'  '+name.lower():raise ValueError('Release checksum mismatch')
    Path(name).write_bytes(executable);Path('SHA256.txt').write_bytes(checksum)
    Path('release-notes.txt').write_text(obj['notes'],encoding='utf-8')
    repo=os.environ['GH_REPO']
    if repo.lower()!='jd-kode/internetmarke-studio-downloads':raise ValueError('Wrong repository')
    releases=json.loads(gh('api','repos/'+repo+'/releases?per_page=100'))
    tag='v'+version;previous=next((x for x in releases if x['tag_name']==tag),None)
    if previous and not previous['draft']:raise ValueError('Release already public; never overwrite an installed version')
    if not previous:gh('release','create',tag,'--draft','--title','Internetmarke Studio '+version,'--notes-file','release-notes.txt')
    gh('release','upload',tag,name,'SHA256.txt','--clobber')
    assets=json.loads(gh('release','view',tag,'--json','assets'))['assets']
    if {a['name'] for a in assets}!={name,'SHA256.txt'}:raise ValueError('Unexpected release assets; draft retained')
    for a in assets:
        if a['size']!=Path(a['name']).stat().st_size:raise ValueError('Uploaded size mismatch')
    gh('release','edit',tag,'--draft=false','--latest')
    print('Published '+tag)

if __name__=='__main__':main()
