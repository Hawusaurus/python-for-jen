# Lesson 14 demo: run from the lesson folder with  python demo.py
# Section 1 for the session 1 briefing, section 2 for session 2.

import sqlite3

import pandas as pd

import demo_helpers          # <- the file next to this one. That's the whole trick.

print("--- 1. Functions compute, scripts print ---")
print("A Wyrm notice: 3,000 cr, 12 days, party fled with a quarter:",
      f"{demo_helpers.per_day(750, 12):.1f} cr a day")
print("A troll hunt:  1,100 cr, 14 days, won:                     ",
      f"{demo_helpers.per_day(1100, 14):.1f} cr a day")
print("success_rate(['Success', 'Fled', 'Failed', 'Success']) =",
      demo_helpers.success_rate(["Success", "Fled", "Failed", "Success"]))

quests = pd.read_csv("data/quests.csv")
print("Success rate, Success only:   ", demo_helpers.success_rate(list(quests["outcome"])))
print("Success rate, Fled counted in:",
      round((quests["outcome"] != "Failed").mean() * 100, 1),
      " <- the Grimoire's number. Running away is not winning.")

print("\n--- 2. Two crafts, one report ---")
con = sqlite3.connect("data/guild.db")
inner = pd.read_sql("""
    SELECT q.region, r.warden, COUNT(*) AS quests
    FROM quests AS q JOIN regions AS r ON q.region = r.region
    GROUP BY q.region""", con)
left = pd.read_sql("""
    SELECT q.region, COALESCE(r.warden, '(none)') AS warden, COUNT(*) AS quests
    FROM quests AS q LEFT JOIN regions AS r ON q.region = r.region
    GROUP BY q.region""", con)
print("JOIN:      ", len(inner), "regions,", inner["quests"].sum(), "quests")
print("LEFT JOIN: ", len(left), "regions,", left["quests"].sum(), "quests  <- Thornwood is back")

table = quests.groupby("monster").agg(avg_reward=("reward", "mean"),
                                      paid=("paid", "sum"), days=("days", "sum"))
table["per_day"] = table["paid"] / table["days"]
print("\nRanked by the notice board:", ", ".join(table["avg_reward"].sort_values(ascending=False).index[:3]))
print("Ranked by crowns per day:  ", ", ".join(table["per_day"].sort_values(ascending=False).index[:3]))
print("<- same data, two questions. Ask Jen which one the Queen asked.")
