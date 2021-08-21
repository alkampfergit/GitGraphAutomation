import json

def refsShouldBeOmitted(ref):
    return ref.startswith("origin/")

def adjustRef(ref):
    if (ref.startswith("HEAD")):
        return ref.split(" -> ")[1]
    return ref

def parseJsonOutput(jsonData):
    if not jsonData:
        return ""
    # remember that we pass a list of objects, the output of git log parametrized
    jsonData = jsonData.rstrip(',') # First of all remove trailing quotes
    jsonData = "[" + jsonData + "]" # Convert into an array

    fullData = json.loads(jsonData)

    # Now we need to start making fixing, first fix is simply change the refs into an array
    # gitgraph library does not seems to be able to render more than one refs, so we simply
    # create an array with the whole list of branches.
    for commit in fullData:
        splittedRefs = commit["refs"].split(",")
        newref = ""

        for ref in splittedRefs:
            # omit every origin refs (need to generalize)
            ref = ref.strip()
            if ref and not refsShouldBeOmitted(ref):
                newref = newref + adjustRef(ref)

        if newref:
            commit["refs"] = [newref]
        else:
            commit["refs"] = []
        
    return fullData