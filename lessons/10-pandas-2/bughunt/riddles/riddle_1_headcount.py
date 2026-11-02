# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 10 · RIDDLE 1: "The Proud Letter"
# ==================================================================
#
#  I called the column proudly, with a capital in front;
#  the Ledger gave no answer, just a puzzled little grunt.
#  In Thornmere's Living Ledger every name is spelled just so,
#  and one tall letter standing proud is all it takes to go.
#
#  Orrin found this on the back of a guild roster. It should count
#  the subjects of the realm, and name the largest and smallest guild.
#
#  Run:  python bughunt/riddles/riddle_1_headcount.py
#  When it's fixed, it prints EXACTLY this:
#
#    THE ROLL OF THE REALM, BY GUILD
#    Subjects of the realm: 200
#    Number of guilds:      8
#    Largest guild:  Forge 60
#    Smallest guild: Kitchens 12
#    Average guild size: 25.0

import pandas as pd

df = pd.read_csv("data/thornmere_payroll.csv")

counts = df["Department"].value_counts()
print("THE ROLL OF THE REALM, BY GUILD")
print("Subjects of the realm:", len(df))
print("Number of guilds:     ", len(counts))
print("Largest guild: ", counts.index[0], counts.iloc[0])
print("Smallest guild:", counts.index[-1], counts.iloc[-1])
average = len(df) / len(counts)
print(f"Average guild size: {average:.1f}")
