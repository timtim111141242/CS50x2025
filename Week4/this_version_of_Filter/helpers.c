#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE r = image[i][j].rgbtRed;
            BYTE b = image[i][j].rgbtBlue;
            BYTE g = image[i][j].rgbtGreen;

            BYTE A = (BYTE) round((r + b + g) / 3.0);

            image[i][j].rgbtRed = A;
            image[i][j].rgbtBlue = A;
            image[i][j].rgbtGreen = A;
        }
    }
    return;
}

int check(int C)
{
    if (C > 255)
    {
        return 255;
    }
    else
    {
        return C;
    }
}
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE r = image[i][j].rgbtRed;
            BYTE b = image[i][j].rgbtBlue;
            BYTE g = image[i][j].rgbtGreen;

            int sr = check(round(0.393 * r + 0.769 * g + 0.189 * b));
            int sg = check(round(0.349 * r + 0.686 * g + 0.168 * b));
            int sb = check(round(0.272 * r + 0.534 * g + 0.131 * b));

            image[i][j].rgbtRed = sr;
            image[i][j].rgbtBlue = sb;
            image[i][j].rgbtGreen = sg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // 建立副本避免讀寫污染
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0, count = 0;
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        sumRed += copy[ni][nj].rgbtRed;
                        sumGreen += copy[ni][nj].rgbtGreen;
                        sumBlue += copy[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }
            image[i][j].rgbtRed = round((float) sumRed / count);
            image[i][j].rgbtGreen = round((float) sumGreen / count);
            image[i][j].rgbtBlue = round((float) sumBlue / count);
        }
    }
    return;
}
