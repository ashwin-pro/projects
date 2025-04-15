def clean(string):
    cleaned_string = ''
    for letter in string:
        if letter.isalpha():
            cleaned_string += letter
    return cleaned_string

already_done = []
adjectives = [
    ['Affable', 'Amiable', 'Attentive', 'Adventurous'],
    ['Brilliant', 'Benevolent', 'Bold', 'Blissful'],
    ['Charismatic', 'Compassionate', 'Courteous', 'Caring'],
    ['Diligent', 'Dynamic', 'Delightful', 'Devoted'],
    ['Eloquent', 'Empathetic', 'Energetic', 'Enthusiastic'],
    ['Friendly', 'Funny', 'Forgiving', 'Fearless'],
    ['Generous', 'Gentle', 'Gracious', 'Gregarious'],
    ['Humble', 'Helpful', 'Honest', 'Hardworking'],
    ['Innovative', 'Inspiring', 'Intelligent', 'Inquisitive'],
    ['Joyful', 'Jovial', 'Judicious', 'Joyous'],
    ['Kind', 'Knowledgeable', 'Keen', 'Kind-hearted'],
    ['Loyal', 'Lively', 'Loving', 'Liberated'],
    ['Modest', 'Motivated', 'Mindful', 'Magnanimous'],
    ['Nurturing', 'Noble', 'Neighborly', 'Natural'],
    ['Optimistic', 'Open-minded', 'Observant', 'Outgoing'],
    ['Patient', 'Positive', 'Polite', 'Passionate'],
    ['Quirky', 'Quick-witted', 'Quiet', 'Quality-conscious'],
    ['Respectful', 'Reliable', 'Radiant', 'Resourceful'],
    ['Sociable', 'Supportive', 'Sincere', 'Spirited'],
    ['Tolerant', 'Thoughtful', 'Trustworthy', 'Tenacious'],
    ['Understanding', 'Upbeat', 'Unique', 'Unpretentious'],
    ['Versatile', 'Vibrant', 'Valiant', 'Vivacious'],
    ['Witty', 'Warm-hearted', 'Wise', 'Wonderful'],
    ['Xenial', ],
    ['Youthful', 'Yearning'], 
    ['Zealous','Zany'],
]

for adjective_sub in adjectives:
    for i,adjective in enumerate(adjective_sub):
        adjective_sub[i] = adjective.lower()

def print_acrostic(name,alphabet={letter:adjectives[count] for count,letter in enumerate(f"abcdefghijklmnopqrstuvwxyz")}):
    for index,letter in enumerate(name):
        num_before = name[:index].count(letter)
        try:
            alphabet[letter][num_before]
            already_done.append(alphabet[letter][num_before])
            print(f"{letter.title()} - {alphabet[letter][num_before].title()}")
        except:
            for very_form in [f"Very {adjective}" for adjective in alphabet[letter]]:
                if very_form not in already_done:
                    print(f"{letter.title()} - {very_form}")
                    already_done.append(very_form)
                    break

            for i in range(name.count(letter)):
                for very_form_ in [f"Very {'very '*(i+1)}{adjective}" for adjective in alphabet[letter]]:
                    if very_form_ not in already_done:
                        print(f"{letter.title()} - {very_form_}")
                        already_done.append(very_form_)
                        break

name = clean(input(f"What's your name? : ").strip().lower())
if name in [f"shashank",f"sahasra",]:
    if name == f"shashank":
        print_acrostic(name=name)
        print()
    else:
        print_acrostic(name=name)
else:
    print_acrostic(name=name)