#include <cs50.h>
#include <math.h>
#include <stdio.h>

int chage(int n);
int main(void)
{
    int n = get_float("Change owed: ");
    if (n < 0)
    {
        n = get_float("Change owed: ");
    }

    printf("%i\n", chage(n));
}
int chage(int total)
{
    int n = 0;
    while (total > 0)
    {
        if (total >= 25)
        {
            n += round(total / 25);
            total %= 25;
        }
        else if (total >= 10)
        {
            n += round(total / 10);
            total %= 10;
        }
        else if (total >= 5)
        {
            n += round(total / 5);
            total %= 5;
        }
        else if (total >= 1)
        {
            n += round(total / 1);
            total = total % 1;
        }
    }
    return n;
}
