# Internetmarke Studio 0.14.0 – öffentliche Beta

Kostenlose Windows-App für das Einlesen passend formatierter JTL-CSV-Dateien, den Kauf einzelner Internetmarken über die eigene Deutsche-Post-Portokasse und den Etikettendruck. Eigenständiges Community-Projekt; kein offizielles Produkt von JTL oder Deutsche Post und keine bestätigte Zertifizierung durch diese Anbieter.

**Beta: Installation und Nutzung erfolgen auf eigenes Risiko. Fehler sind möglich. Vor produktivem Einsatz Daten sichern und den gesamten Ablauf mit einer einzelnen Sendung prüfen. Eine fehlerfreie Funktion auf allen PCs, JTL-Versionen und Druckern wird nicht zugesichert. Gesetzliche Ansprüche bleiben unberührt.**

**Echte Portokosten:** Die Software ist kostenlos, Internetmarken sind kostenpflichtig. Der Kaufbutton löst den verbindlichen Kauf aus – ohne zusätzliche Bestätigungsabfrage. CSV-Import, Verbindungsprüfung und neutrale Druckprobe kaufen keine Marken.

## Download und Voraussetzungen

- [Download Version 0.14.0](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/tag/v0.14.0)
- [Neueste Version](https://github.com/JD-KODE/internetmarke-studio-downloads/releases/latest)
- Windows 10/11 in einer x64-kompatiblen Umgebung, Internetverbindung und installierter Windows-Druckertreiber.
- Eigene freigeschaltete Deutsche-Post-API-Zugangsdaten (API Key und API Secret) sowie Portokasse-Benutzer/E-Mail und Passwort. Ein Portokasse-Konto allein ersetzt die API-Freischaltung nicht.
- JTL-Export im unten beschriebenen CSV-Format. Eine pauschale Kompatibilität mit beliebigen JTL-Exporten wird nicht zugesichert.

## Installation und erste Einrichtung

1. Auf der Release-Seite unter **Assets** die Datei **Internetmarke-Studio-Setup-0.14.0.exe** herunterladen. Die GitHub-Dateien „Source code“ sind nicht der Installer.
2. Eine laufende ältere Version schließen. Bei einem Update vorher unter **Einstellungen → Datensicherung erstellen** eine Sicherung anlegen.
3. Setup starten und dem Installationsassistenten folgen. Desktopverknüpfung bei Bedarf auswählen. Python und BAT-Dateien sind nicht erforderlich.
4. Der Installer ist noch nicht digital signiert. Windows SmartScreen kann deshalb warnen. Nur beim bewusst geprüften Download aus dem oben verlinkten Repository gegebenenfalls **Weitere Informationen → Trotzdem ausführen** verwenden. Windows-Schutz nicht pauschal abschalten. Die veröffentlichte SHA256.txt dient zur Integritätsprüfung, nicht als unabhängiger Sicherheitsnachweis.
5. Internetmarke Studio über Startmenü oder Desktop starten und den Einrichtungsassistenten durchlaufen.
6. Eigene Post-Zugangsdaten eintragen und die Verbindung prüfen. Falls die Post eine Bestätigung per E-Mail verlangt, diese zunächst abschließen. Zugangsdaten können optional für den aktuellen Windows-Benutzer geschützt gespeichert werden; automatische Anmeldung ist optional.
7. Einen eigenen Ordner für den CSV-Austausch anlegen und in der App mit **Exportordner wählen** auswählen. Keine allgemeinen Dokumentenordner verwenden.
8. Unter **Drucklayout** den Drucker und das Papierformat festlegen. Dasselbe Format und dieselbe Ausrichtung im Windows-Druckertreiber einstellen. Beispiel: Brother QL-800 mit DK-11201: 90 × 29 mm, Querformat.
9. Zuerst **Neutrale Druckprobe** ausführen. Sie kostet kein Porto. Ausrichtung, Position, Randabstände und Lesbarkeit prüfen.
10. Erst danach eine echte Sendung importieren, Adresse, Versandart und angezeigten Preis prüfen und bewusst kaufen. Bei aktivem automatischem Druck wird anschließend gedruckt. Bei Unsicherheit zunächst nur kaufen und die vorhandene Marke anschließend im Archiv drucken.

## CSV-Format und automatisches Einlesen

Semikolon als Trennzeichen, eine Kopfzeile, zwölf Spalten in dieser Reihenfolge:

```csv
lieferschein;versandart;firma;firmenzusatz;vorname;nachname;adresszusatz;zu_haenden;strasse;plz;ort;land
"TEST-001";"Deutsche Post: Kompaktbrief";"";"";"Erika";"Musterfrau";"";"";"Musterstraße 5";"01067";"Dresden";"DE"
```

[Beispiel-CSV](Beispiel-JTL.csv) – ausschließlich fiktive Testdaten. Nicht für einen echten Kauf verwenden.

Der JTL-Export muss dieses Schema erzeugen; es gibt keine automatische Zuordnung beliebiger Spalten. UTF-8 (auch mit BOM), Windows-1252 und UTF-16 mit BOM werden unterstützt. Lieferscheinnummern müssen eindeutig bleiben. Postleitzahlen als Text mit führenden Nullen erhalten. Unterstützt werden deutsche Empfänger (DE) sowie Kompaktbrief, Großbrief und Maxibrief. Straße, Ort, gültige fünfstellige PLZ und Name/Firma müssen vorhanden sein.

Die App prüft den gewählten Ordner etwa alle fünf Sekunden, solange sie läuft. Neue bzw. geänderte, fertig geschriebene CSV-Dateien werden eingelesen. Der Ordner bleibt nach Neustart gespeichert. Doppelte Lieferscheine werden berücksichtigt; der Import selbst kauft niemals Porto.

## Kauf, Druck und Fehlerbehandlung

- Die App erstellt **Portoetiketten ohne Empfängeradresse**. Empfängeranschrift separat auf der Sendung anbringen.
- Kein automatischer Stapelkauf. Vor jedem Kauf die einzelne Sendung und den Preis prüfen.
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

Es gibt keinen gemeinsamen Mehrplatzbetrieb und keinen direkten Zugriff auf die JTL-Datenbank. Drucker- und JTL-Versionen müssen im eigenen Ablauf erprobt werden. Automatisierte Tests ersetzen keinen echten Druck- und Versandtest. Die in 0.14.0 hinterlegten Portopreise sind zeitlich begrenzt; ab 2027 ist für weitere Käufe eine aktualisierte Preisversion erforderlich.

Fehler bitte mit App-Version, Windows-Version, JTL-Version, Druckermodell, Papierformat, Reproduktionsschritten und bereinigter Fehlermeldung melden. Keine Passwörter, API-Schlüssel, Kundenadressen oder scannbaren Internetmarken öffentlich posten.

Die Nutzung ist kostenlos. Wer sich bedanken möchte, kann den freiwilligen PayPal-Spendenbutton in der App verwenden. Eine Spende ist keine Voraussetzung für die Nutzung.
