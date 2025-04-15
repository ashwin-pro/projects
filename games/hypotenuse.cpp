#include <iostream>
#include <cmath>

int main()
{
    double a;
    double b;
    double c;
    std::std::cout << "Enter the length of the first side: ";
    std::std::cin >> a;
    std::std::cout << "Enter the length of the second side: ";
    std::std::cin >> b;
    c = sqrt(pow(a, 2) + pow(b, 2));
    std::std::cout << "The length of the hypotenuse of the right triangle is " << c << " units.";
    return 0;
}