# Internetmarke Studio 0.20.0 – Einrichtung in einfachen Schritten

## 1. Herunterladen und installieren
[Aktueller Download](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest) → unter **Assets** die **Internetmarke-Studio-Setup-0.20.0.exe** wählen. Nicht „Source code“. Setup starten und Installation abschließen. Desktop-Verknüpfung wird angelegt; Python oder eine BAT-Datei sind nicht nötig. Installer noch unsigniert; Quelle prüfen und Windows-Schutz nicht generell abschalten.

**Bereits installiert?** Zuerst Datensicherung erstellen. App über Rechtsklick auf das Symbol neben der Windows-Uhr → **Beenden** schließen. Setup über die vorhandene Installation installieren. Kein Löschen des Datenordners. Ab 0.19.0 kann das Setup das geordnete Beenden anfordern; laufenden Vorgang abwarten und danach **Weiter** erneut wählen.

## 2. Post verbinden
Im Einrichtungsassistenten API Key, API Secret, Portokasse-E-Mail und Passwort eintragen. API-Zugang muss bei der Deutschen Post freigeschaltet sein; E-Mail und Passwort allein reichen nicht. **Verbindung prüfen** kauft kein Porto. Zugang optional geschützt speichern und automatische Anmeldung aktivieren. Auf einem neuen PC Zugang neu eingeben.

## 3. CSV nur bei Bedarf einrichten
Für JTL-Versand den Export der Versand-CSV in JTL separat konfigurieren. In der App den Zielordner auswählen und über den CSV-Assistenten Spalten/Versandarten zuordnen. [Beispiel-CSV](Beispiel-JTL.csv). Neue Dateien werden automatisch eingelesen; Einlesen allein kauft kein Porto.
Ohne CSV direkt den **Marken-Shop** verwenden.

## 4. Drucker einrichten
Im Assistenten oder unter **Drucklayout → Drucker einrichten und kalibrieren**:
1. Installierten Windows-Drucker auswählen.
2. Vorlage passend zum eingelegten Papier auswählen.
3. Dieselbe Größe und Ausrichtung im Windows-Treiber einstellen; ein Exemplar, keine Seitenanpassung.
4. Neutrale Kalibrierprobe drucken – kein Porto. Die Messlinie muss 20 mm lang sein.
5. Bei Versatz mit Pfeilen um je 0,2 mm oder per Millimetereingabe korrigieren. Bei falscher Größe zuerst den Treiber prüfen.
6. Optional Logo/mehrzeilige **Absenderadresse** im Layouteditor ergänzen. Es ist eine feste Adresse für jeden Ausdruck, keine automatische Empfängeradresse. Überlappungen/Anschnitt in der Vorschau prüfen. Für kleine Etiketten ggf. separates Adressetikett oder größeres Format verwenden.
7. Einstellungen bei Bedarf als Druckerprofil speichern.

Vorlagen: Brother QL/DK-11201 90 × 29 mm quer (z. B. QL-800), DK-11202 100 × 62 mm quer, allgemeine Etiketten 100 × 50 und 102 × 152 mm sowie A4-Einzelaufdruck. Treiber werden nicht installiert, Rollen nicht automatisch erkannt. Vorlagen am eigenen Gerät testen.

## 5. Arbeitsweise wählen
**Versand:** Sendung auswählen → Preis/Produkt prüfen → kaufen, optional sofort drucken.
**Marken-Shop:** Briefart, Zusatzleistung und Menge wählen → Warenkorb → Gesamtpreis prüfen → kostenpflichtig kaufen.
**Automatik:** Zunächst Testlauf ohne Kauf/Druck ausprobieren. Für Echtbetrieb Automatik ausschalten, Testlauf abwählen, speichern und Automatik bewusst aktivieren. Danach werden offene und neue freigegebene CSV-Sendungen gekauft und gedruckt.
Der Testlauf gilt nicht für Einzelkauf oder Marken-Shop. Ausgabenlimit optional, standardmäßig keines. Nach Programmstart bleibt die Kaufautomatik aus.

## 6. Aufbewahrung bestimmen
Im letzten Einrichtungsschritt oder **Weitere Aktionen → Datenschutz & Diagnose → Aufbewahrung und Löschfristen**. CSV, Kundendaten, Markendateien und app-eigene Sicherungen getrennt aktivieren; empfohlen 30 Tage. Erst **Vorschau – nichts löschen** prüfen.
Ab 0.20.0 beginnen aktivierte Fristen automatisch nach erfolgreicher Druckübergabe. Auch bereits gespeicherte Regeln gelten dafür. **0 Tage kann Daten sofort beim nächsten Lauf löschen – auch bei Papierstau.**

## 7. Erste echte Sendung prüfen
Eine Sendung bewusst kaufen, Papierausdruck und Empfängeradresse prüfen. Jede Marke nur einmal verwenden. „Druck übergeben“ bestätigt nur die Übergabe an Windows. Bei Fehlern erst Archiv und Druckwarteschlange prüfen, nicht erneut kaufen.
[Weitere Bedienung, Grenzen und Datenschutz](BETA-ANLEITUNG.md)
