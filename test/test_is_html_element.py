import unittest

from pyvalidator import *
from . import print_test_ok


class TestIsHtmlElement(unittest.TestCase):

    def test_valid_html_element(self):
        for i in [
            '<div></div>',
            '<div ></ div>',
            '<    div ></ div>',
            '<div class="container"></div>',
            '<a></a>',
            '<a href=""></a>',
            '<input type="password" />',
            '<input disabled />',
            '<!DOCTYPE>',
            '<h1></h1>',
            '<h2></h2>',
            '<h3></h3>',
            '<h4></h4>',
            '<h5></h5>',
            '<h6>text</h6>',
            '<body><div></div></body>',
            '<base href="https://www.w3schools.com/" target="_blank">',
            '<img />',
            '<head></head>',
            '<label for="cars">Choose a car:</label>',
            '<p>&amp;</p>',
            '<textarea id="w3review" name="w3review" rows="4" cols="50"></textarea>',

            """
                        <style>
                            h1 {color:red;}
                            p {color:blue;}
                        </style>
                    """,

            """
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <title>Page Title</title>
                            </head>
                            <body>
                                <h1>This is a Heading</h1>
                                <p>This is a paragraph.</p>
                            </body>
                        </html>
                    """,
        ]:
            self.assertTrue(is_html_element(i))
        print_test_ok()

    def test_invalid_html_element(self):
        for i in [
            '<></>',
            '<<>></>',
            '<>',
            '<random></random>',
            '<body><body>',
            '0',
            '<h2></h1>',
            '<h3></h1>',
            '<h4></h1>',
            '<h5></h1>',
            '<h6>',
            '</h6>',
            '<h6></h6><h3></h3>',
            '<head>',
            '<img',
            '<img <>',
            '<<img <>',
            '<image />',
            '<image />',
            '<input></input>',
            '</textarea>',
            '</span>',
            '</span>',
            '<html lang="en">',
            '.',
            '',
            ' ',
            '<p>paragraph</p> some text after',
            'some text before <p>paragraph</p>',

            """
                        <style>
                            h1 {color:red;}
                            p {color:blue;}
                        <style>
                    """

        ]:
            self.assertFalse(is_html_element(i))
        print_test_ok()

    def test_valid_html_element_contains(self):
        for i in [
            'some text <p>paragraph</p>, exactly.',
            'some text <br>brake, exactly.',
            'some text <input /> input, exactly.',
        ]:
            self.assertTrue(is_html_element(i, {"contains": True}))
        print_test_ok()
