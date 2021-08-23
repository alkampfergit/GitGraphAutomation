import pytest
import os
import json
from src.git_graph_automation.log_parser import parse_json_output

def getTestData(dataFileName):
    with open(f'{os.path.dirname(__file__)}/data/{dataFileName}', 'r') as file:
        data = file.read()
    return data

@pytest.mark.parametrize("dataFileName", [
    ("single.json"),
    ("empty.json")
])
def test_not_throw_during_parsing(dataFileName ):
    try:
        parse_json_output(getTestData(dataFileName))
    except Exception as exc:
        assert False, f"An exception is raised parsing a standard empty array {exc}"

def test_parse_single_record():
    parsed = parse_json_output(getTestData("single.json"))
    assert len(parsed) == 1
    assert parsed[0][ "hashAbbrev"] == "29c6b7c"

def test_fix_of_refs():
    parsed = parse_json_output(getTestData("single.json"))
    elem = parsed[0]
    assert len(elem["refs"]) == 1
    assert elem["refs"] == ["develop"]

def test_empty_refs_generates_empty_list():
    parsed = parse_json_output(getTestData("twocommits.json"))
    elem = parsed[1]
    assert len(elem["refs"]) == 0
    assert elem["refs"] == []
    assert len(elem["parents"]) == 1

def test_two_parents():
    '''
    Git log write parents separated by a space as a single string.
    '''
    parsed = parse_json_output(getTestData("single-twoparents.json"))
    elem = parsed[0]
    assert len(elem["parents"]) == 2
    assert elem["parents"] == ["ec2145c002980352140c2369dba71175de1ebfc6", "ac2145c002980352140c2369dba71175de1ebfc6"]




