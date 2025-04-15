#include <iostream>
using namespace std;
double balance = 1000;
void showBalance()
{
    std::cout << "Your current balance is " << balance << ".\n";
}
void depositCash(double amount)
{
    std::cout << "Depositing " << amount << " into your account.\n";
    ::balance += amount;
}
void withdrawCash(double amount)
{
    std::cout << "Withdrawing " << amount << " from your account.\n";
    ::balance -= amount;
}
int main()
{
    showBalance();
    depositCash(250);
    showBalance();
    withdrawCash(300);
    showBalance();
    depositCash(50);
    showBalance();
    return 0;
}