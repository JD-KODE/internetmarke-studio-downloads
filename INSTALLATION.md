# Einrichtung und Bedienung – 0.19.0

1. Datensicherung erstellen. Bisherige App über das Symbol neben der Windows-Uhr → Beenden vollständig schließen.
2. Setup-EXE aus dem aktuellen Release herunterladen und über die vorhandene Installation installieren. Kein separates Python nötig.
3. Post-API-Zugang freischalten lassen und API Key, API Secret sowie Portokassen-Zugangsdaten im Assistenten eintragen. Verbindung ohne Kauf prüfen.
4. Für CSV-Verarbeitung JTL-Exportordner und Spaltenzuordnung einrichten. Den Export in JTL separat konfigurieren. Der Marken-Shop benötigt keine CSV.
5. Drucker, Papierformat und Ausrichtung auch im Windows-Treiber passend einstellen. Brother QL-800 / DK-11201: 90 × 29 mm, Querformat. Neutrale Druckprobe ausführen.
6. Kauf-/Automatikoptionen wählen. Testlauf betrifft nur Automatik und Mehrfachauswahl, nicht Einzelkauf oder Marken-Shop. Ausgabenlimit optional, standardmäßig keines.
7. Im letzten Einrichtungsschritt Aufbewahrung und Löschfristen bei Bedarf einstellen. Erst Vorschau prüfen. Keine automatische Löschung dieser Kategorien ohne Aktivierung; die bisherige Aufräumsicherung bleibt bis zum Speichern neuer Regeln bestehen.
8. Eine Sendung bewusst kaufen und Ausdruck prüfen. Jede Marke nur einmal verwenden.

## Versand und Marken-Shop
CSV unterstützt Kompakt-, Groß- und Maxibrief DE. Im Marken-Shop zusätzlich Standardbrief und optional Einschreiben Einwurf oder Übergabe. Briefart und Menge wählen, zum Warenkorb hinzufügen, Gesamtpreis prüfen und kostenpflichtig kaufen. Bis zu 100 Marken pro Bestellung. CSV-Automatik vorher ausschalten. Alle ungedruckten Marken lassen sich drucken; keine gemeinsame A4-Bogenverwaltung.

Guthaben steht oben in Versand und Marken-Shop; Abrufzeitpunkt beachten, manuell aktualisieren oder Portokasse aufladen. Keine automatische Aufladung.

## Automatik und Hintergrund
In Versand-Einstellungen zunächst Testlauf verwenden. Für Echtbetrieb ausschalten, Testlauf abwählen, speichern und Automatik bewusst starten. Offene Imports/frühere Testläufe werden nachgeholt; vorhandene und unklare Käufe bleiben ausgeschlossen. Nach jedem Programmstart bleibt die Kaufautomatik aus.

Optional im Startdialog im Hintergrund weiterlaufen lassen. Symbol neben der Windows-Uhr: Öffnen, Pause, Automatik ausschalten, Beenden. PC eingeschaltet und Benutzer angemeldet lassen; kein Windows-Dienst. Ein laufender Vorgang wird beim Beenden abgeschlossen. Eine Druckübergabe an Windows beweist keinen tatsächlichen Ausdruck.

## Fehlerhilfe und Grenzen
Gekauft ohne Download: vorhandenen Kauf im Archiv abrufen, nicht neu kaufen. Bei Druckfehler zuerst Windows-Warteschlange prüfen. Nach absichtlicher Entfernung der Markendateien ist der Abruf in der App gesperrt. Kaufjournal nicht löschen oder durch neue Lieferscheinnummern umgehen.

Wawi-Rückexport für normale Lieferscheine, nicht WMS-Pakete. Shop-Marken haben keinen JTL-Rückexport. Kein gemeinsamer Mehrplatzbetrieb. Preisupdate ab 2027 nötig.

## Datenschutz und Sicherung
Daten lokal, Zugang optional mit Windows-Benutzerschutz; Adressen und Journal nicht vollständig verschlüsselt. Keine Telemetrie implementiert. Diagnoseexport enthält Version, Betriebssystem, Statusanzahlen und Automatik-Schalter, keine Adressen oder Zugangsdaten.

Manuelle Sicherung als passwortgeschützte .imsbackup-Datei; Passwort separat aufbewahren. Entschlüsselung erzeugt ein vertrauliches ZIP, keinen automatischen Import. Auf einem anderen PC Post-Zugang neu eingeben.

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
