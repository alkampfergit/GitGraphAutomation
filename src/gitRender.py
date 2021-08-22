import argparse
from git_graph_automation.renderer import renderHtml
from git_graph_automation.logParser import parseJsonOutput
from git_graph_automation.gitCommand import invokeGitLog

parser = argparse.ArgumentParser(description='Generates a graph with gitgraph.js of an existing commit.')
parser.add_argument('--repo', type=str, help='Path of the repo to dump')
parser.add_argument('--outhtml', type=str, help='destination html file to render.')


if __name__ == '__main__':
    args = parser.parse_args()
    print(args.repo)
    print(args.outhtml)