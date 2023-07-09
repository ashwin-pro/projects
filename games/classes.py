class Ninjago:
    def __init__(self,name="Unknown",age=0,hasPowers=False,strengths=[],weaknesses=[],power_level="Moderate",knowsSpinjitsu=False,allies = [],enemies = [],coins = 50,power_ups = {}):
        self.name = name
        self.age = age
        self.hasPowers = hasPowers
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.power_level = power_level
        self.knowsSpinjitsu = knowsSpinjitsu
        self.allies = allies
        self.enemies = enemies
        self.coins = coins
        self.power_ups = power_ups
    
    def introduce(self):
        if self.strengths:
            strength_string = ''
            for strength in self.strengths[:-2]:
                strength_string += f"{strength}, "
            strength_string += f"{self.strengths[-2]} and {self.strengths[-1]}"
        else:
            strength_string = "none"

        if self.weaknesses:
            weakness_string = ''
            for weakness in self.weaknesses[:-2]:
                weakness_string += f"{weakness}, "
            weakness_string += f"{self.weaknesses[-2]} and {self.weaknesses[-1]}"
        else:
            weakness_string = "none"

        if self.allies:
            ally_string = ''
            for ally in self.allies[:-2]:
                ally_string += f"{ally.title()}, "
            ally_string += f"{self.allies[-2].title()} and {self.allies[-1].title()}"
        else:
            ally_string = "none"

        if self.enemies:
            enemy_string = ''
            for enemy in self.enemies[:-2]:
                enemy_string += f"{enemy.title()}, "
            enemy_string += f"{self.enemies[-2].title()} and {self.enemies[-1].title()}"
        else:
            enemy_string = "none"

        if self.hasPowers:
            powers_introduce = "have"
        else:
            powers_introduce = "do not have"

        if self.knowsSpinjitsu:
            spinjitsu_introduce = "know"
        else:
            spinjitsu_introduce = "do not know"
        global introduction
        introduction = f"Hello, I am {self.name.title()}. I am {self.age} years old. I {spinjitsu_introduce} Spinjitsu. My strengths are {strength_string}. My weaknesses are {weakness_string}. My power level is {self.power_level}. My allies are {ally_string}. My enemies are {enemy_string}. I {powers_introduce} elemental powers. I have {self.coins} coins."
        return introduction

    def get_power_levels(self):
        self.power_levels = 0
        if self.hasPowers:
            self.power_levels += 10
        if self.knowsSpinjitsu:
            self.power_levels += 5
        for _ in range(len(self.allies)):
            self.power_levels += 1
        for _ in range(len(self.enemies)):
            self.power_levels -= 1
        for _ in range(len(self.strengths)):
            self.power_levels += 2.5
        for _ in range(len(self.weaknesses)):
            self.power_levels -= 2.5
        if self.power_level.title() == "Very Low":
            self.power_levels += 1
        elif self.power_level.title() == "Low":
            self.power_levels += 2.5
        elif self.power_level.title() == "Moderate":
            self.power_levels += 5
        elif self.power_level.title() == "High":
            self.power_levels += 7.5
        elif self.power_level.title() == "Extremely High":
            self.power_levels += 10
        
        return self.power_levels

class Elemental_Master(Ninjago):
    def __init__(self,name="Unknown",age=0,strengths=[],weaknesses=[],power_level="Moderate",knowsSpinjitsu=False,allies=[],enemies=[],elemental_power='energy',coins = 50,power_ups = {}):
        self.name = name
        self.age = age
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.power_level = power_level
        self.knowsSpinjitsu = knowsSpinjitsu
        self.allies = allies
        self.enemies = enemies
        self.elemental_power = elemental_power
        self.hasPowers = True
        self.coins = coins
        self.power_ups = power_ups
    def introduce(self):
        raw_introduction = super().introduce()
        print(raw_introduction + f"I am the elemental master of {self.elemental_power}.")    

class Spinjitsu_Master(Ninjago):
    def __init__(self,name="Unknown",age=0,strengths=[],weaknesses=[],power_level="Moderate",allies=[],enemies=[],coins = 50,power_ups = {}):
        self.name = name
        self.age = age
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.power_level = power_level
        self.allies = allies
        self.enemies = enemies
        self.knowsSpinjitsu = True
        self.hasPowers = False
        self.coins = coins
        self.power_ups = power_ups
    def introduce(self):
        print(super().introduce())
    def get_power_levels(self):
        return super().get_power_levels()

class Ninja(Ninjago):
    def __init__(self,name="Unknown",age=0,strengths=[],weaknesses=[],power_level="Moderate",allies=[],enemies=[],elemental_power='energy',coins = 50,power_ups = {}):
        self.name = name
        self.age = age
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.power_level = power_level
        self.knowsSpinjitsu = True
        self.allies = allies
        self.enemies = enemies
        self.elemental_power = elemental_power
        self.hasPowers = True
        self.coins = coins
        self.power_ups = power_ups
    def introduce(self):
        raw_introduction = super().introduce()
        print(raw_introduction + f"I am the elemental master of {self.elemental_power}.")
    def get_power_levels(self):
        return super().get_power_levels()
    
def fight(Person1,Person2):
    Person1.get_power_levels()
    Person2.get_power_levels()
    Person1_permanent_levels = Person1.power_levels
    Person2_permanent_levels = Person2.power_levels
    Person1_permanent_powers = Person1.hasPowers
    Person2_permanent_powers = Person2.hasPowers
    def get_power_ups(Person1):
        if Person1.power_ups:
            power_ups_wanted = f"Do you want to use any of your power-ups for this battle, {Person1.name.title()}?\nIf so, then type 'one'.\nIf you do not want to use any of your power-ups, type 'no'.\n"
            power_ups_wanted += f"If you want to use more than one of your power-ups, enter 'more'.\n"
            power_up = input(power_ups_wanted).lower()
            power_ups_wanted = []
            if power_up == 'no':
                print('Applying no power-ups.')
            elif power_up == 'more':
                num_power_ups = int(input('Enter the number of power-ups you want to add.\n'))
                for _ in range(0,num_power_ups):
                    power_up_added = input(f"Enter a power-up.\n").title()
                    if power_up_added in Person1.power_ups.keys():
                        print('Adding the power-up to this battle.\n')
                        if Person1.power_ups[power_up_added] > 0:
                            Person1.power_levels += Person1.power_ups[power_up_added]
                            del Person1.power_ups[power_up_added]
                        else:
                            Person1.hasPowers = False
                            Person2.hasPowers = False
                    else:
                        print('You do not have this power-up.')
            elif power_up == 'one':
                power_up_added = (f"Enter your power-up.\n").lower()
                if power_up_added in Person1.power_ups.keys():
                        print('Adding the power-up to this battle.\n')
                        Person1.power_levels += Person1.power_ups[power_up_added]
                        del Person1.power_ups[power_up_added]
            else:
                print('Invalid Input. Selecting no power-ups for this battle.\n')
    get_power_ups(Person1)
    get_power_ups(Person2)
    Person1.get_power_levels()
    Person2.get_power_levels()
    if Person1.power_levels > Person2.power_levels:
        print(f"{Person1.name.title()} won.")
        Person1.coins += 15
    elif Person2.power_levels > Person1.power_levels:
        print(f"{Person2.name.title()} won.")
        Person2.coins += 15
    elif Person1.power_levels == Person2.power_levels:
        print(f"{Person1} and {Person2} are tied.")
    Person1.power_levels,Person2.power_levels,Person1.hasPowers,Person2.hasPowers = Person1_permanent_levels,Person2_permanent_levels,Person1_permanent_powers,Person2_permanent_powers

items = {'Vengestone':100,'Scrolls of Forbidden Spinjitsu':250}

def shop(Customer,dict=items):
    want_to_buy = f"Welcome to the shop!\nThis is where you can buy interesting power-ups that will boost your fighting ability.\n"
    want_to_buy += f"We currently have two items available for sale:\n1. Vengestone:\nThis material blocks all elemental powers "
    want_to_buy += f"in a battle, which is useful if you do not have elemental powers and are currently fighting against an elemental master"
    want_to_buy += f" or a ninja. This useful material is on sale for only {dict['Vengestone']} coins.\n\n2. The Scrolls of Forbidden"
    want_to_buy += f" Spinjitsu:\nThese scrolls increase your Spinjitsu ability drastically, and are very useful if you are a Spinjitsu"
    want_to_buy += f" Master or a Ninja. These powerful scrolls are on sale for a low price of only {dict['Scrolls of Forbidden Spinjitsu']}"
    want_to_buy += f" coins.\n\n Please choose one of these power-ups to buy.\nType your choice (1 for Vengestone and 2 for the scrolls) "
    want_to_buy += f"and press enter.\n\n\n"
    def get_input():
        choice = input(want_to_buy).lower()
        if choice == '1' and Customer.coins >= dict['Vengestone']:
            Customer.power_ups['Vengestone'] = -5
            Customer.coins -= dict['Vengestone']
            print('Thank you for your purchase.')
        elif choice == '1' and Customer.coins < dict['Vengestone']:
            print('Sorry, you do not have enough coins to buy this item.')
        elif choice == '2' and Customer.coins >= dict['Scrolls of Forbidden Spinjitsu']:
            Customer.power_ups['Scrolls Of Forbidden Spinjitsu'] = 5
            Customer.coins -= dict['Scrolls of Forbidden Spinjitsu']
            print('Thank you for your purchase.')
        elif choice == '2' and Customer.coins < dict['Scrolls of Forbidden Spinjitsu']:
            print('Sorry, you do not have enough coins to buy this item.')
        else:
            print('Invalid input. Enter 1 or 2.')
            get_input()
    get_input()