'''
Module to render html file with all data to render the image
'''
import os

def render_html(json_content, out_file):
    '''
    Accepts a json content parsed with log_parser module and render html file
    '''
    with open(f'{os.path.dirname(__file__)}/output.html', 'r') as file:
        data = file.read()

    data = data.replace("***COMMITHERE***", json_content)

    with open(out_file, 'w') as file:
        data = file.write(data)
