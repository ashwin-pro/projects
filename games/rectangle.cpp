#include <iostream>

using namespace std;

int main()
{
    int cols;
    int rows;
    char symbol;
    std::cout << "Enter the number of rows the rectangle should have: ";
    std::cin >> rows;
    std::cout << "Enter the number of columns the rectangle should have: ";
    std::cin >> cols;
    std::cout << "Enter the symbol the rectangle should be made of: ";
    std::cin >> symbol;
    for (int i = 1; i <= cols; i++)
    {
        for (int j = 1; j <= rows; j++)
        {
            std::cout << symbol;
        }
        std::cout << "\n";
    }
    return 0;
}