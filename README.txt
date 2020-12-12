För att använda Zoom Quick Launch krävs vissa steg innan.
1. Installera python från https://www.python.org/downloads/
2. Döp om ändelsen på "run.txt" till "run.bat" och döp om "installDependencies.txt" i "installation" mappen till "installDependencies.bat".
3. Öppna "settings.txt" och se till att bredden och höjden på din skärm stämmer
3. Kör "installDependencies.bat"
4. Vid frågan, tryck "y" och sen "Enter" i command fönstret
5. Låt programmet köra. Efter 5 sekunder kan du stänga ned "Zoom enter password" rutan och öppna python programmet som har startas (se aktivitetsfältet)
6. Vänster klicka i programmet. Se bilden "Markering.png" i mappen "installation" för mer specifikt vart du ska trycka i programmet och vilken ordning.
7. Nu kan du köra "launch.bat" och välja bland listan av zoom länkar.

Om det inte fungerar kan det bero på att "delay" i "settings.txt" är för liten. Du kan behöva öka den några sekunder ifall zoom tar lång tid att starta.
I "zoomLinks.txt" kan man skriva in egna zoom länkar enligt denna syntaxen:
Namn på kurs;Länk;Lösenord
Det är viktigt med semicolon mellan värdena. Om länken inte har lösenord, skriv ett x där lösenordet skulle vara tex:
Matematisk analys;https://......com;x