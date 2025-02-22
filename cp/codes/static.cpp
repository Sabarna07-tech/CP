#include <stdio.h>

// Function prototype declaration
int add();

int main()
{
    int i, ret;
    for (i = 1; i <= 10; i++)
    {
        ret = add();
    }
    return 0; // Return statement for the main function
}

int add()
{
    static int sum = 0; // Static variable to retain its value across function calls
    sum++;
    printf("\n sum is %d", sum);
    return sum; // Return the sum (optional based on your needs)
}
