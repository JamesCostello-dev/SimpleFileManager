#!/usr/bin/env python

import os
import random
import string
import time
import sys

def create_files(num):
    if not os.path.exists('random'):
        os.mkdir('random')
    for i in range(num):
        filename = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        with open('random/' + filename + '.txt', 'w') as f:
            f.write(''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(1, 100))))
        time.sleep(0.1)
    print('--------------------------------------------------------------------------------')
    print('Created ' + str(num) + ' files')
    print('--------------------------------------------------------------------------------')

create_files(int(sys.argv[1]))
