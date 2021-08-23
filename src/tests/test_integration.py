import pytest
import os
import json
from src.git_graph_automation.renderer import renderHtml
from src.git_graph_automation.logParser import parseJsonOutput
from src.git_graph_automation.gitCommand import invokeGitLog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import subprocess
from playwright.sync_api import sync_playwright

def test_full_rendering_last_10_commits(tmp_path):
    filePath = tmp_path / "test_full_rendering_last_10_commits.html"

    if os.path.exists(filePath):
        os.remove(filePath)

    gitLog = invokeGitLog(10)
    parsed = parseJsonOutput(gitLog)
    data = json.dumps(parsed) 
    renderHtml(data, filePath)

#@pytest.mark.skip(reason="this will use real browser to dump the file")
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

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(temp_name)
        page.screenshot(path=outputImage.as_posix())
        browser.close()

    # Use selenium to open the file and render the graph in png.
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    # driver = webdriver.Chrome(r'C:/temp/chromedriver_win32/chromedriver.exe', chrome_options=options)

    # driver.get(temp_name) # passing the file name or htmlString doesn't work...creates a blank png with nothing
    # driver.save_screenshot(outputImage.as_posix()) 
    # driver.quit()

    # Now open the file, this work in windows
    if os.name == 'nt':
        subprocess.call(outputImage.as_posix(), shell=True)
    