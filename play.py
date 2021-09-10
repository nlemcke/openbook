sentence = input("Please enter a sentence: ")
newsen = ''

for letters in sentence:
    if letters != " ":
        newsen = newsen + letters
    else:
        continue

print("Your sentence without spaces is: /n", newsen)
