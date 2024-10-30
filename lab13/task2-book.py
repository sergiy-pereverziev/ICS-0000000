import book
def main():
    print("Operating a book")
    b = book.Book("Cinderella", "Charles Perrot", "Art Books", "1997", 2)

    print("Bought me a book\n")
    print(b.display_properties())
    
    while True:
        chapter_name = input("Input chapter (empty to exit): ")
        if not chapter_name:
            break

        try:
            pages = int(input("Input number of pages in this chapter: "))
            if (pages <= 0):
                raise ValueError("Must be a positive number")
        except ValueError as e:
            print(f"Input error: {e}")
            continue

        b.add_section(chapter_name)
        b.add_pages(pages)

    print("Updated book:")
    print(b.display_properties())
    print("Table of contents:")
    print(b.display_contents())

if __name__ == "__main__":
    main()