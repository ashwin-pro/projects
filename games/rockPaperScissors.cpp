#include <iostream>
#include <ctime>

bool isInvalid(int playerChoice)
{
    switch (playerChoice)
    {
    case 1:
        return false;
        break;
    case 2:
        return false;
        break;
    case 3:
        return false;
        break;
    default:
        return true;
        break;
    }
}
int result(int choice1, int choice2)
{
    if (choice1 == choice2)
    {
        return 0;
    }
    if (choice1 == 1)
    {
        return (choice2 == 2 ? 2 : 1);
    }
    if (choice1 == 2)
    {
        return (choice2 == 1 ? 1 : 2);
    }
    return (choice2 == 1 ? 2 : 1);
}

int main()
{
    srand(time(0));
    int playerChoice;
    int botChoice = (rand() % 3) + 1;
    std::std::string userChoice;
    do
    {
        std::std::cout << "\nChoose between rock (1), paper (2), and scissors (3): ";
        std::std::cin >> playerChoice;
    } while (isInvalid(playerChoice));
    std::std::string compChoice;
    switch (botChoice)
    {
    case 1:
        compChoice = "Rock";
        break;
    case 2:
        compChoice = "Paper";
        break;
    case 3:
        compChoice = "Scissors";
        break;
    }
    switch (playerChoice)
    {
    case 1:
        userChoice = "Rock";
        break;
    case 2:
        userChoice = "Paper";
        break;
    case 3:
        userChoice = "Scissors";
        break;
    }
    std::std::cout << "The computer chose " << compChoice << ".\n";
    int outcome = result(playerChoice, botChoice);
    switch (outcome)
    {
    case 0:
        std::std::cout << "As " << userChoice << " and " << userChoice << " cancel out, ";
        std::std::cout << "the result is a tie.";
        break;
    case 1:
        std::std::cout << "As " << userChoice << " beats " << compChoice;
        std::std::cout << ", you win!";
        break;
    case 2:
        std::std::cout << "As " << compChoice << " beats " << userChoice;
        std::std::cout << ", you lose.";
        break;
    }
    return 0;
}