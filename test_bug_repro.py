from unittest import TestCase

from lxml.html import HTMLParser, fromstring


class LxmlHtmlParser(TestCase):
    def test_bug_repro(self):
        with open("test_bug_repro.html") as f:
            parser = HTMLParser(encoding="UTF-8")
            parsed_html = fromstring(f.read(), parser=parser)

            self.assertIn(
                "Did you find what you're looking for?",
                parsed_html.text_content(),
            )
