#!/usr/bin/env python3

from config import *
from Generator import *
from Encode import *
from Decode import *

if __name__ == "__main__":
    end_result = 0
    generator = Generator(N)
    for index, number in (zip(range(V), generator.start())):
        if index == V - 1:
            end_result = number
            print(f"Generator return: {number}")
            en_text = Encode(str(number), METHOD, KEY)
            print(f'Encoded: {en_text}')
            print(f'Decoded: {Decode(str(en_text), METHOD, KEY)}')
