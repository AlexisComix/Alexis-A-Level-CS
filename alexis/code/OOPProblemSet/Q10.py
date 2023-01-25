import string

def display_menu():
    print(
        """
        1. Enter encryption/decryption key
        2. Encrypt a message
        3. Decrypt a message
        4. Exit
        """
    )

class EncryptDecrypt:
    def __init__(self):
        self.__encr_decr_key: int

    @property
    def encr_decr_key(self) -> int:
        try:
            return self.__encr_decr_key
        except:
            Exception("Key cannot be empty")

    @encr_decr_key.setter
    def set_key(self, key: int):
        if key not in range(1, 26):
            raise Exception("Key must be  in range 1-26")
        self.__encr_decr_key = key

    def encrypt(self, text: str) -> str:
        plaintext = text.lower()
        ciphertext = ""
        for character in plaintext:
            if character not in string.ascii_lowercase:
                ciphertext += character
            else:
                index = (
                    string.ascii_lowercase.find(character) 
                    + self.__encr_decr_key
                )
                if index < len(string.ascii_lowercase):
                    ciphertext += string.ascii_lowercase[index]
                else:
                    if index > 25:
                        ciphertext += string.ascii_lowercase[
                            index - len(string.ascii_lowercase)
                        ]
                    elif index < 0:
                        ciphertext += string.ascii_lowercase[
                            index + len(string.ascii_lowercase)
                        ]
        return ciphertext

    def decrypt(self, text: str):
        plaintext = text.lower()
        ciphertext = ""
        for character in plaintext:
            if character not in string.ascii_lowercase:
                ciphertext += character
            else:
                index = (
                    string.ascii_lowercase.find(character) 
                    - self.__encr_decr_key
                )
                if index < len(string.ascii_lowercase):
                    ciphertext += string.ascii_lowercase[index]
                else:
                    if index > 25:
                        ciphertext += string.ascii_lowercase[
                            index - len(string.ascii_lowercase)
                        ]
                    elif index < 0:
                        ciphertext += string.ascii_lowercase[
                            index + len(string.ascii_lowercase)
                        ]
        return ciphertext


def main():
    cipher = EncryptDecrypt()
    running = True
    while running:
        display_menu()
        match int(input("Select an option: ")):
            case 1:
                cipher.set_key = int(input("Enter a key: "))
            case 2:
                print(cipher.encrypt(input("Input some text:\n")))
            case 3:
                print(cipher.decrypt(input("Input some text:\n")))
            case 4:
                running = False
            case _:
                print("Invalid option")

if __name__ == "__main__":
    main()