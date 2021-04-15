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
version = 1.1

#last update
day = "15"
month = "04"
year = "2021"

#list of all particles
particles_ = [
    proton, up, down, charm, strange, top, bottom, electron, muon, tau,
    nue, num, nut,
]

def getList(dict):
    """return a list of the keys of the dictionary dict"""
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ivphbf",\
        ["info", "version", "particle", "help", "boson", "fermion"])
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

        elif o in ("-h", "--help"):
            print("List of every particle and their used syntax on")
            print("github.com/Bra-A-Ket/standardmodel")
            print("")
            print("commands:")
            print("- Use -p <name> or --particle <name> to show information about the particle, e.g.")
            print(">>> sm -p electron")
            print("- Use -b or --boson to list all bosons")
            print("- Use -f or --fermion to list all fermions")

        elif o in ("-b", "--boson"):
            print("Bosons have a integer spin. Particles with s=0 are called scalar boson, with s=1 vector boson, with s=2 tensor boson.\
            they follow the Bose-Einstein-statistics.")
            print("")
            for particle in particles_:
                bool = particle["boson"]
                if bool == True:
                    print(particle["name"] + ", ")

        elif o in ("-f", "--fermion"):
            print("Fermions have half odd integer spin, e.g. s=1/2, 3/2. They follow the Fermi-Dirac-statistics.")
            for particle in particles_:
                bool = particle["fermion"]
                if bool == True:
                    print(particle["name"] + ", ")

        else:
            print("Error: Unkown arg")
            sys.exit(1)

if __name__ == "__main__":
    main()
