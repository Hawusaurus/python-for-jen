# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 00 · RIDDLE 4: "The Order of Things"
# ==================================================================
#
#  Each coin was counted fair and true,
#  yet one sign barged ahead the queue;
#  it multiplied before the sum.
#  Wall in the add, and let it come.
#
#  Pell, the Quartermistress, priced the kit for a march into the Greyfen:
#  rope and a lantern for each of the four heroes, plus one mule.
#
#  Run:  python bughunt/riddles/riddle_4_order.py
#  When it's fixed, it prints EXACTLY this:
#
#    Supplies for the Greyfen march
#    Rope per hero: 12 crowns
#    Lantern per hero: 8 crowns
#    The mule, once: 15 crowns
#    Kit for one hero: 20 crowns
#    Kit for the party: 80 crowns
#    Everything: 95 crowns

rope = 12
lantern = 8
mule = 15
heroes = 4
print("Supplies for the Greyfen march")
print("Rope per hero:", rope, "crowns")
print("Lantern per hero:", lantern, "crowns")
print("The mule, once:", mule, "crowns")
print("Kit for one hero:", rope + lantern, "crowns")
print("Kit for the party:", (rope + lantern) * heroes, "crowns") #needs brackets for bodmas!
print("Everything:", (rope + lantern) * heroes + mule, "crowns")
