#include <iostream>
#include <ctime>

int main()
{
    int range;
    std::std::cout << "What should the maximum possible value for the number be (Starting from 1)?: ";
    std::std::cin >> range;
    srand(time(0));
    int num = rand() % range + 1;
    int guess = 0;
    int tries = 0;
    std::std::cout << "Your goal is to guess a random number between 1 and " << range << ".\n\n";
    while (true)
    {
        tries++;
        std::std::cout << "What is your guess?: ";
        std::std::cin >> guess;
        if (guess == num)
        {
            std::std::cout << "Correct guess! The number is " << num << "!\n";
            std::std::cout << "You got it in " << tries << " tr" << ((tries == 1) ? "y" : "ies") << "!";
            break;
        }
        else if (guess > num)
        {
            std::std::cout << "Too high! Guess lower!\n";
        }
        else
        {
            std::std::cout << "Too low! Guess higher!\n";
        }
    }
    return 0;
}