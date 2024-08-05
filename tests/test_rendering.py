import os
import pytest
import re
from moffie.compositor import Page, PageOption
from moffie.main import render

@pytest.fixture
def example_page():
    doc = """
# Test page
Other Pages
---
Paragraph 1
___
Paragraph 2
***
Paragraph 3
***
Paragraph 4
    """
    return doc

@pytest.fixture
def template_dir():
    return os.path.join(os.path.dirname(__file__), "..", "templates", "base")

def appeared(text, pattern):
    return len(re.findall(pattern, text))

def test_rendering(example_page, template_dir):
    html = render(example_page, template_dir)
    assert appeared(html, "chunk-paragraph") == 5
    assert appeared(html, "\"chunk ") == 7
    assert appeared(html, "chunk-horizontal") == 1
    assert appeared(html, "chunk-vertical") == 1
    
if __name__ == "__main__":
    pytest.main()
