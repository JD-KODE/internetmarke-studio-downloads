# Internetmarke Studio 0.19.0

Kostenlose Windows-App für JTL-CSV und Internetmarken-Kauf ohne CSV. Porto kostenpflichtig, Spenden freiwillig.

[Download](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest) · [Einrichtung](INSTALLATION.md) · [Bedienung](BETA-ANLEITUNG.md)

# Internetmarke Studio 0.19.0 – öffentliche Beta

## Updateablauf
Das Setup prüft vor dem Ersetzen von Dateien, ob die App noch läuft. Ab 0.19.0 fordert es die App zum sicheren Beenden auf; ein laufender Vorgang wird abgeschlossen. Anschließend im Setup erneut Weiter wählen. Ältere Versionen über Rechtsklick auf das Symbol neben der Windows-Uhr → Beenden schließen. Keine erzwungene Prozessbeendigung. Updates aus der App schalten die Automatik aus und verwenden denselben geordneten Abschluss.

## Aufbewahrung
Unter Weitere Aktionen → Datenschutz & Diagnose → Aufbewahrung und Löschfristen. Auch im letzten Einrichtungsschritt verfügbar.

Vier getrennte Optionen: importierte CSV-Dateien; Namen/Adressen in der App; Markendateien/frühere Versuche; alte automatische Sicherungen. Ohne Haken keine Löschung dieser Kategorie. Beim Einschalten sind 30 Tage vorgeschlagen; einstellbar 0–3650 Tage (Sicherungen mindestens 1). Beim Speichern wird die automatische, nicht rückgängig zu machende Löschung ausdrücklich bestätigt. Die bisherigen 30-Tage-Aufräumsicherungen werden durch die gespeicherten neuen Regeln ersetzt, auch wenn alle Optionen ausgeschaltet sind. Ohne gespeicherte neue Regeln bleibt das bisherige Verhalten bestehen.

Vorher mit „Vorschau – nichts löschen“ die aktuell fälligen Mengen prüfen. Bereits fällige Daten werden nach Aktivierung beim nächsten Lauf gelöscht. Bereinigung läuft nur während die App läuft, auch im Hintergrund.

Im Archiv gekaufte Marken auswählen → Weitere Aktionen → Ausdruck geprüft – Löschfrist starten. Mehrfachauswahl möglich. Erst nach Bestätigung beginnen die Fristen für CSV, Kundendaten und Marken. 0 Tage bedeutet beim nächsten Lauf nach Bestätigung, nicht nach bloßer Übergabe an Windows. Eine nochmalige Bestätigung verschiebt die Frist nicht. Unklare oder unbestätigte Käufe bleiben geschützt. Eine CSV wird nur entfernt, wenn unverändert und alle enthaltenen Sendungen bestätigt und fällig sind.

Kundendatenbereinigung entfernt die Empfängerdaten aus dem App-Adressbestand und sendungen.csv; bereits entfernte Adressen werden durch erneuten Import nicht wieder gespeichert. Der gemeinsame Adressetikett-Entwurf wird entfernt. Quelldateien und Sicherungen haben separate Regeln.

Kaufstatus, Lieferschein, Portokassen-Zuordnung sowie Post-Kauf-/Marken-/Trackingkennungen bleiben zum Doppelkaufschutz erhalten. Das ist keine vollständige Anonymisierung. Markendateien können nach ihrer Entfernung weder nachgedruckt noch über die App erneut abgerufen werden. Der Kauf wird dadurch nicht rückgängig gemacht.

Nur Sicherungen im App-Unterordner „sicherungen“ werden nach Alter bereinigt. Extern gespeicherte manuelle Sicherungen, Exportdateien, externe CSV-Kopien und Betriebssystem-Backups selbst verwalten. Keine garantierte sichere Löschung aller Datenträgerspuren. Laufende Datenbank und Zugangsdaten werden nicht gelöscht.

## Testablauf
Zunächst separate Testdaten verwenden. Einstellungen/Vorschau öffnen, Abbrechen prüfen. Mit einer bereits verwendeten Testmarke den Ausdruck bestätigen, danach eine kurze Frist testen. Vorher erforderliche Daten sichern; externe Sicherung selbst geschützt aufbewahren. Kein erneuter Kauf zum Testen erforderlich. 

188 automatisierte Windows-Tests sowie Installation, EXE-Start, Deinstallation und Setup-Sperre bei laufender App bestanden. Keine echten Käufe oder physischen Ausdrucke im Entwicklungstest. Installer weiterhin unsigniert. Beta-Nutzung auf eigenes Risiko; gesetzliche Ansprüche bleiben unberührt. Die Beschriftung „Private Testversion“ im unveränderten geprüften Programm stammt aus der Testphase; dieses Paket ist jetzt öffentlich freigegeben.
