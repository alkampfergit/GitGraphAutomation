import pytest
import os
import json
from src.git_graph_automation.renderer import render_html
from src.git_graph_automation.log_parser import parse_json_output
from src.git_graph_automation.git_command import invoke_git_log
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import subprocess
from playwright.sync_api import sync_playwright


def test_full_rendering_last_10_commits(tmp_path):
    file_path = tmp_path / "test_full_rendering_last_10_commits.html"

    if os.path.exists(file_path):
        os.remove(file_path)

    git_log = invoke_git_log(10)
    parsed = parse_json_output(git_log)
    data = json.dumps(parsed)
    render_html(data, file_path)


@pytest.mark.skip(reason="this will use real browser to dump the file")
def test_full_rendering_in_selenium(tmp_path):
    file_path = tmp_path / "test_full_rendering_last_10_commits.html"
    output_image = tmp_path / "test_full_rendering_last_10_commits.png"

    if os.path.exists(file_path):
        os.remove(file_path)

    if os.path.exists(output_image):
        os.remove(output_image)

    git_log = invoke_git_log(10)
    parsed = parse_json_output(git_log)
    data = json.dumps(parsed)
    render_html(data, file_path)

    # get the name in a correct format
    temp_name = "file://" + file_path.as_posix()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(temp_name)
        page.screenshot(path=output_image.as_posix())
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
        subprocess.call(output_image.as_posix(), shell=True)
