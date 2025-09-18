#include <cs50.h>
#include <stdio.h>

void print_row(int space, int length);
int main(void)
{
    int height = get_int("Height: ");
    if (height <= 0)
    {
        height = get_int("Height: ");
    }

    for (int j = 0; j < height; j++)
    {
        print_row(height - j - 1, j + 1);
    }
}

void print_row(int space, int length)
{
    for (int i = 0; i < space; i++)
    {
        printf(" ");
    }
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    printf("  ");
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    printf("\n");
}
