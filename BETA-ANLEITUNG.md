# Internetmarke Studio 0.20.0 – Funktionen und Bedienung

| Funktion | Nutzen und Bedienung |
|---|---|
| CSV-Import und Ordnerüberwachung | JTL-Exporte übernehmen; Spalten und Versandarten zuordnen. Neue Dateien werden eingelesen. Einlesen löst allein keinen Kauf aus. |
| Versand | Einzelne oder mehrere Sendungen bearbeiten; Kauf oben, Einstellungen separat. Nach Kauf in Versand bleiben. |
| Optionale Automatik | Nach bewusster Aktivierung offene Imports, frühere Testläufe und neue CSV verarbeiten. Bereits gekaufte, archivierte und unklare Vorgänge bleiben ausgeschlossen. |
| Marken-Shop ohne CSV | Standard-, Kompakt-, Groß- und Maxibrief DE, optional Einschreiben Einwurf oder Übergabe. Warenkorb und Mengen, bis zu 100 Marken pro Bestellung. |
| Guthaben | Oben in Versand und Marken-Shop mit Abrufzeitpunkt. Aktualisieren oder Post-Seite zum Aufladen öffnen; keine automatische Aufladung. |
| Drucken | Sofort nach Kauf oder später alle ungedruckten Shop-Marken. Einzelner Nachdruck im Archiv ohne erneuten Kauf. |
| Druckerassistent | Papier-Vorlagen, neutrale Probe, Kalibrierung und gespeicherte Druckerprofile. |
| Layout | Marke positionieren, eigenes Logo, Zusatztext und feste mehrzeilige Absenderadresse. Vorschau prüfen; Empfänger separat bzw. über Adressetikett. |
| Archiv und Suche | Käufe finden, vorhandenen Kauf erneut abrufen, Markennummern nachsehen und nachdrucken. Sendungen ohne Kauf archivieren und später zurückholen. |
| Wawi-Rückdatei | Für normale Lieferscheine; kein automatischer Import in JTL, nicht für WMS-Pakete oder Shop-Marken. |
| Hintergrundbetrieb | Symbol neben der Windows-Uhr: öffnen, pausieren, Automatik ausschalten, beenden. Optionaler Windows-Autostart. |
| Datenschutz | Getrennte optionale Löschregeln und Vorschau; Archiv zeigt früheste Löschdaten. |
| Sicherung und Diagnose | Passwortgeschützte manuelle Sicherung und Diagnoseexport ohne Kundenadressen/Zugangsdaten. |
| Updates und Hilfe | Updates in den Einstellungen; geordneter Abschluss laufender Vorgänge vor Installation. |
| Kostenlos | Alle Funktionen kostenlos. Porto kostenpflichtig; freiwillige PayPal-Spende möglich. |

## Automatik, Kauf und Hintergrund
Testlauf betrifft nur Automatik/Mehrfachauswahl; Einzelkauf und Shop-Kauf kosten echtes Porto. Für Live-Automatik Testlauf abwählen und ausdrücklich aktivieren. Ohne optionales Limit können freigegebene Sendungen bis zum verfügbaren Guthaben gekauft werden. Die Kaufautomatik bleibt nach jedem Programmstart aus. PC muss eingeschaltet und Windows-Benutzer angemeldet bleiben; kein Windows-Dienst. Pause/Beenden wartet den laufenden Vorgang ab.

Bei Teilfehlern im Shop Archiv und Windows-Warteschlange prüfen. „Rest kaufen“ berücksichtigt nur noch nicht gestartete Marken nach Bestätigung. Keine automatische Wiederholung unklarer Drucke. Marken werden einzeln gedruckt, nicht gemeinsam auf einem A4-Bogen.

## Löschfristen ab Version 0.20.0
Unter **Weitere Aktionen → Datenschutz & Diagnose → Aufbewahrung und Löschfristen**, auch in der Ersteinrichtung.
- Vier Kategorien: importierte CSV; Namen/Adressen; Markendateien/frühere Versuche; app-eigene automatische Sicherungen.
- Ohne Haken keine Löschung dieser Kategorie. Beim Einschalten 30 Tage vorgeschlagen, 0–3650 möglich; Sicherungen mindestens 1 Tag.
- Nach erfolgreichem Direktdruck setzt die App automatisch **Druck übergeben** und startet die aktivierten Fristen. Kein zusätzlicher Klick „Ausdruck geprüft“. Dies gilt auch für schon gespeicherte Regeln.
- Kauf ohne Druck, PDF-Öffnen und neutrale Probe starten keine Frist. Externer PDF-Druck kann nicht automatisch erfasst werden.
- Fehlgeschlagener/unterbrochener Druck startet keine Frist. Ein fehlgeschlagener Nachdruck hält sie an; erfolgreicher Nachdruck startet sie neu. Alte Bestätigungen aus 0.19 bleiben erhalten.
- CSV wird nur entfernt, wenn unverändert und alle enthaltenen Sendungen fällig sind. Gemeinsam genutzte Kundendaten warten auf alle zugehörigen Käufe.
- Archivspalten **CSV löschen ab / Kundendaten löschen ab / Marken löschen ab** zeigen den frühesten Termin. „Aus“ = deaktiviert; „Nach Druckübergabe“ = noch nicht freigegeben. Prüfungen/gesperrte Dateien können Löschung verzögern.
- Sicherungen werden nach Dateialter bereinigt, nur im App-Unterordner „sicherungen“. Externe Backups und JTL-Daten selbst verwalten.
- Bereinigung läuft nur bei laufender App, auch im Hintergrund.

**30 Tage empfohlen.** „Druck übergeben“ beweist keinen physischen Ausdruck. Bei 0 Tagen können Markendateien bereits vor einem tatsächlichen Papierausdruck entfernt werden. Entfernte Marken lassen sich in der App nicht mehr nachdrucken oder abrufen. Vorschau vor Aktivierung prüfen; bereits fällige Daten können beim nächsten Lauf entfernt werden.

Neue gespeicherte Regeln ersetzen die frühere 30-Tage-Aufräumsicherung. Ohne Speichern neuer Regeln bleibt das bisherige Verhalten bestehen.

## Datenschutz und Sicherung
Lokale Adressen, Kaufjournal, Marken und ältere/automatische Sicherungen sind nicht vollständig verschlüsselt. Zugangsdaten optional mit Windows-Benutzerschutz. Keine Telemetrie implementiert. Die Post erhält beim Kauf die technisch nötigen Daten; Datenschutzoptionen sind keine vollständige Anonymisierung.
Kaufstatus, Lieferschein sowie Kauf-/Marken-/Trackingkennungen bleiben als Doppelkaufschutz erhalten. Keine garantierte sichere Löschung aller Datenträgerspuren. Externe Kopien, Exporte und Betriebssystem-Backups separat verwalten.
Manuelle Sicherung als passwortgeschützte .imsbackup-Datei; Passwort separat aufbewahren. Entschlüsselung erzeugt ein vertrauliches ZIP, keinen automatischen Import. Auf einem anderen PC Post-Zugang neu eingeben.

## Fehlerhilfe und Grenzen
Gekauft ohne Download: vorhandenen Kauf im Archiv abrufen, nicht erneut kaufen. Druckproblem: Windows-Warteschlange kontrollieren, dann vorhandene Marke nachdrucken. Unklarer Kauf: Archiv und Portokasse prüfen. Journal nicht löschen oder Doppelkaufschutz durch neue Lieferscheinnummern umgehen.
CSV unterstützt Kompakt-, Groß- und Maxibrief DE; Standardbrief/Einschreiben zunächst im Marken-Shop. Kein gemeinsamer Mehrplatzbetrieb. Preisupdate ab 2027 nötig. Vorlagen sind keine Zusage für jeden Drucker/Treiber; Ausdrucke selbst testen. Kein offizielles Produkt von JTL oder Deutsche Post.

## Prüfung und Beta
200 automatisierte Windows-Tests, Installation, EXE-Start, alle neuen Assistentenschritte, Setup-Sperre und Deinstallation bestanden. Entwicklungstests ohne echte Käufe oder physische Ausdrucke. Installer unsigniert. Nutzung auf eigenes Risiko; gesetzliche Ansprüche bleiben unberührt.
Das unveränderte geprüfte Paket ist öffentlich freigegeben; die Beschriftung „Private Testversion“ stammt noch aus der Testphase.
