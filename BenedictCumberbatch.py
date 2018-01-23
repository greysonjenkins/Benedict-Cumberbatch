from random import randint
from sys import exit

firstnames = ['Banister', 'Buttercup', 'Bonkyhort', 'Bendynoodle', 'Bodysnatch', 'Beneding', 'Beneficiary', 'Pumpernickle',
             'Bentobox', 'Barnoldswick', 'Badongawonk','Bogadogus', 'Bile', 'Bangkok', 'Bigglesworthy', 'Bambino']

lastnames = ['Cucumberbatch', 'Crumblebench', 'Crumperbunts', 'Pumpkinpatch', 'Chickenstrips', 'Clombyclomp', 'Crackerdong',
             'Upperclass', 'Crimpysnitch', 'Curdledong', 'Crimblenimbus', 'Cogglesnatch', 'Congleton', 'Congalatch', 'Casketlaunch']

def generateName():
    name = firstnames[randint(0, len(firstnames)-1)] + " " + lastnames[randint(0, len(lastnames)-1)]
    print ("What's this guy's name?\n" + name, '\n\n')

print('Press enter to generate a new name, or enter "stop" to end the program.\n')
userinput = input().lower

while userinput != 'stop':
    generateName()
    userinput = input()
    userinput = userinput.lower()
