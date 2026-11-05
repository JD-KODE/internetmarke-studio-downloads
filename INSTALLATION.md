# Internetmarke Studio 0.16.0 – öffentliche Beta

Kostenlose Windows-App für das Einlesen passend formatierter JTL-CSV-Dateien, den Kauf einzelner Internetmarken über die eigene Deutsche-Post-Portokasse und den Etikettendruck. Eigenständiges Community-Projekt; kein offizielles Produkt von JTL oder Deutsche Post und keine bestätigte Zertifizierung durch diese Anbieter.

**Beta: Installation und Nutzung erfolgen auf eigenes Risiko. Fehler sind möglich. Vor produktivem Einsatz Daten sichern und den gesamten Ablauf mit einer einzelnen Sendung prüfen. Eine fehlerfreie Funktion auf allen PCs, JTL-Versionen und Druckern wird nicht zugesichert. Gesetzliche Ansprüche bleiben unberührt.**

**Echte Portokosten:** Die Software ist kostenlos, Internetmarken sind kostenpflichtig. Der Kaufbutton löst den verbindlichen Kauf aus – ohne zusätzliche Bestätigungsabfrage. Verbindungsprüfung und neutrale Druckprobe kaufen keine Marken. CSV-Import ohne aktivierte Live-Automatik kauft keine Marken. Eine ausdrücklich aktivierte Live-Automatik kauft neue CSV-Sendungen kostenpflichtig ohne Einzelrückfrage.

## Marken ohne CSV kaufen

Links **Marken kaufen** öffnen, Briefart und Menge wählen und dem Warenkorb hinzufügen. Gesamtpreis prüfen, optional „Nach dem Kauf alle Marken drucken“ aktivieren und **Kostenpflichtig kaufen** wählen. Der CSV-Testmodus gilt nicht für diesen Kaufbutton. Bis zu 100 Marken pro Bestellung; echte Käufe werden nacheinander ausgeführt und einzeln archiviert.

Unter **Meine Bestellungen** lassen sich noch ungedruckte Marken gemeinsam drucken. Bei Fehlern Archiv und Druckwarteschlange prüfen. „Rest kaufen“ kauft nur noch nicht gestartete Marken nach Bestätigung. Shop-Marken haben keinen JTL-Lieferschein und sind vom Wawi-Rückexport ausgeschlossen. CSV-Ordner und JTL-Export sind nur für den Versandbereich erforderlich.

## Weitere Funktionen

CSV-Assistent, Versandregeln, Druckerprofile, Sammelverarbeitung, Automatik mit Pause/Budget/Testlauf und Wawi-Sammelrückdateien. Enthält den Drucklayout-KeyError-Fix aus 0.15.1. **[Neue Funktionen Schritt für Schritt](BETA-ANLEITUNG.md)**.

## Download und Voraussetzungen

- [Download Version 0.16.0](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.16.0)
- [Neueste Version](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest)
- Windows 10/11 in einer x64-kompatiblen Umgebung, Internetverbindung und installierter Windows-Druckertreiber.
- Eigene freigeschaltete Deutsche-Post-API-Zugangsdaten (API Key und API Secret) sowie Portokasse-Benutzer/E-Mail und Passwort. Ein Portokasse-Konto allein ersetzt die API-Freischaltung nicht.
- Nur für CSV-Versand: JTL-Export im unten beschriebenen CSV-Format. Eine pauschale Kompatibilität mit beliebigen JTL-Exporten wird nicht zugesichert.

## Einrichtung für Einsteiger – bitte der Reihe nach

**Für diese Einrichtung Automatik ausgeschaltet lassen. Bis einschließlich Schritt 6 wird keine Briefmarke gekauft. Der manuelle Kaufbutton in Schritt 7 kostet Porto.** Die App ist eine Beta: Nutzung auf eigenes Risiko. Vor Änderungen an einer vorhandenen Installation eine Datensicherung erstellen.

### 1. Das Programm herunterladen und installieren

1. Öffne die [Downloadseite für Version 0.16.0](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.16.0).
2. Suche auf der Seite den Bereich **Assets**. Das ist die Liste der herunterladbaren Dateien; gegebenenfalls aufklappen.
3. Klicke auf **Internetmarke-Studio-Setup-0.16.0.exe**. Die Dateien mit „Source code“ brauchst du nicht. Für den Download ist kein GitHub-Konto nötig.
4. Öffne deinen Windows-Ordner **Downloads** und doppelklicke auf die heruntergeladene Datei.
5. Folge den Schritten im Installationsfenster. Wähle die Desktopverknüpfung aus, falls sie angeboten wird.
6. Starte danach **Internetmarke Studio** über die Verknüpfung oder über das Windows-Startmenü.

Python musst du nicht installieren. Du musst auch keine BAT-Datei starten.

**Windows zeigt eine Warnung?** Der Installer ist noch nicht digital signiert. Wenn du bewusst die Datei aus dem oben verlinkten Repository heruntergeladen und geprüft hast, kannst du bei SmartScreen gegebenenfalls **Weitere Informationen → Trotzdem ausführen** wählen. Schalte den Windows-Schutz nicht insgesamt ab.

**Das sollte jetzt zu sehen sein:** das Programm und bei der ersten Einrichtung das Fenster „Willkommen bei Internetmarke Studio“. Klicke dort auf **Weiter**.

### 2. Die vier Zugangsdaten für die Post bereitlegen

Die App braucht zwei Arten von Zugangsdaten:

| Feld im Programm | Was du dort einträgst |
| --- | --- |
| API Key | Den technischen Zugangsschlüssel, den du für deinen freigeschalteten Post-API-Zugang erhalten hast. |
| API Secret | Den dazugehörigen geheimen Schlüssel. Das ist nicht dein normales Passwort. |
| Portokasse E-Mail | Die E-Mail-Adresse deines Portokasse-Kontos. |
| Passwort | Das Passwort dieses Portokasse-Kontos. |

**Was bedeutet API?** Damit ist der technische Zugang gemeint, über den das Programm mit der Deutschen Post kommuniziert. Die Portokasse ist das Konto, über das deine Briefmarken bezahlt werden.

**Du hast nur E-Mail und Passwort, aber keinen API Key und kein API Secret?** Dann fehlt noch der technische Zugang. Die Installation allein richtet ihn nicht ein. Kläre mit der Deutschen Post die Freischaltung für die Internetmarke-Schnittstelle und die zugehörigen Zugangsschlüssel. Eine mögliche Anfrage lautet: „Ich möchte Internetmarken über eine eigene Windows-Anwendung kaufen. Wie erhalte ich einen freigeschalteten Internetmarke-API-Zugang mit API Key und API Secret für meine Portokasse?“ Warte auf die Freischaltung, bevor du echte Käufe versuchst.

Die Beta ist an dieser Stelle noch nicht vollständig ohne technische Vorbereitung nutzbar. JTL-Zugangsdaten gehören nicht in diese vier Felder. Poste die Schlüssel und Passwörter niemals im Forum.

### 3. Das Programm mit der Post verbinden

1. Trage im Einrichtungsschritt **Post verbinden** die vier Angaben in die passenden Felder ein.
2. Klicke auf **Verbindung prüfen (kein Kauf)**.
3. Warte auf die Rückmeldung im Programm. Falls die Post eine Bestätigung per E-Mail verlangt, öffne dein Postfach, bestätige die Freigabe und prüfe die Verbindung anschließend erneut.
4. Wenn die Anmeldung funktioniert, kannst du **Zugang geschützt speichern** anklicken.
5. Wenn du dich später nicht jedes Mal selbst anmelden möchtest, setze danach das Häkchen bei **Automatisch anmelden (nach Speichern)**.
6. Klicke auf **Weiter**.

**Wenn die Anmeldung nicht funktioniert:** Prüfe zuerst, ob alle vier Angaben stimmen und der API-Zugang tatsächlich freigeschaltet ist. Nicht auf Kaufen klicken. Die Verbindungsprüfung selbst kostet kein Porto.

### 4. Einen Ordner für deine Versanddateien auswählen

Eine **CSV-Datei** ist eine einfache Tabelle mit den Daten deiner Sendungen. JTL muss diese Datei zunächst exportieren. Internetmarke Studio liest sie dann aus einem Ordner ein.

1. Öffne den Windows-Datei-Explorer, zum Beispiel mit **Windows-Taste + E**.
2. Öffne **Dokumente**.
3. Erstelle dort einen neuen Ordner, zum Beispiel **Internetmarke-CSV**: Rechtsklick auf eine freie Stelle → **Neu → Ordner**, Namen eingeben.
4. Kehre zum Einrichtungsfenster der App zurück.
5. Klicke auf **CSV-Ordner auswählen** und wähle den gerade angelegten Ordner. In der normalen Programmoberfläche heißt die Auswahl **Exportordner wählen**.
6. Klicke auf **Weiter**.

Verwende diesen Ordner ausschließlich für den CSV-Austausch. Die App kann erledigte, alte CSV-Dateien nach Sicherung automatisch entfernen; Details stehen weiter unten.

**Wichtig für JTL:** Das Auswählen des Ordners erstellt noch keinen Export in JTL. Dein JTL-Export muss eine Datei mit den vorgegebenen Spalten erzeugen und in diesem Ordner speichern. Eigene Spalten lassen sich unter Einstellungen → CSV-Assistent & Versandregeln zuordnen und als Profil speichern. Wenn du noch keine passende Exportvorlage hast, lass sie anhand des CSV-Schemas weiter unten einrichten. Für genaue Klicks innerhalb von JTL werden deine JTL-Version und die bisherige Exportart benötigt; eine universelle Anleitung dafür wäre unzuverlässig.

### 5. Drucker und Papier einstellen

1. Schalte deinen Drucker ein und lege die Etiketten beziehungsweise das Papier ein.
2. Der Drucker muss in Windows bereits eingerichtet sein. Wenn er dort noch fehlt, installiere zuerst den Treiber des Druckerherstellers.
3. Klicke im Einrichtungsschritt **Drucker und Layout** auf **Drucker wählen** und wähle deinen Drucker.
4. Klicke auf **Papier wählen** und stelle die Größe deines tatsächlich eingelegten Papiers ein.
5. Stelle dieselbe Größe und Ausrichtung auch in den Windows-Druckeinstellungen dieses Druckers ein.

**Beispiel – nur für dieses Material:** Brother QL-800 mit DK-11201: **90 × 29 mm, Querformat**. Für andere Etiketten wählst du deren eigene Größe. Breite und Höhe stehen meist auf der Verpackung.

### 6. Kostenlos ausprobieren, ob der Druck passt

1. Klicke im Einrichtungsfenster auf **Druckprobe**. Später findest du die Funktion unter **Drucklayout → Neutrale Druckprobe**.
2. Prüfe den Ausdruck: Ist alles vollständig auf dem Papier? Ist nichts abgeschnitten? Stimmt die Ausrichtung?
3. Falls etwas nicht passt, korrigiere Papierformat und Ausrichtung in App und Druckertreiber. Wiederhole dann die Druckprobe.
4. Wenn die Probe passt, klicke auf **Weiter** und anschließend auf **Einrichtung abschließen**.

**Diese Probe ist keine gültige Briefmarke und kostet kein Porto.** Für den ersten echten Druck die Marke in Originalgröße lassen und nicht mit Logos oder Text überdecken.

### 7. Die erste echte Sendung bearbeiten – ab hier kann Porto kosten

1. Lass aus JTL zunächst **nur eine echte Sendung** im geforderten CSV-Format in den ausgewählten Ordner exportieren.
2. Lass Internetmarke Studio geöffnet. Nach ungefähr fünf Sekunden sollte die Sendung in **Versand** erscheinen.
3. Prüfe Empfänger, Lieferscheinnummer, Versandart und Preis. Nutze nicht die fiktive Beispieladresse für einen echten Kauf.
4. Entscheide, ob nach dem Kauf automatisch gedruckt werden soll. Wenn du zunächst nur die Marke kaufen möchtest, lasse den automatischen Druck ausgeschaltet.
5. **Erst wenn alles stimmt, klicke einmal auf den Kaufbutton mit dem Preis. Dieser Klick kauft verbindlich – es kommt keine zweite Nachfrage.**
6. Warte auf das Ergebnis. Bei Bedarf kannst du die bereits vorhandene Marke im **Archiv** auswählen und über **Marke direkt drucken** drucken.

**Es erscheint keine Sendung?** Prüfe, ob die Datei wirklich im ausgewählten Ordner liegt, auf „.csv“ endet und das vorgegebene Format hat. Die App muss laufen. Ohne aktivierte Live-Automatik kauft der Import keine Briefmarke.

**Die App meldet nach dem Kauf einen Downloadfehler?** Nicht erneut kaufen. Öffne **Archiv → Vorhandenen Kauf abrufen**. Bei einem Druckproblem zuerst die Windows-Druckwarteschlange prüfen und die vorhandene Marke verwenden.

**Vor dem Versenden:** Die App druckt nur die Frankierung, nicht die Empfängeradresse. Bringe die Adresse separat auf der Sendung an. Die Marke muss vollständig und lesbar sein. Eine gekaufte Marke darf nur für eine Sendung verwendet werden.

### 8. Beim nächsten Start

Wenn du die Zugangsdaten gespeichert und die automatische Anmeldung aktiviert hast, meldet sich die App automatisch an. Den CSV-Ordner musst du nicht erneut auswählen. Neue passende Dateien werden eingelesen, solange das Programm läuft. **Automatik ist nach jedem Neustart aus.** Manuelle Käufe sind möglich; die Live-Automatik muss bewusst neu aktiviert werden.

## CSV-Format und automatisches Einlesen

Semikolon als Trennzeichen, eine Kopfzeile, zwölf Spalten in dieser Reihenfolge:

```csv
lieferschein;versandart;firma;firmenzusatz;vorname;nachname;adresszusatz;zu_haenden;strasse;plz;ort;land
"TEST-001";"Deutsche Post: Kompaktbrief";"";"";"Erika";"Musterfrau";"";"";"Musterstraße 5";"01067";"Dresden";"DE"
```

[Beispiel-CSV](Beispiel-JTL.csv) – ausschließlich fiktive Testdaten. Nicht für einen echten Kauf verwenden.

Ohne eigenes Profil gilt dieses Schema. Andere Spaltennamen ordnest du im CSV-Assistenten anhand einer Beispiel-Datei zu. UTF-8 (auch mit BOM), Windows-1252 und UTF-16 mit BOM werden unterstützt. Lieferscheinnummern müssen eindeutig bleiben. Postleitzahlen als Text mit führenden Nullen erhalten. Unterstützt werden deutsche Empfänger (DE) sowie Kompaktbrief, Großbrief und Maxibrief. Straße, Ort, gültige fünfstellige PLZ und Name/Firma müssen vorhanden sein.

Die App prüft den gewählten Ordner etwa alle fünf Sekunden, solange sie läuft. Neue bzw. geänderte, fertig geschriebene CSV-Dateien werden eingelesen. Der Ordner bleibt nach Neustart gespeichert. Doppelte Lieferscheine werden berücksichtigt; bei aktivierter Live-Automatik werden neue Sendungen anschließend kostenpflichtig gekauft und gedruckt. Ohne diesen Modus bleibt der Import kostenlos.

## Kauf, Druck und Fehlerbehandlung

- Die App erstellt **Portoetiketten ohne Empfängeradresse**. Empfängeranschrift separat auf der Sendung anbringen.
- Sammelverarbeitung: Sendungen mit Strg/Shift markieren → Auswahl verarbeiten. Anzahl und Gesamtporto vor dem Start prüfen. Testlauf ist standardmäßig aktiv. Livebetrieb kauft kostenpflichtig.
- Bei „gekauft, aber nicht heruntergeladen“: **Archiv → Vorhandenen Kauf abrufen**. Nicht erneut kaufen.
- Bei Druckfehler: Windows-Druckwarteschlange prüfen. Eine bereits vorhandene Marke über **Marke direkt drucken** ausgeben; keinen neuen Kauf auslösen. Dieselbe Marke darf nicht für mehrere Sendungen verwendet werden.
- Bei ungeklärtem Kaufstatus zuerst Portokasse und Archiv prüfen. Das Kaufjournal nicht löschen und nicht durch neue Lieferscheinnummern umgehen.
- Eine vollständige Marke in Originalgröße verwenden. Matrixcode und übrige Bestandteile dürfen nicht abgeschnitten, verdeckt oder unleserlich sein. Freie Layouts können Warnungen auslösen; diese blockieren den Druck nicht. Ein speicherbares Layout ist daher keine Bestätigung postalischer Gültigkeit.
- Die Dublettenprüfung gilt für das lokale Journal. Sie schützt nicht über unabhängige PCs, andere Programme oder gelöschte Journale hinweg.

## Archiv, Aufräumen und Datensicherung

Das Archiv ist durchsuchbar. Erledigte Einträge mit vorhandener Originalmarke werden nach 30 Tagen gesichert und ausgeblendet; das Kaufjournal bleibt zur Dublettenprüfung erhalten.

CSV-Dateien werden nur nach Sicherung entfernt, wenn sie älter als 30 Tage, erfolgreich importiert und unverändert sind und alle zugehörigen Käufe abgeschlossen vorliegen. Unverarbeitete oder geänderte Dateien bleiben erhalten. Das ist keine pauschale Löschung des gesamten Ordners.

Unter **Einstellungen → Datensicherung erstellen** regelmäßig sichern. Daten liegen unter `%LOCALAPPDATA%\MyBeltInternetmarkeDirekt`. Sicherungen enthalten personenbezogene Daten und sind vertraulich zu behandeln. Die Deinstallation lässt Benutzerdaten bestehen. Alte und neue App nicht gleichzeitig verwenden. Die frühere Demo 0.12 verwendet separate Daten.

## Updates

Ab Version 0.14.0 unter **Einstellungen → Updates** nach neuen Versionen suchen. Die Suche beim Start ist optional; die Installation erfolgt erst nach Bestätigung. Das Update wird aus dem öffentlichen GitHub-Repository geladen und anhand der bereitgestellten Prüfsumme geprüft.

Ältere Versionen ohne Updatefunktion einmal manuell durch Installation des aktuellen Setups aktualisieren. Vorher sichern und die App schließen. Bestehende Daten der bisherigen Live-App sollen erhalten bleiben.

## Datenschutz, Grenzen und Feedback

Adressdaten und Kaufjournal werden lokal gespeichert und sind nicht vollständig verschlüsselt. Gespeicherte Post-Zugangsdaten sind über Windows DPAPI an den Windows-Benutzer gebunden. Eine kopierte Sicherung macht diese Zugangsdaten nicht automatisch auf einem neuen PC nutzbar. Für Post-Funktionen wird die Post-API kontaktiert, für Updates GitHub und beim Spendenbutton PayPal. Keine Telemetrie implementiert.

Es gibt keinen gemeinsamen Mehrplatzbetrieb und keinen direkten Zugriff auf die JTL-Datenbank. Drucker- und JTL-Versionen müssen im eigenen Ablauf erprobt werden. Automatisierte Tests ersetzen keinen echten Druck- und Versandtest. Die in 0.16.0 hinterlegten Portopreise sind zeitlich begrenzt; ab 2027 ist für weitere Käufe eine aktualisierte Preisversion erforderlich.

Fehler bitte mit App-Version, Windows-Version, JTL-Version, Druckermodell, Papierformat, Reproduktionsschritten und bereinigter Fehlermeldung melden. Keine Passwörter, API-Schlüssel, Kundenadressen oder scannbaren Internetmarken öffentlich posten.

Die Nutzung ist kostenlos. Wer sich bedanken möchte, kann den freiwilligen PayPal-Spendenbutton in der App verwenden. Eine Spende ist keine Voraussetzung für die Nutzung.
