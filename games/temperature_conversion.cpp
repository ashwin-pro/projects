#include <iostream>
#include <cctype>
using namespace std;

int main()
{
    char unit;
    double temperature;
    std::cout << "Which unit would you like to convert to? (C for Celsius, F for Fahrenheit): ";
    std::cin >> unit;
    unit = tolower(unit);
    std::cout << "What is the temperature (in degrees " << ((unit == 'f') ? "Celsius" : "Fahrenheit") << ")?: ";
    std::cin >> temperature;
    switch (unit)
    {
    case 'c':
        std::cout << "The temperature is " << (5 * (temperature - 32) / 9) << " degrees Celsius.";
        break;
    case 'f':
        std::cout << "The temperature is " << (9 * temperature * 0.2 + 32) << " degrees Fahrenheit.";
        break;
    default:
        std::cout << "Invalid unit.";
        break;
    }
    return 0;
}