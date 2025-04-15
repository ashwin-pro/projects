#include <std::string>
#include <iostream>

void func(int i);

int main()
{
    int i = 0;
    const std::std::string ARRAY[4] = {"a", "b", "c", "d"};
    func(i);
    std::std::cout << "The variable is now: " << i;
    return 0;
}

void func(int i)
{
    i++;
}