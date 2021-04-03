define shark = Character(" ")
define narrator = Character("Narrator")

screen hpbar:
    text "Fish: [sharkHealth]/[sharkHealthMax]" xalign 0.02 yalign 0.05
    bar value sharkHealth range sharkHealthMax xalign 0.05 yalign 0.1 xmaximum 200

#cold water scenes
label start:
    $sharkHealth = 20
    $sharkHealthMax = 30

    scene bg blue ocean
    show screen hpbar

    show shark at truecenter
    with dissolve

    narrator "A lonely tiger shark must to travel to warmer waters from these cold waters as the seasons change."
    narrator "It swims along, preparing its migration to its second home."
    shark "Summer is ending, but before you begin travelling to warmer waters, you try to find a meal."
    hide shark
    menu:
        "Move towards the rocks (-5 fish)":
            $sharkHealth -= 5
            if (sharkHealth <= 0):
                jump die
            jump rocks

        "Stay in the area":
            jump driftingBoat

label rocks:
    scene bg rocks
    show seal at truecenter
    with dissolve

    shark "You spot a seal in the waters ahead!"

    menu:
        "ATTACK!!!!! (-7 fish)":
            $sharkHealth -= 7
            if (sharkHealth <= 0):
                jump die
            hide seal
            jump killSeal
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            jump driftingBoat

label killSeal:
    shark "Success! The seal had no change against your agility (+10 fish)"
    $sharkHealth += 10
    shark "What will you do now?"

    menu:
        "Continue searching for seals (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            jump driftingBoat
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            jump openOcean

label driftingBoat:
    scene bg drifting boat
    show shark at truecenter
    with dissolve

    shark "Instead of finding food, you see a boat drifting towards you."
    menu:
        "Investigate (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            jump illegalFishermen
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            jump rocks

label illegalFishermen:
    scene bg drifting boat
    show shark at truecenter
    with dissolve

    narrator "As the shark approach the boat, it has an alarming realization."
    shark "!!"
    shark "You realize the boat containss illegal fishers."
    scene bg boat
    show imsorryshark at truecenter
    with dissolve
    shark "You are caught, your fins taken, and dropped back into the ocean."
    hide imsorryshark
    scene bg black
    show seal at truecenter
    with dissolve
    shark "As you sink, you see a seal. It taunts you..."

    menu:
        "Attempt to catch the seal even without fins":
            jump theStruggleToSurvive
        "Accept your fate":
            jump acceptedDeath


#open ocean scenes
label openOcean:
    scene bg black
    narrator "Soon...one day the ocean scene will be ready to be played."
    return


#death scenes
label die:
    scene bg died
    with dissolve
    shark "You died."

    return

label acceptedDeath:
    scene bg black
    with dissolve

    narrator "The humans say they see a white light, "
    narrator "but all the shark sees is darkness as it sinks into the empty abyss of the ocean."
    shark " "
    narrator "The water brushes past its striped skin for the last time....."
    shark " "

    return

label theStruggleToSurvive:
    scene bg red
    with fade
    show seal at truecenter

    shark "You flail you body in an attempt to catch the seal."
    narrator "The seal swims towards the shark, mocking its struggle."
    narrator "The seal watches with cold eyes as the finless shark slowly sinks into the empty abyss of the ocean."

    scene bg black
    shark " "
    return
