# Internetmarke Studio 0.23.14 – Einrichtung und Update

## 1. Installieren
[Aktuelles Windows-Setup](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest) öffnen. Unter **Assets** die **Internetmarke-Studio-Setup-0.23.14.exe** herunterladen und starten. Kein Python und keine BAT-Datei nötig. Der Installer ist noch unsigniert; Quelle prüfen und den Windows-Schutz nicht generell abschalten.

**Update:** Studio- und Wawi-Daten sichern. Studio vollständig über das Symbol neben der Windows-Uhr → **Beenden** schließen. Laufenden Vorgang abwarten. Setup über die vorhandene Installation installieren; Datenordner nicht löschen.

## 2. Post verbinden
API Key, API Secret, Portokasse-E-Mail und Passwort im Assistenten eingeben. Freigeschalteter Post-API-Zugang und Freigabe der Geschäftsanwendung in der Portokasse sind nötig. Anmeldung kauft kein Porto. Zugang optional mit Windows-Benutzerschutz speichern; auf einem anderen PC neu eingeben.

## 3. Versandquelle wählen
**JTL direkt:** Wawi-Installation, SQL-Verbindung, Datenbank und Benutzer im Assistenten einrichten. Studio muss die offenen Lieferscheine zuerst anzeigen. Erst beim anschließenden „Ausführen“ mit „als versendet setzen“ in Wawi wird die aktuelle Versandart ausgewertet. Unter **Versand → Weitere Aktionen → Automatik-Einstellungen → Wawi & Versandquelle** bzw. **Einstellungen → Versand & Betrieb → Wawi & Versandquelle** die Versandarten einmalig zuordnen. Ohne Zuordnung wartet die Sendung.
Die Rückmeldung ergänzt die Markennummer als Sendungsnummer. Sie löst keine erneute Plattformmeldung und keinen vollständigen Versandabschluss über jtlCore.dll aus. Den Wawi-/Plattformablauf separat prüfen.

**CSV alternativ:** CSV-Export in Wawi einrichten, denselben Ordner in Studio auswählen und Spalten zuordnen. [Beispieldatei](Beispiel-JTL.csv). Der zusätzliche CSV-Reiter lässt sich in den Einstellungen einblenden.

**Nur Marken kaufen:** Dafür reicht der Marken-Shop; kein Lieferschein und keine CSV nötig.

## 4. Drucker und Layout
**Drucklayout → Drucker einrichten** öffnen: Windows-Drucker, Papier und passende Vorlage wählen. Im Windows-Treiber dieselbe Größe/Ausrichtung einstellen, keine Seitenanpassung. Kostenlose neutrale Druckprobe und Kalibrierung durchführen. Danach unter **Layout bearbeiten** Marke, Adresse oder Logo anordnen. Vorlage am eigenen Drucker testen; sie installiert keinen Treiber.

## 5. Automatik kontrolliert testen
Zunächst Testlauf und Druckprobe verwenden. Der Testlauf kauft und druckt in der Versandautomatik nichts; er gilt nicht für ausdrückliche Einzelkäufe im Marken-Shop.

Nach abgeschlossener Einrichtung und Post-Anmeldung kann die Automatik beim Start im gespeicherten Test-/Echtmodus anlaufen. Im Echtbetrieb kauft sie freigegebene Sendungen kostenpflichtig ohne Einzelrückfrage. Sofortdruck wird beim Einschalten standardmäßig aktiviert, kann aber ausgeschaltet werden. Ausgabenlimit optional.

Bei JTL erst prüfen, dass der offene Lieferschein in Studio erfasst ist, dann in Wawi „Ausführen“. Nach Kauf Ausdruck, Archiv und Wawi-Sendungsnummer kontrollieren. Nur eine Studio-Instanz für dieselben Sendungen verwenden. Hintergrundbetrieb benötigt laufenden PC und angemeldeten Windows-Benutzer; kein Windows-Dienst.

## 6. Automatische Portoaufladung – BETA
**Einstellungen → Post-Zugang → Aufladeeinstellungen**:
1. Gültiges SEPA-Mandat in der Portokasse hinterlegen.
2. Guthabengrenze und Aufladebetrag wählen, z. B. unter 10 € um 50 €.
3. Funktion aktivieren und Lastschrift beim Speichern bestätigen.

Standardmäßig aus, kontogebunden, nur bei laufender App und nicht im Testlauf. Der Aufladebetrag muss mindestens der Guthabengrenze entsprechen. Wiederholte Aufladungen sind möglich, wenn das Guthaben nach erfolgreicher Aufladung erneut unter die Grenze fällt.

Die Versandautomatik wartet bei fehlendem Guthaben und prüft jede Minute erneut. Nach ausreichender Aufladung werden Sendung, Freigabe und Kaufstatus erneut geprüft. Nur ausdrücklich wegen Guthaben wartende Vorgänge vor dem Kaufaufruf dürfen automatisch fortgesetzt werden; alte unklare Käufe nicht blind erneut kaufen.

**Unklare Aufladung:** Kein automatischer Wiederholungsauftrag. Umsatz in der Portokasse prüfen; erst danach unter Aufladeeinstellungen die Sperre bewusst aufheben. PayPal-Aufladung erfolgt über die Post-Webseite. Die SEPA-Funktion wurde mit simulierten Antworten geprüft, noch nicht mit einer echten Lastschrift im Entwicklungstest.

## 7. Datenschutz und Hilfe
Unter **Einstellungen → Datenschutz** Aufbewahrung und Sicherung festlegen. CSV, Kundendaten, Markendateien und Sicherungen haben getrennte Optionen. Vor Aktivierung die Löschvorschau prüfen. Aktivierte Fristen beginnen nach erfolgreicher Druckübergabe; 0 Tage kann Dateien vor dem tatsächlichen Papierausdruck entfernen.

Bei Fehlern zuerst Archiv und Windows-Druckwarteschlange prüfen. Kein erneuter Kauf einer bereits gekauften oder unklaren Marke. Für Rückmeldungen App-/Windows-/Wawi-Version und Ablauf nennen; keine Passwörter, Kundenadressen oder scannbaren Marken veröffentlichen.

Öffentliche Beta auf eigene Verantwortung; gesetzliche Ansprüche bleiben unberührt. Software kostenlos, Porto kostenpflichtig. Kein offizielles Produkt von JTL oder Deutsche Post.
