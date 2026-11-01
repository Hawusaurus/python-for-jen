# Lesson 11: Charts and Excel output (lecture notes for Lars)

**Goal:** Jen can turn a DataFrame into a PNG chart and into a formatted
Excel workbook, from a script, without touching a mouse. This is the "last
mile" of every analysis and the last piece she needs for the capstone.

Run `demo.py` section by section (`python demo.py` writes into `demo_output/`).
Open the PNGs and the workbook on screen as they appear.

---

## [Opener, 1 min] Gerald's email

Read Gerald's memo from `GUIDE.pdf`. The board reads pictures and then asks
for "the Excel". Dave did this by hand over a weekend. We'll do it in a
script, and next lesson it becomes the pay gap report.

## [0–3 min] A chart is a file

```python
import matplotlib
matplotlib.use("Agg")           # no window: we're writing files
import matplotlib.pyplot as plt
```

- In Excel a chart lives in the workbook. Here a chart is a PNG we *save*.
- `Agg` = "draw into memory". Without it, scripts try to open a window
  and either hang or complain. Always these three lines, in this order.
- Show the recipe: `figure` → draw → decorate → `tight_layout` → `savefig`.
  Same order every time. Draw it on the whiteboard as five boxes.

## [3–7 min] Bar chart and histogram (demo sections 1–2)

```python
counts = df["department"].value_counts()
plt.figure(figsize=(8, 4))
plt.bar(counts.index, counts.values, color="#1f3a5f")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("demo_output/headcount.png", dpi=150)
```

- Open the PNG. Then delete `tight_layout()` and run again: labels cut off.
  Put it back. That's the one line she'll forget.
- `plt.hist(df["annual_salary"], bins=12)`: a bar chart of *how many* fall
  in each bucket. Ask: "where's the middle?" → `axvline(median)`.
- Mention Excel's histogram exists (2016+) but nobody finds it.

## [7–9 min] Two series side by side (demo section 3)

- `pivot_table` gives a table with F and M columns, which she knows from lesson 10.
- Trick: positions `x = np.arange(n)`, draw one series at `x - 0.2` and the
  other at `x + 0.2`, both with `label=`, then `plt.legend()`.
- Look at the Warehouse bars together. Don't explain; let her notice.

## [9–12 min] pandas writes Excel (demo section 4)

```python
df.to_excel("demo_output/one.xlsx", sheet_name="Data")

with pd.ExcelWriter("demo_output/many.xlsx") as writer:
    by_dept.to_excel(writer, sheet_name="By department")
    top10.to_excel(writer, sheet_name="Top 10", index=False)
```

- `to_excel` needs openpyxl, which is why it's in `requirements.txt`.
- `index=False` drops the row numbers. For grouped tables the index *is*
  the department name, so keep it.
- Open the workbook: correct, and ugly. Columns squashed, no formats.

## [12–15 min] openpyxl makes it pretty (demo section 5)

```python
wb = load_workbook(path); ws = wb["Data"]
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F3A5F")
cell.number_format = "£#,##0.00"      # exactly the Format Cells string
ws.column_dimensions["A"].width = 16
ws.freeze_panes = "A2"
wb.save(path)
```

- Two layers: pandas writes values, openpyxl edits looks. Like typing the
  numbers, then selecting and formatting, except it's code and it's forever.
- Point out the colour gotcha: matplotlib wants `#1f3a5f`, openpyxl wants
  `1F3A5F`. She *will* hit this.
- Reopen the workbook, show the result. Hand over to `EXERCISES.pdf` and
  `CHEATSHEET.pdf`. Remind her: `pip install -r requirements.txt` first.

---

## Excel → Python cheat table (show at the end)

| Excel | Python |
|---|---|
| Insert → Chart → Column | `plt.bar(labels, values)` |
| Insert → Chart → Histogram | `plt.hist(values, bins=12)` |
| Chart title, axis titles | `plt.title()`, `plt.xlabel()`, `plt.ylabel()` |
| Legend | `label=` on each series, then `plt.legend()` |
| Save As picture | `plt.savefig("x.png", dpi=150)` |
| Save As .xlsx | `df.to_excel(path, sheet_name=...)` |
| New sheet | `pd.ExcelWriter`, or `wb.create_sheet("Name")` |
| Bold / fill colour | `Font(bold=True)`, `PatternFill("solid", fgColor=...)` |
| Format Cells → Custom | `cell.number_format = "£#,##0.00"` |
| Column width | `ws.column_dimensions["A"].width = 16` |
| Freeze Panes | `ws.freeze_panes = "A2"` |
| Insert → Picture | `ws.add_image(Image("x.png"), "B2")` |

**Questions to check understanding:**
- Why is there no `plt.show()` in a script, and what do we do instead?
- What does pandas do to an Excel file, and what does openpyxl do?
- Where exactly does `"£#,##0.00"` come from?
