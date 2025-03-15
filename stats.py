from itertools import count


# Fetches content to read and stores it into container
file = open('/home/anthony-kral/Documents/GitHub/bookbot/books/frankenstein.txt', "r")
contents = file.read()

    # checks if the file has closed correctly
file.close()

word_list = contents.split()
num_words = len(word_list)
print(f"{num_words} words found in the document")


# counts number of characters
words = contents.lower()
t = 0
p = 0
c = 0
for char in words:
    if char == "t":
        t += 1
print(f"'t': {t}'"),
for char in words:
    if char == "p":
        p += 1
print(f"'p': {p}'")
for char in words:
    if char == "c":
        c += 1
print(f"'c': {c}'")
    

