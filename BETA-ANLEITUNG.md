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

# Bedienung ab 0.18.1

## Versand
CSV einlesen, Sendung in der Liste auswählen, Preis prüfen und oben kaufen. „Nach dem Kauf sofort drucken“ ist optional. „Mehrere Sendungen …“ verarbeitet die markierte Auswahl nach Übersicht und Bestätigung. Adresse bei Bedarf separat ansehen; seltene Aktionen stehen unter „Weitere Aktionen“.

## Marken-Shop ohne CSV
Briefart und Menge wählen. Optional genau ein Häkchen: Einschreiben Einwurf oder Einschreiben/Übergabe; ohne Häkchen normale Marke. Zum Warenkorb hinzufügen und Gesamtpreis prüfen. „Kostenpflichtig kaufen“ kauft echtes Porto – der Automatik-Testmodus gilt hier nicht. Maximal 100 Marken pro Warenkorb. CSV-Automatik für Shop-Käufe ausschalten.
Optional sofort drucken oder später „Alle ungedruckten drucken“. Bereits übergebene oder unklare Druckaufträge werden ausgelassen. PDF-Druck außerhalb der App wird nicht erfasst. Kein neuer Kauf beim Nachdruck. Shop-Marken haben keinen Lieferschein und keinen Wawi-Rückexport. Bei Teilfehlern im Archiv prüfen; „Rest kaufen“ kauft nur noch nicht gestartete Marken nach Bestätigung.

## Automatik und Testlauf
1. Unten Versand-Einstellungen öffnen. Für einen kostenlosen Versuch Testlauf aktivieren und speichern. Ein Ausgabenlimit ist optional, standardmäßig keines.
2. „Automatisch kaufen und drucken“ aktivieren. Bereits eingelesene, noch ungekaufte Sendungen einschließlich vorheriger Testläufe werden übernommen; neue CSV folgen.
3. Für Echtbetrieb Automatik ausschalten, Testlauf in Versand-Einstellungen abwählen, speichern und Automatik erneut aktivieren. Anzahl, Porto und optionales Limit in der Bestätigung prüfen.
4. Die App muss laufen; das Fenster darf im Hintergrund ausgeblendet sein. Pause stoppt nach dem aktuellen Auftrag. Fehler stoppen den Lauf; gekaufte, archivierte und ungeklärte Kaufversuche werden nicht neu gekauft.

Nach Neustart ist die Automatik aus. Gespeicherter Testmodus und Limit bleiben erhalten – den Modus vor Aktivierung prüfen. Ohne Ausgabenlimit können alle freigegebenen offenen und neu eintreffenden Sendungen bis zum verfügbaren Guthaben gekauft werden. Die Guthabenprüfung und der lokale Schutz vor Doppelkäufen bleiben aktiv.

## Hilfe
Gekauft ohne Download: Archiv → vorhandenen Kauf abrufen. Druckproblem: Warteschlange prüfen und gespeicherte Marke verwenden. Unklarer Kauf: Archiv und Portokasse prüfen; Journal nicht löschen oder neue Lieferscheinnummern als Umgehung verwenden. Vor Updates sichern.

[Installation und Datenschutz](INSTALLATION.md) · [Download](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.18.1)
