import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I used to play piano by ear, but now I use my hands.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you get when you cross a snowman and a dog? Frostbite.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
]

def get_random_joke():
    return random.choice(jokes)

# Generate and print a random joke
random_joke = get_random_joke()
print("Random Joke:")
print(random_joke)
