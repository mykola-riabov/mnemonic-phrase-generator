from mnemonic import Mnemonic

mnemo = Mnemonic("english")

num_phrases = 1  # Number of seed phrases you want to generate
num_words = 24  # Number of words in each seed phrase

with open("mnemonic_phrases.txt", "w") as file:
    for _ in range(num_phrases):
        words = mnemo.generate(strength=256).split()
        seed_phrase = " ".join(words[:num_words])
        file.write(seed_phrase + "\n")

print("Seed phrase generation and saving completed.")