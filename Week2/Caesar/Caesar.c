#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string words = get_string("plaintext: ");
    int move = atoi(argv[1]);
    if (move <= 0)
    {
        printf("Key must be a positive integer.\n");
        return 1;
    }
    printf("ciphertext: ");
    for (int i = 0, n = strlen(words); i < n; i++)
    {
        char c = words[i];

        if (isupper(c))
        {
            printf("%c", 'A' + (c - 'A' + move) % 26);
        }
        else if (islower(c))
        {
            printf("%c", 'a' + (c - 'a' + move) % 26);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
    return 0;
}

bool only_digits(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}
