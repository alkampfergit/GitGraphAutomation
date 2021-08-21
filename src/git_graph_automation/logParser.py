import json

def parseJsonOutput(jsonData):
    if not jsonData:
        return ""
    # remember that we pass a list of objects, the output of git log parametrized
    jsonData = jsonData.rstrip(',') # First of all remove trailing quotes
    jsonData = "[" + jsonData + "]" # Convert into an array
    fullData = json.loads(jsonData)
    return fullData