# Lesson 09 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import pandas as pd

pd.set_option("display.width", 120)

print("--- Open it and look ---")
df = pd.read_csv("data/thornmere_payroll.csv")
print(df.shape)
print(df.head())
print(list(df.columns))
df.info()
print(df.describe().round(1))

print("\n--- Columns ---")
print(df["annual_salary"].head(3))
print(df["annual_salary"].mean())
print(df[["first_name", "annual_salary"]].head(3))
df["hourly"] = (df["annual_salary"] / 52 / df["weekly_hours"]).round(2)
print(df[["first_name", "hourly"]].head(3))
# print(df["first_name", "annual_salary"])   # <- uncomment: the double-bracket mistake

print("\n--- AutoFilter ---")
print(len(df[df["annual_salary"] > 40000]))
print(df[(df["department"] == "Guard") & (df["weekly_hours"] < 37.5)][["first_name", "weekly_hours"]])
print(len(df[df["location"].isin(["Westmarch", "Harbourtown"])]))
print(len(df[df["job_title"].str.contains("Warden")]))

print("\n--- Sort (returns a copy) ---")
print(df.sort_values("hourly", ascending=False)[["first_name", "last_name", "hourly"]].head())
print(df[["first_name", "hourly"]].head(2), "<- df itself is unchanged")
print(df.nlargest(3, "hourly")[["first_name", "hourly"]])

print("\n--- Excel in ---")
xl = pd.read_excel("data/payroll.xlsx", sheet_name="Payroll")
print(xl.shape)
print(pd.read_excel("data/payroll.xlsx", sheet_name="Notes"))

print("\n--- Mistress Pell's month in five lines ---")
part = df[df["weekly_hours"] < 37.5].sort_values("department")
part.to_csv("my_work/demo_part_timers.csv", index=False)
print(pd.read_csv("my_work/demo_part_timers.csv").head(3))
