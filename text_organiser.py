def organise_text(text):
    """
    Organises the given text by converting it to lowercase, removing unnecessary whitespace,
    and sorting the words alphabetically.

    Args:
        text (str): The input text to be organised.

    Returns:
        str: The organised text.
    """
    # Remove extra whitespaces
    no_extra_spaces = " ".join(text.split())

    # Convert text to lowercase
    lower_text = text.lower()

    # Split text into words
    words = lower_text.split(" ")

    # Split words alphabetically
    sorted_words = sorted(words)

    # Join words back into a string
    organised_text = " ".join(sorted_words)

    return organised_text

def main():
    """
    Function to get user input text
    """

    user_text = input("Enter the text you want to organise: ")
    organised_text = organise_text(user_text)
    print("\nText organised:")
    print(organised_text)

if __name__ == "__main__":
    main()







