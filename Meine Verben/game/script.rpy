label start: #bleiben
    stop audio
    scene bg lake
    play audio "Nature Sounds.mp3" fadein 2.0

    "Memorise three forms of verbs and choose the correct one for a sentence"

label bleiben_retry:
    scene bg lake

    "Bleiben — Blieb — (ist) Geblieben"

    window show
    "David ist noch eine Woche in Klagenfurt __?__"

    menu:
        "David ist noch eine Woche in Klagenfurt __?__"
        "gebleiben":
            "❌ Nah, das ist falsch! Noch einmal."
            jump bleiben_retry
        "gebliebt":
            "❌ Meinst du das ernst?!"
            jump bleiben_retry
        "geblieben":
            "👏 Gut gemacht!"
            "✅ David ist noch eine Woche in Klagenfurt geblieben."
            jump bringen

label bringen:

    scene bg village
    "Bringen — Brachte — (hat) Gebracht"

    "Mein Bruder hat mir heute morgen eine Kiste Mandarinen __?__"

    menu:
        "Mein Bruder hat mir heute Morgen eine Kiste Mandarinen __?__"
        "Brachte":
            "❌ Hey! Come on!"
            jump bringen
        "Gebracht":
            "👏 Super!"
            "✅ Mein Bruder hat mir heute Morgen eine Kiste Mandarinen gebracht."
            jump denken
        "Gebraucht":
            "❌ Oops! Noch einmal."
            jump bringen

label denken:

    scene bg street
    "Denken — Dachte — (hat) Gedacht"

    "Ich habe __?__, dass du zu Hause bist."

    menu:
        "Ich habe __?__, dass du zu Hause bist."
        "Gedacht":
            "👏 Sehr gut!"
            "✅ Ich habe gedacht, dass du zu Hause bist."
            jump essen
        "Gedenken":
            "❌ Bitte?"
            jump denken
        "Gedenken":
            "❌ Was hast du gesagt?"
            jump denken
    
label essen:
    scene bg supper
    "Now try to memorise the following sentences"

label essen_retry:

    scene bg supper
    "Essen — Aß — (hat) Gegessen"

    "Die Kinder haben schon in der Schule __?__"

    menu:
        "Gesessen":
            "❌ Was??? Was haben sie gemacht?"
            jump essen_retry
        "Gegessen":
            "👏 Ja, ganz genau!"
            "✅ Die Kinder haben schon in der Schule gegessen."
            jump fahren
        "Gegesst":
            "❌ Das ist fast richtig. Versuche es noch einmal."
            jump essen_retry

label fahren:
    scene bg skiing
    "Fahren — Fuhr — (ist) Gefahren"

    "Julia _?_ gestern für eine Woche nach Wien __?__"

    menu:
        "hat Gefahrt":
            "❌ Nicht ganz."
            jump fahren
        "ist Gefuhr":
            "❌ Oh nein!"
            jump fahren
        "Ist gefahren":
            "👏 Sehr schön!"
            "✅ Julia ist gestern für eine Woche nach Wien gefahren."
            jump ending
        "Hat gefahren":
            "❌ Bist du sicher?"
            jump fahren

label ending:

    scene bg ending

    "Danke für deine Aufmerksamkeit!
    Thank you for your attention!"
    "Wir laden dich ein, unsere kurze Story durchzuspielen.
    We invite you to play through our short story."

    stop audio fadeout 2.0
    return
