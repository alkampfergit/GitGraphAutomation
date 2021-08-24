"""
Parser to manipulate raw git log json format to be compatible with
the format needed by GitGraph.js
"""
import json


def refs_should_be_omitted(ref: str):
    """
    Determine if a ref should be completely omitted from json output, we do not want
    to show origin
    @param ref: string containing the ref
    @return: True if this ref should be omitted from the list
    """
    return ref.startswith("origin/")


def adjust_ref(ref: str):
    """
    Refs should be adjusted, as an example HEAD -> should be removed
    @param ref: string containing the ref
    @return: correct ref string value to be passed to GitGraph.js library
    """
    if ref.startswith("HEAD"):
        return ref.split(" -> ")[1]
    return ref


def parse_json_output(json_data: str):
    """
    Takes raw git log in json format and adjust some part of it to be compatible
    with GitGraph.js
    @param json_data: contains the json output of a git log formatted in json
    @return: json output with various fix to be used as json input for GitGraph.js, return
    is an array of commit object
    """
    if not json_data:
        return ""
    # remember that we pass a list of objects, the output of git log parametrized
    json_data = json_data.rstrip(',')  # First of all remove trailing quotes
    json_data = "[" + json_data + "]"  # Convert into an array

    full_data = json.loads(json_data)

    # Now we need to start making fixing, first fix is simply change the refs into an array
    # gitgraph library does not seems to be able to render more than one refs, so we simply
    # create an array with the whole list of branches.
    for commit in full_data:
        fix_ref(commit)
        fix_parents(commit)

    return full_data


def fix_parents(commit):
    """
    We need to generate a parent list that is a list not a single string space separated
    @param commit:  commit parsed from json, it is a dictionary
    """
    parents = commit["parents"]
    if ' ' in parents:
        splitted_parents = parents.split(' ')
        commit["parents"] = splitted_parents
    else:
        commit["parents"] = [parents]


def fix_ref(commit):
    """
    Fix refs of the commit, this is needed because refs are comma separated in raw json
    output of git log
    @param commit: commit parsed from json, it is a dictionary
    """
    splitted_refs = commit["refs"].split(",")
    newref = ""

    for ref in splitted_refs:
        # omit every origin refs (need to generalize)
        ref = ref.strip()
        if ref and not refs_should_be_omitted(ref):
            newref += adjust_ref(ref)

    if newref:
        commit["refs"] = [newref]
    else:
        commit["refs"] = []
