#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
int count_letters(string n);
int count_words(string n);
int count_sentences(string n);

int main(void)
{
    string text = get_string("Test: ");
    int letters = count_letters(text);     // 字母總數
    int words = count_words(text);         // 單字總數
    int sentences = count_sentences(text); // 句子總數

    double L = (double) letters / words * 100;
    double S = (double) sentences / words * 100;

    double index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = (int) round(index);
    // printf("%f,%f,%d\n",L,S,index);
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
    return 0;
}

int count_letters(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    if (strlen(text) == 0)
    {
        return 0;
    }
    int count = 1; // 第一個單字前沒有空白
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count;
}
int count_sentences(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}
