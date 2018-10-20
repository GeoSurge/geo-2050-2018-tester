from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard
import unittest

"""
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
        image = self.browser.find_element_by_css_selector('img')
        if image.is_displayed():
            self.assertTrue(image.is_displayed())
            print('image displayed')
        else:
            print('image display error')

    def testSpeakerListLength(self):
        speakerList = self.browser.find_elements_by_xpath("//div[contains(@class, 'speaker')]")
        numberSpeakers = len(speakerList)
        self.assertGreater(numberSpeakers,30)
        print(numberSpeakers, "speakers appear")

    ###Speaker Bio test-WIP

    def testSpeakerBio(self):
        speakerBio = self.browser.find_element_by_xpath("//div[contains(@class, 'speaker')]")
        speakerBio.click()
        alert = self.browser.switch_to_alert()
        sleep(4)
        Alert(self.browser).accept()

    ### Add test for image comparison


class testProgram(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://2018.geo2050.org')

    def testTwoDaysAppear(self):
        programDays = self.browser.find_elements_by_class_name('program-day-title')
        numberDays = len(programDays)
        self.assertEqual(numberDays, 2)
        print("conference days", numberDays, "days")

    def testTimes(self):
        time = self.browser.find_element_by_class_name('program-section-time')
        if time.is_displayed():
            self.assertTrue(time.is_displayed())
            print("time displayed")
        else:
            print("schedule-time display error")

    ### WIP YAML data should match testSections
    def testSections(self):
    """

class testSponsors(unittest.TestCase):

    def testNumberSponsors(self):
        sponsors = self.browser.find_elements_by_xpath('')
        numberSponsors = len(sponsors)
        if numberSponsors >= 15:
            self.assertGreater(numberSponsors, 15)
            print(numberSponsors, "sponsors displayed")
        else:
            print("missing sponsors")

### def testSponsorLogo (see speaker image comparison test above)

class testSponsorshipOpportunities(unittest.TestCase):

    def testSponsorshipPDF(self):
        opportunity = self.browser.find_element_by_class_name("opportunity")
        opportunity.click()
        self.assertEqual(self.browser.current_url, "https://s3.amazonaws.com/geo2050/2018%20PREMIUM%20SPONSOR%20Description.pdf")

    def testNumberOpportunities(self):
        opportunities = self.browser.find_elements_by_class_name("opportunity")
        self.assertEqual(len(opportunities), 14)
