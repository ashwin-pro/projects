class Object:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = length*breadth


object_list = []
print("Enter a letter to quit\n")
while True:
    try:
        l = float(input("Enter the length of the item: "))
        b = float(input("Enter the breadth of the item: "))
        object_list.append(Object(l, b))
    except:
        break
# abcbaabcdedefgaabcdeeefddgdeceabcbaabcdedefgaabcdeeefddgdeccfgagfabcdefgagfabcdecdedcdefgafaegdfceacge
