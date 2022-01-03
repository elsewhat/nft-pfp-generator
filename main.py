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
        self.totalWeight = 0

    def addTrait(self,trait):
        self.traits.append(trait)
        self.traitsWeights.append(trait.weight)
        self.totalWeight += trait.weight
                


def main():
    #wallet = sys.argv[0]

    traitGroups = {}

    traitGroupDirectories = [(f.path,f.name) for f in os.scandir('traits/') if f.is_dir()]

    for (traitGroupDirPath,traitGroupDirName) in traitGroupDirectories:
        print('Found trait group: {}'.format(traitGroupDirName))
        traitGroup = TraitGroup(traitGroupDirPath)

        traitGroupFiles = [f.name for f in os.scandir(traitGroupDirPath) if f.is_dir() != True]

        for traitFile in traitGroupFiles:
            print('Adding trait from file {}'.format(traitFile))
            traitGroup.addTrait(Trait(traitFile,traitFile,1))

        traitGroups[traitGroupDirName]= traitGroup


    #for name in files:
        #print(os.path.join(path, name))


if __name__ == '__main__':
   main()