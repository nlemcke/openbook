macros = [("carbs", ["pasta", "rice", "beans", "peanuts"]),
        ("protein", ["chicken", "beans", "peanuts"]),
        ("fat", ["avocado", "coconut", "peanuts"])]

for (macro, foods) in macros:
    count = len(foods)
    print("There are", count, "foods in", macro)

