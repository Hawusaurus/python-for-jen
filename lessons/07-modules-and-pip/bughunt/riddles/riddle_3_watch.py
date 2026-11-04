# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 07 · RIDDLE 3: "The Same Face Every Night"
# ==================================================================
#
#  Each dusk the lots are cast again,
#  and every dusk the same name wins.
#  You plant the seed inside the night:
#  plant it once, before it begins.
#
#  Captain Siv's night-watch rota for the road to Saltmarsh. The heroes
#  have noticed something, and one of them has stopped sleeping.
#
#  Run:  python bughunt/riddles/riddle_3_watch.py
#  When it's fixed, it prints EXACTLY this:
#
#    Moonday    Wren keeps the watch
#    Tewsday    Tamsin keeps the watch
#    Wodensday  Bram keeps the watch
#    Thornsday  Wren keeps the watch
#    Freyday    Bram keeps the watch
#    Wren keeps 2 of the 5 watches

import random

heroes = ["Wren", "Bram", "Tamsin", "Osric", "Maren", "Elowen"]
nights = ["Moonday", "Tewsday", "Wodensday", "Thornsday", "Freyday"]

on_watch = []
for night in nights:
    random.seed(1019)
    hero = random.choice(heroes)
    on_watch.append(hero)
    print(f"{night:<10} {hero} keeps the watch")

print("Wren keeps", on_watch.count("Wren"), "of the", len(nights), "watches")
