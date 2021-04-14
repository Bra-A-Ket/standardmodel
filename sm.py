"""List/table of particles in the standard model and their
attributes
"""

#inputs
import os
import getopt
import sys
from particles import *

#header
author = "Falk Adamietz"
version = 1.0

#last update
day = "14"
month = "04"
year = "2021"

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ivp",\
        ["info", "version", "particle"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for o, a in opts:
        if o in ("-v", "--version"):
            print("Version: {}".format(version))

        elif o in ("-i", "--info"):
            print("Author: {}".format(author))
            print("Version: {}".format(version))
            print("Last update: {0}.{1}.{2}".format(day, month, year))

        elif o in ("-p", "--particle"):
            particle_list = sys.argv[2:]
            print("-------------")
            for particle in particle_list:
                keys = getList(eval(particle))
                for key in keys:
                    item = eval(particle)[key]
                    if item == True:
                        print(key)
                    elif item == False:
                        pass
                    else:
                        print(key + ": " + item)
                print("-------------")

        else:
            print("Error: Unkown arg")
            sys.exit(1)

if __name__ == "__main__":
    main()
