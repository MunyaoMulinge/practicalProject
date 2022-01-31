from textblob import TextBlob
t = 1
while t:
    a = input("Enter word to be checked:\n")
    print(f"Original text is {a}")

    b = TextBlob(a)
    print(f"Corrected text is {b.correct()}")

    t = int(input("Try again? 1:0"))

