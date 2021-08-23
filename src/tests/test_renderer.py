from src.git_graph_automation.renderer import render_html

def test_render_basic_capabilities(tmp_path):
    data = "string_test"
    file = tmp_path / "outfile.html"
    render_html(data, file)

    with open(file, 'r') as file:
        rendered = file.read()

    assert data in rendered
    