
// Including the necessary header files.
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>
#include <chrono>
#include <thread>

std::string arrangements[8][3] = {{"A1", "B1", "C1"}, {"A1", "A2", "A3"}, {"A1", "B2", "C3"}, {"A2", "B2", "C2"}, {"A3", "B2", "C1"}, {"A3", "B3", "C3"}, {"B1", "B2", "B3"}, {"C1", "C2", "C3"}};
char board[3][3];
char row_letters[3] = {'A', 'B', 'C'};
int winner = 0;
std::string temp;
char player;
char computer;
char playerTwo;
char blank;
bool isSinglePlayer = true;
std::string playerOneName = "You";
std::string playerTwoName = "Computer";

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
    std::cout << "Would you like to play with another player instead? (y/n): ";
    std::string modeChoice;
    getline(std::cin, modeChoice);
    if (modeChoice[0] == 'y' || modeChoice[0] == 'Y')
    {
        std::cout << "Choosing two-player mode.\n";
        isSinglePlayer = false;
        std::cout << "What is the name of Player One?: ";
        getline(std::cin, temp);
        while (temp.empty())
        {
            std::cout << "Enter a NONEMPTY name: ";
            getline(std::cin, temp);
        }
        playerOneName = temp;
        std::cout << "What is the name of Player Two?: ";
        getline(std::cin, temp);
        while (temp.empty() || temp == playerOneName)
        {
            std::cout << "The name CANNOT be REPEATED or EMPTY: ";
            getline(std::cin, temp);
        }
        playerTwoName = temp;
    }
    else
    {
        std::cout << "Choosing single-player mode.\n";
    }
    std::cout << "This is the board, with coordinates referring to the squares:-\n\n";
    initialRenderBoard();
    std::cout << "\nEach turn, you will have the option to put a piece on any square which is not already taken. You must enter the coordinates of the    square.\n";
    std::cout << "Your goal is to make a straight line with three of your pieces before your opponent. If your opponent does it first, then they win.\n";
    std::cout << "The lines can be horizontal, vertical, or diagonal.\n";
    std::cout << "What character do you want to represent blank squares with?: ";
    getline(std::cin, temp);
    while (temp.empty())
    {
        std::cout << "Enter a NONEMPTY character: ";
        getline(std::cin, temp);
    }
    blank = temp[0];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = blank;
        }
    }
    std::cout << (isSinglePlayer ? "What character do you want to represent the squares occupied by your pieces with?: " : "What character do you want to represent the squares occupied by " + playerOneName + "'s pieces with?: ");
    getline(std::cin, temp);
    while (temp[0] == blank || temp.empty())
    {
        std::cout << "The character CANNOT be REPEATED or EMPTY, enter again: ";
        getline(std::cin, temp);
    }
    player = temp[0];

    std::cout << (!isSinglePlayer ? "What character do you want to represent the squares occupied by " + playerTwoName + " (Player Two)'s pieces with?: " : "What character do you want to represent the squares occupied by the computer with?: ");
    getline(std::cin, temp);
    while (temp[0] == blank || temp[0] == player || temp.empty())
    {
        std::cout << "The character CANNOT be REPEATED or EMPTY, enter again: ";
        getline(std::cin, temp);
    }
    if (isSinglePlayer)
    {
        computer = temp[0];
    }
    else
    {
        playerTwo = temp[0];
    }
    std::string raw_starting;
    int starting;
    if (!isSinglePlayer)
    {
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
    }

    std::cout << " Now, let the game begin!\n\n";
    std::cout << "\n**************************************************************************************\n\n";
    while (numEmptySquares(board) > 0)
    {
        winner = checkSequenceAndDetermineWinner(board);
        std::string move;
        std::cout << "This is the current board:-\n\n";
        drawBoard(board);

        if (isSinglePlayer)
        {
            do
            {
                std::cout << "\nEnter the VALID coordinates of the EMPTY square you wish to place your piece on (ex: A1, B3, or C2): ";
                std::cin >> move;
            } while (!positionIsFree(board, move) || (move.length() != 2 || move[0] < 'A' || move[0] > 'C' || move[1] < '1' || move[1] > '3'));
            placePiece(board, move, true);
        }
        else
        {
            do
            {
                std::cout << "\n"
                          << (starting == 1 ? playerOneName : playerTwoName) << ", enter the VALID coordinates of the EMPTY square you wish to place your piece on (ex: A1, B3, or C2): ";
                std::cin >> move;
            } while (!positionIsFree(board, move) || (move.length() != 2 || move[0] < 'A' || move[0] > 'C' || move[1] < '1' || move[1] > '3'));
            placePiece(board, move, starting == 1);
        }

        if (numEmptySquares(board) == 0)
        {
            break;
        }
        winner = checkSequenceAndDetermineWinner(board);

        std::cout << "\n------------------------------\n\n";
        drawBoard(board);
        std::cout << "\n\n------------------------------\n";

        if (isSinglePlayer)
        {
            std::string computerMove = botChoice(board);
            std::cout << "\n\n\n\nThe computer places a piece on square " << computerMove << ".\n";
            placePiece(board, computerMove, false);
        }
        else
        {
            do
            {
                std::cout << "\n"
                          << (starting == 2 ? playerOneName : playerTwoName) << ", enter the VALID coordinates of the EMPTY square you wish to place your piece on (ex: A1, B3, or C2): ";
                std::cin >> move;
            } while (!positionIsFree(board, move) || (move.length() != 2 || move[0] < 'A' || move[0] > 'C' || move[1] < '1' || move[1] > '3'));
            placePiece(board, move, starting == 2);
        }
        winner = checkSequenceAndDetermineWinner(board);
        std::cout << "\n**************************************************************************************\n\n";
    }
    drawBoard(board);
    std::cout << "\n\n\nThere is a tie between " << playerOneName << " and " << playerTwoName << ", as all the squares have been taken up.\n\n";
    return 0;
}

void initialRenderBoard()
{
    for (int i = 0; i < 3; i++)
    {
        char current_row = row_letters[i];
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
            if (board[i][j] == blank)
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
    if (x >= 0 && x < 3 && y >= 0 && y < 3 && board[x][y] == blank)
    {
        board[x][y] = isPlayerPiece ? player : (isSinglePlayer ? computer : playerTwo);
    }
}

int numPieces(char board[3][3], bool isPlayerPieces)
{
    int numSquares = 0;
    char symbol = isPlayerPieces ? player : (isSinglePlayer ? computer : playerTwo);
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == symbol)
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
    for (int sequenceNum = 0; sequenceNum < 8 && victor == 0; sequenceNum++)
    {
        for (int index = 1; index < 3 && victor == 0; index++)
        {
            char character = (index == 1) ? player : (isSinglePlayer ? computer : playerTwo);
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
                    for (int square = 0; square < 3; square++)
                    {
                        sequence[square] = arrangements[sequenceNum][square];
                    }
                }
            }
        }
    }
    if (victor == 0)
        return 0;
    drawBoard(board);
    std::cout << "\n\n\n";
    switch (victor)
    {
        {
        case 1:
            if (isSinglePlayer)
            {
                std::cout << "Congratulations! You win, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << "!";
            }
            else
            {
                std::cout << "Congratulations, " << playerOneName << "! You win, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << "!";
            }
        }
        break;
    case 2:
        if (isSinglePlayer)
        {
            std::cout << "The computer wins, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << ". Better luck next time!";
        }
        else
        {
            std::cout << "Congratulations, " << playerTwoName << "! You win, by the sequence " << sequence[0] << '-' << sequence[1] << '-' << sequence[2] << "!";
        }
        break;
    }
    std::cout << "\n\n\n\n";
    exit(0);
}

bool positionIsFree(char board[3][3], std::string loc)
{
    int x = loc[0] - 'A';
    int y = loc[1] - '1';
    return board[x][y] == blank;
}

std::string botChoice(char board[3][3])
{
    std::cout << "\n\n Bot's turn to move\n";
    std::vector<std::string> squaresDone;
    std::vector<std::string> optionsBlock;
    std::vector<std::string> optionRand;
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

        if (count(valuesSoFar.begin(), valuesSoFar.end(), blank) >= 1)
        {
            std::string value = coordinatesSoFar.at(index(valuesSoFar, blank));

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
            else
            {
                std::cout << "😐 Doesn't help me win or block. Saving " << value << " as a backup.\n";
                optionRand.push_back(value);
                std::this_thread::sleep_for(std::chrono::milliseconds(600));
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
    srand(time(0));
    int randomIndex = rand() % optionRand.size();
    std::string chosen = optionRand[randomIndex];
    std::cout << "\n🤷‍♂️  Nothing special to do. I’ll go with one of my last resorts.";
    std::cout << " I have " << optionRand.size() << " options. I'll go with " << chosen << ".";
    std::this_thread::sleep_for(std::chrono::milliseconds(800));
    return optionRand[randomIndex];
}

int index(std::vector<char> vec, char target)
{
    auto it = find(vec.begin(), vec.end(), target);
    return (it != vec.end()) ? distance(vec.begin(), it) : -1;
}
