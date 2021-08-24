import os
import pytest

from src.git_graph_automation.log_parser import parse_json_output


def get_test_data(data_file_name):
    """
    Load test data from a file in /data/ subdirectory
    @param data_file_name: Name of the test file
    @return: The content of the file
    """
    with open(f'{os.path.dirname(__file__)}/data/{data_file_name}', 'r') as file:
        data = file.read()
    return data


@pytest.mark.parametrize("data_file_name", [
    "single.json",
    "empty.json"
])
def test_not_throw_during_parsing(data_file_name):
    try:
        parse_json_output(get_test_data(data_file_name))
    except Exception as exc:
        assert False, f"An exception is raised parsing a standard empty array {exc}"


def test_parse_single_record():
    parsed = parse_json_output(get_test_data("single.json"))
    assert len(parsed) == 1
    assert parsed[0]["hashAbbrev"] == "29c6b7c"


def test_fix_of_refs():
    parsed = parse_json_output(get_test_data("single.json"))
    elem = parsed[0]
    assert len(elem["refs"]) == 1
    assert elem["refs"] == ["develop"]


def test_empty_refs_generates_empty_list():
    parsed = parse_json_output(get_test_data("twocommits.json"))
    elem = parsed[1]
    assert len(elem["refs"]) == 0
    assert elem["refs"] == []
    assert len(elem["parents"]) == 1


def test_two_parents():
    """
    Git log write parents separated by a space as a single string.
    """
    parsed = parse_json_output(get_test_data("single-twoparents.json"))
    elem = parsed[0]
    assert len(elem["parents"]) == 2
    assert elem["parents"] == ["ec2145c002980352140c2369dba71175de1ebfc6", "ac2145c002980352140c2369dba71175de1ebfc6"]
