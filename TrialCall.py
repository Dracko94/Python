import requests
import json

trialCall = "https://pokeapi.co/api/v2/generation/generation-iii"

response = requests.get(trialCall)
data = response.json()

data['version_groups']

#Get API Data

dataStr = str(data['version_groups'])

#Change Data Dict to Str

file = open("TrialCall.txt", "x")
file.write(dataStr)
file.close()

#Write to a file

file = open("TrialCall.txt", "r")
print(file.read())
file.close()

#Read written file



