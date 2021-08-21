import pytest
import os
import json
from src.git_graph_automation.renderer import renderHtml
from src.git_graph_automation.logParser import parseJsonOutput
from src.git_graph_automation.gitCommand import invokeGitLog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_full_rendering_last_10_commits(tmp_path):
    filePath = tmp_path / "test_full_rendering_last_10_commits.html"

    if os.path.exists(filePath):
        os.remove(filePath)

    gitLog = invokeGitLog(10)
    parsed = parseJsonOutput(gitLog)
    data = json.dumps(parsed) 
    renderHtml(data, filePath)

#@pytest.mark.skip(reason="still does not work")
def test_full_rendering_in_selenium(tmp_path):
    filePath = tmp_path / "test_full_rendering_last_10_commits.html"
    outputImage = tmp_path / "test_full_rendering_last_10_commits.png"

    if os.path.exists(filePath):
        os.remove(filePath)

    if os.path.exists(outputImage):
        os.remove(outputImage)

    gitLog = invokeGitLog(10)
    parsed = parseJsonOutput(gitLog)
    data = json.dumps(parsed) 
    renderHtml(data, filePath)

    # get the name in a correct format
    temp_name = "file://" + filePath.as_posix()

    driver = webdriver.Chrome(r'C:/temp/chromedriver_win32/chromedriver.exe')
    driver.set_window_size(1024, 768) 
    #driver.get('https://google.com/') # this works fine
    driver.get(temp_name) # passing the file name or htmlString doesn't work...creates a blank png with nothing
    driver.save_screenshot(outputImage) 
    driver.quit()
    