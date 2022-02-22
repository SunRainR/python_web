from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=r'/home/tarena/桌面/web/chromedriver')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('to_do', self.browser.title)
        self.fail('finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
