import os
import json
import pytest
from src.git_graph_automation.gitCommand import invokeGitLog

def test_basic_git_invocation():
    '''
    Just a test to verify that we are able to grab git log output.
    '''
    output = invokeGitLog() 
    print (output)
    assert output != ""
    assert "hashAbbrev" in output

@pytest.mark.parametrize("num", [
    (2),
    (4)
])
def test_git_invocation_can_limit(num):
    '''
    Verify that we are able to limit the number of commit we can log.
    '''
    output = invokeGitLog(num) 
    parsed = json.loads("[" + output.strip(',') + "]")

    assert len(parsed) == num