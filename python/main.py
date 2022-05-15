from PIL import Image, ImageOps
import random
import json

####################################
######  Image Initializing  ########
####################################

# currently 5 types
background_colors = ["White", "Red", "Green", "Blue", "Black"]
background_weights = [20, 20, 20, 20, 20]
background_images = {"Background1","Background2","Background3","Background4","Background5"}
background_dictionary = {"White": "Background1", "Red": "Background2", "Green": "Background3" , "Blue": "Background4" ,"Black": "Background5"}

# currently 14 types
#duck_colors = ["Yellow", "Green", "White", "Grey", "Brown", "Red", "Blue", "Mallard", "Canvasback", "Tie Dye", "Cyborg",
#               "Skeleton", "Galaxy", "Gold"]
#duck_weights = [11.75, 11.75, 11.75, 11.75, 11.75, 11.75, 11.75, 7.5, 7.5, 1.15, 0.5, 0.5, 0.3, 0.3]
duck_colors = ["Dark Red"  , "Blue", "Gray", "Green", "Light Blue", "White", "Light Green", "Pink", "Mint", "Bright Yellow" , "Purple", "Red"  , "Yellow", "Galaxy", "Golden", "Wooden"]
duck_weights = [19          ,6      ,6      ,6       ,6            ,6       ,6             ,6      ,6      ,6               ,6        ,6       ,6        , 2       , 2       , 5       ]
duck_images = {"duck1"     ,"duck2","duck3","duck4" ,"duck5"      ,"duck6" ,"duck7"       ,"duck8","duck9","duck10"        ,"duck11" ,"duck12","duck13"  , "duck14", "duck15", "duck16"}
duck_dictionary = {"Dark Red" : "duck1", "Blue" : "duck2", "Gray" : "duck3" , "Green" : "duck4" ,"Light Blue" : "duck5" ,"White" : "duck6", "Light Green" : "duck7" ,"Pink" : "duck8" ,"Mint" : "duck9" ,"Bright Yellow" : "duck10" ,"Purple" : "duck11" ,"Red" : "duck12" ,"Yellow" : "duck13", "Galaxy": "duck14", "Golden": "duck15", "Wooden": "duck16"}

# currently 12 types
# mouth_styles = ["None", "Tongue Out", "Vampire", "Smile", "Face Mask", "Fish", "Derpy", "Angry", "Cyborg", "Gold Smile",
#                 "Rose", "Crack Teeth"]
# mouth_weights = [18.5, 10, 5, 10, 19, 5, 5, 7.5, 5, 5, 5, 5]
mouth_styles = ["Default", "Angry"   , "Smile" , "Mask"  , "Derpy" , "Fish Face", "Golden Smile", "Red Lips", "Vampire", "Rose"  , "Sad"   , "Tongue Out" ]
mouth_weights = [25      , 6         , 12       , 6       , 6       , 6          , 3             , 6         , 6        , 6       , 6       , 6 ]
mouth_images = {"mouthNone", "mouth1", "mouth2", "mouth3", "mouth4", "mouth5"   ,"mouth6"       ,"mouth7"   ,"mouth8"  ,"mouth9" ,"mouth10" ,"mouth11"}
mouth_dictionary = {"Default": "mouthNone", "Angry": "mouth1", "Smile": "mouth2", "Mask": "mouth3", "Derpy": "mouth4", "Fish Face": "mouth5", "Golden Smile": "mouth6", "Red Lips": "mouth7" , "Vampire": "mouth8", "Rose": "mouth9" , "Sad": "mouth10", "Tongue Out": "mouth11"  }

# currently 15 types
# eye_styles = ["None", "Green", "Blue", "Fire", "Water", "Void", "Money", "Hearts", "ETH", "Sleepy", "Lazy-Eye",
#               "Static", "Lasers", "Eye Patch", "Cyclops"]
# eye_weights = [10, 13.5, 13.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 9, 8.5, 3, 0.5, 8, 1]
eye_styles = ["Angry", "Default", "Blue", "Closed", "Money", "Eye-Patch", "Fire", "Galaxy", "Glasses", "Green", "Hearts", "Sad" , "Sunglasses", "Cat Eyes", "Wink"]
eye_weights = [16    ,6         ,6      ,  6      ,6       ,6           ,6      ,6        ,6         ,6      ,6         ,6      ,6            ,6          ,6  ]
eye_images = {"eye1" , "eye2"   , "eye3", "eye4"  , "eye5" , "eye6"     , "eye7", "eye8"  , "eye9"   , "eye10", "eye11" ,"eye12", "eye13"     , "eye14"   , "eye15"}
eye_dictionary = {"Angry": "eye1", "Default": "eye2", "Blue": "eye3", "Closed": "eye4", "Money": "eye5", "Eye-Patch": "eye6" ,"Fire": "eye7" ,"Galaxy": "eye8" ,"Glasses": "eye9" ,"Green": "eye10" ,"Hearts": "eye11" ,"Sad": "eye12" ,"Sunglasses": "eye13" ,"Cat Eyes": "eye14" ,"Wink": "eye15" }

# currently 14 types
# hat_types = ["None", "Sailor", "Baseball", "Football Helmet", "Fez", "Bandana", "Rain Hat", "War Helmet", "Astronaut",
#              "Pilot headgear", "Beanie", "Crown", "Airpods", "Golden Airpods"]
# hat_weights = [10, 8, 9.5, 9.5, 9.5, 9.5, 11, 5, 5, 7.5, 9, 1, 5, 0.5]
hat_types = ["None"    , "Astronaut", "Black Cat Ears", "Blue Bucket Hat", "Blue Football Helmet", "Cow Bucket Hat", "Crown", "Gray Beanie", "Halo", "Leopard Bucket Hat", "Orange Cat Ears", "Pink Bucket Hat", "Pink Cat Ears", "Red Football Helmet", "Brown Beanie"]
hat_weights = [16       ,6           ,6                ,6                 ,6                      ,6                ,6       ,6             ,6      ,6                    ,6                 ,6                 ,6               ,6                     ,6               ]
hat_images = {"hatNone","hat1"      ,"hat2"           ,"hat3"            , "hat4"                ,"hat5"           ,"hat6"  ,"hat7"        ,"hat8" ,"hat9"               ,"hat10"           ,"hat11"           ,"hat12"         ,"hat13"               ,"hat14"      }
hat_dictionary = {"None": "hatNone", "Astronaut": "hat1", "Black Cat Ears": "hat2", "Closed": "hat3", "Blue Football Helmet": "hat4", "Cow Bucket Hat": "hat5" ,"Gray Beanie": "hat7" ,"Crown": "hat6" ,"Halo": "hat8" ,"Leopard Bucket Hat": "hat9" ,"Orange Cat Ears": "hat10" ,"Pink Bucket Hat": "hat11" ,"Pink Cat Ears": "hat12" ,"Red Football Helmet": "hat13" ,"Brown Beanie": "hat14", "Blue Bucket Hat": "hat3"}

# currently 8 types
accessories_type = ["None"           , "Airpods"     , "Black Sling", "Bread"     , "Gold Chain", "White Sling", "Puka Necklace", "Quirky Necklace", "Tote Bag"]
accessories_weights = [12            ,11             ,11            ,11           ,11           ,11            ,11              ,11                , 11]
accessories_images = {"accessoryNone","accessory1"   , "accessory2" , "accessory3", "accessory4", "accessory5" , "accessory6"   , "accessory7"     , "accessory8"}
accessories_dictionary = {"None": "accessoryNone", "Airpods": "accessory1", "Black Sling": "accessory2", "Bread": "accessory3", "Gold Chain": "accessory4", "White Sling": "accessory5", "Puka Necklace": "accessory6", "Quirky Necklace": "accessory7", "Tote Bag": "accessory8"}

# currently 12 types
# outfit_types = ["None", "Sailor", "Rain Jacket", "Baseball Uni", "Football Uni", "TieDye Shirt", "Life Jacket",
#                 "Business Suit", "Bikini", "Astronaut Suit", "Turtle Neck", "Karate"]
# outfit_weights = [10, 8, 11, 9.5, 9.5, 5, 8.5, 7.5, 8, 4, 9.5, 9.5]
outfit_types = ["None"       , "Blue Shirt", "Business Suit", "Cow Shirt", "Flower Shirt", "Clothing Jacket", "Leopard Shirt", "Life Jacket", "Tie Dye Shirt", "Turtleneck"]
outfit_weights = [10         , 10          ,10              ,10          ,10             ,10                ,10              ,10            ,10              ,10]
outfit_images = {"outfitNone", "outfit1"   , "outfit2"      , "outfit3"  , "outfit4"     , "outfit5"        , "outfit6"      , "outfit7"    , "outfit8"      , "outfit9"}
outfit_dictionary = {"None": "outfitNone", "Blue Shirt": "outfit1", "Business Suit": "outfit2", "Cow Shirt": "outfit3", "Flower Shirt": "outfit4", "Clothing Jacket": "outfit5", "Leopard Shirt": "outfit6", "Life Jacket": "outfit7", "Tie Dye Shirt": "outfit8", "Turtleneck": "outfit9" }

# currently 6
special_effect = ["None", "Mirror", "Upside-Down", "Trippy Background", "Inverted Colors", "Crypto Background",
                  "Deep-Fry"]
effect_weights = [100, 0, 0, 0, 0, 0, 0]
effect_images = {}
special_backgrounds = ["Trippy Background", "Crypto Background"]


####################################
###### Pick Duck Attributes ########
####################################

# Definetly a better way to do this but this will do.
# I don't want the same duck with different background that's lame.
# (special effect does not need to be checked because you purchase one)
def isDuckUnique(duck):
    if duck == {}:
        return False

    for tempDuck in listOfDucks:
        if tempDuck["Duck"] == duck["Duck"]:
            if tempDuck["Mouth"] == duck["Mouth"]:
                if tempDuck["Eyes"] == duck["Eyes"]:
                    if tempDuck["Hat"] == duck["Hat"]:
                        if tempDuck["Outfit"] == duck["Outfit"]:
                            print("This duck needs to be remade, it matches everything except background", duck)
                            global countOfFailedDucks
                            countOfFailedDucks = countOfFailedDucks + 1
                            return False

    return True


def createDuck(index):
    duck = {}

    while not isDuckUnique(duck):
        duck["ID"] = index
        duck["Background"] = random.choices(background_colors, background_weights)[0]
        duck["Duck"] = random.choices(duck_colors, duck_weights)[0]
        duck["Mouth"] = random.choices(mouth_styles, mouth_weights)[0]
        duck["Eyes"] = random.choices(eye_styles, eye_weights)[0]
        duck["Hat"] = random.choices(hat_types, hat_weights)[0]
        duck["Outfit"] = random.choices(outfit_types, outfit_weights)[0]
        duck["special_effect"] = random.choices(special_effect, effect_weights)[0]
        duck["Accessory"] = random.choices(accessories_type, accessories_weights)[0]

    return duck


####################################
######   Generate Images    ########
####################################

def combineImages(img1, img2):
    return Image.alpha_composite(img1, img2)



def compileImage(duck):

    # TODO MAKE SURE THE LAYERING IS CORRECT
    # Collect needed images
    # if duck[special_effect] == "None":
    #     background = Image.open(f'./BACKGROUNDS/{str(background_images[duck["Background"]])}.jpg').convert('RGBA')
    # elif duck[special_effect] in special_backgrounds:
    #     background = Image.open(f'./BACKGROUNDS/{str(background_images[duck["Background"]])}.jpg').convert('RGBA')
    # elif duck[special_effect] == "Deep-Fry":
    #     background = Image.open(f'./BACKGROUNDS/{str(background_images[duck["Trippy Background"]])}.jpg').convert('RGBA')
    # else:
    background = Image.open(f'./BACKGROUNDS/{str(background_dictionary[duck["Background"]])}.png').convert('RGBA')
    duck_type = Image.open(f'./DUCKS/{str(duck_dictionary[duck["Duck"]])}.png').convert('RGBA')
    mouth = Image.open(f'./MOUTHS/{str(mouth_dictionary[duck["Mouth"]])}.png').convert('RGBA')
    eyes = Image.open(f'./EYES/{str(eye_dictionary[duck["Eyes"]])}.png').convert('RGBA')
    accessory = Image.open(f'./ACCESSORIES/{str(accessories_dictionary[duck["Accessory"]])}.png').convert('RGBA')
    hat = Image.open(f'./HATS/{str(hat_dictionary[duck["Hat"]])}.png').convert('RGBA')
    outfit = Image.open(f'./OUTFITS/{str(outfit_dictionary[duck["Outfit"]])}.png').convert('RGBA')

    # Combine images (order matters here)
    combination1 = Image.alpha_composite(background, duck_type)
    combination1 = Image.alpha_composite(combination1, eyes)
    combination1 = Image.alpha_composite(combination1, mouth)
    if(duck_type != "None"):
        combination1 = Image.alpha_composite(combination1, hat)
    if(outfit_images != "None"):
        combination1 = Image.alpha_composite(combination1, outfit)
    if(accessories_type != "None"):
        combination1 = Image.alpha_composite(combination1, accessory)

    convertedImage = combination1

    # if special_effect == "Mirror":
    #     convertedImage = ImageOps.mirror(convertedImage)
    # elif special_effect == "Upside-Down":
    #     convertedImage = ImageOps.flip(convertedImage)
    # elif special_effect == "Inverted Colors":
    #     convertedImage = ImageOps.invert(convertedImage)
    # elif special_effect == "Deep-Fry":
    #     convertedImage = ImageOps.posterize(convertedImage, 2)

    convertedImage = combination1.convert('RGB')

    fileName = "Duck #" + str(duck["ID"]) + ".jpg"
    convertedImage.save("./finalDucks/" + fileName)


####################################
######   Run Statistics    ########
####################################

def runStats():
    global listOfDucks

    numPosibilities = len(background_weights) * len(duck_weights) * len(mouth_weights) * len(eye_weights) * \
                      len(hat_weights) * len(outfit_weights)
    print("There are " + str(numPosibilities) + " possible combination of ducks")
    print("There are " + str(
        numPosibilities * len(effect_weights)) + " possible combination of ducks after special effects")

    usedBackgrounds = []
    usedDuck = []
    usedMouth = []
    usedEyes = []
    usedHat = []
    usedOutfit = []

    for duck in listOfDucks:
        if duck["Background"] not in usedBackgrounds:
            usedBackgrounds.append(duck["Background"])
        if duck["Duck"] not in usedDuck:
            usedDuck.append(duck["Duck"])
        if duck["Mouth"] not in usedMouth:
            usedMouth.append(duck["Mouth"])
        if duck["Eyes"] not in usedEyes:
            usedEyes.append(duck["Eyes"])
        if duck["Hat"] not in usedHat:
            usedHat.append(duck["Hat"])
        if duck["Outfit"] not in usedOutfit:
            usedOutfit.append(duck["Outfit"])

    if len(usedBackgrounds) != len(background_weights):
        print("Not all backgrounds were used, these were the ones used ", usedBackgrounds)
    if len(usedDuck) != len(duck_weights):
        print("Not all ducks were used, these were the ones used ", usedDuck)
    if len(usedMouth) != len(mouth_weights):
        print("Not all mouths were used, these were the ones used ", usedMouth)
    if len(usedEyes) != len(eye_weights):
        print("Not all eyes were used, these were the ones used ", usedEyes)
    if len(usedHat) != len(hat_weights):
        print("Not all hats were used, these were the ones used ", usedHat)
    if len(usedOutfit) != len(outfit_weights):
        print("Not all outfits were used, these were the ones used ", usedOutfit)


####################################
######   Main Controller    ########
####################################

def getAttributes(duck):
    # background, duck, mouth, eyes, accessory, Hat, Outfit, special_effect
    background_attribute = {"trait_type" : "Background", "value": duck["Background"]}
    duck_attribute = {"trait_type" : "Duck", "value": duck["Duck"]}
    mouth_attribute = {"trait_type" : "Mouth", "value": duck["Mouth"]}
    eyes_attribute = {"trait_type" : "Eyes", "value": duck["Eyes"]}
    accessory_attribute = {"trait_type" : "Accessory", "value": duck["Accessory"]}
    hat_attribute = {"trait_type" : "Hat", "value": duck["Hat"]}
    outfit_attribute = {"trait_type" : "Outfit", "value": duck["Outfit"]}
    special_effect_attribute = {"trait_type" : "special_effect", "value": duck["special_effect"]}
    return [background_attribute, duck_attribute, mouth_attribute, eyes_attribute, accessory_attribute, hat_attribute, outfit_attribute, special_effect_attribute]


def createMetaData(listOfDucks):
    listOfMetaData = []
    for duck in listOfDucks:
        attributes = getAttributes(duck)
        name = "Duck #" + str(duck["ID"])
        description = ""
        external_url = ""
        image = ""
        duckMetaData ={"description": description, "external_url": external_url, "image": image, "name": name , "attributes": attributes}
        listOfMetaData.append(duckMetaData)

    return listOfMetaData


def createSpecificDuck():
    duck = {}

    duck["ID"] = 1
    duck["Duck"] = "test"
    duck["Outfit"] = "test"
    duck["Hat"] = "test"
    duck["Eyes"] = "test"
    duck["Mouth"] = "test"

    background = Image.open(f'./BACKGROUNDS/test.png').convert('RGBA')
    duck_type = Image.open(f'./DUCKS/test.png').convert('RGBA')
    mouth = Image.open(f'./MOUTHS/test.png').convert('RGBA')
    eyes = Image.open(f'./EYES/test.png').convert('RGBA')
    hat = Image.open(f'./OUTFITS/test.png').convert('RGBA')
    outfit = Image.open(f'./HATS/test.png').convert('RGBA')

    # Combine images (order matters here)
    combination1 = Image.alpha_composite(background, duck_type)
    combination2 = Image.alpha_composite(combination1, mouth)
    combination3 = Image.alpha_composite(combination2, eyes)
    combination4 = Image.alpha_composite(combination3, hat)
    combination5 = Image.alpha_composite(combination4, outfit)

    convertedImage = combination5.convert('RGB')

    fileName = "Duck #" + str(duck["ID"]) + ".jpg"
    convertedImage.save("./finalDucks/" + fileName)

    return


def runGeneration():
    #numberOfDucks = 4097
    numberOfDucks = 100

    counter = 1
    while counter < numberOfDucks:
        # print("duck number: " + str(counter) + " created")
        duck = createDuck(counter)
        listOfDucks.append(duck)
        counter += 1

    for duck in listOfDucks:
        compileImage(duck)
        print("Successfully created the image for duck ID: ", duck["ID"])

    # TODO FIGURE OUT IPFS
    # with open("IPFS_File", 'r') as IPFS:
    #     hashes = json.load(IPFS)
    # for hash, ID in hashes.ducks():
    #     listOfDucks[ID]["IPFS"] = hash

    # finalMetaData = createMetaData(listOfDucks)

    # with open("Ducks.json", 'w') as output:
    #     json.dump(finalMetaData, output, indent=4)

    with open("Ducks.json", 'w') as output:
        json.dump(listOfDucks, output, indent=4)

    runStats()


####################################
######   Global Variables   ########
####################################
listOfDucks = []
countOfFailedDucks = 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Run the initial set of ducks
    runGeneration()

    # Ability to create your own duck TODO
    # createSpecificDuck()

    # Ability to regenerate ducks TODO
    # rerunExistingDucks()

    # TEST FUNCTION
    #createSpecificDuck()
