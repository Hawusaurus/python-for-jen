# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 4: "The Order of Things"
# ==================================================================
#
#  The sum was fair, the coins were true,
#  but one sign jumped the queue,
#  and multiplied before it should:
#  a bracket makes the order good.
#
#  Queen Aldara wanted the cost of two weeks of feasts:
#  120 crowns for the hall plus 80 for the food, each week.
#
#  Run:  python bughunt/riddles/riddle_4_order.py
#  When it's fixed, it prints EXACTLY this:
#
#    The Midsummer feast budget
#    Hall per week: 120 crowns
#    Food per week: 80 crowns
#    Minstrels, once: 40 crowns
#    One week of feasts: 200 crowns
#    Two weeks of feasts: 400 crowns
#    Two weeks with minstrels: 440 crowns

hall = 120
food = 80
minstrels = 40
print("The Midsummer feast budget")
print("Hall per week:", hall, "crowns")
print("Food per week:", food, "crowns")
print("Minstrels, once:", minstrels, "crowns")
print("One week of feasts:", hall + food, "crowns")
print("Two weeks of feasts:", hall + food * 2, "crowns")
print("Two weeks with minstrels:", (hall + food) * 2 + minstrels, "crowns")
