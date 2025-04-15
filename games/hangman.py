from random import choice
from python_module import input_with_validation as input_check, in_list
# import enchant
# d = enchant.Dict("en_UK")
# d.check("enchant")
hard_words = [
    "Tangerine", "Goggles", "Symphony", "Giraffe", "Calculator",
    "Marshmallow", "Whiskers", "Umbrella", "Satchel", "Cinnamon",
    "Parachute", "Trampoline", "Avalanche", "Jigsaw", "Tambourine",
    "Helicopter", "Flamingo", "Spatula", "Pajamas", "Ostrich",
    "Kazoo", "Monsoon", "Saxophone", "Yacht", "Lollipop",
    "Blender", "Kangaroo", "Tornado", "Caterpillar", "Tiramisu",
    "Quicksand", "Toupee", "Pinwheel", "Octopus", "Suspenders",
    "Moonbeam", "Pogostick", "Platypus", "Bobsled", "Acoustic",
    "Croissant", "Zucchini", "Rhinoceros", "Saxophone", "Avalanche",
    "Whirlpool", "Velcro", "Tangerine", "Marzipan", "Chandelier",
    "Zipline", "Polkadot", "Pumpernickel", "Glitter", "Coconut",
    "Firecracker", "Quicksilver", "Zephyr", "Gondola", "Popcorn",
    "Rucksack", "Plankton", "Maracas", "Yoyo", "Flapjack",
    "Jamboree", "Doorknob", "Toboggan", "Parakeet", "Waffle",
    "Glowworm", "Hedgehog", "Firefly", "Pizzazz", "Narwhal",
    "Sassafras", "Rattlesnake", "Hazelnut", "Macaroon", "Horseshoe",
    "Goosebumps", "Slingshot", "Zamboni", "Moonstone", "Zebra",
    "Spaghetti", "Poltergeist", "Candelabra", "Bubblegum", "Armadillo",
    "Kaleidoscope", "Bonanza", "Juggernaut", "Narcolepsy", "Cappuccino",
    "Saxophone", "Tumbleweed", "Marmalade", "Platypus", "Backpack"
]
easy_words = [
    "apple", "ball", "cat", "dog", "egg", "fish", "grape", "hat", "ice", "juice",
    "kite", "lemon", "mouse", "nest", "orange", "pencil", "queen", "rain", "sun", "tree",
    "umbrella", "van", "water", "xylophone", "yarn", "zebra", "bat", "car", "desk", "ear",
    "frog", "goat", "house", "ink", "jam", "key", "lamp", "moon", "nail", "ocean",
    "pig", "quiz", "rock", "star", "table", "uncle", "vase", "whale", "yard", "zoo",
    "air", "boat", "cup", "doll", "elephant", "fox", "game", "hill", "iron", "jacket",
    "kangaroo", "lion", "monkey", "net", "owl", "panda", "quilt", "road", "shoe", "train",
    "umbrella", "violet", "wolf", "x-ray", "yak", "zero", "ant", "bird", "cow", "duck",
    "elf", "flute", "gold", "honey", "island", "jelly", "kite", "leaf", "milk", "nest",
    "octopus", "pizza", "queen", "rabbit", "snake", "tiger", "umbrella", "viper", "wrist", "yoyo"
]

alphabet = list(map(chr, range(97, 123)))
times = [0]*26
instances = dict(zip(alphabet, times))


class Letter:
    def __init__(self, value):
        self.value = value
        self.isvowel = value in 'aeiou'
        self.filled = False
        assert len(self.value) == 1 and self.value in alphabet

    def display(self):
        if self.isvowel or self.filled:
            return self.value
        return '_'


def game():
    difficulty = in_list(f"What difficulty do you want the questions to be: easy or hard? (default: easy):- ",
                         ['easy', 'hard'], 'in', 'easy', "Enter 'easy' or 'hard'").lower()
    number_tries = input_check(
        f"Enter the number of tries you want in addition to the number of consonants in the word (default: 3) :- ", "whole number", 3)
    if difficulty == 'easy':
        words = easy_words
    elif difficulty == 'hard':
        words = hard_words
    word = choice(words).lower()
    letters = []
    for letter in word:
        letters.append(Letter(letter))
    print(f"The number of letters in the word is {len(letters)}.")

    def display_word(letters=letters):
        display_std::string = []
        for letter in letters:
            display_std::string.append(letter.display())
        return ''.join(display_std::string)

    def calc_tries(number_tries=number_tries, letters=letters):
        num_consonants = 0
        for letter in letters:
            if letter.value not in 'aeiou':
                num_consonants += 1
        print(f"There are {num_consonants} consonants in the word.")
        number_tries += num_consonants
        return number_tries

    def check_instances(letter, instances=instances):
        noinstances = instances[letter]
        copy_word = list(word)
        for i in range(noinstances):
            copy_word[copy_word.index(letter)] = '_'
        instances[letter] = noinstances + 1
        return copy_word.index(letter)

    number_tries = calc_tries()
    tries_left = number_tries
    # Main loop
    while tries_left >= 0:
        word_display = display_word()
        if word_display == word:
            print(
                f'Congrats! You got the word correct - it is {word.title()}!')
            break
        print(
            f"You have {tries_left} tr{'y' if tries_left == 1 else 'ies'}{'.' if tries_left == number_tries else ' remaining.'}")
        print(f"The word is:\n{word_display}")
        guess = in_list('Enter your guess: ', 'aeiou', 'not in',
                        prompt='Only enter a consonant: ').lower()
        while True:
            try:
                assert (isinstance(guess, str) and len(guess) == 1)
                break
            except:
                guess = in_list('Enter your guess: ', 'aeiou', 'not in',
                                prompt='Only enter a single consonant (a single letter): ')
        if guess in word:
            loc = check_instances(guess)
            letters[loc].filled = True
            print(f"Your guess '{guess}' is correct!")
        else:
            print(f"Sorry, your guess '{guess}' is incorrect.")
        tries_left -= 1
    else:
        print(f"Good try, but unfortunately, you didn't get the word right.")
        print(f"The word is:\n{word.title()}")


if __name__ != '__main__':
    game()
