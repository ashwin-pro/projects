#include <iostream>

using namespace std;

int searchArray(int array[], int target, int size);

int main()
{
    int array[] = {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    };
    int size = sizeof(array) / sizeof(int);
    int target;
    std::cout << "What element do you want to search for?: ";
    std::cin >> target;
    int result = searchArray(array, target, size);
    if (result == -1)
    {
        std::cout << "The element is not in the array.";
    }
    else
    {
        std::cout << "The element is in the array at index " << result << ", or position " << result + 1 << ".";
    }
    return 0;
}

int searchArray(int array[], int target, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (array[i] == target)
        {
            return i;
        }
    }
    return -1;
}