#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int point[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int number(string n);
int main(void)
{
    int word[2];
    string C1 = get_string("Player 1: ");
    word[0] = number(C1);
    string C2 = get_string("Player 2: ");
    word[1] = number(C2);
    // printf("%i,%i",word[0],word[1]);

    if (word[0] > word[1])
    {
        printf("Player 1 wins!");
    }
    else if (word[0] < word[1])
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }
    printf("\n");
}

int number(string n)
{
    int i = 0;
    int total = 0;
    while (n[i] != '\0')
    {
        if (isalpha(n[i]))
        {
            char t = toupper(n[i]);
            total += point[t - 'A'];
        }
        i++;
    }
    return total;
}
