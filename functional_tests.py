# from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# TODO: import modules to display the current date, and add date requirements
# to tests starting in line 40.

class NewVisitorTest(unittest.TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()

    def tearDown(self):

        self.browser.quit()

    def test_user_can_make_a_weekly_plan_and_retrieve_it_later(self):

        # a Hackbright grad hears about a new app to track her job search progress.
        # She goes to the webpage to check it out.
        self.browser.get('http://localhost:8000')

        # She notices the title and header mention weekly progress
        self.assertIn('Weekly Progress', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Weekly Progress', header_text)

        # She is invited to log some information about what she is practicing this week right away

        inputbox = self.browser.find_element_by_id('id_practice_log')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'What are you practicing this week?')

        # She types 'Reviewing Classes lectures and practicing OOP' into a text box
        row_text = 'Reviewing Classes lectures and practicing OOP'
        inputbox.send_keys(row_text)

        # She hits enter, the page updates, and "<current_date>: Reviewing Classes
        # lectures and practicing OOP" appears under the heading "Practice"

        inputbox.send_keys(Keys.ENTER)
        p_list = self.browser.find_element_by_id('id_practice_list')
        p_rows = p_list.find_elements_by_tag_name('li')
        self.assertIn(row_text, [row.text for row in p_rows])
        self.fail('Finish the test!')

        # She also sees a text box related to 'Learning'
        # She types "Working on TDD in Django" into the box and hits enter

        # As before, the page updates and now she sees both the Practice heading
        # with her previous information, as well as a new heading titled "Learning"
        # which contains only one entry - "<current_date>: Working on TDD in Django"

        # She wonders if this app will remember her information.  She refreshes
        # the page, and can still see her items.

        # Satisfied, she clicks away to take an imgur break.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
