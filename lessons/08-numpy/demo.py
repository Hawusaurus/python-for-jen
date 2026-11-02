# Lesson 08 demo: run from the lesson folder with  python demo.py
# or copy sections into the REPL one by one.
import csv
import numpy as np

rewards = []
paid = []
days = []
difficulty = []
outcomes = []
with open("data/quests.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rewards.append(float(row["reward"]))
        paid.append(float(row["paid"]))
        days.append(float(row["days"]))
        difficulty.append(int(row["difficulty"]))
        outcomes.append(row["outcome"])

print("--- The loop vs the line ---")
per_day_loop = []
for i in range(len(paid)):
    per_day_loop.append(paid[i] / days[i])
rewards = np.array(rewards)
paid = np.array(paid)
days = np.array(days)
difficulty = np.array(difficulty)
outcomes = np.array(outcomes)
per_day = paid / days
print([round(x, 2) for x in per_day_loop[:3]])
print(per_day[:3].round(2))
print(paid.shape, paid.dtype)

print("\n--- Summaries ---")
print(rewards.min(), rewards.max(), round(rewards.mean(), 2), rewards.sum())
print(np.median(rewards))
print(np.percentile(rewards, 75))
print(np.percentile(rewards, [25, 50, 75]))
print(rewards.mean)   # <- the classic mistake: no brackets

print("\n--- Masks ---")
big = rewards > 1000
print(big[:5])
print("count:", big.sum(), " share:", big.mean())
print("their mean:", rewards[big].mean().round(2))
success = outcomes == "Success"
print("won:", success.sum())
print("big and won:", (big & success).sum())
# print((rewards > 1000) and (outcomes == "Success"))   # <- uncomment to see the error

print("\n--- Axis ---")
loot = np.array([
    [620, 0, 1380, 550, 2710, 740],
    [260, 310, 0, 430, 260, 0],
    [480, 550, 670, 0, 910, 620],
])
print(loot.sum(), loot.sum(axis=0), loot.sum(axis=1))
print(loot[1, 3], loot[:, 2])

print("\n--- The Charter question in four lines ---")
for d in range(1, 6):
    level = difficulty == d
    print(f"difficulty {d}: {success[level].mean() * 100:.0f}% succeed, "
          f"{per_day[level].mean():.2f} cr per quest-day")
