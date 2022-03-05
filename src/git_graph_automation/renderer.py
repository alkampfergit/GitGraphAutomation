"""
Module to render html file with all data to render the image
"""
import os


def render_html(json_content: str, out_file: str):
    """
    Accepts a json content parsed with log_parser module and render html file
    @param json_content: Content of json parsed by the log_parser module
    @param out_file: Path of the output file where this routine will write result file
    """
    with open(f'{os.path.dirname(__file__)}/output.html', 'r') as file:
        data = file.read()

    data = data.replace("***COMMITHERE***", json_content)

    with open(out_file, 'w') as file:
        data = file.write(data)
