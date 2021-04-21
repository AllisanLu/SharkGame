define shark = Character(" ")
define narrator = Character("Narrator")

screen hpbar:
    text "Fish: [sharkHealth]/[sharkHealthMax]" xalign 0.02 yalign 0.05
    bar value sharkHealth range sharkHealthMax xalign 0.05 yalign 0.1 xmaximum 200

label start:
    play music "audio/introduction.mp3"
    scene bg instructions
    with dissolve

    narrator "Hello! I have some quick instructions on how to play the game. First to continue
    the dialog, simply click on the dialogue box!"
    narrator "For settings, simply press esc."
    narrator "Finally, when options show up press one of the options!"
    narrator "Do you get it?"

    menu:
        "Yes!":
            narrator "good~"
            jump coldwater
        "No":
            narrator "Oh no, to repeat, click on dialog box to continue dialogue."
            narrator "To open settings press esc"
            narrator "To choose an option from the menu, simply just click on the option."
            narrator "Alright you should be good to go!"
            jump coldwater

#cold water scenes
label coldwater:
    #add something ehre to like give instructions on how to play
    play music "audio/adventure.mp3"
    $sharkHealth = 10
    $sharkHealthMax = 50

    scene bg blue ocean
    show screen hpbar

    show shark at truecenter
    with dissolve

    shark "You are a lonely tiger shark. You swim along, preparing for your migration to your second home."
    shark "Summer is ending, but before you begin travelling to warmer waters, you try to find a meal."
    shark "There might be more food near the rocks, but you don’t know if it’s worth the risk."
    hide shark
    menu:
        "Move towards the rocks (-5 fish)":
            $sharkHealth -= 5
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump rocks

        "Stay in the area":
            $sharkHealth += 5
            jump driftingBoat

label rocks:
    scene bg rocks
    show seal at truecenter
    with dissolve

    shark "You spot a seal in the waters ahead!"

    menu:
        "ATTACK!!!!! (-8 fish)":
            $sharkHealth -= 8
            if (sharkHealth <= 0):
                jump die
            hide seal
            jump killSeal
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump driftingBoat

label killSeal:
    shark "You follow the seal, silently stalking it."
    shark "You take your chance and propel forward, your jaw clenching around soft flesh. Success."
    shark "The seal had no chance against your agility. (+10 fish)"
    $sharkHealth += 10
    shark "What will you do now?"

    menu:
        "Continue searching for seals in the area (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump driftingBoat
        "Continue swimming and looking for seals in other areas (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump continueSearching

label driftingBoat:
    scene bg drifting boat
    show shark at truecenter
    with dissolve

    shark "Instead of finding food, you see a strange shape on top of the water drifting towards you."
    shark "You see dead fish floating around it. It smells good, but not as good as fresh fish."
    menu:
        "Investigate (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump illegalFishermen
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump rocks

label illegalFishermen:
    scene bg drifting boat
    show shark at truecenter
    with dissolve

    shark "As you swim closer, a strange object is suddenly dropped in front of you."
    shark "!!"
    shark "You get tangled and are pulled out of the water."
    scene bg boat
    show imsorryshark at truecenter
    with dissolve
    shark "You panic but there’s nothing you can do. "
    shark "Your fins are taken, and you dropped back into the ocean."
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

label continueSearching:
    scene bg rocks
    show shark at truecenter
    with dissolve

    shark "Despite your effort, you are unable to find a seal this time."
    shark "You could keep searching, but you also know you need to continue your journey."

    menu:
        "Continue to search for seals (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            jump driftingBoat
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            jump openOcean


#open ocean scenes
label openOcean:
    scene bg ocean
    show shark at truecenter
    with dissolve
    shark "You made it to the open ocean. The sunlight glistens on your striped skin. It’s beautiful, but not without dangers."
    shark "You think the sunlight is nice, and you do believe you deserve a break, but there is still much more to go."

    menu:
        "Take a moment and enjoy the sunlight":
            $sharkHealth += 2
            jump boatAhead
        "Continue Swimming ahead (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 3):
                jump die
            $sharkHealth += 4
            jump lessFish

label boatAhead:
    scene bg drifting boat
    show shark at truecenter
    with dissolve
    shark "There aren't as many fish as there used to be. It doesn't bother you."
    shark "As you soak in the sunlight you see a strange shape on top of the water up ahead."
    shark "You see dead fish floating around it. It smells good, but not as good as fresh fish."

    menu:
        "Investigate (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            jump illegalWhale
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump whale

label illegalWhale:
    scene bg drifting boat
    show shark at truecenter
    shark "As you swim closer, a strange object is suddenly dropped in front of you."
    shark "!!"
    shark "You get tangled and are pulled out of the water."
    scene bg boat
    show imsorryshark at truecenter
    with dissolve
    shark "You panic but there’s nothing you can do. "
    shark "Your fins are taken, and you dropped back into the ocean."
    scene bg whale
    with dissolve
    hide imsorryshark
    shark "As you sink into the empty abyss of the ocean, you see a whale caracss up ahead."
    shark "How cruel of life to taunt you this way."
    scene bg black
    with dissolve
    shark "Water brushes past your striped skin for the last time."
    return

label lessFish:
    scene bg ocean
    show shark at truecenter
    with dissolve
    shark "There aren't as many fish as there used to be."
    shark "You might need to try and find a meal."

    menu:
        "Search for food (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump whale
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 5
            jump tigerShark

label whale:
    scene bg whale
    with dissolve
    shark "It's your lucky day!"
    shark "You see a whale caracas up ahead."
    shark "This would be an easy meal, almost too easy..."

    menu:
        "Swim towards it (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            jump chillOcean
        "Continue Swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 4
            jump tigerShark

label tigerShark:
    scene bg tiger shark
    with dissolve
    shark "You see another tiger shark ahead. Maybe friendly maybe not."

    menu:
        "Swim closer to the shark (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 4
            jump angryShark
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 4
            jump boatAhead

label angryShark:
    scene bg tiger shark
    show shark at truecenter
    with dissolve
    shark "The shark is agressive. Maybe they are noticing that there are less fish too. They must not want to share."

    menu:
        "Fight (-8 fish)":
            $sharkHealth -= 8
            if (sharkHealth <= 0):
                jump die
            jump fight
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump avoidShark

label fight:
    scene bg tiger shark
    show shark at truecenter
    with dissolve

    shark "The battle is tough. They put up a good fight."
    shark "You reign victorious, but not without consequences. (-20 fish)"
    $sharkHealth -= 20
    if (sharkHealth <= 0):
        jump die
    shark "The battle took a lot of energy from you, and you have become hungry,
    but you know that you can't delay your migration for too long."
    menu:
        "Look for food (-2 fish)":
            $sharkHealth -= 2
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump lessFish
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump coastline

label avoidShark:
    scene bg tiger shark
    with dissolve
    shark "You try to avoid the fight, but the other shark has different plans."
    shark "It attacks."

    menu:
        "Fight back (-8 fish)":
            $sharkHealth -= 8
            if (sharkHealth <= 0):
                jump die
            jump fight
        "Accept you fate":
            jump sharkDeath

label chillOcean:
    scene bg whale
    show shark at truecenter
    with dissolve
    shark "You notice less fish are nearby."
    shark "Good thing you made it to this whale carcass. (+10 fish)"
    $sharkHealth += 10
    shark "You wonder if there are more meals nearby."

    menu:
        "Look for food (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump tigerShark
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump coastline


#coastline scenes
label coastline:
    scene bg coastline
    show shark at truecenter
    with dissolve

    shark "You make it to the coastline!"
    shark "The water already feels warmer. This confuses you."
    shark "You haven't even passed the reef yet, so you know you must keep going."
    shark "You notice strange floating objects- maybe food?"

    menu:
        "Try to eat the floating objects (-1 fish)":
            $sharkHealth -= 1
            if (sharkHealth <= 0):
                jump die
            jump nomPlastic
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump freshWater

label nomPlastic:
    scene bg plastic
    show shark at truecenter
    with dissolve

    shark "This is unlike any fish you've ever eaten. It's shiny, and you can't chew it."

    menu:
        "Stop eating and keep swimming (-5 fish)":
            $sharkHealth -= 5
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump freshWater
        "Continue to eat":
            jump plasticDie

label freshWater:
    scene bg coastline
    show shark at truecenter
    with dissolve

    shark "You continue on your path, the same one you take every year, but this time something different happens.
    You start to notice freshwater."

    menu:
        "Keep to the path (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump net
        "Find a new path with more salt water (-7 fish)":
            $sharkHealth -= 7
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump awayFromCoast

label net:
    scene bg net
    show shark at truecenter
    with dissolve

    shark "You decide to stay on the path that is familiar to you."
    shark "Suddenly you find yourself stuck in a strange floating object."
    shark "It wraps around you, entangling your body."
    shark "As you try to move you feel the fibers slicing into your flesh."

    menu:
        "Try to escape (-7 fish)":
            $sharkHealth -= 7
            if (sharkHealth <= 0):
                jump die
            jump netDeath
        "Accept your fate":
            jump acceptNetDeath

label awayFromCoast:
    scene bg ocean nice
    show shark at truecenter
    with dissolve

    shark "You swim further away from the coastline. You're much more comfortable away from the fresh water."
    shark "You know you are almost at the reef, but may need food to get there."

    menu:
        "Search for food (-4 fish)":
            $sharkHealth -= 4
            if (sharkHealth <= 0):
                jump die
            jump turtle
        "Push through and keep swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            jump coastPatrol

label turtle:
    scene bg turtle
    with dissolve
    shark "You know you are close to the reef as you see a turtle up ahead. You feast. (+5 fish)"
    $sharkHealth += 5
    shark "You are nearing the end of your journey, so you know you should keep moving."

    menu:
        "Keep searching for food (-4 fish)":
            $sharkHealth -= 4
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump coastPatrol
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 3
            jump reef


#reef scenes
label reef:
    scene bg reef
    show shark at truecenter
    with dissolve

    shark "You made it to the reef."
    shark "Expecting to see the radiant colors of the coral as you swim past,
    you are instead greeted with a much duller site."
    shark "Something has happened, but you don't know what."
    shark "As you continue to swim, you notice a plethora of objects tethered to the ocean floor.
    They are accompanied by new smells and chemicals, none of which seem natural."
    shark "Although you notice less of your normal food source, you find that
    there are many more four limbed creatures on the reef now, but they don’t look very appetising."

    menu:
        "Search for more appetizing food (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump reefShark
        "Swim away from the strange creatures (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump hungry

label reefShark:
    scene bg reef shark
    with dissolve

    shark "You find a reef shark. Like you, it is noticing the decline in fish near the normally high-populated reef."
    shark "It looks sad, and you can relate to tis struggle."

    menu:
        "Eat it. (+5 fish)":
            $sharkHealth += 5
            shark "You take advantage of the opportunity for a meal, then continue on your journey."
            jump coastPatrol

        "Pity it and keep searching (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 1
            jump hungry

label hungry:
    scene bg reef 2
    show shark at truecenter
    with dissolve

    shark "You continue your journey."
    shark "You know you are close to your destination but are definitely feeling hunger creep in."

    menu:
        "Search for food (-4 fish)":
            $sharkHealth -= 4
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 1
            jump shellFish
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 1
            jump coastPatrol

label shellFish:
    scene bg reef
    show shellfish at truecenter
    with dissolve

    shark "You find a shellfish that wandered too close to the edge of the reef."
    shark "As you eat it, you notice its shell was weaker; an easy meal was made almost too easy. (+3 fish)"
    hide shellfish
    show shark at truecenter
    with dissolve
    $sharkHealth += 3
    shark "You begin to wonder what is happening to your home."

    menu:
        "Keep searching for food (-4 fish)":
            $sharkHealth -= 4
            if (sharkHealth <= 0):
                jump die
            jump otherShellfish
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 1
            jump coastPatrol

label otherShellfish:
    scene bg reef
    show shellfish at truecenter
    with dissolve

    shark "You find another shellfish, and the same thing happens."
    shark "The shell breaks with no effort on your part, but you are not complaining. (+3 fish)"
    hide shellfish
    show shark at truecenter
    with dissolve
    $sharkHealth += 3
    shark "You know you are close to the end of your journey."

    menu:
        "Keep searching for food (-4 fish)":
            $sharkHealth -= 4
            if (sharkHealth <= 0):
                jump die
            $sharkHealth += 2
            jump coastPatrol
        "Continue swimming (-3 fish)":
            $sharkHealth -= 3
            if (sharkHealth <= 0):
                jump die
            jump finishJourney

label finishJourney:
    scene bg end
    show shark at truecenter
    with dissolve

    shark "You made it to the warm waters for the winter!"
    shark "However, there are now so few fish you couldnt find any on the last stretch of your journey."
    shark "The reef looked dead, food was sparce, and there were far more obstacles in your migration than any year before."
    shark "You are safe, for now, but begin to wonder how you will migrate again if the conditions worsen."

    narrator "The shark has finished its journey, its quest per say, and will now spend some time in the reef."
    narrator "Congratulations! You have survived the migration."
    hide shark
    stop music fadeout 1.0
    play music "audio/introduction.mp3"
    hide hpbar
    scene bg the end
    $ renpy.pause()
    return


#death scenes
label die:
    stop music fadeout 1.0
    scene bg died
    with dissolve

    shark "Hunger sets in, and you no longer have the energy to continue your journey."
    shark "You wonder why the migration was so much harder this time..."
    shark "Water brushes past your striped skin for the last time."
    return

label acceptedDeath:
    stop music fadeout 1.0
    scene bg black
    with dissolve

    shark "The humans say they see a white light, "
    shark "but all you see is darkness as it sinks into the empty abyss of the ocean."
    shark " "
    shark "The water brushes past your striped skin for the last time....."
    shark " "

    return

label theStruggleToSurvive:
    scene bg red
    with fade
    show seal at truecenter

    shark "You flail you body in an attempt to catch the seal."
    shark "The seal swims towards you, mocking your struggle."
    shark "The seal watches with cold eyes as you slowly sink into the empty abyss of the ocean."
    stop music fadeout 1.0
    scene bg black
    shark " "
    shark "The water brushes past your striped skin for the last time....."
    return

label sharkDeath:
    stop music fadeout 1.0
    scene bg black
    with dissolve

    shark "Exhausted, you give up. As you sinks into the empty abyss of the ocean, the victorious shark swims
    out of your vision."
    shark "You hope they can finish the journey that you will never complete."
    shark "Water brushes past your stripped skin for the last time."
    return

label plasticDie:
    scene bg plastic
    show shark at truecenter
    with dissolve

    shark "You try to eat more, you only option is to swallow."
    shark "Some of the strange objects are sharp and metallic, while others are flimsy and plastic."
    shark "Hungry from the lack of fish, you continue to feast, but soon realize this was a mistake.
    The trash has defeated you."
    stop music fadeout 1.0
    scene bg black
    hide shark
    shark "Water brushes past the your striped skin for the last time..."
    return

label netDeath:
    scene bg net
    show shark at truecenter
    with dissolve

    shark "You desperately flail your body in an attempt to escape the net, but do not succeed."
    shark "You look around and notice how different your ocean looks now. It's sadder, like it lost its vibrance."
    shark "You don't know how this happened."
    stop music fadeout 1.0
    scene bg black
    hide shark
    shark "Water brushes past the your striped skin for the last time..."
    return

label acceptNetDeath:
    scene bg net
    show shark at truecenter
    with dissolve

    shark "You give up. The journet was becoming very difficult anyway."
    shark "You look around and notice how different your ocean looks now. It's sadder, like it lost its vibrance."
    shark "You don't know how this happened."
    stop music fadeout 1.0
    scene bg black
    hide shark
    shark "Water brushes past the your striped skin for the last time..."
    return

label coastPatrol:
    scene bg drifting boat
    show shark at truecenter
    with dissolve

    shark "As you swim, you notice a really strange shadow coming towards you. You move out of its way, but it follows you."
    shark "Panicked, you swim faster, but it makes no difference."
    scene bg boat
    show shark at truecenter
    with dissolve
    shark "You are draffed out of the water and onto the strange vessel."
    shark "These people claim they are doing this to protect swimmers in the ocean, but they forget that you have been
    swimming here longer than any human."
    stop music fadeout 1.0
    scene bg black
    hide shark
    shark "Water brushes past the your striped skin for the last time..."
    return
