# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image wolke ="wolke.png"
image black = "#ffffff"
image white = "#000"
image logo = "TeamTsukiLogo.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define akira = Character('Akira', color="#FF66E5")
define takashi = Character('Takashi', color="#0080FF")
define yuki = Character('Yuki', color="#8000FF")
define akuya = Character('Frau Akuya', color="#64FE2E")
define unbekannt = Character('???', color="#FFFFFF")



# Hier beginnt das Spiel.
transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_white:
    on show:
        alpha 0
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

label splashscreen:
    scene black
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)

    show logo at transform_logo
    $ renpy.pause(6, hard=True)

    hide logo
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(3, hard=True)


    return

label start:
    scene wolke
    unbekannt "Hast du deine Klasse gefunden?"

    unbekannt "Ehm.."

    unbekannt "Oh, Ich bin in der Klasse B-1"

    unbekannt "Schade.. Ich bin in der Klasse A-1"

    unbekannt "Ja.. Dafür sehen wir uns ja im Lese-Klub."

    unbekannt "Stimmt."

    unbekannt "Ist jemand von deiner Klasse im Lese-Klub?"

    unbekannt "Ja.. ein Typ Namens ´Takashi´."

    unbekannt "Okay.. Ich muss dan jetzt ins Klassenzimmer. Bis Später, Akira"

    akira "Ja, Bis Später, Yuki"

    yuki "Bis Später"

    akira "Ich sollte Langsam auch ins Klassenzimmer."

    akuya "Guten Morgen, Liebe Mitschülerinen und Mitschüler. Ich bin Frau Akuya, eure Lehrerin."




    takashi "Test"

    return
