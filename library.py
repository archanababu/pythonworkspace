import random

feetInMiles = 5280
metersInKilometers = 1000

beatles = ["Jim", "Charlene", "Troy", "Alex", "Michael"]

def getFileExt(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)

