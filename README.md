# nft-pfp-generator
Generate ERC721 NFTS based on multiple png layers

This project is in progress.

Current status:
1. DONE: Generation of token images
2. DONE: Weight/rarity for traits
3. Next up: Optional trait groups


## How to use
### Install
`pip install -r requirements.txt`

`python3 main.py`

### Simple adjustments
Simple adjustments can be done in the main method of `main.py`.
Here you defined the name of the collection, the directory to use for traits, the number of tokens to generate and the directory to generate the token files.
```
def main():
    nftCollection = NFTCollection('Cubeheads')
    nftCollection.initializeTraits('traits/')
    nftCollection.generateTokens(100)
    nftCollection.generateImages('tokens/')
```

## Concepts
### Trait groups
Define trait groups by creating a subdirectory of `traits\`. Use `<priority>-<trait group name>` where the number defines the order it will be composited.

### Traits
Each trait group will have several traits represented by a .png file with alpha transparency (lowest priority trait group is expected to have now alpha transparency).

The rarity of each trait within a trait group is defined by adding the weight as part of the file name.
`<weight>_traitname.png` (the lower the weight, the less likely it will be used) 



### License
Code is open-sourced, but example traits and token images in repo are not.
