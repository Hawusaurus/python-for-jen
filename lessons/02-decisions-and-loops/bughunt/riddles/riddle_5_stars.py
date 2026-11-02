# ==================================================================
#  THE GRIMOIRE'S RIDDLES · LESSON 02 · RIDDLE 5: "The Stars That Fell"
# ==================================================================
#
#  A star was named, then named again,
#  the second word replaced the first, and then
#  the count grew loud in every row.
#  Two faults to find. One more to go.
#
#  Lady Siv's review scroll. Ratings of 4 or 5 are stars, 3 is solid, below is watch.
#  Dalvric's version calls nobody a star and can't stop counting.
#
#  Run:  python bughunt/riddles/riddle_5_stars.py
#  When it's fixed, it prints EXACTLY this:
#
#    Maren  star
#    Jory   watch
#    Bram   solid
#    Elowen star
#    Stars: 2

records = "Maren/5;Jory/2;Bram/3;Elowen/4"
stars = 0
for record in records.split(";"):
    name, rating_text = record.split("/")
    rating = int(rating_text)
    if rating >= 4:
        label = "star"
        stars = stars + 1
    if rating == 3:
        label = "solid"
    else:
        label = "watch"
    print(f"{name:<7}{label}")
    print("Stars:", stars)
