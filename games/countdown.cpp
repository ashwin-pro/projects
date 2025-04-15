#include <iostream>
using namespace std;

int main()
{
    for (int i = 10; i > 0; i--)
    {
        std::cout << "T-minus " << i << " second" << ((i == 1) ? "" : "s") << "\n";
    }
    std::cout << "TAKEOFF!";
    return 0;
}