#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    char op;
    double num1;
    double num2;
    std::cout << "Enter the operation (+, -, *, /, or ^): ";
    std::cin >> op;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    char eq = '=';
    switch (op)
    {
    case '+':
        std::cout << num1 << " " << op << " " << num2 << " " << eq << " " << (num1 + num2);
        break;
    case '-':
        std::cout << num1 << " " << op << " " << num2 << " " << eq << " " << (num1 - num2);
        break;
    case '*':
        std::cout << num1 << " " << op << " " << num2 << " " << eq << " " << (num1 * num2);
        break;
    case '/':
        std::cout << num1 << " " << op << " " << num2 << " " << eq << " " << (num1 / num2);
        break;
    case '^':
        std::cout << num1 << " " << op << " " << num2 << " " << eq << " " << pow(num1, num2);
        break;
    default:
        std::cout << "Invalid operation.";
        break;
    }
    return 0;
}