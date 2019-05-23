## Diese Datei enthält einige Optionen, die verändert werden können,
## um Ihr Ren'Py Spiel anzupassen. Sie enthält nur die häufigsten Optionen.
## Es gibt ziemlich viel, was angepasst werden kann.
##
## Zeilen, die mit zwei '#'-Zeichen beginnen, sind Kommentare und sollten
## nicht entfernt werden. Zeilen, die mit einem '#'-Zeichen beginnen,
## sind deaktivierte Codezeilen und können aktiviert werden, indem das
## Zeichen entfernt wird.

init -1 python hide:

    ## Sollen wir die Entwicklertools aktivieren? Das sollte auf
    ## "False" gesetzt werden, bevor das Spiel veröffentlicht wird,
    ## damit der Spieler mithilfe der Entwicklertools nicht schummeln kann.

    config.developer = True

    ## Hiermit wird die Breite und Höhe des Bildschirms festgelegt.

    config.screen_width = 1680
    config.screen_height = 1050

    ## Hiermit wird der Titel des Fensters festgelegt, wenn Ren'Py im
    ## Fenstermodus läuft.

    config.window_title = u"My First Love"

    # Hiermit wird der Name und die Version des Spiels festgelegt,
    # die in Tracebacks und anderen Protokollen festgehalten werden.
    config.name = "My First Love"
    config.version = "Beta 1.0"

    #########################################
    # Themes

    ## Hiermit lässt sich die Theme-Funktion anpassen. "themes.roundrect" ist
    ## ein Theme, das abgerundete Rechtecken verwendet. Es ist das einzige
    ## Theme, das derzeit unterstützt wird.
    ##
    ## Die Theme-Funktion läuft mit verschiedenen Parametern, die
    ## das Farbschema anpassen können.

    theme.roundrect(
        ## Theme: Roundrect
        ## Color scheme: Grape Jelly

        ## The color of an idle widget face.
        widget = "#c45693",

        ## The color of a focused widget face.
        widget_hover = "#5e2862",

        ## The color of the text in a widget.
        widget_text = "#ffffff",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#e59eae",

        ## The color of a disabled widget face.
        disabled = "#81859a",

        ## The color of disabled widget text.
        disabled_text = "#5e2862",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#8ea9b0",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "background2.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "background2.png",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## Diese Einstellungen lassen Sie das Fenster anpassen, welches Dialoge
    ## und Erzählungen enthält. Sie können es mit einer Grafik ersetzen.

    ## Der Hintergrund des Fensters. Im "Frame" sind die zwei Nummern
    ## jeweils die Größe des linken/rechten und des oberen/unteren
    ## Abstands.

    # style.window.background = Frame("frame.png", 12, 12)

    ## Der Rand ist der Freiraum, der das Fenster umgibt und wo der Hintergrund
    ## nicht zu sehen ist.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## "Padding" ist der Raum innerhalb des Fenster, wo der
    ## Hintergrund zu sehen ist.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Dies ist die Mindesthöhe des Fensters, inklusive des Randes
    ## und "Padding".

    # style.window.yminimum = 250


    #########################################
    ## Hiermit lässt sich die Platzierung des Hauptmenüs ändern.

    ## Um die Platzierung vorzunehmen, suchen wir uns einen
    ## Ankerpunkt auf einer anzeigbaren Position auf dem
    ## Bildschirm. Dann platzieren wir diesen so, damit
    ## beide Punkte an derselben Stelle sind.

    ## Ein Ankerpunkt kann als "integer" oder ein "floating point"
    ## Nummer angeben werden. Als "integer" wird die Nummer als eine
    ## Pixelanzahl von der oberen linken Ecke aus interpretiert. Als "floating point",
    ## wird die Nummer als ein Bruchteil der Grö0e der anzeigbaren
    ## Position oder des Bildschirms interpretiert.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Hiermit können Sie die Standard-Schriftart einstellen, die Ren'Py für den Text verwendet.

    ## Die Datei, die die Standard-Schriftart enthält.

    # style.default.font = "DejaVuSans.ttf"

    ## Die Standardgröße des Texts.

    # style.default.size = 22

    ## Bedenken Sie, dass dies nur die Größe von einigen Texten anpassen kann.
    ## Andere Schaltflächen haben ihren eigenen Stile.


    #########################################
    ## Mit diesen Einstellungen können Sie die Soundeffekte anpassen, die
    ## Ren'Py verwendet.

    ## Stellen Sie dies auf "False", wenn das Spiel keine Soundeffekte bietet.

    config.has_sound = True

    ## Stellen Sie dies auf "False", wenn das Spiel keine Musik bietet.

    config.has_music = True

    ## Stellen Sie dies auf "True", wenn das Spiel Sprachausgabe bietet.

    config.has_voice = False

    ## Soundeffekte, die verwendet werden, wenn auf Schaltflächen oder "Imagemaps" geklickt wird.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Soundeffekte, die verwendet werden, wenn Sie das Spielmenü aufrufen oder verlassen.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Ein Beispiel-Soundeffekt, der abgespielt werden kann, um die Lautstärke zu testen.

    # config.sample_sound = "click.wav"

    ## Musik, die abgespielt wird, während sich der Benutzer im Hauptmenü befindet.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Hilfe.

    ## Hiermit lässt sich die Einstellung der Hilfeoption in den Ren'Py Menüs einstellen.
    ## Das könnte sein:
    ## - Ein Label im Skript, wobei zum Label gesprungen wird,
    ##   um dem Benutzer die Hilfe anzuzeigen.
    ## - Eine Datei, die sich im Hauptverzeichnis befinden und die dann
    ##   in einem Browser geöffnet wird.
    ## - None, um die Hilfe zu deaktivieren.
    config.help = "README.html"


    #########################################
    ## Übergänge.

    ## Beim Aufrufen des Spielmenüs aus dem Spiel heraus.
    config.enter_transition = None

    ## Beim Verlassen des Spielmenüs zurück ins Spiel.
    config.exit_transition = None

    ## Beim Wechsel zwischen Menüs im Spielmenü.
    config.intra_transition = None

    ## Beim Aufrufen des Spielmenüs aus dem Hauptmenü heraus.
    config.main_game_transition = None

    ## Beim Zurückkehren zum Hauptmenü aus dem Spiel heraus.
    config.game_main_transition = None

    ## Beim Aufrufen des Hauptmenüs vom "Splashscreen".
    config.end_splash_transition = None

    ## Beim Aufrufen des Hauptmenüs, nachdem das Spiel beendet wurde.
    config.end_game_transition = None

    ## Beim Laden eines Spiels.
    config.after_load_transition = None

    ## Beim Aufrufen des Fensters.
    config.window_show_transition = None

    ## Beim Verbergen des Fensters.
    config.window_hide_transition = None

    ## Beim Anzeigen des NVL-Modus direkt nach dem ADV-Modus.
    config.adv_nvl_transition = dissolve

    ## Beim Anzeigen des ADV-Modus direkt nach dem NVL-Modus.
    config.nvl_adv_transition = dissolve

    ## Beim Aufrufen der Ja/Nein Abfrage.
    config.enter_yesno_transition = None

    ## Beim Verlassen der Ja/Nein Abfrage.
    config.exit_yesno_transition = None

    ## Beim Aufrufen einer Wiederholung.
    config.enter_replay_transition = None

    ## Beim Verlassen einer Wiederholung.
    config.exit_replay_transition = None

    ## Beim Wechsel einer Grafik mit einem "say statement" und "image attributes".
    config.say_attribute_transition = None

    #########################################
    ## Dies ist der Name des Verzeichnisses, wo die Spieldaten gelagert
    ## werden. (Dies muss früh festgelegt werden, bevor ein anderer "init code"
    ## aufgerufen wird, damit die persistenten Informationen im "init code" gefunden werden können.)
python early:
    config.save_directory = "My First Love-1558390014"

init -1 python hide:
    #########################################
    ## Standardwerte für Einstellungen.

    ## Anmerkung: Diese Optionen werden nur beim ersten Start
    ## übernommen. Damit sie ein zweites Mal übernommen werden,
    ## löschen Sie game/saves/persistent.

    ## Soll das Spiel im Vollbildmodus starten?

    config.default_fullscreen = False

    ## Die Standardzeit für die Textgeschwindigkeit in Buchstaben pro Sekunde. 0 bedeutet ohne Zeitverzögerung.

    config.default_text_cps = 0

    ## Die Standardzeit für den automatischen Vorlauf.

    config.default_afm_time = 10

    config.window_icon = "logo.png"
    config.windows_icon = "logo32.png"

    #########################################
    ## Weitere Anpassungen können hier eingefügt werden.
