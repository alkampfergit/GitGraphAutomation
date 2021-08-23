import argparse
import tempfile
import json
import subprocess
import os
from playwright.sync_api import sync_playwright
from git_graph_automation.renderer import renderHtml
from git_graph_automation.logParser import parseJsonOutput
from git_graph_automation.gitCommand import invokeGitLog

parser = argparse.ArgumentParser(description='Generates a graph with gitgraph.js of an existing commit.')
parser.add_argument('--repo', type=str, help='Path of the repo to dump')
parser.add_argument('--outhtml', type=str, help='destination html file to render.')
parser.add_argument('--renderpng', type=str, help='if specified, will use playwright to render a png of the graph')

if __name__ == '__main__':
    args = parser.parse_args()
    f = args.outhtml
    if (f == None):
        tempFile = tempfile.TemporaryFile()
        f = tempFile.name
    
    print (f'Writing output file to {f}')
    gitLog = invokeGitLog(limit=100, directory=args.repo)
    html = parseJsonOutput(gitLog)
    data = json.dumps(html) 
    renderHtml(data, f)

    if (args.renderpng != None):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f)
            page.screenshot(path=args.renderpng, full_page=True)
            browser.close()  
        
        if os.name == 'nt':
            subprocess.call(args.renderpng, shell=True)