from random import choice as c
class Npc:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        return f"Hello, I am {self.name}."
power_list = ['fire','water','green','energy','ice','earth','fusion','tech',]
class Fighter:
    def __init__(self,name="Unknown",hasPowers=False,strengths=[],weaknesses=[],power_level="Moderate",knowsSpinjitsu=False,allies = [],enemies = [],coins = 50,power_ups = {},position = {'x':0,'y':0,'z':0},quest=False,weapon=False):
        self.name = name
        self.hasPowers = hasPowers
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.power_level = power_level
        self.knowsSpinjitsu = knowsSpinjitsu
        self.allies = allies
        self.enemies = enemies
        self.coins = coins
        self.power_ups = power_ups
        self.position = position
        self.quest = quest
        self.weapon = weapon

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

    def max_power_levels(self):
        self.max_power_levels = self.get_power_levels()
        for power_up in self.power_ups.keys():
            if self.power_ups[power_up] > 0:
                self.max_power_levels += self.power_ups[power_up]
        return self.max_power_levels

class Elemental_Master(Fighter):
    def __init__(self,name="Unknown",strengths=[],weaknesses=[],power_level="Moderate",knowsSpinjitsu=False,allies=[],enemies=[],elemental_power=c(power_list),coins = 50,power_ups = {},position = {'x':0,'y':0,'z':0},quest = False,weapon = False):
        self.name = name
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
        self.position = position
        self.quest = quest
        self.weapon = weapon

class Spinjitsu_Master(Fighter):
    def __init__(self,name="Unknown",strengths=[],weaknesses=[],power_level="Moderate",allies=[],enemies=[],coins = 50,power_ups = {},position = {'x':0,'y':0,'z':0},quest = False,weapon = False):
        self.name = name
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.power_level = power_level
        self.allies = allies
        self.enemies = enemies
        self.knowsSpinjitsu = True
        self.hasPowers = False
        self.coins = coins
        self.power_ups = power_ups
        self.position = position
        self.quest = quest
        self.weapon = weapon
    def get_power_levels(self):
        return super().get_power_levels()

class Ninja(Fighter):
    def __init__(self,name="Unknown",strengths=[],weaknesses=[],power_level="Moderate",allies=[],enemies=[],elemental_power=c(power_list),coins = 50,power_ups = {},position = {'x':0,'y':0,'z':0},quest = False,weapon = False):
        self.name = name
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
        self.position = position
        self.quest = quest
        self.weapon = weapon
    def get_power_levels(self):
        return super().get_power_levels()
    
def fight(Person1,Person2):
    #First check if both players are in the same position
    #Only then start the fight
        if Person1.position == Person2.position:
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
        else:
            print('Players are too far away and cannot fight.')


power_ups = {'Vengestone':100,'Scrolls of Forbidden Spinjitsu':250}

def power_up_shop(Customer,dict=power_ups):
    global num_times
    num_times = 0
    want_to_buy = f"Welcome to the shop!\nThis is where you can buy interesting power-ups that will boost your fighting ability.\n"
    want_to_buy += f"We currently have two items available for sale:\n1. Vengestone:\nThis material blocks all elemental powers "
    want_to_buy += f"in a battle, which is useful if you do not have elemental powers and are currently fighting against an elemental master"
    want_to_buy += f" or a ninja. This useful material is on sale for only {dict['Vengestone']} coins.\n\n2. The Scrolls of Forbidden"
    want_to_buy += f" Spinjitsu:\nThese scrolls increase your Spinjitsu ability drastically, and are very useful if you are a Spinjitsu"
    want_to_buy += f" Master or a Ninja. These powerful scrolls are on sale for a low price of only {dict['Scrolls of Forbidden Spinjitsu']}"
    want_to_buy += f" coins.\n\n Please choose one of these power-ups to buy.\nType your choice (1 for Vengestone and 2 for the scrolls) "
    want_to_buy += f"and press enter.\n\n\n"
    def get_input():
        global num_times
        num_times += 1
        if num_times == 1:
            choice = input(want_to_buy).lower()
        else:
            choice = input('Invalid input. Enter 1 or 2.\n').lower()
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
            get_input()
    get_input()

weapons = {'sword':25,'nunchucks':25,'hammer':25,'shurikens':25}

def weapon_shop(Customer,dict=weapons):
    want_to_buy = f"There are four weapons available:\n\n1. Sword - A sword is a melee weapon that does point damage and bleeding damege.\n"
    want_to_buy += f"2. Nunchucks - Nunchucks are short to medium range weapons. They can be thrown to do ranged damage. They do blunt damage.\n"
    want_to_buy += f"3. Hammer - A hammer is a melee weapon that does blunt and AOE damage. It has a knockback effect that pushes your opponent away.\n"
    want_to_buy += f"4. Shurikens - Shurikens are medium to long range weapons. They can be thrown to deal point damage and bleeding damage.\n"
    want_to_buy += f"Each of these items cost 25 coins. Please enter your chosen weapon.\n\nYou currently have {Customer.coins} coins.\n\n\n"
    global chosen
    chosen = input(want_to_buy).strip().lower()
    def get_input():        
        def get_weapon():
            global chosen
            if chosen in dict.keys():
                if Customer.coins >= dict[chosen]:
                    Customer.weapon = chosen
                    Customer.coins -= dict[chosen]
                    print(f"You now have {Customer.coins} coins.\n\n\n")
                else:
                    chosen = input('Sorry, you do not have enough coins to buy this item. Please choose another item. The choices are Sword, Hammer, Nunchucks or Shurikens. Each of these items cost 25 coins\n')
                    get_weapon()
            else:
                chosen = input('Sorry, this weapon is not available. Please choose another. The choices are Sword, Hammer, Nunchucks or Shurikens. Each of these items cost 25 coins\n')
                get_weapon()
        get_weapon()
    get_input()