# test tree rendering
import pytest


@pytest.fixture
def voila_args(notebook_directory, voila_args_extra):
    return ['--Voila.root_dir=%r' % notebook_directory, '--VoilaTest.log_level=DEBUG'] + voila_args_extra


@pytest.fixture
def voila_args_extra():
    return ['--Voila.extension_language_mapping={".xcpp": "C++11"}']


async def test_tree(fetch, token):
    response = await fetch('voila', params={'token': token}, method='GET')
    assert response.code == 200
    text = response.body.decode('utf-8')
    assert 'print.ipynb' in text, 'tree handler should render ipynb files'
    assert 'print.xcpp' in text, 'tree handler should render xcpp files (due to extension_language_mapping)'
    assert 'print.py' not in text, 'tree handler should not render .py files (due to extension_language_mapping)'
