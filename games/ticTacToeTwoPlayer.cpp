
#include <iostream>
#include <ctime>
#include <std::string>
#include <std::vector>
#include <algorithm>

using namespace std;

std::string arrangements[8][3] = {{"A1", "B1", "C1"}, {"A1", "A2", "A3"}, {"A1", "B2", "C3"}, {"A2", "B2", "C2"}, {"A3", "B2", "C1"}, {"A3", "B3", "C3"}, {"B1", "B2", "B3"}, {"C1", "C2", "C3"}};
char board[3][3];
char row_letters[3] = {'A', 'B', 'C'};
int winner = 0;
std::string temp;
char playerOne;
char playerTwo;
char blank;
std::string playerOneName;
std::string playerTwoName;

void initialRenderBoard();
int numPieces(char board[3][3], bool isPlayerPieces);
int numEmptySquares(char board[3][3]);
void drawBoard(char board[3][3]);
void placePiece(char board[3][3], std::string loc, bool isPlayerPiece);
int checkSequenceAndDetermineWinner(char board[3][3]);
std::string botChoice(char board[3][3]);
bool positionIsFree(char board[3][3], std::string loc);
int index(std::vector<char> vec, char target);

int main()
{
    std::cout << "This is a game of tic-tac-toe, played between two players.\n";
    std::cout << "This is the board, with coordinates referring to the squares:-\n\n";
    initialRenderBoard();
    std::cout << "\nEach turn, the players will have the option to put pieces on any squares which are not already taken. They must enter the coordinates of their chosen squares.\n";
    std::cout << "Your goal is to make a straight line with three of your pieces before your opponent. If your opponent does it first, then they win.\n";
    std::cout << "The lines can be horizontal, vertical, or diagonal.\n";
    std::cout << "What is the name of Player One?: ";
    getline(std::cin, ::temp);
    while (::temp.empty())
    {
        std::cout << "Enter a NONEMPTY name: ";
        getline(std::cin, ::temp);
    }
    ::playerOneName = ::temp;
    std::cout << "What is the name of Player Two?: ";
    getline(std::cin, ::temp);
    while (::temp.empty() || ::temp == ::playerOneName)
    {
        std::cout << "The name CANNOT be REPEATED or EMPTY: ";
        getline(std::cin, ::temp);
    }
    ::playerTwoName = ::temp;
    std::cout << "What character do you want to represent blank squares with?: ";
    getline(std::cin, ::temp);
    while (::temp.empty())
    {
        std::cout << "Enter a NONEMPTY character: ";
        getline(std::cin, ::temp);
    }
    ::blank = ::temp[0];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            ::board[i][j] = ::blank;
        }
    }
    std::cout << "What character do you want to represent the squares occupied by " << playerOneName << " (Player One)'s pieces with?: ";
    getline(std::cin, ::temp);
    while (::temp[0] == ::blank || ::temp.empty())
    {
        std::cout << "The character CANNOT be REPEATED or EMPTY, enter again: ";
        getline(std::cin, ::temp);
    }
    ::playerOne = ::temp[0];
    std::cout << "What character do you want to represent the squares occupied by " << playerTwoName << " (Player Two)'s pieces with?: ";
    getline(std::cin, ::temp);
    while (::temp[0] == ::blank || ::temp[0] == ::playerOne || ::temp.empty())
    {
        std::cout << "The character CANNOT be REPEATED or EMPTY, enter again: ";
        getline(std::cin, ::temp);
    }
    ::playerTwo = ::temp[0];

    std::string raw_starting;
    int starting;
    std::cout << "Does " << ::playerOneName << " (Player One) or " << ::playerTwoName << " (Player Two) want to start?\n";
    std::cout << "Enter 1 if " << ::playerOneName << " is to start, and 2 if " << ::playerTwoName << " is starting. Enter anything else for the picking to be random: ";
    getline(std::cin, raw_starting);
    std::cout << '\n';
    if (raw_starting == "1")
    {
        starting = 1;
    }
    else if (raw_starting == "2")
    {
        starting = 2;
    }
    else
    {
        srand(time(0));
        starting = rand() % 2 + 1;
    }
    std::cout << (starting == 1 ? playerOneName : playerTwoName) << " is starting.";
    std::cout
        << "\nNow, let the game begin!\n\n";
    std::cout << "\n**************************************************************************************\n\n";
    while (numEmptySquares(::board) > 0)
    {
        ::winner = checkSequenceAndDetermineWinner(::board);
        if (::winner != 0)
        {
            break;
        }
        std::string startingPlayerChoice;
        std::cout << "This is the current board:-\n\n";
        drawBoard(::board);
        do
        {
            std::cout << '\n'
                      << (starting == 1 ? playerOneName : playerTwoName) << ", enter the VALID coordinates of the EMPTY square you wish to place your piece on (ex: A1, B3, or C2): ";
            std::cin >> startingPlayerChoice;
        } while (!positionIsFree(::board, startingPlayerChoice) || (startingPlayerChoice.length() != 2 || startingPlayerChoice[0] < 'A' || startingPlayerChoice[0] > 'C' || startingPlayerChoice[1] < '1' || startingPlayerChoice[1] > '3'));
        placePiece(::board, startingPlayerChoice, (starting == 1));
        if (numEmptySquares(::board) == 0)
        {
            break;
        }
        checkSequenceAndDetermineWinner(board);
        std::cout << "\n------------------------------\n\n";
        drawBoard(::board);
        std::cout << "\n\n------------------------------\n";
        std::string endingPlayerChoice;
        std::cout << '\n'
                  << (starting == 1 ? playerTwoName : playerOneName) << ", enter the VALID coordinates of the EMPTY square you wish to place your piece on (ex: A1, B3, or C2): ";
        std::cin >> endingPlayerChoice;
        placePiece(board, endingPlayerChoice, (starting == 2));
        winner = checkSequenceAndDetermineWinner(::board);
        if (winner != 0)
        {
            break;
        }
        std::cout << "\n**************************************************************************************\n\n";
    }
    drawBoard(::board);
    std::cout << "\n\n\nThere is a tie between " << playerOneName << " and " << playerTwoName << ", as all the squares have been taken up.\n\n";
    return 0;
}

void initialRenderBoard()
{
    for (int i = 0; i < 3; i++)
    {
        char current_row = ::row_letters[i];
        std::cout << "  " << current_row << 1 << "  " << '|' << "  " << current_row << 2 << "  " << '|' << "  " << current_row << 3 << "\n  ____|______|_____\n";
    }
}
void drawBoard(char board[3][3])
{
    std::cout << "\n     1     2     3";
    for (int i = 0; i < 3; i++)
    {
        std::cout << "\n   -----------------";
        std::cout << "\n " << row_letters[i] << " ";
        for (int j = 0; j < 3; j++)
        {
            std::cout << "|  " << board[i][j] << "  ";
        }
        std::cout << "|";
    }
    std::cout << "\n   -----------------\n";
}

int numEmptySquares(char board[3][3])
{
    int numEmpty = 0;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == ::blank)
            {
                numEmpty++;
            }
        }
    }
    return numEmpty;
}
void placePiece(char board[3][3], std::string loc, bool isPlayerOnePiece)
{
    int x = loc[0] - 'A';
    int y = loc[1] - '1';
    if (x >= 0 && x < 3 && y >= 0 && y < 3 && board[x][y] == ::blank)
    {
        ::board[x][y] = (isPlayerOnePiece == true) ? playerOne : playerTwo;
    }
}
int numPieces(char board[3][3], bool isPlayerPieces)
{
    int numSquares = 0;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == ((isPlayerPieces == true) ? playerOne : playerTwo))
            {
                numSquares++;
            }
        }
    }
    return numSquares;
}
int checkSequenceAndDetermineWinner(char board[3][3])
{
    int victor = 0;
    std::string sequence[3];
    if (numPieces(board, true) < 3 && numPieces(board, false) < 3)
    {
        return 0;
    }
    for (int sequenceNum = 0; sequenceNum < 8; sequenceNum++)
    {
        if (victor == 0)
        {
            for (int index = 1; index < 3; index++)
            {
                if (victor == 0)
                {
                    char character = (index == 1) ? playerOne : playerTwo;
                    for (int squareNum = 0; squareNum < 3; squareNum++)
                    {
                        int i = arrangements[sequenceNum][squareNum][0] - 'A';
                        int j = arrangements[sequenceNum][squareNum][1] - '1';
                        if (board[i][j] != character)
                        {
                            break;
                        }
                        if (squareNum == 2)
                        {
                            victor = (character == playerOne ? 1 : 2);
                            for (int square = 0; square < 3; square++)
                            {
                                sequence[square] = arrangements[sequenceNum][square];
                            }
                            break;
                        }
                    }
                }
                else
                {
                    break;
                }
            }
        }
        else
        {
            break;
        }
    }
    if (victor == 0)
    {
        return 0;
    }
    std::cout << "\n\n\n";
    drawBoard(board);
    std::cout << "\n\n\n";
    switch (victor)
    {
    case 1:
        std::cout << "Congratulations, " << playerOneName << "! You win, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << "!";
        break;
    case 2:
        std::cout << "Congratulations, " << playerTwoName << "! You win, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << "!";
        break;
    }
    std::cout << "\n\n\n\n";
    exit(0);
}
bool positionIsFree(char board[3][3], std::string loc)
{
    int x = loc[0] - 'A';
    int y = loc[1] - '1';
    if (board[x][y] == ::blank)
    {
        return true;
    }
    return false;
}