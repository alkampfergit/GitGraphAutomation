from src.git_graph_automation.logParser import parseJsonOutput

def test_branch_parsing():
    try:
        parseJsonOutput("")
    except Exception as exc:
        assert False, f"An exception is raised parsing a standard empty array {exc}"


