with open("text_files/my_novel.txt", "w") as file:
    while True:
        user_input = input(": ")
        if user_input == "quit":
            break
        file.write(user_input + "\n")