import unittest

from pyvalidator import *


class TestIsHtmlElement(unittest.TestCase):

    def test_valid_html_element(self):
        self.assertTrue(is_html_element('<div></div>'))
        self.assertTrue(is_html_element('<div ></ div>'))
        self.assertTrue(is_html_element('<    div ></ div>'))
        self.assertTrue(is_html_element('<div class="container"></div>'))
        self.assertTrue(is_html_element('<a></a>'))
        self.assertTrue(is_html_element('<a href=""></a>'))
        self.assertTrue(is_html_element('<input type="password" />'))
        self.assertTrue(is_html_element('<input disabled />'))
        self.assertTrue(is_html_element('<!DOCTYPE>'))
        self.assertTrue(is_html_element('<h1></h1>'))
        self.assertTrue(is_html_element('<h2></h2>'))
        self.assertTrue(is_html_element('<h3></h3>'))
        self.assertTrue(is_html_element('<h4></h4>'))
        self.assertTrue(is_html_element('<h5></h5>'))
        self.assertTrue(is_html_element('<h6>text</h6>'))
        self.assertTrue(is_html_element('<body><div></div></body>'))
        self.assertTrue(is_html_element('<base href="https://www.w3schools.com/" target="_blank">'))
        self.assertTrue(is_html_element('<img />'))
        self.assertTrue(is_html_element('<head></head>'))
        self.assertTrue(is_html_element('<label for="cars">Choose a car:</label>'))
        self.assertTrue(is_html_element('<p>&amp;</p>'))
        self.assertTrue(is_html_element('<textarea id="w3review" name="w3review" rows="4" cols="50"></textarea>'))
        self.assertTrue(is_html_element("""
            <style>
                h1 {color:red;}
                p {color:blue;}
            </style>
        """))
        self.assertTrue(is_html_element("""
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
        """))
        print('OK - test_valid_html_element')

    def test_invalid_html_element(self):
        self.assertFalse(is_html_element('<></>'))
        self.assertFalse(is_html_element('<<>></>'))
        self.assertFalse(is_html_element('<>'))
        self.assertFalse(is_html_element('<random></random>'))
        self.assertFalse(is_html_element('<body><body>'))
        self.assertFalse(is_html_element('0'))
        self.assertFalse(is_html_element('<h2></h1>'))
        self.assertFalse(is_html_element('<h3></h1>'))
        self.assertFalse(is_html_element('<h4></h1>'))
        self.assertFalse(is_html_element('<h5></h1>'))
        self.assertFalse(is_html_element('<h6>'))
        self.assertFalse(is_html_element('</h6>'))
        self.assertFalse(is_html_element('<h6></h6><h3></h3>'))
        self.assertFalse(is_html_element('<head>'))
        self.assertFalse(is_html_element('<img'))
        self.assertFalse(is_html_element('<img <>'))
        self.assertFalse(is_html_element('<<img <>'))
        self.assertFalse(is_html_element('<image />'))
        self.assertFalse(is_html_element('<image />'))
        self.assertFalse(is_html_element('<input></input>'))
        self.assertFalse(is_html_element('</textarea>'))
        self.assertFalse(is_html_element('</span>'))
        self.assertFalse(is_html_element('</span>'))
        self.assertFalse(is_html_element('<html lang="en">'))
        self.assertFalse(is_html_element('.'))
        self.assertFalse(is_html_element(''))
        self.assertFalse(is_html_element(' '))
        self.assertFalse(is_html_element('<p>paragraph</p> some text after'))
        self.assertFalse(is_html_element('some text before <p>paragraph</p>'))
        self.assertFalse(is_html_element("""
            <style>
                h1 {color:red;}
                p {color:blue;}
            <style>
        """))
        print('OK - test_invalid_html_element')

    def test_valid_html_element_contains(self):
        self.assertTrue(is_html_element('some text <p>paragraph</p>, exactly.', { "contains": True }))
        self.assertTrue(is_html_element('some text <br>brake, exactly.', { "contains": True }))
        self.assertTrue(is_html_element('some text <input /> input, exactly.', { "contains": True }))
        print('OK - test_valid_html_element_contains')
