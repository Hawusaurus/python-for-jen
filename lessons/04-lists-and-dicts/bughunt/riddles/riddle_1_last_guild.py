# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 04 · RIDDLE 1: "The Last Banner"
# ==================================================================
#
#    Five guild banners hang in a row;
#    I counted them twice, and still I go
#    one step beyond the final door,
#    and find the hall has nothing more.
#
#  Found under Mistress Pell's inkpot. It should name the first and
#  the last guild on the roll.
#
#  Run:  python bughunt/riddles/riddle_1_last_guild.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guilds on the roll: 5
#     - Forge
#     - Harbour
#     - Guard
#     - Treasury
#     - Kitchens
#    Banners to sew (two each): 10
#    First guild: Forge
#    Second guild: Harbour
#    Middle guild: Guard
#    Last guild: Kitchens

guilds = ["Forge", "Harbour", "Guard", "Treasury", "Kitchens"]
banners = len(guilds)

print("Guilds on the roll:", banners)
for guild in guilds:
    print(" -", guild)

print("Banners to sew (two each):", banners * 2)
print("First guild:", guilds[0])
print("Second guild:", guilds[1])
print("Middle guild:", guilds[banners // 2])
print("Last guild:", guilds[banners])
