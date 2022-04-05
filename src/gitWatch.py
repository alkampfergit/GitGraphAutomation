import argparse
import json

from flask import Flask
from flask_cors import cross_origin

from git_graph_automation.git_command import invoke_git_log
from git_graph_automation.log_parser import parse_json_output

parser = argparse.ArgumentParser(description='Generates a graph with gitgraph.js of an existing commit.')
parser.add_argument('--repo', type=str, help='Path of the repo to dump')
parser.add_argument('--port', default=10000, type=int, help='Port to listen')
parser.add_argument('--limit', default=100, type=int, help='limit the number of commits to render')

args = parser.parse_args()
app = Flask(__name__)

print(f"monitoring folder {args.repo} with maximum number of commit {args.limit}")


@app.route('/data', methods=['GET'])
@cross_origin()
def data():
    git_log = invoke_git_log(limit=args.limit, directory=args.repo)
    html = parse_json_output(git_log)
    json_data = json.dumps(html)
    return json_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
