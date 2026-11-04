# Lesson 01 demo: run it with  python demo.py
# or copy sections into the REPL one by one.

print("--- Variables ---")
reward = 4860
name = "Wren Hawkridge"
print(name, "led a quest worth", reward, "crowns")

print("\n--- Numbers ---")
print("1000 / 3   =", 1000 / 3)
print("1000 // 3  =", 1000 // 3, "  <- whole crowns per hero")
print("1000 % 3   =", 1000 % 3, "  <- left for the guild chest")
print("2 ** 10    =", 2 ** 10)
print("2 ^ 10     =", 2 ^ 10, "  <- NOT a power!")
print("0.1 + 0.2  =", 0.1 + 0.2)
print("round(2.5) =", round(2.5), "  round(3.5) =", round(3.5))

print("\n--- Strings ---")
first = "  wREN "
last = "hawkridge"
clean = first.strip().title() + " " + last.title()
print(repr(clean))
ref = "GOB-0042"
print(ref[0], ref[:3], ref[-4:], len(ref))

print("\n--- Types ---")
print(type(42), type(4.2), type("42"), type(True), type(None))
days_from_scroll = "9"
print(reward / int(days_from_scroll), "crowns per day")
# print("5" + 3)   # <- uncomment to see the TypeError

print("\n--- f-strings ---")
share = reward / 4
print(f"Each hero gets {share:,.2f} cr")
print(f"Success rate: {0.648:.1%}")
print(f"{'Reward':<15}{f'{reward:,.2f} cr':>12}")
print(f"{'Guild cut':<15}{f'{reward * 0.10:,.2f} cr':>12}")
print(f"Q{42:04d}")

print("\n--- Booleans ---")
reward = 1300
print(reward == 1300, 400 <= reward <= 1200, reward != 1300)
print(reward > 1200 or name == "Wren Hawkridge")
