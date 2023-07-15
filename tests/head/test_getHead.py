import unittest
import requests

from head.getHead import Medium, logger
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread

logger.disabled = True

class MediumTest(unittest.TestCase):
    def setUp(self):
        self.httpd = TCPServer(("", 8000), SimpleHTTPRequestHandler)
        self.httpd.allow_reuse_address = True
        Thread(target=self.httpd.serve_forever).start()

        self.url = "http://localhost:8000/tests/head/sample.html"
        self.options = {
            "Ordered": "ol",
            "Unordered": "ul",
            "Custom": "p",
        }
        self.mark = ""
        # logger.disabled = True
        self.med = Medium(self.url, '')

    def test_empty_url(self):
        # med = Medium('', '')
        # self.assertRaises(ValueError, Medium, "", "")
        with self.assertRaises(ValueError) as err:
            Medium("", "")
        self.assertEqual(str(err.exception), "Please provide URL, it is empty!.")

        with self.assertRaises(TypeError) as err:
            Medium([], "")
        self.assertEqual(str(err.exception), "Please provide URL string.")

        with self.assertRaises(requests.exceptions.MissingSchema) as err:
            Medium("*", "")
        self.assertEqual(str(err.exception), "Invalid URL '*': No scheme supplied. Perhaps you meant https://*?")

    def test_html_generate(self):
        actual = self.med.htmlGenerate()
        expected = ["<a href=http://localhost:8000/tests/head/sample.html#28b3'>Create Account:</a>", "<a href=http://localhost:8000/tests/head/sample.html#959b'>Settings.py.</a>", "<a href=http://localhost:8000/tests/head/sample.html#cc63'>Clone Repo:</a>", "<a href=http://localhost:8000/tests/head/sample.html#f7df'>Install requirements:</a>", "<a href=http://localhost:8000/tests/head/sample.html#718d'>Create Web App:</a>", "<a href=http://localhost:8000/tests/head/sample.html#c261'>Database Setup:</a>", "<a href=http://localhost:8000/tests/head/sample.html#7972'>Video:</a>"]
        self.assertEqual(actual, expected, "Make sure it returns list with links")
    
    def test_plain_print(self):
        actual = self.med.plainPrint()
        expected = """Create Account: #28b3\nSettings.py. #959b\nClone Repo: #cc63\nInstall requirements: #f7df\nCreate Web App: #718d\nDatabase Setup: #c261\nVideo: #7972"""
        self.assertEqual(actual, expected, "Make sure it returns Title and link")

    def test_formatted_html(self):
        actual = self.med.formattedHtml(mark="", type_order="ul")
        expected = """<ul><li><a href=http://localhost:8000/tests/head/sample.html#28b3>Create Account:</a></li> <li><a href=http://localhost:8000/tests/head/sample.html#959b>Settings.py.</a></li> <li><a href=http://localhost:8000/tests/head/sample.html#cc63>Clone Repo:</a></li> <li><a href=http://localhost:8000/tests/head/sample.html#f7df>Install requirements:</a></li> <li><a href=http://localhost:8000/tests/head/sample.html#718d>Create Web App:</a></li> <li><a href=http://localhost:8000/tests/head/sample.html#c261>Database Setup:</a></li> <li><a href=http://localhost:8000/tests/head/sample.html#7972>Video:</a></li></ul>"""
        self.assertEqual(actual, expected, "It should contain HTML lists. <type_order>")

    def tearDown(self):
        self.httpd.shutdown()
        self.httpd.server_close()


if __name__ == "__main__":
    unittest.main()