import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=300)

with dpg.window(no_title_bar=True, width=400, height=300):
    with dpg.child_window(width=380, height=120, horizontal_scrollbar=True):
        dpg.add_text("Saul, Saul... this man that we spoke of before, this... this person that you said could... "
                     "\ncould disappear me, get me a whole new life and make sure that I'm never found. Yeah I need "
                     "\nhim, Saul. Gus is gonna murder my whole family. I need this man now. Saul... now, "
                     "\nSaul! Anything suspicious? Well... then should we go? Any uh... Cartel news these days? Seems "
                     "\nlike I'm always reading something or other in the paper. I don't want to talk about it. To you "
                     "\nor anyone else. I'm done explaining myself. Gus is dead. We've got work to do. Jesse Jackson? "
                     "\nDo you even... ah, I see you have a telephone at least. You know that blinking thing I've been "
                     "\ncalling you on? I will break this, I will BREAK THIS. Damn druggie idiot. Is this what you've "
                     "\nbeen doing the whole time I've been trying to reach you? The game has changed. The word is out. "
                     "\nAnd you... are a killer. Apparently it's all over town. Somebody crossed you, you got angry, you "
                     "\ncrushed their skull with an ATM machine. Who cares! Just as long as it's our competitors who "
                     "\nbelieve it and not the police. Don't you see how great this is? You, you are a... Jesse look at me. "
                     "\nYou... are a blowfish. A blowfish! Think about it. Small in stature, not swift, not cunning. "
                     "\nEasy prey for predators but the blowfish has a secret weapon doesn't he. Doesn't he? "
                     "\nWhat does the blowfish do, Jesse. What does the blowfish do? The blowfish puffs up, okay? "
                     "\nThe blowfish puffs himself up four, five times larger than normal and why? Why does he do that? "
                     "\nSo that it makes him intimidating, that's why. Intimidating! So that the other, scarier fish are "
                     "\nscared off. And that's you! You are a blowfish. You see it's just all an illusion. "
                     "\nYou see it's... it's nothing but air. Now... who messes with the blowfish, Jesse? "
                     "\nYou're damn right. You are a blowfish. Say it again. Say it like you mean it. You're a BLOWFISH! "
                     "\nMy partner was about to get himself shot. I intervened. He was angry because those two dealers "
                     "\nof yours had just murdered an eleven year-old boy. Then again, maybe he thought it was "
                     "\nyou who gave the order. He has enough money to last forever. He knows he needs to keep moving. "
                     "\nYou'll never find him. He's out of the picture. I saved his life, I owed him that, but now he "
                     "\nand I are done. Which is exactly what you wanted, isn't it. You've always struck me as a very "
                     "\npragmatic man so if I may, I would like to review options with you. Of which, it seems to me "
                     "\nyou have two. Option A, you kill me right here and now. Apparently I've made that very easy "
                     "\nfor you. You can kill me, no witnesses and then spend the next few weeks or months tracking "
                     "\ndown Jesse Pinkman and you kill him too. A pointless exercise it seems to me but that is "
                     "\nOption A. I continue cooking, you and I both forget about Pinkman. We forget this ever happened. "
                     "\nWe consider this a lone hiccup in an otherwise long and fruitful business arrangement. "
                     "\nI prefer Option B. He'll live. I asked to see you in order to... clear the air. There are uh, "
                     "\nsome... issues that could cause a misunderstanding between us and I think it's in our best interest to lay the cards on the table. My brother-in-law, moments before he was attacked, someone called to warn him. I believe that same person was protecting me.  Those two men, the assassins. I believe I was their prime target, but that somehow they were steered away from me to my brother-in-law. Because of this 'intervention' I am alive. And yet, I think that this person was playing a much deeper game. He made that phone call because he wanted a shootout not a silent assassination. In one stroke, he bloodied both sides - set the American and Mexican governments against the Cartel, and cut off the supply of methamphetamine to the southwest. If this man had his own source of product on this side of the border, he would have the market to himself. The rewards would be... enormous. We're both adults. I can't pretend I don't know that person is you. I want there to be no confusion. I know I owe you my life. And more than that, I respect the strategy. In your position, I would have done the same. One issue, which troubles me, I don't know what happens when our three-month contract ends. You know why I do this. I want security for my family. No speeches. Short speech. You lost your partner today. What's his name - Emilio? Emilio is going to prison. The DEA took all your money, your lab. You got nothing. Square one. But you know the business and I know the chemistry. I'm thinking... maybe you and I could partner up. I'm sorry, what were you asking me? Oh, yes, that stupid plastic container I asked you to buy. You see, hydrofluoric acid won't eat through plastic. It will, however, dissolve metal, rock, glass, ceramic. So there's "
                     "\nthat. How about something with some protein, maybe? Something green, huh? How are you even "
                     "\nalive? That is seventeen five - your half of the thirty-five thousand. Plus there's an extra "
                     "\nfifteen in there, it's all yours, you've earned it. We made a deal. That's right. Because I think that we can do business together - we came to an understanding. Take a look at the money in your hand. Now just imagine making that every week. That's right. Two pounds a week, thirty-five thousand a pound. Look... I feel like I'm running out of ways to explain this to you but once more, I shall try. This fly is a major problem for us.It will ruin our batch.And we need to destroy it and every trace of it, so we can cook.Failing that, we're dead. There's no more room for error.Not with these people.You asked me if we were in the meth business or the money business.Neither, I’m in the empire business.I was under the impression that you had this under control.Well, that's what this is - problem solving. Skyler this is a simple division of labor - I bring in the money, you launder the money. This is what you wanted. Who are you talking to right now? Who is it you think you see? Do you know how much I make a year? I mean, even if I told you, you wouldn't believe it.Do you know what would happen if I suddenly decided to stop going into work? ")
    with dpg.child_window(width=380, height=120):
        dpg.add_text("FARSA")

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
