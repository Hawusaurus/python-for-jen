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
#   one is a default value that quietly changes what everyone is paid.
#
# Run it from inside the lesson folder:
#   python bughunt/spaghetti_bug.py
#
# When it's fixed, it prints EXACTLY this:
#
#   2,708.33 cr
#   Pension at 5%: 135.42 cr
#   Pension at 8%: 216.67 cr
#   Basic pay       2,708.33 cr
#   Pension           135.42 cr
#
# Fix ONE bug per commit and explain it in the message, like a detective:
#   git commit -m "Bug hunt: <what was wrong and why>"


def money(amount):
    """Crowns with thousands separator and 2 decimals."""
    text = f"{amount:,.2f} cr"


def pension(basic, rate=0.5):
    """Monthly pension deduction."""
    return basic * rate


def scroll_line(label, amount):
    return f"{label:<15}{money(amount):>12}"


monthly = 32500 / 12
print(money(monthly))
print("Pension at 5%:", money(pension(monthly)))
print("Pension at 8%:", money(pension(monthly, rate=0.08)))
print(scroll_line("Basic pay", monthly))
print(scroll_line("Pension", pension(monthly))
