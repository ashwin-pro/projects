
#include <iostream>
#include <ctime>
#include <std::string>
#include <std::vector>
#include <algorithm>
#include <chrono>
#include <thread>

using namespace std;

std::string arrangements[8][3] = {{"A1", "B1", "C1"}, {"A1", "A2", "A3"}, {"A1", "B2", "C3"}, {"A2", "B2", "C2"}, {"A3", "B2", "C1"}, {"A3", "B3", "C3"}, {"B1", "B2", "B3"}, {"C1", "C2", "C3"}};
char board[3][3];
char row_letters[3] = {'A', 'B', 'C'};
int winner = 0;
std::string temp;
char player;
char computer;
char blank;

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
    std::cout << "This is a game of tic-tac-toe, played between you and a computer.\n";
    std::cout << "This is the board, with coordinates referring to the squares:-\n\n";
    initialRenderBoard();
    std::cout << "\nEach turn, you will have the option to put a piece on any square which is not already taken. You must enter the coordinates of the    square.\n";
    std::cout << "Your goal is to make a straight line with three of your pieces before your opponent. If your opponent does it first, then they win.\n";
    std::cout << "The lines can be horizontal, vertical, or diagonal.\n";
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
    std::cout << "What character do you want to represent the squares occupied by your pieces with?: ";
    getline(std::cin, ::temp);
    while (::temp[0] == ::blank || ::temp.empty())
    {
        std::cout << "The character CANNOT be REPEATED or EMPTY, enter again: ";
        getline(std::cin, ::temp);
    }
    ::player = ::temp[0];
    std::cout << "What character do you want to represent the squares occupied by the computer with?: ";
    getline(std::cin, ::temp);
    while (::temp[0] == ::blank || ::temp[0] == ::player || ::temp.empty())
    {
        std::cout << "The character CANNOT be REPEATED or EMPTY, enter again: ";
        getline(std::cin, ::temp);
    }
    ::computer = ::temp[0];

    std::cout
        << "Now, let the game begin!\n\n";
    std::cout << "\n**************************************************************************************\n\n";
    while (numEmptySquares(::board) > 0)
    {
        ::winner = checkSequenceAndDetermineWinner(::board);
        if (winner != 0)
        {
            break;
        }
        std::string playerChoice;
        std::cout << "This is the current board:-\n\n";
        drawBoard(::board);
        do
        {
            std::cout << "\nEnter the VALID coordinates of the EMPTY square you wish to place your piece on (ex: A1, B3, or C2): ";
            std::cin >> playerChoice;
        } while (!positionIsFree(::board, playerChoice) && (playerChoice.length() != 2 || playerChoice[0] < 'A' || playerChoice[0] > 'C' || playerChoice[1] < '1' || playerChoice[1] > '3'));
        placePiece(::board, playerChoice, true);
        if (numEmptySquares(::board) == 0)
        {
            break;
        }
        checkSequenceAndDetermineWinner(board);
        std::cout << "\n------------------------------\n\n";
        drawBoard(::board);
        std::cout << "\n\n------------------------------\n";
        std::string computerChoice = botChoice(::board);
        std::cout << "\n\n\n\nThe computer places a piece on square " << computerChoice << ".\n";
        placePiece(board, computerChoice, false);
        winner = checkSequenceAndDetermineWinner(::board);
        if (winner != 0)
        {
            break;
        }
        std::cout << "\n**************************************************************************************\n\n";
    }
    drawBoard(::board);
    std::cout << "\n\n\nThere is a tie between you and the computer, as all the squares have been taken up. Better luck next time!\n\n";
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
void placePiece(char board[3][3], std::string loc, bool isPlayerPiece)
{
    int x = loc[0] - 'A';
    int y = loc[1] - '1';
    if (x >= 0 && x < 3 && y >= 0 && y < 3 && board[x][y] == ::blank)
    {
        ::board[x][y] = (isPlayerPiece == true) ? player : computer;
    }
}
int numPieces(char board[3][3], bool isPlayerPieces)
{
    int numSquares = 0;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == ((isPlayerPieces == true) ? player : computer))
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
                    char character = (index == 1) ? player : computer;
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
                            victor = (character == player ? 1 : 2);
                            for (int square; square < 3; square++)
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
        std::cout << "Congratulations! You win, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << "!";
        break;
    case 2:
        std::cout << "The computer wins, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << ". Better luck next time!";
        break;
    }
    std::cout << "\n\n";
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
std::string botChoice(char board[3][3])
{
    std::cout << "\n\n Bot's turn to move\n";
    std::vector<std::string> squaresDone;
    std::vector<std::string> optionsBlock;
    std::string optionRand = "";
    std::vector<char> valuesSoFar;
    std::vector<std::string> coordinatesSoFar;

    std::cout << "\n🤖 Thinking...\n";

    for (int sequenceNum = 0; sequenceNum < 8; sequenceNum++)
    {
        valuesSoFar.clear();
        coordinatesSoFar.clear();

        for (int squareNum = 0; squareNum < 3; squareNum++)
        {
            int i = arrangements[sequenceNum][squareNum][0] - 'A';
            int j = arrangements[sequenceNum][squareNum][1] - '1';
            valuesSoFar.push_back(board[i][j]);
            coordinatesSoFar.push_back(arrangements[sequenceNum][squareNum]);
        }

        if (count(valuesSoFar.begin(), valuesSoFar.end(), ::blank) >= 1)
        {
            std::string value = coordinatesSoFar.at(index(valuesSoFar, ::blank));

            std::cout << "\n💭 I'm considering square " << value << ", in sequence " << arrangements[sequenceNum][0] << '-' << arrangements[sequenceNum][1] << '-' << arrangements[sequenceNum][2] << "...\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(1200));

            if (count(valuesSoFar.begin(), valuesSoFar.end(), computer) >= 2)
            {
                std::cout << "😏 If I place it on " << value << ", I win!\n";
                std::this_thread::sleep_for(std::chrono::milliseconds(1000));
                std::cout << "✅ I'm going for it!\n";
                std::this_thread::sleep_for(std::chrono::milliseconds(1000));
                return value;
            }
            else if (count(valuesSoFar.begin(), valuesSoFar.end(), player) >= 2)
            {
                std::cout << "🛡️ That square could block the player from winning...\n";
                std::this_thread::sleep_for(std::chrono::milliseconds(1000));
                std::cout << "📝 I'll keep " << value << " in mind just in case.\n";
                optionsBlock.push_back(value);
                std::this_thread::sleep_for(std::chrono::milliseconds(600));
            }
            else if (optionRand.empty())
            {
                std::cout << "😐 Doesn't help me win or block. Saving " << value << " as a backup.\n";
                optionRand = value;
                std::this_thread::sleep_for(std::chrono::milliseconds(600));
            }
            else
            {
                std::cout << "❌ " << value << " isn't useful, and I already have a backup.\n";
                std::this_thread::sleep_for(std::chrono::milliseconds(300));
            }
        }
        std::cout << "\n------------------------------\n";
    }

    if (!optionsBlock.empty())
    {
        std::cout << "\n🧱 No win possible, time to block the player...\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));

        if (optionsBlock.size() == 1)
        {
            std::cout << "Only one block option: " << optionsBlock.at(0) << ".\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(700));
            return optionsBlock.at(0);
        }
        else
        {
            srand(time(0));
            int randIndex = rand() % optionsBlock.size();
            std::cout << "I’ve got " << optionsBlock.size() << " ways to block. Picking " << optionsBlock[randIndex] << ".\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(900));
            return optionsBlock[randIndex];
        }
    }

    std::cout << "\n🤷‍♂️ Nothing special to do. I’ll go with my last resort: " << optionRand << ".\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(800));
    return optionRand;
}

int index(std::vector<char> vec, char target)
{
    auto it = find(vec.begin(), vec.end(), target);

    if (it != vec.end())
    {
        return distance(vec.begin(), it);
    }
    else
    {
        return -1;
    }
}