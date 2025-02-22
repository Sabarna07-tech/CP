#include <iostream>
using namespace std;
unsigned int reverseHex(unsigned int hex)
{
    unsigned int reversedHex = 0;

    while (hex > 0)
    {
        reversedHex <<= 4;          // Shift left by 4 bits to make room for the next nibble
        reversedHex |= (hex & 0xF); // Extract the lowest nibble and add it to the reversed number
        hex >>= 4;                  // Shift right by 4 bits to process the next nibble
    }

    return reversedHex;
}

int main()
{
    unsigned int num = 0xABCDE;
    unsigned int reversedNum = reverseHex(num);

    std::cout << "Original: 0x" << std::hex << num << std::endl;
    std::cout << "Reversed: 0x" << std::hex << reversedNum << std::endl;

    return 0;
}
