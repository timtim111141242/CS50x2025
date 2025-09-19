text = input("Text:")


def count_letters(TText):
    count = 0
    for i in TText:
        if i.isalpha():
            count += 1
    return count


def count_words(TText):
    count = 1
    for i in TText:
        if i == " ":
            count += 1
    return count


def count_sentences(TText):
    count = 0
    for i in TText:
        if i == "." or i == "!" or i == "?":
            count += 1
    return count


letters = count_letters(text)
words = count_words(text)
sentences = count_sentences(text)

L = letters / words * 100
S = sentences / words * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
