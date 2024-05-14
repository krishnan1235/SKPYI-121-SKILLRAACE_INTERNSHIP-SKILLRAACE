class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._royalty_amount = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._royalty_amount = self._price * 0.1 * copies_sold
        elif copies_sold <= 1500:
            self._royalty_amount = (500 * 0.1 + (copies_sold - 500) * 0.125) * self._price
        else:
            self._royalty_amount = (500 * 0.1 + 1000 * 0.125 + (copies_sold - 1500) * 0.15) * self._price

        return self._royalty_amount
class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, value):
        self._ebook_format = value

    def royalty(self, copies_sold):
        royalty_amount = super().royalty(copies_sold)
        gst_deduction = royalty_amount * 0.12
        return royalty_amount - gst_deduction
def main():
    book1 = Book("Python", "Krish", "TT Publications", 28.0)
    book1.title = "Python"
    book1.author = "Krish"
    book1.publisher = "TT Publications"
    book1.price = 28.0
    #royality
    book_royalty = book1.royalty(800)
    print("Royalty for the book:", book_royalty)

    ebook1 = Ebook("Python (Ebook)", "Krish", "TT Publications", 23.0, "PDF")
    ebook1.title = "Python (Ebook)"
    ebook1.author = "Krish"
    ebook1.publisher = "TT Publications"
    ebook1.price = 23.0
    ebook1.ebook_format = "PDF"

    # Calculating royalty for ebook
    ebook_royalty = ebook1.royalty(540)
    print("Royalty for the ebook:", ebook_royalty)

if __name__ == "__main__":
    main()
