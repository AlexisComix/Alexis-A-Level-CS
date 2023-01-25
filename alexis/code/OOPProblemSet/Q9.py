class Info:
    def __init__(self):
        self.__user_text: str

    @property
    def user_text(self) -> str:
        try:
            return self.__user_text
        except:
            raise Exception("User Text not set")

    @user_text.setter
    def set_user_text(self, text: str):
        if text == "":
            raise Exception("Text cannot be empty")
        self.__user_text = text

    def get_spaces_count(self) -> int:
        return self.__user_text.count(" ")

    def get_words_count(self) -> int:
        return self.get_spaces_count() + 1

    def get_vowels_count(self) -> int:
        return len(
            list(
                filter(
                    lambda x: x.lower() in "aeiou",
                    self.__user_text
                )
            )
        )

    def get_letters_count(self) -> int:
        return len(
            list(
                filter(
                    lambda x: x != " ",
                    self.__user_text
                )
            )
        )


def main():
    text = input("Enter some text:\n")
    info = Info()
    info.set_user_text = text
    print(info.get_spaces_count())
    print(info.get_words_count())
    print(info.get_vowels_count())
    print(info.get_letters_count())

if __name__ == "__main__":
    main()