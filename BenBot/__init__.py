import requests
name = 'BenBot'

BEN_BOT = 'http://benbotfn.tk:8080/api/'

# Get any cosmetic, not checking cosmetic type.

def getCosmetic(search):
    url = BEN_BOT + 'cosmetics/search?displayName=' + search
    benResponse = requests.get(url).json()
    return benResponse

def getCosmeticId(search):
    url = BEN_BOT + 'cosmetics/search?displayName=' + search
    benResponse = requests.get(url).json()
    return benResponse['id']

def getCosmeticFromId(search):
    url = BEN_BOT + 'cosmetics/search?id=' + search
    benResponse = requests.get(url).json()
    return benResponse

# Gets cosmetic with type Outfit.

def getSkin(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Outfit':
            return cosmetic

def getSkinId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Outfit':
            return cosmetic['id']

# Gets cosmetic with type Harvesting Tool.

def getPickaxe(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Harvesting Tool':
            return cosmetic

def getPickaxeId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Harvesting Tool':
            return cosmetic['id']

# Gets cosmetic with type Back Bling.

def getBackpack(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Back Bling':
            return cosmetic

def getBackpackId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Back Bling':
            return cosmetic['id']

# Gets cosmetic with type Glider.

def getGlider(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Glider':
            return cosmetic

def getGliderId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Glider':
            return cosmetic['id']

# Gets cosmetic with type Emote.

def getEmote(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Emote':
            return cosmetic

def getEmoteId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    benResponse = requests.get(url).json()
    for cosmetic in benResponse:
        if cosmetic['type'] == 'Emote':
            return cosmetic['id']