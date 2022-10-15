def slow_down():
    speech = ""
    while speech == "":
        speech = input("Input text to slow... down...\n")
        if speech == "":
            print("Speech cannot be blank!")

    return speech.replace(" ", "... ") + "..."

if __name__ == "__main__":
    slowed = slow_down()
    print(slowed)