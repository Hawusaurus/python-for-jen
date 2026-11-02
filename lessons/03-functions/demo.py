# Lesson 03 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- Before: last week's purse loop ---")
total = 0
for record in "Wren/3100/4/14;Jory/2450/2/30;Biscuit/400/5/0".split(";"):
    name, reward_text, difficulty_text, quests_text = record.split("/")
    reward, difficulty, quests_done = int(reward_text), int(difficulty_text), int(quests_text)
    if quests_done < 3:
        rate = 0
    elif difficulty >= 4:
        rate = 0.25
    elif difficulty == 3:
        rate = 0.10
    else:
        rate = 0
    total += reward * rate
print("total", total)


print("\n--- def and return ---")
def share(reward, party_size):
    """Each hero's share of the reward, to the penny."""
    return round(reward / party_size, 2)

print(share(1000, 3))
print(share)                     # the recipe, not the result
help(share)


print("\n--- return is not print ---")
def money_print(x):
    print(f"{x:,.2f} cr")

def money(x):
    return f"{x:,.2f} cr"

result = money_print(5)
print("money_print gave back:", result)
print(money(5) + " each")
# print(money_print(5) + " each")   # <- uncomment: TypeError, None + str


print("\n--- After: the napkin as a function ---")
def purse_rate(quests_done, difficulty):
    """The Queen's napkin. Change it HERE and only here."""
    if quests_done < 3:
        return 0
    if difficulty >= 4:
        return 0.25
    if difficulty == 3:
        return 0.10
    return 0

def purse(reward, quests_done, difficulty):
    return reward * purse_rate(quests_done, difficulty)

total = 0
for record in "Wren/3100/4/14;Jory/2450/2/30;Biscuit/400/5/0".split(";"):
    name, reward, difficulty, quests_done = record.split("/")
    total += purse(int(reward), int(quests_done), int(difficulty))
print("total", total)


print("\n--- defaults and keywords ---")
def percent(x, decimals=1):
    return f"{x * 100:.{decimals}f}%"

print(percent(0.125), percent(0.125, 0), percent(0.125, decimals=2))


print("\n--- scope ---")
rate = 0.10

def guild_cut(reward):
    cut = reward * rate          # can read the outer rate
    return cut

def cut_with_rate(reward, rate):     # its own rate
    return reward * rate

print(guild_cut(2000), cut_with_rate(2000, 0.05), rate)
# print(cut)   # <- uncomment: NameError, it only exists inside guild_cut()
