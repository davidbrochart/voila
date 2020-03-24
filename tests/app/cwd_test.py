# tests the --template argument of voila
import pytest
import os


@pytest.fixture
def voila_notebook(notebook_directory):
    return os.path.join(notebook_directory, 'cwd.ipynb')


async def test_template_cwd(fetch, token):
    response = await fetch('voila', params={'token': token}, method='GET')
    html_text = response.body.decode('utf-8')
    assert 'check for the cwd' in html_text
