def to_lowercase(text):
    # Convert the text to lowercase
    return text.lower()

def main():
    # Get input from the user
    user_input = input("Enter some text: ")

    # Convert the input to lowercase
    lowercase_text = to_lowercase(user_input)

    # Print the lowercase text
    print("Lowercase text:", lowercase_text)

if __name__ == "__main__":
    main()