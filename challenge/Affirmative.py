#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=188
# A: http://www.hacker.org/challenge/chal.php?answer=no&id=188&go=Submit

# Squint at the output, and there is a "NO" in the picture.

def main():
    symbols = ['79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '0d', '0a', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '0d', '0a', '73', '79', '45', '73', '79', '65', '53', '79', '65', '73', '59', '45', '53', '79', '65', '73', '0d', '0a', '79', '65', '53', '59', '65', '73', '59', '65', '73', '59', '65', '73', '79', '45', '73', '79', '0d', '0a', '65', '73', '59', '45', '73', '79', '45', '73', '79', '45', '73', '79', '65', '53', '79', '65', '0d', '0a', '73', '79', '45', '73', '59', '65', '53', '79', '65', '53', '79', '65', '73', '59', '65', '73', '0d', '0a', '79', '65', '53', '79', '45', '73', '59', '65', '73', '59', '65', '73', '79', '45', '73', '79', '0d', '0a', '65', '73', '59', '65', '73', '59', '45', '73', '79', '45', '73', '79', '65', '53', '79', '65', '0d', '0a', '73', '79', '45', '73', '79', '45', '53', '79', '65', '53', '79', '65', '73', '59', '65', '73', '0d', '0a', '79', '65', '53', '79', '65', '73', '59', '65', '73', '79', '45', '53', '59', '65', '73', '79', '0d', '0a', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '0d', '0a', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '79', '65', '73', '0d', '0a']
    print(''.join(map(lambda symbol: chr(int(symbol, 16)) if symbol[0] == '0' else chr(int(symbol)), symbols)))

if __name__ == '__main__':
    main()
