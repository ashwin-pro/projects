import csv
batting_averages = open('C:\\Users\\Ashwin\\OneDrive\\Documents\\projects\\games\\batting-averages.csv')
minimum = 999999999999999999
maximum = -0.1
batting_averages = list(csv.reader(batting_averages))
for i in range(1,len(batting_averages)):
    name = batting_averages[i][0]
    average = float(batting_averages[i][1])
    if average > maximum:
        maximum = average
        maximum_name = name
    elif average < minimum:
        minimum = average
        minimum_name = name
    if average >= 0.4:
        score = 'extremely rare and difficult to achieve'
    elif average >= 0.3:
        score = 'excellent'
    elif average >= 0.2:
        score = 'average'
    elif average >= 0.1:
        score = 'inferior'
    else:
        score = 'apalling'
    print(f"{name.title()}'s batting average is {average}, which is an {score} average.")
print(minimum,maximum,maximum-minimum,'~',maximum_name,' ~',minimum_name)
class Human:
    def __init__(self,legs,iq):
        self.legs = 4
        self.iq = 100
ashwin = Human(None,130)
print(ashwin.legs,ashwin.iq)