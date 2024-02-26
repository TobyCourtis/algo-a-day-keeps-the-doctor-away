Attempt:

We can add the integers by conversion to binary, using XOR/AND and bitshifting.


Case a = 9 + b = 11:

9: 1001
11: 1011

Loop until we do not have anything as result of the AND:
1.
a ^ b =      0010   (XOR'd)
a & b << 1 = 10010  (AND bit shifted left 1)

2.
0010 ^ 10010 = 10000
0010 & 10010 = 00100

3.
10000 ^ 00100 = 10100
10000 & 00100 = 00000

result = 10100 = 20



AND with bitshift explained:

a: 01
b: 01

a AND b = 10

we and the first values AND(1,1) = 1 and then we carry the 1 into the next higher power bit (2^1 here).

<br>

Case a=1, b=1:

xor = 11
and << 1 = 00

result = 11 = 3

<br>

Usage of 'mask' explained:

- python's binary representation has unlimited leading 1s
- logical_xor > mask // 2
  - a 32 bit signed int is positive if 32nd bit is 0, negative if 32nd bit is 1
  - mask // 2 is the largest number we can have (31 1s) before we are representing negative values
  - So this check determines if our number is negative or not
- Our representation of -3 in 32 bits: (...0000000)11111111111111111111111111111101
- XOR with mask, aka flip rightmost 32 bits: (...0000000)00000000000000000000000000000010
- NOT, aka flipping all bits: (...1111111)1111111111111111111111111111101
- The result is Python's representation of -3, including an unlimited number of leading 1's.


Runtime beat 94%, memory beat 62%  