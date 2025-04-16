#include <iostream>
#include <ctime>
int main()
{
    srand(time(0));
    int n = rand();
    std::cout << "The number is: " << n;
    while (true)
    {
        std::cout << '\n';
        if (n == 1)
        {
            std::cout << "End case reached";
            break;
        }
        if (n % 2 == 0)
        {
            n /= 2;
        }
        else
        {
            n = 3 * n + 1;
        }
        std::cout << n;
    }
    return 0;
}