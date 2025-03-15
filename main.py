# Fetches content to read and stores it into container
with open('/home/anthony-kral/Documents/GitHub/bookbot/books/frankenstein.txt', encoding="utf-8") as f:
    read_data = f.read()
    
# checks if the file has closed correctly
f.closed
def main():
    print(read_data)


main()
