# Internetmarke Studio

**Kostenlose Windows-App · öffentliche Beta 0.23.17**

1. **JTL direkt:** offene Lieferscheine ohne CSV laden; nach „Ausführen“ in Wawi die aktuelle Versandart prüfen.
2. **Automatik:** Internetmarken kaufen, optional drucken und die Markennummer an Wawi zurückmelden – auch im Hintergrund.
3. **Marken-Shop:** Einzelmarken und Warenkorb, „Kaufen & drucken“ oder „Nur kaufen“.
4. **Archiv & Drucklayout:** Marken finden, Nummern kopieren, Wawi-Status sehen und eigene Etiketten gestalten.
5. **Porto automatisch aufladen – BETA:** optionaler Guthabengrenzwert und Aufladebetrag per SEPA-Lastschrift.

[**Windows-Setup herunterladen**](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest) · [Einrichtung und Update](INSTALLATION.md)

## Neu in 0.23.17

- Status direkt in der Spalte **Wawi-Status**, ohne zusätzliche Filter- oder Aktionsleiste.
- Hinweise per Doppelklick; Aktionen per Rechtsklick auf die Sendung.
- Ältere Archivkäufe mit Prüfhinweis werden nicht mehr zusätzlich im Versand angezeigt. Archivdaten und Kaufsperren bleiben erhalten.
- Prüfhinweise verändern den gespeicherten Wawi-Datenstand nicht mehr.

## Neu in 0.23.16

- Einzelne problematische Sendungen werden zur Prüfung zurückgestellt; andere gültige, von Wawi freigegebene Sendungen laufen weiter.
- Sendungsstatus **Wartet auf Wawi**, **In Bearbeitung** und **Bitte prüfen**; ab 0.23.17 direkt in der Sendungszeile.
- Archiv mit drei Hauptaktionen: **Marke stornieren**, **Marke drucken**, **Sendung löschen**. Weitere Funktionen per Rechtsklick, Details per Doppelklick. Bestehende Schutzregeln für Kauf und Löschen bleiben erhalten.
- Markenkauf, Druckübergabe und Wawi-Rückmeldung getrennt sichtbar.
- Erkannte Updates bleiben deutlich in der Statusleiste sichtbar.
- Kürzerer Einrichtungsassistent und neuer Schalter **Porto automatisch aufladen AN/AUS · BETA** direkt im Versand. Beim Aktivieren Guthabengrenze, Betrag und wiederholte Lastschrift bestätigen.

[Aktueller Forumsbeitrag](https://forum.jtl-software.de/threads/beta-kostenlos-internetmarke-studio-jtl-csv-einlesen-internetmarken-kaufen-und-drucken.250123/#post-1373008)

## Neu in 0.23.15

- Vollständige Namen werden auch in nur einem Namensfeld akzeptiert und unverändert übernommen.
- Gültige Namens- und Adresskorrekturen aus Wawi werden beim Ausführen übernommen. Paketzuordnung und Schutz vor Doppelkauf bleiben bestehen.
- Adresshinweise benennen das fehlende oder ungültige Feld.
- **Ignorieren und weitermachen:** Betroffene Sendungen für diese Sitzung ohne Kauf und Druck auslassen. Die übrigen freigegebenen Sendungen können nach Aktivierung der Automatik weiterlaufen. Geänderte Daten und ein Neustart führen zu einer erneuten Prüfung.

## Neu in 0.23.14

- Offene Lieferscheine bleiben sichtbar, wenn andere Sendungen eine Prüfung benötigen. Hinweise nennen den Lieferschein und den Grund; unklare Freigaben berechtigen nicht zum Kauf.
- Kompakte Statusleiste unten mit farbigem Moduspunkt und Text.
- **Portoaufladung BETA:** Einstellungen → Post-Zugang → Aufladeeinstellungen. Standardmäßig aus; pro Post-Konto aktivierbar. Beispiel: unter 10 € um 50 € aufladen.
- Die Versandautomatik wartet bei fehlendem Guthaben und prüft jede Minute erneut. Vor dem Fortsetzen werden Sendung und Guthaben erneut geprüft.
- Unklare Aufladungen sperren weitere automatische Abbuchungen auch nach Neustart, bis der Ausgang in der Portokasse geprüft und die Sperre bewusst aufgehoben wurde.

Ein gültiges SEPA-Mandat in der Portokasse ist erforderlich. PayPal-Aufladung nur über die Post-Webseite. Automatisches Aufladen läuft nur bei geöffneter App, auch im Hintergrund, und nicht im Testlauf. Echte Lastschriften wurden im Entwicklungstest nicht ausgeführt. Vorhandene unklare Kaufversuche werden nicht pauschal erneut gekauft.

## Hinweise zum Ablauf

Studio muss den offenen Lieferschein zuvor erfasst haben. Die Versandart wird erst nach „Ausführen“ ausgewertet und über eine einmalige Zuordnung dem Portoprodukt zugewiesen. CSV bleibt als Alternative verfügbar. Die JTL-Anbindung verarbeitet eindeutig zuordenbare Lieferscheine mit genau einem Paket. Sie ergänzt die Sendungsnummer per SQL; sie löst keinen vollständigen Versandabschluss über jtlCore.dll und keine erneute Plattformmeldung aus. Den eigenen Wawi-/Plattformablauf prüfen.

DHL und andere Anbieter können unter **Wawi & Versandquelle → Anderer Versanddienstleister – kein Markenkauf** ausgeschlossen werden. Sie werden nach erkannter Wawi-Freigabe ohne Internetmarkenkauf archiviert. Es werden keine DHL-Etiketten erstellt.

## Update

Daten sichern → Studio vollständig beenden, auch neben der Windows-Uhr → Setup über die vorhandene Installation installieren → ersten Ablauf kontrolliert prüfen. Kein separates Python nötig.

Automatisierte Tests sowie Windows-Installation und Programmstart erfolgreich geprüft. Keine echten Käufe, Lastschriften oder physischen Ausdrucke im Entwicklungstest.

Öffentliche Beta, Nutzung auf eigene Verantwortung; gesetzliche Ansprüche bleiben unberührt. Software kostenlos, Porto kostenpflichtig. Freigegebene Live-Automatik kauft ohne Einzelrückfrage. „Druck übergeben“ bestätigt die Windows-Übergabe, nicht den Papierausdruck. Installer unsigniert. Unabhängiges Projekt, kein offizielles Produkt von JTL, DHL oder Deutsche Post.

Dieses Repository enthält Downloads und Dokumentation. **Der Quellcode bleibt privat.**
