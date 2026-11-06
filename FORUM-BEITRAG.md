# JTL-Forenbeitrag – 0.20.0

Veröffentlicht im [JTL-Forum](https://forum.jtl-software.de/threads/beta-kostenlos-internetmarke-studio-jtl-csv-einlesen-internetmarken-kaufen-und-drucken.250123/#post-1372147).

BBCode-Fassung; die Anhänge liegen direkt im Forum.

```text
[LIST]
[*][B]Weniger Handarbeit:[/B] JTL-CSV automatisch einlesen und auf Wunsch Marken kaufen und drucken.
[*][B]Auch ohne CSV:[/B] Marken-Shop mit Warenkorb, Mengenwahl und Einschreiben Einwurf oder Übergabe.
[*][B]Neu in 0.20.0:[/B] Druckerassistent mit Vorlagen, Kalibrierung sowie Logo und mehrzeiliger Absenderadresse.
[*][B]Alles im Blick:[/B] Guthaben, durchsuchbares Archiv, Nachdruck und geplante Löschdaten.
[*][B]Du entscheidest:[/B] Automatik, Hintergrundbetrieb und Aufbewahrung optional – passend zu deinem Ablauf.
[*][B]Kostenlose Windows-App:[/B] Normale Installation mit Desktop-Verknüpfung, kein separates Python. Porto bleibt kostenpflichtig.
[/LIST]
[B][URL='https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.20.0']Download: Internetmarke Studio 0.20.0[/URL][/B] · [URL='https://github.com/JD-KODE/internetmarke-studio-downloads/blob/main/INSTALLATION.md']Einrichtung Schritt für Schritt[/URL] · [URL='https://github.com/JD-KODE/internetmarke-studio-downloads/blob/main/BETA-ANLEITUNG.md']Alle Funktionen und Bedienung[/URL]

Ich entwickle die App für meinen eigenen Versand und die Community und kaufe damit selbst echte Marken. Ziel: weniger Wechsel zwischen Programmen und ein einfacher Ablauf vom CSV-Import bis zum Druck.

[ATTACH type="full"]134071[/ATTACH]

[B]Öffentliche Beta – Nutzung auf eigenes Risiko.[/B] Software kostenlos, Porto kostenpflichtig. Kaufbuttons kaufen verbindlich; freigegebene Live-Automatik kauft ohne Einzelrückfrage. Zuerst eine Sendung testen. Unabhängiges Projekt, kein offizielles Produkt von JTL oder Deutsche Post. Gesetzliche Ansprüche bleiben unberührt.

[B]Wichtig beim Update:[/B] Sichern → App am Symbol neben der Windows-Uhr vollständig beenden → Setup über die vorhandene Installation installieren. Bereits aktivierte Löschfristen beginnen ab 0.20.0 automatisch nach erfolgreicher Druckübergabe; keine manuelle Ausdruck-Bestätigung mehr nötig. 30 Tage Aufbewahrung empfohlen.

[SPOILER="In wenigen Schritten startklar"]
[LIST=1]
[*]Download öffnen → unter Assets die Setup-EXE wählen → installieren. Kein Python und keine BAT-Datei nötig. Installer noch unsigniert: Quelle prüfen, Windows-Schutz nicht generell abschalten.
[*]Post verbinden: freigeschalteter API-Zugang mit API Key, API Secret sowie Portokasse-E-Mail und Passwort. E-Mail/Passwort allein reichen nicht. Verbindung ohne Kauf prüfen; Zugang optional geschützt speichern und automatisch anmelden.
[*]Für JTL den CSV-Export separat einrichten, Zielordner auswählen und Spalten/Versandarten zuordnen. Einlesen kauft noch nichts. Für den Marken-Shop entfällt dieser Schritt.
[*]Drucklayout → Drucker einrichten und kalibrieren. Drucker/Papier wählen und dieselbe Größe im Windows-Treiber einstellen. Neutrale Probe drucken; Messlinie muss 20 mm lang sein.
[*]Kauf-, Automatik- und Datenschutzoptionen wählen. Testlauf gilt nur für Automatik/Mehrfachauswahl, nicht für Einzelkauf oder Marken-Shop. Ausgabenlimit optional, standardmäßig keines.
[*]Eine echte Sendung bewusst kaufen, Papierausdruck prüfen und Empfängeradresse anbringen. Jede Marke nur einmal verwenden.
[/LIST]
Der Einrichtungsassistent bleibt unter Einstellungen erreichbar. Updates ebenfalls dort. Das Setup kann die laufende App ab 0.19.0 zum geordneten Beenden auffordern; laufenden Vorgang abwarten und anschließend erneut Weiter wählen.
[/SPOILER]

[SPOILER="CSV, Automatik und Hintergrund – weniger Routinearbeit"]
[LIST]
[*][B]CSV-Assistent:[/B] Eigene Spalten und Versandarten zuordnen. Ordnerüberwachung liest neue Dateien automatisch ein.
[*][B]Versand:[/B] Einzelne oder mehrere Sendungen bearbeiten. Hauptaktion Kaufen oben, Einstellungen separat. Nach dem Kauf bleibst du im Versandbereich.
[*][B]Optionale Automatik:[/B] Neue und offene CSV-Sendungen kaufen und drucken; auch frühere Testläufe nachholen. Bereits gekaufte, archivierte und unklare Kaufversuche bleiben ausgeschlossen.
[*][B]Kontrolle behalten:[/B] Testlauf, Pause, Status und optionales Ausgabenlimit. Für Echtbetrieb Automatik ausschalten, Testlauf abwählen, speichern und bewusst starten.
[*][B]Im Hintergrund:[/B] Über das Symbol neben der Windows-Uhr öffnen, pausieren oder beenden. Windows-Autostart optional. Laufender Vorgang wird vor dem Beenden abgeschlossen.
[/LIST]
Nach jedem Programmstart bleibt die Kaufautomatik aus. PC muss eingeschaltet und Windows-Benutzer angemeldet bleiben; kein Windows-Dienst. Ohne Limit können freigegebene Sendungen bis zum verfügbaren Guthaben gekauft werden.
[/SPOILER]

[SPOILER="Marken-Shop und Guthaben – auch ohne JTL-CSV"]
Standard-, Kompakt-, Groß- und Maxibrief DE auswählen, optional Einschreiben Einwurf ODER Übergabe und Menge wählen → Warenkorb → Gesamtpreis prüfen → kostenpflichtig kaufen. Ohne Zusatz normale Briefmarke. Bis zu 100 Marken pro Bestellung. CSV-Automatik vorher ausschalten; Testmodus gilt nicht für diesen Kaufbutton.

Guthaben steht oben in Versand und Marken-Shop, mit Abrufzeitpunkt. Aktualisieren oder mit „Portokasse aufladen“ die Post-Seite öffnen. Keine automatische Aufladung.

Sofort drucken oder später „Alle ungedruckten drucken“. Nachdruck vorhandener Marken ohne neuen Kauf. Bei Teilfehlern Archiv und Warteschlange prüfen; „Rest kaufen“ berücksichtigt nur noch nicht gestartete Marken nach Bestätigung. Shop-Marken haben keinen JTL-Lieferschein/Rückexport. Einzelne Ausdrucke, keine gemeinsame A4-Bogenverwaltung.
[/SPOILER]

[SPOILER="Drucker, Kalibrierung und eigenes Layout"]
[B]Neu: geführte Einrichtung in drei Schritten.[/B] Drucker/Papier wählen → Position fein einstellen → Layout und Profil speichern.
[LIST]
[*]Vorlagen für Brother QL/DK-11201 (90 × 29 mm quer, z. B. QL-800), DK-11202 (100 × 62 mm quer), allgemeine Etiketten 100 × 50 / 102 × 152 mm sowie A4-Einzelaufdruck.
[*]Kalibrierung mit Pfeilen in 0,2-mm-Schritten oder Millimetereingabe. Die Kalibrierung verändert nicht die Markengröße.
[*]Neutrale Druckprobe ohne Portokauf, mit 20-mm-Messlinie zur Kontrolle.
[*]Logo, Zusatztext und feste mehrzeilige Absenderadresse im Layouteditor hinzufügen und verschieben. Vorschau auf Anschnitt/Überlappungen prüfen.
[*]Druckerprofile speichern Drucker, Papier, Layout und Kalibrierung zusammen – praktisch bei wechselnden Druckern oder Formaten.
[/LIST]
Vorlagen ersetzen keine Treiberinstallation und erkennen keine Rolle. Treibereinstellungen und Hardware selbst prüfen. Absenderadresse ist ein festes Feld für jeden Ausdruck, keine automatische Empfängerzuordnung. Kleine Etiketten bieten ggf. zu wenig Platz: größeres Format oder separates Adressetikett verwenden. Bestehende freie Layouts bleiben erhalten.
[/SPOILER]

[SPOILER="Archiv, Nachdruck und Wawi-Rückdatei – Überblick behalten"]
Käufe über die Suche finden, Markennummern nachsehen und gespeicherte Marken nachdrucken. Bei Downloadproblemen den vorhandenen Kauf abrufen statt neu zu kaufen. Unklare Versuche bleiben zum Schutz vor Doppelkäufen gesperrt.

Sendungen lassen sich ohne Kauf archivieren und später zurückholen. Eine Wawi-Rückdatei kann für normale Lieferscheine erstellt werden; der Import in JTL erfolgt separat. Nicht für WMS-Pakete oder Marken-Shop-Käufe.

[B]Neu:[/B] „Druck übergeben“ erscheint nach erfolgreichem Direktdruck automatisch. Das bestätigt die Übergabe an Windows, keinen tatsächlich fertigen Papierausdruck. PDF-Öffnen oder externer PDF-Druck können nicht automatisch bestätigt werden.
[/SPOILER]

[SPOILER="Datenschutz und Löschfristen – selbst bestimmen, was bleibt"]
Weitere Aktionen → Datenschutz & Diagnose → Aufbewahrung und Löschfristen. Auch in der Ersteinrichtung.
[LIST]
[*]CSV-Dateien, Namen/Adressen, Markendateien/frühere Versuche und app-eigene Sicherungen getrennt aktivieren. Ohne Haken keine Löschung dieser Kategorie. Vorschlag: 30 Tage.
[*]„Vorschau – nichts löschen“ zeigt aktuell fällige Mengen. Beim Speichern automatische Löschung bestätigen; bereits fällige Daten können beim nächsten Lauf entfernt werden.
[*][B]Ab 0.20.0 automatisch:[/B] Erfolgreiche Druckübergabe startet die gewählten Fristen. Kein zusätzlicher Klick „Ausdruck geprüft“. Bereits gespeicherte Regeln gelten ebenfalls.
[*]Fehlgeschlagener/unterbrochener Druck startet keine Frist. Fehlgeschlagener Nachdruck hält sie an; erfolgreicher Nachdruck startet sie neu. Kauf ohne Druck und neutrale Probe starten keine Frist.
[*]Archiv zeigt getrennt „CSV löschen ab“, „Kundendaten löschen ab“ und „Marken löschen ab“. Gemeinsame Daten warten auf alle betroffenen Vorgänge. CSV wird nur unverändert und nach Fälligkeit aller enthaltenen Sendungen gelöscht.
[*]Sicherungen: Frist ab Dateialter, mindestens 1 Tag; nur App-Unterordner „sicherungen“. Externe Backups und JTL-Daten selbst verwalten.
[/LIST]
[B]30 Tage empfohlen:[/B] Bei 0 Tagen können Markendateien vor dem tatsächlichen Papierausdruck entfernt werden – etwa bei Papierstau. Danach kein Nachdruck/Abruf in der App mehr möglich. Kaufkennungen/Lieferscheine bleiben als Doppelkaufschutz erhalten; keine vollständige Anonymisierung. Bereinigung nur bei laufender App, auch im Hintergrund. Neue gespeicherte Regeln ersetzen die frühere Aufräumsicherung; ohne Speichern bleibt das bisherige Verhalten bestehen.

Zugangsdaten optional mit Windows-Benutzerschutz. Adressen, Journal und Marken nicht vollständig verschlüsselt. Keine Telemetrie implementiert. Diagnoseexport ohne Kundenadressen/Zugangsdaten. Manuelle Sicherung passwortgeschützt; Passwort separat aufbewahren. Entschlüsselung erzeugt eine vertrauliche ZIP-Datei, keinen automatischen Import. Externe Kopien separat verwalten; keine garantierte sichere Entfernung aller Datenträgerspuren.
[/SPOILER]

[SPOILER="Aktuelle Screenshots – Version 0.20.0"]
Originalansichten aus dem Windows-Test, mit neutralen Testdaten. Die Übersichtsgrafik oben ist eine Illustration, keine Programmoberfläche.
[B]Kalibrierung:[/B]
[ATTACH type="full"]134072[/ATTACH]
[B]Aufbewahrung:[/B]
[ATTACH type="full"]134073[/ATTACH]
[B]Marken-Shop:[/B]
[ATTACH type="full"]134074[/ATTACH]
[/SPOILER]

[SPOILER="Versionsverlauf"]
[B]0.20.0 – aktuell öffentlich[/B]
Druckerassistent und Vorlagen, Kalibrierung im Profil, mehrzeilige Absenderadresse. Automatischer Status „Druck übergeben“, Fristbeginn nach Druckübergabe und getrennte Löschdaten im Archiv.

[B]0.19.0[/B]
Optionale Löschfristen, Vorschau und Datenschutz in der Einrichtung. Setup-Sperre bei laufender App und geordnetes Beenden. Die damalige manuelle Ausdruck-Bestätigung entfällt ab 0.20.0.

[B]0.18.1 / 0.18.0[/B]
Kompakter Automatik-Startdialog, Hintergrundbetrieb, optionaler Windows-Autostart, Fehlerhilfe, Diagnose und passwortgeschützte Sicherung.

[B]0.17.3 / 0.17.2 / 0.17.1[/B]
Optionales Ausgabenlimit, aufgeräumter Versandbereich und Nachholen offener CSV-Sendungen/früherer Testläufe.

[B]0.17 / 0.16[/B]
Guthabenanzeige, Portokasse aufladen, Einschreiben sowie Marken-Shop mit Warenkorb und Kauf ohne CSV.

Das unveränderte geprüfte 0.20.0-Paket ist öffentlich freigegeben. Die Fensterbeschriftung „Private Testversion“ stammt noch aus der Testphase.

Ältere Testansichten (0.14–0.17.3, nicht der aktuelle Stand):
[ATTACH]134059[/ATTACH] [ATTACH]134060[/ATTACH] [ATTACH]134061[/ATTACH] [ATTACH]134062[/ATTACH] [ATTACH]134063[/ATTACH] [ATTACH]134064[/ATTACH] [ATTACH]134069[/ATTACH] [ATTACH]134070[/ATTACH]
[/SPOILER]

[SPOILER="Beta-Hinweise und Fehlerhilfe"]
200 automatisierte Windows-Tests sowie Installation, Programmstart, neue Assistentenschritte, Deinstallation und Setup-Sperre bestanden. Entwicklungstests ohne echte Käufe oder physische Ausdrucke. Ich kaufe selbst Marken mit der App; andere Drucker und Abläufe bitte zusätzlich testen.

Gekauft ohne Download: vorhandenen Kauf im Archiv abrufen. Druckfehler: Windows-Warteschlange prüfen. Unklarer Kauf: Archiv und Portokasse prüfen. Nicht neu kaufen, Journal löschen oder neue Lieferscheinnummern zur Umgehung verwenden.

CSV: Kompakt-, Groß- und Maxibrief DE. Standardbrief/Einschreiben zunächst nur im Marken-Shop. Kein gemeinsamer Mehrplatzbetrieb, kein Windows-Dienst und keine gemeinsame A4-Bogenverwaltung. Preisupdate ab 2027 erforderlich.
[/SPOILER]

Feedback willkommen: App-/Windows-/JTL-Version, Drucker, Papierformat und Schritte nennen. Keine Zugangsdaten, Kundenadressen oder scannbaren Marken posten. [B]Alle Funktionen bleiben kostenlos; PayPal-Spenden sind freiwillig.[/B]
```
