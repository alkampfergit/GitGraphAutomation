import argparse
import tempfile
import json
import subprocess
import os
from playwright.sync_api import sync_playwright
from git_graph_automation.renderer import render_html
from git_graph_automation.log_parser import parse_json_output
from git_graph_automation.git_command import invoke_git_log

parser = argparse.ArgumentParser(description='Generates a graph with gitgraph.js of an existing commit.')
parser.add_argument('--repo', type=str, help='Path of the repo to dump')
parser.add_argument('--outhtml', type=str, help='destination html file to render.')
parser.add_argument('--renderpng', type=str, help='if specified, will use playwright to render a png of the graph')
parser.add_argument('--limit', default=100, type=int, help='limit the number of commits to render')

if __name__ == '__main__':
    args = parser.parse_args()
    f = args.outhtml
    if f is None:
        tempFile = tempfile.TemporaryFile()
        f = tempFile.name

    print(f"Writing output file to {f}")
    git_log = invoke_git_log(limit=args.limit, directory=args.repo)
    html = parse_json_output(git_log, True)
    data = json.dumps(html)
    render_html(data, f)

    if args.renderpng is not None:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            file_uri = f"file://{f}"
            page.goto(file_uri)
            page.screenshot(path=args.renderpng, full_page=True)
            browser.close()

        if os.name == 'nt':
            subprocess.call(args.renderpng, shell=True)
