def indoor_voice():
    message = ""
    while message == "":
        message = input("Input your message: ")
        if message == "":
            print("Message cannot be blank!")
    return message.lower()

if __name__ == "__main__":
    message = indoor_voice()
    print(message)