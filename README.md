# Internetmarke Studio

**Weniger Handarbeit beim Briefversand – kostenlose Windows-App, öffentliche Beta 0.23.11.**

- **JTL direkt:** offene Lieferscheine beobachten; erst nach „Ausführen“ die Versandart auswerten und bei aktivierter Automatik Internetmarken kaufen und drucken.
- **Andere Dienstleister:** DHL und weitere Versandarten ausdrücklich ausschließen und automatisch ohne Markenkauf archivieren.
- **CSV alternativ:** vorhandenen CSV-Export weiterverwenden.
- **Marken-Shop:** Einzelmarken oder Warenkorb, „Kaufen & drucken“ oder „Nur kaufen“.
- **Druck und Übersicht:** Druckerassistent, Layout, Guthaben, Archiv mit Wawi-Status, Kopierfunktion und Stornoanträgen.
- **Im Alltag:** Hintergrundbetrieb, optionale Löschfristen, Sicherung und integrierte Updateprüfung.

[**Windows-Installer herunterladen**](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest) · [Versionshinweise](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.23.11)

## Andere Versanddienstleister einrichten

Unter **Versand → Wawi & Versandquelle** die entsprechende Versandart auf **„Anderer Versanddienstleister – kein Markenkauf“** setzen und speichern. Versandarten erscheinen nach dem ersten Ausführen; ohne Zuordnung wartet die Sendung.

Studio muss den offenen Lieferschein zuvor erfasst haben. Nach „Ausführen“ in Wawi wird die aktuelle Versandart geprüft. Extern zugeordnete Sendungen landen auch bei Automatik AUS im Archiv: **„Anderer Dienstleister – kein Markenkauf“**, Rückmeldung **„Nicht nötig“**. Die tatsächliche Versandart bleibt sichtbar. Es erfolgen kein Kauf, kein Druck und keine Änderung der Wawi-Sendungsnummer. Dies erstellt keine DHL-Etiketten.

Bereits vorher versendete Sendungen werden nicht nachträglich importiert. Die Anbindung verarbeitet weiterhin nur eindeutig zuordenbare Lieferscheine mit genau einem Paket. Fehlende Zuordnungen werden nicht automatisch als externe Versandarten behandelt.

## Installation und Update

1. Studio- und Wawi-Daten sichern.
2. Studio vollständig beenden, auch über das Symbol neben der Windows-Uhr.
3. Windows-Setup herunterladen und über die bestehende Installation installieren. Einstellungen und Kaufjournal bleiben erhalten.
4. Versandzuordnung und Drucker prüfen und zunächst eine Sendung kontrolliert testen.

Kein separates Python nötig. Ein freigeschalteter Post-API-Zugang ist für Internetmarken erforderlich. Software kostenlos; Porto kostenpflichtig. Eine freigegebene Live-Automatik kauft ohne Einzelrückfrage. Druckübergabe bestätigt keinen tatsächlichen Papierausdruck.

Öffentliche Beta, Nutzung auf eigenes Risiko; gesetzliche Ansprüche bleiben unberührt. Unabhängiges Projekt, kein offizielles Produkt von JTL, DHL oder Deutsche Post. Der Installer ist noch nicht signiert.

Dieses Repository enthält öffentliche Downloads und Dokumentation. **Der Quellcode bleibt privat.**
