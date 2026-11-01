# Lesson 10 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("data/brightwell_payroll.csv")
df["hourly"] = df["annual_salary"] / 52 / df["weekly_hours"]

print("--- groupby is the PivotTable ---")
print(df["department"].value_counts())
print(df.groupby("department")["annual_salary"].mean().round(0))
print(df.groupby("department")["annual_salary"].agg(["count", "mean", "median"]).round(0))
both = df.groupby(["department", "gender"])["hourly"].mean()
print(both.round(2).head(4))
print(both.unstack().round(2))
# print(df.groupby("department", "gender")["hourly"].mean())   # <- uncomment: the two-keys mistake

print("\n--- pivot_table: the dialog with names ---")
print(df.pivot_table(index="department", columns="gender", values="hourly",
                     aggfunc="mean", margins=True).round(2))

print("\n--- merge is XLOOKUP ---")
depts = pd.read_csv("data/departments.csv")
left = df.merge(depts, on="department", how="left")
inner = df.merge(depts, on="department", how="inner")
print("rows:", len(df), "left:", len(left), "inner:", len(inner))
print("NaN cost centres:", left["cost_centre"].isna().sum())
print(sorted(left[left["cost_centre"].isna()]["department"].unique()))
left["cost_centre"] = left["cost_centre"].fillna("CC-999")
print("after fillna:", left["cost_centre"].isna().sum())

print("\n--- Quartiles ---")
df["quartile"] = pd.qcut(df["hourly"], 4, labels=["Lower", "Lower middle", "Upper middle", "Upper"])
print((pd.crosstab(df["quartile"], df["gender"], normalize="index") * 100).round(1))

print("\n--- The board pack in one line ---")
table = df.groupby(["department", "gender"])["hourly"].mean().unstack()
table["gap_pct"] = ((table["M"] - table["F"]) / table["M"] * 100).round(1)
print(table.round(2).sort_values("gap_pct", ascending=False))
