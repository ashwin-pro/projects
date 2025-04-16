#include <string>
#include <iostream>

void func(std::string array[]);

int main()
{
    int i = 0;
    std::string ARRAY[4] = {"a", "b", "c", "d"};
    func(ARRAY);
    // std::cout << "The variable is now: " << i;
    for (std::string element : ARRAY)
    {
        std::cout << element << '\n';
    }
    return 0;
}

void func(std::string array[])
{
    array[0] = "abcde";
}