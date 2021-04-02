define shark = Character("Narrator")

screen hpbar:
    text "Fish: [sharkHealth]/[sharkHealthMax]" xalign 0.02 yalign 0.05
    bar value sharkHealth range sharkHealthMax xalign 0.05 yalign 0.1 xmaximum 200

label start:
    $sharkHealth = 20
    $sharkHealthMax = 30

    scene bg blue ocean
    show screen hpbar

    show shark at truecenter
    with dissolve

    shark "Summer is ending, but before you begin travelling to warmer waters, you try to find a meal."
    hide shark
    menu:
        "Move towards the rocks":
            $sharkHealth -= 5
            jump rocks

        "Stay in the area":
            jump opening

label rocks:
    scene bg rocks
    show seal at truecenter
    with dissolve

    shark "You spot a seal in the waters ahead!"

    hide seal
    return

label opening:
    scene bg drifting boat
    show shark at truecenter
    with dissolve

    shark "Instead of finding food, you see a boat drifting towards you."

    hide shark
    return
