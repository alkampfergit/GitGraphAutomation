import json
import pytest
from src.git_graph_automation.git_command import invoke_git_log


def test_basic_git_invocation():
    """
    Just a test to verify that we are able to grab git log output.
    """
    output = invoke_git_log()
    print(output)
    assert output != ""
    assert "hashAbbrev" in output


@pytest.mark.parametrize("num", [
    2,
    4
])
def test_git_invocation_can_limit(num):
    """
    Verify that we are able to limit the number of commit we can log.
    """
    output = invoke_git_log(num)
    json_to_parse = "[" + output.strip(',') + "]"
    parsed = json.loads(json_to_parse)

    print(parsed)
    assert len(parsed) == num
