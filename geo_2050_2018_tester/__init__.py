from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import keyboard
import unittest


class testSpeaker(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://2018.geo2050.org')

    def testSpeakerSection(self):
        speakerSection = self.browser.find_element_by_id('speakers')
        self.assertTrue(speakerSection.is_displayed())
        print("Speakers", speakerSection.size)

    def testSpeakerImage(self):
        speakerImages = self.browser.find_elements_by_css_selector('img')
        for speakerImage in speakerImages:
            self.assertTrue(speakerImage.is_displayed())
            if speakerImage.is_displayed():
                pass
            else:
                print(speakerImages.index(), "image display error")

    def testSpeakerListLength(self):
        speakerList = self.browser.find_elements_by_xpath("//div[contains(@class, 'speaker')]")
        numberSpeakers = len(speakerList)
        self.assertGreater(numberSpeakers,30)
        if len(speakerList) > 30:
            print(numberSpeakers, "speakers appear")
        else:
            print(numberSpeakers, "verify speaker list")
    """
    ###Speaker Bio test-WIP
    def testSpeakerBio(self):
        speakerBio = self.browser.find_element_by_xpath("//div[contains(@class, 'speaker')]")
        speakerBio.click()
        alert = self.browser.switch_to_alert()
        sleep(4)
        Alert(self.browser.).accept()

    ### Add test for image comparison
    """

class testProgram(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://2018.geo2050.org')

    def testTwoDaysAppear(self):
        programDays = self.browser.find_elements_by_class_name('program-day-title')
        numberDays = len(programDays)
        self.assertEqual(numberDays, 2)
        print("program displays", numberDays, "days")

    def testTimes(self):
        time = self.browser.find_element_by_class_name('program-section-time')
        self.assertTrue(time.is_displayed())
        if time.is_displayed():
            print("time displayed")
        else:
            print("schedule-time display error")
    """
    ### WIP YAML data should match testSections
    def testSections(self):
    """

class testSponsors(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://2018.geo2050.org')

    def testNumberSponsors(self):
        sponsors = self.browser.find_elements_by_css_selector('#partners-and-sponsors a')
        numberSponsors = len(sponsors)
        self.assertGreaterEqual(numberSponsors, 15)
        if numberSponsors > 15:
            print(numberSponsors, "sponsors displayed")
        else:
            print("missing sponsors")

    def testSponsorLink(self):
        sponsorLinks = self.browser.find_elements_by_css_selector('#partners-and-sponsors a')
        for sponsorLink in sponsorLinks:
            print("for link:", sponsorLink)
            sponsorLink.click()
            sleep(8)
            lastHandle = self.browser.window_handles[-1]
            self.browser.switch_to.window(lastHandle)
            #for handle in self.browser.window_handles:
            self.assertTrue(self.browser.current_url != 'https://2018.geo2050.org/')
            if self.browser.current_url != 'https://2018.geo2050.org/':
                pass
            else:
                print(sponsorLinks.index(), "broken sponsor link")
            self.browser.switch_to.window(self.browser.window_handles[0])


### def testSponsorLogo (see speaker image comparison test above)

class testSponsorshipOpportunities(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://2018.geo2050.org')

    def testSponsorshipPDF(self):
        opportunity = self.browser.find_element_by_class_name("opportunity")
        opportunity.click()
        self.assertTrue(self.browser.current_url.endswith('.pdf'))

    def testNumberOpportunities(self):
        opportunities = self.browser.find_elements_by_class_name("opportunity")
        self.assertEqual(len(opportunities), 14)
        print(len(opportunities))
