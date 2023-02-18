"""
Algorithm:     Uses a generator expression to print all of the file names which are longer
               than 10 characters.
"""

import os
import os.path

for dirpath, dirnames, filenames in os.walk("c:/TestData/"):
    for filename in (f for f in filenames if len(f.split(".")[0]) > 14):
        print(os.path.join(dirpath, filename))

