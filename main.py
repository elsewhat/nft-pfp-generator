from PIL import Image 
from IPython.display import display 
import random
import os


class Trait:
    def __init__(self, name, file, weight):
        self.name = name
        self.file = file
        self.weight = weight

class TraitGroup:
    def __init__(self, groupName):
        self.groupName = groupName
        self.traits = []
        self.traitsWeights = []

    def addTrait(self,trait):
        self.traits.push(trait)
        self.traitsWeights.push(trait.weight)
                


def main():
    #wallet = sys.argv[0]
    for path, subdirs, files in os.walk('traits/'):
        for traitGroup in subdirs:
            print(traitGroup)
            for path2, subdirs2, traitFiles in os.walk(os.path.join('traits/',traitGroup)):
                for traitFile in traitFiles:
                    print(os.path.join(path, traitFile))

        #for name in files:
            #print(os.path.join(path, name))


if __name__ == '__main__':
   main()