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



def clean(string):
    cleaned_string = ''
    for letter in string:
        if letter.isalpha():
            cleaned_string += letter
    return cleaned_string


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
            else:
                do_break = False
                for i in range(name.count(letter)):
                    if do_break:
                        break
                    for verys_form in [f"Very {'very '*(i+1)}{adjective}" for adjective in alphabet[letter]]:
                        if verys_form not in already_done:
                            print(f"{letter.title()} - {verys_form}")
                            already_done.append(verys_form)
                            do_break = True
                            break


def feedback():
    def get_rating():
        rating = input(f"Please rate the game out of 5 stars : ")
        correct_input = False
        while not correct_input:
            try:
                rating = float(rating)
                if rating <= 5 and rating > 0:
                    correct_input = True
                else:
                    rating = input(f"Please enter a number below 5 and above 0: ")
            except:
                rating = input(f"Please enter a number (below 5 and above 0) : ")
        return rating
    
    def confirm_rating(rating):
        confirm = input(f"Please confirm your rating of {rating}\nEnter 'y' to confirm and 'n' to change your rating. If incorrect input is given, 'y' is selected by default : ")
        correct_input = False
        while not correct_input:
            try:
                confirm = confirm.strip().lower()
                correct_input = True
            except:
                confirm = input(f"Enter 'y' or 'n' : ").strip()
        correct_input = False
        while not correct_input:
            if confirm in ['y','n',]:
                correct_input = True
                if confirm == 'y':
                    messages = {5:"Thank you for your support. If you have any compliments, please enter them : ",4:"Thank you for your feedback. If you have any suggestions, please enter them : ",3:"Thank you for your time. If you have any suggestions or complaints, please enter them : ",2:"Thank you for your time. If you have any complaints, please enter them : ",1:"Thank you for your time."}
                    for rating_ in messages.keys():
                        if (int(rating)+(rating > int(rating))) == rating_:
                            suggestions = input(messages[rating_])
                            print(f"Thank you for your input. It will really help improve the quality of this game.")
                            with open("greet_suggestions.txt",'a') as g_s:
                                g_s.write(suggestions)
                            del suggestions
                else:
                    print(f"Okay, getting rating again ...\n")
                    confirm_rating(rating=get_rating())
            else:
                print(f"Selecting 'y' by default ...")
                confirm = 'y'

    confirm_rating(rating=get_rating())


print_acrostic(name=clean(input(f"What's your name? : ").strip().lower()))
feedback()