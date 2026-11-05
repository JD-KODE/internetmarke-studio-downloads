# [Beta, kostenlos] Internetmarke Studio – JTL-CSV einlesen, Internetmarken kaufen und drucken

Hallo zusammen,

ich möchte euch Internetmarke Studio vorstellen: eine kostenlose Windows-App, die passend formatierte CSV-Exporte aus JTL einliest und einzelne Internetmarken über die eigene Deutsche-Post-Portokasse kauft und druckt. Ich suche Rückmeldungen von freiwilligen Beta-Testern mit unterschiedlichen Druckern und Arbeitsabläufen.

**Version 0.14.0 ist eine Beta. Installation und Nutzung erfolgen auf eigenes Risiko. Bitte vorher Daten sichern und zunächst nur einen einzelnen Vorgang testen. Fehler sind möglich; eine zuverlässige Funktion in jeder Umgebung ist noch nicht zugesichert. Gesetzliche Ansprüche bleiben unberührt.**

Das ist ein unabhängiges Community-Projekt, kein offizielles Produkt von JTL oder Deutsche Post.

**Download:** https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.14.0
**Ausführliche Anleitung:** https://github.com/JD-KODE/internetmarke-studio-downloads/blob/main/INSTALLATION.md
**Beispiel-CSV:** https://github.com/JD-KODE/internetmarke-studio-downloads/blob/main/Beispiel-JTL.csv

**Was die App bietet**

- Windows-Setup mit Desktopverknüpfung; keine separate Python-Installation.
- Einrichtung mit eigenen Post-API-Zugangsdaten, optional gespeicherter Anmeldung.
- Automatisches Einlesen neuer CSV-Dateien aus einem gewählten Ordner, während die App läuft.
- Einzeln ausgelöste Käufe, verschiedene Papierformate, anpassbares Drucklayout und kostenlose neutrale Druckprobe.
- Durchsuchbares Archiv sowie erneutes Abrufen und Drucken bereits gekaufter Marken.
- Gesichertes Aufräumen erledigter Vorgänge und geeigneter CSV-Dateien nach 30 Tagen.
- Updatefunktion ab Version 0.14.0.
- Kostenlose Nutzung; freiwilliger PayPal-Spendenbutton in der App.

**Voraussetzungen und Einrichtung**

1. Windows 10/11 in x64-kompatibler Umgebung und einen installierten Windows-Druckertreiber verwenden.
2. Eigene freigeschaltete Post-API-Zugangsdaten (API Key/Secret) sowie Portokasse-Zugang bereithalten. Ein Portokasse-Konto allein genügt nicht für den API-Zugang.
3. Auf der Downloadseite unter „Assets“ die „Internetmarke-Studio-Setup-0.14.0.exe“ herunterladen, starten und installieren. Bei Updates vorher in den Einstellungen sichern und die alte App schließen.
4. Der Installer ist noch nicht digital signiert. SmartScreen kann warnen. Nur beim bewusst geprüften Download aus dem verlinkten Repository gegebenenfalls „Weitere Informationen → Trotzdem ausführen“ wählen; den Windows-Schutz nicht generell abschalten.
5. App starten, Einrichtungsassistent durchlaufen, Post-Zugang eintragen und Verbindung prüfen. Die Verbindungskontrolle kauft keine Marke.
6. Einen eigenen CSV-Austauschordner anlegen und „Exportordner wählen“ verwenden. Die App prüft ihn etwa alle fünf Sekunden, solange sie läuft.
7. Unter „Drucklayout“ Drucker, Papierformat und Ausrichtung festlegen; identische Einstellungen im Windows-Treiber wählen. Zuerst eine „Neutrale Druckprobe“ ausführen.
8. Erst danach eine echte Sendung importieren und Versandart, Anschrift und Preis prüfen.

**CSV und JTL-Anbindung**

Es ist kein beliebiger JTL-Export importierbar: Der Export muss das vorgegebene Schema erzeugen. Eine automatische Spaltenzuordnung gibt es nicht. Semikolon als Trennzeichen, Kopfzeile und diese zwölf Spalten in genau dieser Reihenfolge:

lieferschein;versandart;firma;firmenzusatz;vorname;nachname;adresszusatz;zu_haenden;strasse;plz;ort;land

Lieferscheinnummern eindeutig halten und führende Nullen in Postleitzahlen erhalten. Unterstützt werden deutsche Empfänger (DE) und Kompaktbrief, Großbrief sowie Maxibrief. Die verlinkte Beispiel-CSV enthält fiktive Daten und darf nicht für einen echten Kauf verwendet werden. Es gibt keinen direkten Zugriff auf die JTL-Datenbank.

**Achtung: echter kostenpflichtiger Kauf**

Die Software ist kostenlos, Porto ist kostenpflichtig. Ein Klick auf den Kaufbutton löst den Kauf unmittelbar aus – ohne zweite Bestätigungsabfrage. Das automatische Einlesen kauft niemals Porto. Bei aktiviertem automatischem Druck wird die Marke nach dem Kauf gedruckt.

Die App erzeugt Portoetiketten ohne Empfängeradresse. Die Anschrift muss separat auf die Sendung. Marke und Matrixcode vollständig und lesbar in Originalgröße drucken. Freie Layouts werden nicht auf postalische Gültigkeit zertifiziert; Layoutwarnungen können trotz möglicher Probleme einen Druck zulassen.

**Bei Fehlern**

Ist die Marke gekauft, aber der Download fehlgeschlagen: „Archiv → Vorhandenen Kauf abrufen“. Bei Druckproblemen zuerst die Windows-Druckwarteschlange prüfen und die vorhandene Marke erneut drucken. Nicht erneut kaufen. Bei ungeklärtem Kaufstatus Portokasse und Archiv prüfen; das Journal nicht löschen. Eine Marke darf nicht für mehrere Sendungen verwendet werden.

**Aufräumen, Daten und Updates**

Nach 30 Tagen werden erledigte Archiveinträge gesichert und ausgeblendet; das Kaufjournal bleibt erhalten. Nur erfolgreich importierte, unveränderte CSV-Dateien mit abgeschlossenen zugehörigen Käufen werden nach Sicherung entfernt. Daher einen eigenen Austauschordner nutzen.

Daten liegen lokal unter %LOCALAPPDATA%\MyBeltInternetmarkeDirekt. Adressen und Kaufjournal sind nicht vollständig verschlüsselt; gespeicherte Zugangsdaten werden mit Windows DPAPI geschützt. Sicherungen vertraulich behandeln. Post-Funktionen kontaktieren die Post, Updates GitHub und der Spendenbutton PayPal.

Updates findet ihr unter „Einstellungen → Updates“. Ältere Versionen ohne diese Funktion zunächst manuell aktualisieren. Es gibt keinen gemeinsamen Mehrplatzbetrieb. Die Portopreise dieser Beta sind zeitlich begrenzt; ab 2027 ist für neue Käufe eine aktualisierte Preisversion nötig.

**Feedback willkommen**

Bitte nennt App-, Windows- und JTL-Version, Druckermodell, Papierformat, die Schritte bis zum Fehler und die bereinigte Fehlermeldung. Bitte keine Zugangsdaten, Kundenadressen oder scannbaren Internetmarken posten.

Vielen Dank fürs Testen und für eure Rückmeldungen!
