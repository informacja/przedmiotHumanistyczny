from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FomularzTest(StaticLiveServerTestCase):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.wiek = 28
        self.plec = 'k'
        self.wyksztalcenie = 2

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def runTest(self):
        self.selenium.get("%s/wypelnij/" % self.live_server_url)
        self.selenium.find_element(By.ID, "id_wiek").send_keys(self.wiek)
        # self.selenium.find_element("id_plec").send_keys(self.plec)
        self.selenium.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        WebDriverWait(self.selenium, 2).until(lambda driver: driver.find_element_by_css_selector("#content h1"))

        # self.assertEqual("Site administration", self.selenium.find_element_by_css_selector("#content h1").text)
