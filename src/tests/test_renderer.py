import pytest
import os
import json
from src.git_graph_automation.renderer import renderHtml

def test_render_basic_capabilities(tmp_path):
    data = "string_test"
    file = tmp_path / "outfile.html"
    renderHtml(data, file)

    with open(file, 'r') as file:
        rendered = file.read()

    assert data in rendered
    