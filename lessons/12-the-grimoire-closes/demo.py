# Lesson 12 demo: run from the lesson folder with  python demo.py
# Section 1 for the session 1 briefing, section 2 for session 2.

import pandas as pd
import demo_helpers          # <- the file next to this one. That's the whole trick.

print("--- 1. Functions compute, scripts print ---")
print("Part-timer on 10,300 cr for 18.75 h:",
      f"{demo_helpers.hourly_rate(10300, 18.75):.2f} cr per hour")
print("Full-timer on 20,600 cr for 37.5 h: ",
      f"{demo_helpers.hourly_rate(20600, 37.5):.2f} cr per hour  <- same rate, half the salary")
print("gap_percent(20.00, 17.40) =", demo_helpers.gap_percent(20.00, 17.40))
print("gap_percent(17.40, 20.00) =", demo_helpers.gap_percent(17.40, 20.00),
      " <- divide by the wrong group and the number changes")

df = pd.read_csv("data/thornmere_payroll.csv")
df["hourly_rate"] = df["annual_salary"] / 52 / df["weekly_hours"]
men = df.loc[df["gender"] == "M", "hourly_rate"]
women = df.loc[df["gender"] == "F", "hourly_rate"]
print("mean gap:  ", demo_helpers.gap_percent(men.mean(), women.mean()))
print("median gap:", demo_helpers.gap_percent(men.median(), women.median()))
print("Grimoire:  ", round((men.mean() - women.mean()) / women.mean() * 100, 1),
      " <- the Grimoire divided by women's pay")

print("\n--- 2. From numbers to a report ---")
bands = pd.qcut(df["hourly_rate"], 4, labels=["Lower", "Lower middle", "Upper middle", "Upper"])
quartiles = (pd.crosstab(bands, df["gender"], normalize="index") * 100).round(1)
print(quartiles)
print(f"\nShare of women overall: {(df['gender'] == 'F').mean() * 100:.1f}%")
print("Read each row as a sentence: '72% of the lowest-paid quarter are women.'")

print("\nThe Kitchens, by hand:")
kitchens = df[df["department"] == "Kitchens"]
print(kitchens[["first_name", "gender", "job_title", "grade", "hourly_rate"]]
      .sort_values("hourly_rate", ascending=False).round(2).to_string(index=False))
print("<- 67% women, biggest gap in the realm. Ask Jen why.")
