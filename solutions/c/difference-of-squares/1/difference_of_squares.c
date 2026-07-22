#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number)
{
    unsigned int sum = 0;
    for (unsigned int n = 1; n <= number; n++)
    {
        sum += n * n;
    }
    return sum;
}
unsigned int square_of_sum(unsigned int number)
{
    unsigned int n = number;
    unsigned int sum = n*(n+1) / 2;
    return sum * sum;
}
unsigned int difference_of_squares(unsigned int number)
{
    unsigned int result = square_of_sum(number) - sum_of_squares(number);
    return result;
}