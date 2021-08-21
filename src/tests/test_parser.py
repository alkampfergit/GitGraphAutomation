import pytest
import os
import json
from src.git_graph_automation.logParser import parseJsonOutput

def getTestData(dataFileName):
    with open(f'{os.path.dirname(__file__)}/data/{dataFileName}', 'r') as file:
        data = file.read()
    return data;

@pytest.mark.parametrize("dataFileName", [
    ("single.json"),
    ("empty.json")
])
def test_not_throw_during_parsing(dataFileName ):
    try:
        parseJsonOutput(getTestData(dataFileName))
    except Exception as exc:
        assert False, f"An exception is raised parsing a standard empty array {exc}"

def test_parse_single_record():
    parsed = parseJsonOutput(getTestData("single.json"))
    assert len(parsed) == 1
    assert parsed[0][ "hashAbbrev"] == "29c6b7c"

def test_fix_of_refs():
    parsed = parseJsonOutput(getTestData("single.json"))
    elem = parsed[0]
    assert len(elem["refs"]) == 2




