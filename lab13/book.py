class Book:
    __name = ""
    __author = "" 
    __publisher = "" 
    __year = 0
    __pages = 0
    __sections: list[str] = []

    def __init__(self, name: str, author: str, publisher: str, year: int, pages: int):
        self.__name = name
        self.__author = author
        self.__publisher = publisher
        self.__year = year
        self.__pages = pages

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages: int):
        if (pages <= 0):
            raise ValueError("Must have at least 1 page")
        
    def add_section(self, section: str):
        self.__sections.append(section)

    def remove_section(self, section: str):
        if not (section in self.__sections):
            raise ValueError(f"No such section: {section}")
    
    def display_properties(self):
        return f"Name: {self.__name}\nAuthor: {self.__author}\nPublisher: {self.__publisher}\nYear: {self.__year}\nTotal pages: {self.__pages}"

    def display_contents(self):
        result = ""
        for i in range(len(self.__sections)):
            result += f"Chapter {i + 1}. {self.__sections[i]}\n"

        return result
            
    def add_pages(self, num: int):
        self.__pages += num

    def dec_pages(self, num: int):
        if (self.__pages <= num):
            raise ValueError("Cannot remove last page from the book")
        
        self.__pages -= num