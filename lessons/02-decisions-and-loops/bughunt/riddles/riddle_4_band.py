# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 4: "The Edge of the Band"
# ==================================================================
#
#  She stood upon the border line,
#  and asked: am I yours or am I thine?
#  The sign said 'more', but she was 'same'.
#  Allow the equal into the game.
#
#  Lady Siv's pay bands: band B starts at 30,000 crowns.
#  Wren earns exactly 30,000 and somehow ends up in band A.
#
#  Run:  python bughunt/riddles/riddle_4_band.py
#  When it's fixed, it prints EXACTLY this:
#
#    Bram    28,500 cr  band A
#    Wren    30,000 cr  band B
#    Corwin  41,200 cr  band B
#    Ysolde  52,000 cr  band C
#    In band B: 2

records = "Bram/28500;Wren/30000;Corwin/41200;Ysolde/52000"
band_b = 0
for record in records.split(";"):
    name, salary_text = record.split("/")
    salary = int(salary_text)
    if salary >= 50000:
        band = "C"
    elif salary > 30000:
        band = "B"
        band_b = band_b + 1
    else:
        band = "A"
    print(f"{name:<7} {salary:>6,} cr  band {band}")
print("In band B:", band_b)
