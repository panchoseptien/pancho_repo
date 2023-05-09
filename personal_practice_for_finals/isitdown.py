#!/usr/bin/env python3

import os
import sys


for url in sys.argv[1:]:
    if os.system(f'curl -s {url} > /dev/null') == 0:
        print(f'{url} is UP')
    else 
        print(f'{url} is DOWN')