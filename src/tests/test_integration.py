import pytest
import os
import json
from src.git_graph_automation.renderer import renderHtml
from src.git_graph_automation.logParser import parseJsonOutput
from src.git_graph_automation.gitCommand import invokeGitLog

def test_full_rendering_last_10_commits():
    filePath = "/tmp/test_full_rendering_last_10_commits.html"

    if os.path.exists(filePath):
        os.remove(filePath)

    gitLog = invokeGitLog(10)
    parsed = parseJsonOutput(gitLog)
    data = json.dumps(parsed) 
    renderHtml(data, filePath)

    
    