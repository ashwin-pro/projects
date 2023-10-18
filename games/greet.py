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

def print_acrostic(name,alphabet={letter:adjectives[count] for count,letter in enumerate(f"abcdefghijklmnopqrstuvwxyz")},):
    for index,letter in enumerate(name):
        num_before = name[:index].count(letter)
        try:
            alphabet[letter][num_before]
            already_done.append(alphabet[letter][num_before])
            print(f"{letter.title()} - {alphabet[letter][num_before].title()}")
        except:
            pass
            

name = clean(input(f"What's your name? : ").strip().lower())
if name in [f"shashank",f"sahasra",]:
    if name == f"shashank":
        print(f'''S - Smart
H - Heroic
A - Awesome
S - Spectacular
H - Hallowed
A - Agreeable
N - Noble
K - Knowledgeable''')
    else:
        print(f'''S - Sapient
# Do adjectives''')
else:
    print_acrostic(name=name)