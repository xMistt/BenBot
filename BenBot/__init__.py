import aiohttp
name = 'BenBotAsync'
version = '0.0.4'

BEN_BOT = 'http://benbotfn.tk:8080/api/'

# Get any cosmetic, not checking cosmetic type.

async def getCosmetic(search):
    url = BEN_BOT + 'cosmetics/search?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            return benResponse

async def getCosmeticId(search):
    url = BEN_BOT + 'cosmetics/search?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            return benResponse['id']

async def getCosmeticFromId(search):
    url = BEN_BOT + 'cosmetics/search?id=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            return benResponse

# Gets cosmetic with type Outfit.

async def getSkin(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Outfit':
                    return cosmetic

async def getSkinId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Outfit':
                    return cosmetic['id']

# Gets cosmetic with type Harvesting Tool.

async def getPickaxe(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Harvesting Tool':
                    return cosmetic

async def getPickaxeId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Harvesting Tool':
                    return cosmetic['id']

# Gets cosmetic with type Back Bling.

async def getBackpack(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Back Bling':
                    return cosmetic

async def getBackpackId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Back Bling':
                    return cosmetic['id']

# Gets cosmetic with type Glider.

async def getGlider(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Glider':
                    return cosmetic

async def getGliderId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Glider':
                    return cosmetic['id']

# Gets cosmetic with type Emote.

async def getEmote(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Emote':
                    return cosmetic

async def getEmoteId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['type'] == 'Emote':
                    return cosmetic['id']

# Gets cosmetic with type Pet.

async def getPet(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['backendType'] == 'AthenaPetCarrier':
                    return cosmetic

async def getPetId(search):
    url = BEN_BOT + 'cosmetics/search/multiple?displayName=' + search
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            benResponse = await r.json()
            for cosmetic in benResponse:
                if cosmetic['backendType'] == 'AthenaPetCarrier':
                    return cosmetic['id']
