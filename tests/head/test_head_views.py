# import unittest
# from django.test import Client
from django.test import TestCase
from django.urls import reverse
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread


class HeadTest(TestCase):
    def setUp(self):
        self.url = "http://localhost:8000/tests/head/sample.html"
        self.options = {
            "Ordered": "ol",
            "Unordered": "ul",
            "Custom": "p",
        }
        self.mark = ""
        self.httpd = TCPServer(("", 8000), SimpleHTTPRequestHandler)
        self.httpd.allow_reuse_address = True
        Thread(target=self.httpd.serve_forever).start()

    def test_form_ordered(self):
        resp = self.client.post(
            reverse("head"),
            {
                # You can create, an Html Offline to test it.
                "url": self.url,
                "choice": self.options.get("Ordered"),
                "mark": self.mark,
            },
        ).content
        self.assertEqual(b"<h2>Ordered Headings</h2>" in resp, True)
        self.assertEqual(b"<ol><li>" in resp, True)
        self.assertEqual(b"Create Account:" in resp, True)
        self.assertEqual(b"Video:" in resp, True)

    def test_form_unordered(self):
        resp = self.client.post(
            reverse("head"),
            {
                # You can create, an Html Offline to test it.
                "url": self.url,
                "choice": self.options.get("Unordered"),
                "mark": self.mark,
            },
        ).content
        self.assertEqual(b"<h2>Unordered Heading</h2>" in resp, True)
        self.assertEqual(b"<ul><li>" in resp, True)
        self.assertEqual(b"Create Account:" in resp, True)
        self.assertEqual(b"Video:" in resp, True)

    def test_form_custom(self):
        resp = self.client.post(
            reverse("head"),
            {
                # You can create, an Html Offline to test it.
                "url": self.url,
                "choice": self.options.get("Custom"),
                "mark": "✓",
            },
        ).content.decode()
        # print(resp)
        self.assertEqual("<h2>Custom Mark</h2>" in resp, True)
        # self.assertEqual(b"<p>\xe2\x9c\x93" in resp, True)
        self.assertEqual("<p>✓" in resp, True)
        self.assertEqual("Create Account:" in resp, True)
        self.assertEqual("Video:" in resp, True)

    def tearDown(self): 
        self.httpd.shutdown()
        self.httpd.server_close()
