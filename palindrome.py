print("==== PALINDROME CHECKER ====")

while True:
    stack = []
    queue = []

    text = input("\nEnter a word or number: ")

    if text == "":
        print("Error: Please enter a word or number.")
        continue

    for char in text:
        stack.append(char)
        queue.append(char)

    palindrome = True

    while stack:
        stack_char = stack.pop()
        queue_char = queue.pop(0)

        if stack_char != queue_char:
            palindrome = False
            break

    if palindrome:
        print("Result: It is a PALINDROME.")
    else:
        print("Result: It is NOT a PALINDROME.")

    choice = input("\nDo you want to check another input? (Yes/No): ")

    if choice.lower() != "yes":
        print("Thank you for using Palindrome Checker!")
        break
