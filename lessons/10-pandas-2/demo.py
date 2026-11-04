# Lesson 10 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import pandas as pd

pd.set_option("display.width", 120)
quests = pd.read_csv("data/quests.csv")

print("--- groupby is the PivotTable ---")
print(quests["region"].value_counts())
print(quests.groupby("region")["reward"].mean().round(0))
print(quests.groupby("region")["reward"].agg(["count", "mean", "median"]).round(0))
both = quests.groupby(["monster", "outcome"])["quest_id"].count()
print(both.head(4))
print(both.unstack(fill_value=0))
# print(quests.groupby("monster", "outcome")["quest_id"].count())   # <- uncomment: the two-keys mistake

print("\n--- pivot_table: the dialog with names ---")
print(quests.pivot_table(index="region", columns="outcome", values="quest_id",
                         aggfunc="count", margins=True))

print("\n--- merge is XLOOKUP ---")
regions = pd.read_csv("data/regions.csv")
left = quests.merge(regions, on="region", how="left")
inner = quests.merge(regions, on="region", how="inner")
print("rows:", len(quests), "left:", len(left), "inner:", len(inner))
print("NaN wardens:", left["warden"].isna().sum())
print(sorted(left[left["warden"].isna()]["region"].unique()))
left["warden"] = left["warden"].fillna("(no warden)")
print("after fillna:", left["warden"].isna().sum())

print("\n--- Reward bands ---")
labels = ["Pittance", "Fair", "Handsome", "King's ransom"]
quests["band"] = pd.qcut(quests["reward"], 4, labels=labels)
print((pd.crosstab(quests["band"], quests["outcome"], normalize="index") * 100).round(1))

print("\n--- The War Table in a few lines ---")
table = quests.groupby(["region", "outcome"])["quest_id"].count().unstack(fill_value=0)
table["quests"] = table.sum(axis=1)
table["success_pct"] = (table["Success"] / table["quests"] * 100).round(1)
print(table.sort_values("success_pct", ascending=False))

print("\n--- Who goes where: crowns per day, by monster ---")
quests["per_day"] = quests["paid"] / quests["days"]
print(quests.groupby("monster")["per_day"].mean().round(1).sort_values(ascending=False))
