def reverse(func):
    def wrapper():
        return tuple(func())[::-1]
    for _ in wrapper():
        print(_,end="")
if __name__ == "__main__":
    @reverse
    def lambda_():
        yield 1,2,3,4,5,6,7,8,9,10
        print("12345678910 reversed is:")