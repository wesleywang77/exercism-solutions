#include "grains.h"

uint64_t square(uint8_t index)
{
    if (index == 1) return 1;
    uint64_t result;
    result = square(index - 1) * 2;
    return result;
}
uint64_t total(void)
{
    uint64_t sum = 0;
    int i;
    for (i = 0; i <= 64; i++)
    {
        sum += square(i);
    }
    return sum;
}