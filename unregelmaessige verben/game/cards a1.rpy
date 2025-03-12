# Инициализируем переменные
init python:
    cards_a1 = [
        ["beginnen - begann - hat begonnen", "begin"],
        ["bleiben - blieb - ist geblieben", "stay"],
        ["bringen - brachte - hat gebracht", "bring"],
        ["denken - dachte - hat gedacht", "think"],
        ["dürfen - durfte - hat gedurft", "may"],
        ["essen - aß - hat gegessen", "eat"],
        ["fahren - fuhr - hat/ist gefahren", "drive/ride"]
    ]
    current_card = 0
    is_flipped = False

# Добавляем анимацию переворота
transform card_flip:
    perspective True
    rotate_pad False
    xalign 0.5
    yalign 0.5
    
    on show:
        rotate 0
    on hide:
        rotate 90
        
    on replace:
        rotate 0
        linear 0.3 rotate 90
    on replaced:
        rotate 90
        linear 0.3 rotate 180

# Начало упражнения
label cards_level1:
    scene bg Klagenfurt-1-scaled
    $ current_card = 0
    $ is_flipped = False
    
    show screen flashcard
    while True:
        $ result = ui.interact()

# Основной экран с карточкой
screen flashcard:
    frame:
        xalign 0.5
        yalign 0.4
        xsize 800
        ysize 400
        background "#89e2ee"
        
        button:
            xsize 800
            ysize 400
            xalign 0.5
            yalign 0.5
            action [ToggleVariable("is_flipped"), Show("flashcard_content")]
            
            use flashcard_content

    # Кнопки навигации
    hbox:
        xalign 0.5
        yalign 0.8
        spacing 50
        
        textbutton "Previous" action [SetVariable("current_card", current_card - 1 if current_card > 0 else len(cards_a1) - 1), SetVariable("is_flipped", False)]:
            background "#aaaaaa"
            insensitive_background "#cccccc"
        
        textbutton "Next" action [SetVariable("current_card", (current_card + 1) % len(cards_a1)), SetVariable("is_flipped", False)]:
            background "#aaaaaa"
        
        textbutton "Back to Menu" action ShowMenu("cards_menu"):
            background "#aaaaaa"

# Содержимое карточки с анимацией
screen flashcard_content:
    frame:  # Wrap the content in a frame and apply "at"
        at card_flip  # Correct placement of the at statement

        xfill True
        yfill True
        xalign 0.5
        yalign 0.5
        
        text "[cards_a1[current_card][1] if is_flipped else cards_a1[current_card][0]]":
            xalign 0.5
            yalign 0.5
            size 30
            color "#000000"
            text_align 0.5



