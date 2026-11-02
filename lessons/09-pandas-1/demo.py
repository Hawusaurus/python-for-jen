# Lesson 09 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import pandas as pd

pd.set_option("display.width", 120)

print("--- Open it and look ---")
df = pd.read_csv("data/quests.csv")
print(df.shape)
print(df.head())
print(list(df.columns))
df.info()
print(df.describe().round(1))

print("\n--- Columns ---")
print(df["reward"].head(3))
print(df["reward"].mean())
print(df[["quest_id", "reward"]].head(3))
df["per_day"] = (df["paid"] / df["days"]).round(2)
print(df[["quest_id", "per_day"]].head(3))
# print(df["quest_id", "reward"])   # <- uncomment: the double-bracket mistake

print("\n--- AutoFilter ---")
print(len(df[df["reward"] > 1000]))
print(df[(df["region"] == "Northern Wilds") & (df["outcome"] == "Failed")][["quest_id", "monster"]])
print(len(df[df["region"].isin(["Greyfen", "Saltmarsh"])]))
print(len(df[df["title"].str.contains("old mill")]))

print("\n--- Sort (returns a copy) ---")
print(df.sort_values("per_day", ascending=False)[["quest_id", "monster", "per_day"]].head())
print(df[["quest_id", "per_day"]].head(2), "<- df itself is unchanged")
print(df.nlargest(3, "per_day")[["quest_id", "per_day"]])

print("\n--- Excel in ---")
xl = pd.read_excel("data/guild_ledger.xlsx", sheet_name="Quests")
print(xl.shape)
print(pd.read_excel("data/guild_ledger.xlsx", sheet_name="Notes"))

print("\n--- The Quartermistress's month in five lines ---")
fled = df[df["outcome"] == "Fled"].sort_values("region")
fled.to_csv("my_work/demo_fled.csv", index=False)
print(pd.read_csv("my_work/demo_fled.csv")[["quest_id", "region", "monster"]].head(3))
