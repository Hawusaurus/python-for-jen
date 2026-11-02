# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 01 · RIDDLE 2: "The Hours with a Tail"
# ==================================================================
#
#  A number came with luggage on,
#  a little tail that won't be gone;
#  convert me now and I refuse:
#  first cut the tail, then use.
#
#  The Scriptorium copied the guards' hours as "37.5 hrs".
#  Orrin needs them as a number to work out the week.
#
#  Run:  python bughunt/riddles/riddle_2_hours.py
#  When it's fixed, it prints EXACTLY this:
#
#    Guard: Nye Pennyworth
#    Hours per week: 37.5
#    Hours per day: 7.5
#    Pay per week: 615.00 cr

guard = "Nye Pennyworth"
hours_text = "37.5 hrs"
rate_text = "16.40"
hours = float(hours_text)
rate = float(rate_text)
days = 5
print("Guard:", guard)
print("Hours per week:", hours)
print("Hours per day:", hours / days)
print(f"Pay per week: {hours * rate:,.2f} cr")
