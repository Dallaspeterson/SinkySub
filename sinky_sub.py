def reverse_text(text):
    return text[::-1]

def main():
    # Get input from the user
    user_input = input("Enter some text: ")

    # Convert the input to lowercase
    lowercase_text = user_input.lower()

    # Print the lowercase text
    print("Lowercase text:", lowercase_text)

    # Reverse the text and print it
    reversed_text = reverse_text(user_input)
    print("Reversed text:", reversed_text)

if __name__ == "__main__":
    main()