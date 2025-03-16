#characters
define Julia = Character("Julia", color="#ADD8E6")
define Sara = Character("Sara", color="ff69b4")

label story_script:
    scene bg story

label first_choice:
    Sara "Oh, hallo Julia! Ich habe __, dass du nach Wien __ bist."
        
    menu:
            "Oh, hallo Julia! Ich habe __, dass du nach Wien __ bist."
            "gedenken, gefahren":
                "❌ Was?"
                jump first_choice
            "gedacht, gefahren":
                "✅ Oh, hallo Julia! Ich habe gedacht, dass du nach Wien gefahren bist."
                jump second_choice
            "gedenkt, gefahrt":
                "❌ Nein-nein."
                jump first_choice

label second_choice:
    Julia "Hallo Sara! Nah, ich habe hier viel zu tun." 
    Julia "Deshalb __ ich hier __."
        
    menu:
            "Deshalb __ ich hier __."
            "habe, geblieben":
                "❌ The verb 'bleiben' comes with the auxilary verb 'sein'."
                jump second_choice
            "bin, gebleiben":
                "❌ Bitte?"
                jump second_choice
            "bin, geblieben":
                "✅ Deshalb bin ich hier geblieben."
    
    "Thank you for playing our prototype."

    return