# Neu in 0.16.0: Marken kaufen ohne CSV

Links „Marken kaufen“ öffnen. Kompakt-, Groß- oder Maxibrief wählen, Menge einstellen und zum Warenkorb hinzufügen. Der Warenkorb zeigt Anzahl und Gesamtporto. „Auswahl entfernen“ entfernt eine Briefart; gewünschte Menge danach neu hinzufügen.

Mit eigener Portokasse anmelden. Der Button „Kostenpflichtig kaufen“ startet den echten Einkauf zum angezeigten Gesamtpreis. Kein CSV-Import, Empfänger oder JTL-Lieferschein erforderlich. Bis zu 100 Marken pro Warenkorb, sequenziell verarbeitet und einzeln im Archiv gespeichert. Portoetiketten ohne Empfängeradresse; Adresse separat anbringen.

Optional „Nach dem Kauf alle Marken drucken“ aktivieren. Drucker vorher wählen und neutrale Probe ausführen. Alternativ später unter „Meine Bestellungen“ die Bestellung auswählen und „Alle ungedruckten drucken“ anklicken. Das kauft kein neues Porto. Bereits an Windows übergebene oder unklare Druckaufträge werden ausgelassen. Übergabe bestätigt keinen physischen Ausdruck. Nachdruck einzelner Marken im Archiv nur nach Prüfung der Warteschlange; dieselbe Marke nicht für mehrere Sendungen verwenden. Beim PDF-Druck außerhalb der App kann der Druckstatus nicht automatisch erfasst werden.

„Stopp“ beendet nach der aktuellen Marke. Bei Teilfehler bleiben gekaufte Marken erhalten. „Im Archiv öffnen“ zeigt die zugehörigen Einträge; unklare Käufe zuerst prüfen/abrufen. „Rest kaufen“ kauft nur noch nicht gestartete Marken nach erneuter Bestätigung. Nach Neustart wird kein Einkauf automatisch fortgesetzt. Warenkorbentwürfe sind nur während der Sitzung gespeichert; gestartete Bestellungen sind dauerhaft gespeichert und nach Anmeldung im gleichen Postkonto sichtbar.

Die CSV-Automatik muss vor Shop-Käufen ausgeschaltet sein. Ihr Testlauf-Schalter gilt nicht für den Shop: der Shop-Kaufbutton kauft immer echtes Porto. Shop-Marken ohne Lieferschein können nicht als Wawi-Versanddaten exportiert werden. Preisstand nur bis Ende 2026. Öffentliche Beta, zunächst eine Marke im eigenen Ablauf prüfen.

---

# Internetmarke Studio 0.15.2 – Beta: Einrichtung und Test

Kostenlose öffentliche Beta. Nutzung auf eigene Gefahr; Fehler sind möglich. Keine offizielle Software von JTL oder Deutsche Post. Vor Einsatz Daten sichern und zunächst eine Sendung testen. Windows 10/11 x64, Python muss nicht installiert sein. Der Installer verwendet dieselbe App-ID und denselben Datenordner wie die vorherige Version.

## Installation

1. In der bisherigen App unter Einstellungen eine Datensicherung erstellen.
2. App vollständig schließen. Neues Setup starten und das bisherige Installationsverzeichnis beibehalten.
3. Über die Desktop-Verknüpfung öffnen. Die Versionsnummer muss 0.15.2 zeigen.
4. Vor dem Livebetrieb eine neutrale Druckprobe durchführen. Bestehende Käufe niemals mit neuer Lieferscheinnummer erneut importieren.

## Eigene CSV einrichten

1. Einstellungen → CSV-Assistent & Versandregeln öffnen.
2. Einen Profilnamen eingeben; Trennzeichen wählen (Semikolon, Komma oder Tab).
3. Eine eigene Beispiel-CSV öffnen. Die Datei wird nur geprüft, nicht frankiert.
4. Für jedes Feld die passende Quellspalte auswählen. Benötigt werden Lieferschein, Versandart, Straße, PLZ, Ort sowie Nachname oder Firma. Nicht vorhandene optionale Felder leer lassen.
5. Die CSV muss Land DE enthalten. Fehlt die Landspalte und sind wirklich alle Empfänger in Deutschland, „Wenn Land leer ist, ausdrücklich DE verwenden“ aktivieren.
6. Bei eigenen Versandnamen eine Regel je Zeile eintragen, z. B. `Brief Inland = Großbrief`. Erlaubte Ziele: Kompaktbrief, Großbrief, Maxibrief. Namen müssen exakt passen. Gewicht wird nicht automatisch ermittelt.
7. „Vorschau prüfen – kostenlos“ anklicken, dann „Profil speichern & verwenden“. Ein aktives Profil gilt für manuelle UND automatische CSV-Importe. Bereits eingelesene Sendungen behalten ihre geprüften Daten.

Weitere Profile lassen sich unter einem anderen Namen speichern. Zum Wechsel das Profil wählen, passende Beispiel-CSV öffnen, prüfen und speichern. „Standardformat verwenden“ aktiviert wieder das mitgelieferte CSV-Format. PLZ-Spalten in Wawi als Text exportieren, damit führende Nullen erhalten bleiben.

## Druckerprofile

1. Unter Drucklayout Drucker, Papierformat und Layout einstellen.
2. Unter Einstellungen → Druckerprofile diese Einstellungen unter einem Namen speichern, z. B. „Brother 90 × 29“.
3. Zum Wechsel ein gespeichertes Profil wählen und „Gewähltes Profil verwenden“ anklicken.
4. Papierformat und Ausrichtung auch im Windows-Druckertreiber prüfen und eine neutrale Druckprobe durchführen.

Gespeichert werden App-Druckerwahl, Papier und Layout. Windows-Treiber werden nicht umkonfiguriert. Referenzierte Logo-Dateien müssen am gespeicherten lokalen Pfad vorhanden bleiben.

## Zuerst kostenlos testen

1. Unter Einstellungen den CSV-Ordner wählen. Die App muss geöffnet bleiben.
2. Unter Versand **Testlauf ohne Kauf/Druck** eingeschaltet lassen (Standard bei jedem App-Start).
3. Ein Limit eintragen, z. B. 10,00 Euro. Im Testlauf simuliert es nur das Porto.
4. **Automatisch verarbeiten** einschalten. Erst danach eine neue CSV mit neuer, eindeutiger Lieferscheinnummer aus Wawi erzeugen.
5. Nach etwa 5–10 Sekunden stabiler Datei wird sie eingelesen. Unter **Status** muss „Testlauf“ stehen. Es gibt weder Postkauf noch Druckauftrag.

Bereits vor der Aktivierung vorhandene Dateien/Sendungen werden nicht automatisch abgearbeitet. Zum Test vorhandener Sendungen diese mit Strg/Shift markieren und **Auswahl verarbeiten …** verwenden. Die Sammelübersicht zeigt Anzahl und Gesamtporto vor dem Start.

## Kostenpflichtig kaufen und drucken

1. Automatik ausschalten. Post anmelden, Drucker und neutrale Druckprobe prüfen.
2. Haken bei **Testlauf ohne Kauf/Druck** entfernen. Ein bewusst gewähltes Limit setzen.
3. Entweder **Automatisch verarbeiten** aktivieren und die einmalige Freigabe bestätigen, oder vorhandene Sendungen markieren und **Auswahl verarbeiten …** bestätigen.
4. Zunächst nur eine echte Sendung verarbeiten. Die App kauft kostenpflichtig und übergibt den Druckauftrag an Windows. Danach Abbuchung, Archiv und den physischen Ausdruck kontrollieren.

Neue CSV-Lieferscheine werden im aktivierten Livebetrieb ohne weitere Einzelbestätigung gekauft und gedruckt. Der Automatikdruck ist unabhängig vom bisherigen Haken „Nach dem Kauf sofort drucken“, der weiterhin für manuelle Käufe gilt.

Während eines Laufs sind Testmodus und Limit gesperrt. **Pause** verhindert den nächsten Auftrag; der laufende wird beendet. **Fortsetzen** behält das verbrauchte Budget bei. Das Budget zählt vor jedem Kaufversuch reserviertes Porto, auch bei unklaren Fehlern; es ist keine Kontostandsanzeige. Beim Erreichen des Limits pausiert die Verarbeitung. Für ein neues Budget ausschalten, Rest prüfen und bewusst einen neuen Lauf starten.

Ausschalten verwirft die wartende Liste, beendet aber keinen bereits laufenden Auftrag. Nach Neustart ist Automatik aus. Konto-/Konfigurationswechsel und Import-/Kauf-/Download-/Druckfehler stoppen den Lauf. Bereits versuchte Käufe sind im Journal gegen erneuten Kauf gesperrt. Nicht durch Umbenennen der Lieferscheine umgehen. Bezahlte Marken im Archiv prüfen und bei Bedarf erneut herunterladen/drucken.

**Druck übergeben** bestätigt nur die Übergabe an Windows. Es bestätigt keinen physischen Ausdruck: Bei Papiermangel oder Offline-Drucker Windows-Warteschlange kontrollieren. Die App ist kein Windows-Hintergrunddienst.

## Wawi-Sammelrückimport

1. Erst tatsächlich versandte Käufe im Archiv mit Strg/Shift markieren.
2. **Wawi-Sammeldatei erstellen** wählen, tatsächliches Versanddatum eingeben und Versand bestätigen.
3. Die App öffnet den Dateiordner und kopiert den Dateipfad in die Zwischenablage. Eine UTF-8-CSV mit Semikolon und einer Kopfzeile enthält alle ausgewählten Käufe desselben Postkontos.
4. In JTL-Wawi eine Vorlage für den Versanddatenimport konfigurieren: Lieferschein → ID-Nummer, Trackingnummer → Tracking-Nr, Versanddatum → Versanddatum, Versandinfos → Versandinfos. Erste Zeile als Kopfzeile behandeln.
5. Den richtigen Mandanten wählen und die Importvorschau für eine Sendung kontrollieren. Erst dann importieren. Der Import kann Versandstatus und Kundenbenachrichtigungen auslösen.

Keine direkte Datenbankänderung und keine automatische Bestätigung eines erfolgreichen Wawi-Imports. Ohne echte Trackingnummer bleibt das Feld leer; eine Marken-ID wird nicht als Tracking erfunden. Dieselbe Datei nicht mehrfach importieren. Ein anderes Datum für bereits exportierte Käufe wird blockiert.

Diese Zuordnung gilt für normale Wawi-Lieferscheine. WMS-Pakete benötigen eine andere Referenz und sind hier nicht unterstützt. Siehe auch Wawi-Import-Anleitung.txt.

## Adressetikett – nur Entwurf

Unter Versand genau eine Sendung auswählen, dann Drucklayout → **Adressetikett als Entwurf ansehen**. Das PDF im Format 102 × 152 mm zeigt die Empfängeradresse und einen neutralen Platzhalter. Es enthält keine gekaufte Marke und ist ausdrücklich nicht zum Frankieren geeignet. Der echte kombinierte Post-Ausgabemodus ist noch nicht freigegeben.

## Testgrenzen

Automatisierte Entwicklungstests verwenden simulierte Post-Antworten und Drucker. Ein Windows-Build prüft Installation, installierten EXE-Start, Dialoge, Desktop-Verknüpfung und Deinstallation. Echte Postkäufe, physischer Etikettendruck und Import in deine Wawi-Installation müssen in der eigenen Umgebung mit einer Sendung geprüft werden. Der hinterlegte Preisstand endet am 31.12.2026; danach blockiert die App neue Käufe bis zur Aktualisierung.
