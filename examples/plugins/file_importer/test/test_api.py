from steamship.plugin.importer import ImportRequest
from steamship.plugin.service import PluginRequest
from src.api import FileImporterPlugin
from steamship import MimeTypes

import os

__copyright__ = "Steamship"
__license__ = "MIT"

def _read_test_file(filename: str) -> str:
    folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(folder, '..', 'test_data', filename), 'r') as f:
        return f.read()

def _test_file(filename: str, expectMime: str):
    importer = FileImporterPlugin()

    file = _read_test_file(filename)
    request = PluginRequest(data=ImportRequest(url=filename))
    response = importer.run(request)

    assert(response.error is None)
    assert(response.data is not None)

    assert (response.data.data == file)
    assert (response.data.mimeType == expectMime)

def test_importer():
    _test_file('roses.txt', MimeTypes.MKD)
    _test_file('facts.txt', MimeTypes.TXT)
