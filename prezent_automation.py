from asyncio import timeout

from select import select
from seleniumbase import BaseCase
import time

class PrezentAutomation(BaseCase):

    def login(self):
        self.open("https://prezent-uatstaging.myprezent.com/signin")
        self.type("input[id='username']", "engg_user.noreply@prezent.ai")
        self.click("button[id='continue']")
        self.type("input[id='password']", "kiqjemkh")
        self.click("button[id='submit']")
        self.assert_element("div[name='profile-icon']", timeout=30)

    def task1(self):
        self.login()
        self.click("div[name='profile-icon']")
        self.click("[id='templates-tab']")

        self.wait_for_element(".templateNameAndShare__content > div", timeout=30)
        templates = self.find_elements(".templateNameAndShare__content > div")
        template_names = sorted([template.text for template in templates])
        print("First five templates in alphabetical order:", template_names[:5])

        active_template = self.find_element("//button[@data-pendo-id='selected-template']/parent::div/div/div/div/div")
        print("Current active template:", active_template.text)

        self.click("[id='basics-tab']")
        self.click("[data-pendo-id='profile-left-panel'] > .log-out-button")

    def task2(self):
        self.login()
        self.click("div[name='profile-icon']")
        self.click("[id='fingerprint-tab']")

        self.click("[data-pendo-id='fingerprint-retake']")

        self.wait_for_element("#discover", timeout=30)
        self.click("#discover")
        for i in range(0,6):
            self.click(".images-wrapper> div:nth-child(1)")
            self.wait(1)

        self.click(".selection:nth-child(1)")
        self.click("#show-fingerprint-for-btn--auto")

        for i in range(0,2):
            self.click(".cards:nth-child(1)")
            self.click("#show-fingerprint-for-btn--auto")
            self.wait(1)

        self.click(".selections:nth-child(1)")
        self.click("#show-fingerprint-for-btn--auto")
        self.wait(1)

        self.click(".cards-wrapper:nth-child(1)")
        self.click("#show-fingerprint-for-btn--auto")
        self.wait(1)

        self.click("[placeholder='Job Title']")
        self.click_xpath("//*[contains(text(),'Access Analyst')]")
        self.click("#show-fingerprint-for-btn--auto")

        self.type("#name-input-0", text="Automation")
        self.type("#lastname-input-0", text="Testing")
        self.type("#email-input-0", text="automationtesting@testing.com")
        self.click(".next-button > span")

        self.wait_for_element("//*[contains(text(),'View my fingerprint')]", timeout=60)
        self.click("//*[contains(text(),'View my fingerprint')]")

        self.wait_for_element("//*[contains(text(),'Back to Prezent')]", timeout=60)
        self.click_xpath("//*[contains(text(),'Back to Prezent')]")
        self.click("div[name='profile-icon']")
        self.click("[data-pendo-id='profile-left-panel'] > .log-out-button")

    def task3(self):
        self.login()
        self.click("[data-pendo-id='left-sidebar-generate']")
        self.click("[data-pendo-id='generate-propmt']")
        suggested_options = self.find_elements(".promptDropdown > div")
        if len(suggested_options) >= 3:
            suggested_options[2].click()
            print("Selected 3rd suggested example:", suggested_options[2].text)

        self.click("[data-pendo-id='generate-btn']")
        self.wait_for_text("Smart Layout", timeout=120)
        self.click("[name='favorite-icon']")
        self.click_xpath("//span[contains(text(),'Add to Favorites')]")
        self.wait_for_text("Added to Favorites", timeout=60)
        self.click(".generateActionModalContainer > .closeIconContainer")

        self.click("[name='download-icon']")
        self.click(".download-actions > .downloadPreferences")
        self.click("#download-btn-from-list")

        self.wait_for_element("div[name='profile-icon']", timeout=60)
        self.click("div[name='profile-icon']")
        self.click("[data-pendo-id='profile-left-panel'] > .log-out-button")

    def test_run_all_tasks(self):
        self.task1()
        self.task2()
        self.task3()
