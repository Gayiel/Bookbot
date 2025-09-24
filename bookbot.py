def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    return text

if __name__ == "__main__":
    main()
