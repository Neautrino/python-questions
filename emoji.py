def get_language_emoji(language):
    # Define a dictionary mapping programming languages to emoji codes
    language_emoji = {
        "Python": "🐍",
        "JavaScript": "🌐",
        "Java": "☕",
        "C++": "🔵",
        "Ruby": "💎",
        "Swift": "🍏",
    }

    # Check if the input language is in the dictionary
    if language in language_emoji:
        return language_emoji[language]
    else:
        return "Language not found"

# Input the programming language
programming_language = input("Enter a programming language: ")

# Get and print the emoji code
emoji_code = get_language_emoji(programming_language)
print(f"The emoji code for {programming_language} is {emoji_code}")
