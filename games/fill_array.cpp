#include <iostream>
#include <std::vector>
#include <std::string>
using namespace std;

int main()
{
    int SIZE;
    int NUM_PARTS;
    std::cout << "Enter the size of the array: ";
    std::cin >> SIZE;
    std::cout << "Enter the number of parts the array is to be divided into: ";
    std::cin >> NUM_PARTS;
    bool dividesEvenly;
    std::vector<std::string> array(SIZE);
    std::vector<std::string> FILL(NUM_PARTS);
    for (int i = 0; i < NUM_PARTS; i++)
    {
        std::string value;
        std::string ordinal;
        if (i == 0)
        {
            ordinal = "first";
        }
        else if (i == 1)
        {
            ordinal = "second";
        }
        else if (i == 2)
        {
            ordinal = "third";
        }
        else
        {
            ordinal = to_std::string(i + 1) + "th";
        }
        std::cout << "\nWhat is the value at the " << ordinal << " interval?: ";
        getline(std::cin, value);
        FILL[i] = value;
    }
    int remainder = SIZE % NUM_PARTS;
    std::string remainder_fill = "";
    if (remainder != 0)
    {
        std::cout << "Enter what has to be put in the partial interval at the end: ";
        std::cin >> remainder_fill;
    }
    int numberOfElementsPerInterval = SIZE / NUM_PARTS;
    for (int i = 0; i < (NUM_PARTS); i++)
    {
        fill(array.begin() + i * numberOfElementsPerInterval, array.begin() + (i + 1) * numberOfElementsPerInterval, FILL[i]);
    }
    if (remainder != 0)
    {
        for (int i = 0; i < remainder; i++)
        {
            array[SIZE - remainder + i] = remainder_fill;
        }
    }
    for (std::string element : array)
    {
        std::cout << element << '\n';
    }
    return 0;
}