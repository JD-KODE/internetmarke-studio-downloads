## Internetmarke Studio 0.18.1 – öffentliche Beta
- Hintergrundbetrieb mit Symbol neben der Windows-Uhr: öffnen, pausieren und beenden.
- Optionaler Start bei der Windows-Anmeldung; Kaufautomatik nach Neustart weiterhin aus.
- Kurzer Startdialog mit „Automatik starten“, „Abbrechen“ und optionalem Wechsel in den Hintergrund.
- Verständlichere Fehlerhilfe; unklare Käufe nicht erneut kaufen.
- Datenschutzübersicht, Diagnoseexport ohne Kundendaten und passwortgeschützte manuelle Sicherungen.
- Ausgabenlimit weiterhin optional; standardmäßig keines.

**Vor dem Update:** Datensicherung erstellen. App über Rechtsklick auf das Symbol neben der Windows-Uhr → Beenden vollständig schließen und laufende Vorgänge abwarten. Erst dann Setup installieren. Bei „Anwendungen konnten nicht geschlossen werden“ App beenden und „Nochmals versuchen“ wählen, nicht ignorieren.

169 automatisierte Windows-Tests sowie Installation, EXE-Start und Deinstallation bestanden. Keine echten Käufe oder physischen Ausdrucke im Entwicklungstest. Installer noch unsigniert. Nutzung als Beta auf eigenes Risiko; gesetzliche Ansprüche bleiben unberührt.

Hintergrundbetrieb benötigt einen eingeschalteten PC und angemeldeten Windows-Benutzer; kein Windows-Dienst. Bestehende lokale Adressen, Kaufjournal und ältere/automatische Sicherungen sind nicht vollständig verschlüsselt. Die Bezeichnung „Private Testversion“ im Programmfenster stammt aus der Testphase; dieses unveränderte, geprüfte Paket ist jetzt als öffentliche Beta freigegeben.

---

# Einrichtung und Update – Internetmarke Studio 0.18.1

**Öffentliche Beta, Nutzung auf eigenes Risiko.** Vorher Datensicherung erstellen. Echte Käufe kosten Porto; der einzelne Kaufbutton kauft ohne weitere Bestätigung. Keine offizielle JTL-/Post-Anwendung.

## Installation
1. [Version 0.18.1 öffnen](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.18.1).
2. Unter Assets **Internetmarke-Studio-Setup-0.18.1.exe** herunterladen und öffnen.
3. Setup abschließen und die Desktop-Verknüpfung starten. Python ist enthalten.
4. Der Installer ist noch nicht digital signiert. Quelle prüfen; Windows-Schutz nicht generell abschalten.

## Einrichtungsassistent: sechs Schritte
1. **Willkommen:** Hinweise zu echten Portokäufen lesen. Die Einrichtung selbst kauft nichts.
2. **Post verbinden:** API Key, API Secret, Portokassen-E-Mail und Passwort eintragen. API-Zugang zuerst bei der Deutschen Post freischalten lassen; E-Mail/Passwort allein reichen nicht. Verbindung ohne Kauf prüfen. Die Geschäftsanwendung gegebenenfalls in der Portokasse freigeben. Optional Zugang mit Windows-Benutzerschutz speichern und automatische Anmeldung wählen.
3. **CSV-Ordner:** Nur für JTL-CSV erforderlich. Einen Exportordner anlegen und in App und JTL verwenden. Die App richtet den JTL-Export nicht selbst ein. Beispiel-JTL.csv verwenden oder im CSV-Assistenten Spalten und Versandarten zuordnen. Der reine Import kauft nichts.
4. **Drucker und Layout:** Windows-Treiber installieren; Drucker, Papierformat und Ausrichtung in App und Treiber passend einstellen. Brother QL-800/DK-11201: 90 × 29 mm, Querformat. Kostenlose neutrale Druckprobe ausführen.
5. **Kauf und Automatik:** Druck nach Einzelkauf wählen. Testlauf gilt nur für Automatik/Mehrfachauswahl. Das Ausgabenlimit ist standardmäßig AUS und kann optional aktiviert werden. Testmodus und Limit werden gespeichert; die Automatik bleibt zunächst ausgeschaltet.
6. **Ersten Live-Test prüfen:** Produkt, Preis, Empfänger und Druck prüfen. Marke vollständig in Originalgröße drucken; Empfängeradresse separat anbringen. Jede Marke nur für eine Sendung verwenden.

Der Assistent ist später unter Einstellungen erneut erreichbar.

## Update einer vorhandenen Installation
Unter Einstellungen eine Datensicherung erstellen, App schließen und neues Setup über die vorhandene Installation installieren. Bestehenden Datenordner nicht löschen. Alternativ Einstellungen → Updates. Die Automatik danach bewusst neu aktivieren und Modus prüfen.

## Guthaben und Aufladen
Oben in Versand und Marken-Shop stehen Guthaben und Zeitpunkt des letzten Abrufs. ↻ aktualisiert. „Portokasse aufladen“ öffnet die offizielle Post-Seite; nach externer Aufladung aktualisieren. Die App lädt kein Geld automatisch auf. Vor Kauf wird das Guthaben geprüft; bei zu wenig Guthaben wird der fehlende Betrag angezeigt.

## Wichtige Grenzen
CSV unterstützt weiterhin Kompakt-, Groß- und Maxibrief DE; Standardbrief und Einschreiben sind zunächst im Marken-Shop auswählbar. Kein direkter JTL-Datenbankzugriff. Wawi-Rückdateien gelten für normale Lieferscheine, nicht WMS-Pakete; Import kann Status und Benachrichtigungen ändern. Mehrere Marken werden einzeln gedruckt, nicht gemeinsam auf einem A4-Bogen. Druckerprofile ändern keine Windows-Treibereinstellungen. Adressetikett-Vorschau ist ein Entwurf, keine Frankierung. Kein gemeinsamer Mehrplatzbetrieb.

Bei Downloadfehlern gespeicherten Kauf im Archiv abrufen, nicht neu kaufen. Bei Druckfehlern zuerst die Windows-Warteschlange prüfen. „Druck übergeben“ bestätigt keinen physischen Ausdruck.

Daten unter %LOCALAPPDATA%\\MyBeltInternetmarkeDirekt. Adressen und Journal sind nicht vollständig verschlüsselt; Zugangsdaten optional per Windows DPAPI geschützt. Backups vertraulich behandeln. Kaufjournal bleibt beim Aufräumen erhalten. Nur importierte, unveränderte alte CSV mit abgeschlossenen Käufen werden nach Sicherung entfernt. Keine Telemetrie implementiert.

154 automatisierte Tests und Windows-Installation/App-Start/Deinstallation geprüft. Entwicklungstests ohne echte Portokäufe; eigene Live-Prüfung erforderlich. Gesetzliche Ansprüche bleiben unberührt.
