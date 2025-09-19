#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file %s\n", argv[1]);
        return 1;
    }

    uint8_t buffer[512];
    FILE *output = NULL;
    int jpeg_count = 0;
    char filename[8];

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // 關閉前一個JPEG文件（如果存在）
            if (output != NULL)
            {
                fclose(output);
            }

            sprintf(filename, "%03d.jpg", jpeg_count);
            jpeg_count++;

            output = fopen(filename, "w");
            if (output == NULL)
            {
                fclose(card);
                printf("Could not create %s\n", filename);
                return 1;
            }
        }

        if (output != NULL)
        {
            fwrite(buffer, 1, 512, output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }
    fclose(card);

    return 0;
}
