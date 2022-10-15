def faces():
    text = ""
    while text == "":
        text = input("Input text to face-ify!\n")
        if text == "":
            print("Text cannot be blank!")

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

if __name__ == "__main__":
    face_ified = faces()
    print(face_ified)