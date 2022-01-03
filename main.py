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

    def getRandomTrait(self):
        return random.choices(self.traits,self.traitsWeights)[0]

class Token:
    def __init__(self, name, tokenId):
        self.name = name
        self.traits=[]
        self.tokenId=tokenId
    
    def addTrait(self,trait):
        self.traits.append(trait)

    def generateImage(self,rootDir):
        #Process first trait outside for loop
        tokenImage = Image.open(self.traits[0].file).convert('RGBA')
        for trait in self.traits[1:]:
            traitLayer = Image.open(trait.file).convert('RGBA')
            tokenImage = Image.alpha_composite(tokenImage, traitLayer)

        tokenImage = tokenImage.convert('RGB')
        tokenImage.save(os.path.join(rootDir,'{}.png'.format(self.tokenId)))

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and self.traits == other.traits
    ) 

    # Hash function is used for checking for duplicates. Therefore only consideres traits
    def __hash__(self):
        return hash(tuple(self.traits))       

class NFTCollection:

    def __init__(self, name):
        self.name = name
        self.traitGroups = []
        self.tokens = []
        self.tokenHashes = {}
        self.tokenCounter=1

    def initializeTraits(self, traitRootDir):
        traitGroupDirectories = [(f.path,f.name) for f in os.scandir(traitRootDir) if f.is_dir()]

        for (traitGroupDirPath,traitGroupDirName) in traitGroupDirectories:
            print('Found trait group: {}'.format(traitGroupDirName))
            traitGroup = TraitGroup(traitGroupDirPath)

            traitGroupFiles = [(f.path,f.name) for f in os.scandir(traitGroupDirPath) if f.is_dir() != True]

            for (traitFile,traitName) in traitGroupFiles:
                print('Adding trait from file {}'.format(traitFile))

                #Let's parse weight based on filename
                traitWeight = 1
                traitNameComponents = traitName.split('_')
                if len(traitNameComponents) >=2 and traitNameComponents[0].isdigit():
                    traitWeight = int(traitNameComponents[0])
                    traitName= '_'.join(traitNameComponents[1:])

                traitGroup.addTrait(Trait(traitName,traitFile,traitWeight))
                print('Added trait {} with weight {}'.format(traitName,traitWeight))

            self.traitGroups.append(traitGroup)
        
    def generateTokens(self,count):
        for i in range(count):
            token = Token('{} #{}'.format(self.name, (i+self.tokenCounter)), (i+self.tokenCounter))
            for traitGroup in self.traitGroups:
                token.addTrait(traitGroup.getRandomTrait())

            if hash(token) in self.tokenHashes:
                print('Duplicate detected {}'.format(hash(token)))
                continue
            else:
                self.tokens.append(token)
                self.tokenHashes[hash(token)]= True
                
    def generateImages(self,rootDir):
        for token in self.tokens:
            token.generateImage(rootDir)
        




def main():
    nftCollection = NFTCollection('Cubeheads')
    nftCollection.initializeTraits('traits/')
    nftCollection.generateTokens(100)
    nftCollection.generateImages('tokens')



if __name__ == '__main__':
   main()