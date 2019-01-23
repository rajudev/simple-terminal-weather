#!/usr/bin/python3

import subprocess


# Replace Gurgaon with the City name of your choice
# Ensure that the `inxi` program is installed on your system

weather = subprocess.check_output("inxi -W Gurgaon", shell=True)
celcius = weather.split()
C = ''.join(str(celcius[1]) + str(celcius[2]) + str(celcius[3])).replace('\'',' ').replace('b','').replace('erature','').replace('  ', ' ').strip()
print(C)
