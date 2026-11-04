# ==================================================================
#  PAGES FROM THE GRIMOIRE, PAGE 3: "helpers_v7_USE_THIS.py"
# ==================================================================
#
# Dalvric discovered functions late in his career. He was very excited.
# He wrote three of them, then went back to copying incantations by
# hand because "functions kept returning nothing". They did. Here's why.
#
# THREE bugs:
#   one crashes (read the error message!),
#   one makes a function hand back nothing at all,
#   one is a default value that quietly takes the whole reward.
#
# Run it from inside the lesson folder:
#   python bughunt/tangle_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   4,860.00 cr
#   Guild cut at 10%: 486.00 cr
#   Guild cut at 5%: 243.00 cr
#   Reward          4,860.00 cr
#   Guild cut         486.00 cr
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"


def money(amount):
    """Crowns with thousands separator and 2 decimals."""
    text = f"{amount:,.2f} cr"


def guild_cut(reward, rate=1.0):
    """The guild's cut of a reward. The standard rate is 10%."""
    return reward * rate


def notice_line(label, amount):
    return f"{label:<15}{money(amount):>12}"


reward = 4860
print(money(reward))
print("Guild cut at 10%:", money(guild_cut(reward)))
print("Guild cut at 5%:", money(guild_cut(reward, rate=0.05)))
print(notice_line("Reward", reward))
print(notice_line("Guild cut", guild_cut(reward))
