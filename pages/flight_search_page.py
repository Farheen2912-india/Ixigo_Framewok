from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class FlightSearchPage(BasePage):

    FROM_FIELD = (By.XPATH,"//*[@data-testid='originId']")
    FROM_INPUT = (By.XPATH,"//input[contains(@class,'!pt-5')]")
    FROM_SUGGESTION = (By.XPATH,"//span[normalize-space()='BOM']/parent::*")
    TO_FIELD = (By.XPATH,"//*[@data-testid='destinationId']")
    TO_INPUT = (By.XPATH,"//input[contains(@class,'!pt-5')]")
    TO_SUGGESTION = (By.XPATH,"(//*[contains(text(),'New Delhi')])[2]")
    DEPARTURE_DATE = (By.XPATH,"//p[@data-testid='departureDate']")
    SEARCH_BUTTON = (By.XPATH,"//button[contains(text(),'Search')]")
    RESULT_PAGE = (By.XPATH,"//h1[contains(text(),'Flights')]")

    def enter_from_location(self, city):
        origin = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.FROM_FIELD)) #Wait until From field is present
        self.driver.execute_script("arguments[0].click();",origin) #Click it using JavaScript

        input_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.FROM_INPUT))  #Wait for input box
        input_box.clear()               #Removes previous value.
        input_box.send_keys(city)       #Enter city name.

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.FROM_SUGGESTION)).click() #Wait for suggestion then Select suggestion.

    def enter_to_location(self, city):

        destination = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(self.TO_FIELD))
        self.driver.execute_script("arguments[0].click();",destination)

        input_box = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.TO_INPUT))
        input_box.clear()
        input_box.send_keys(city)

        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.TO_SUGGESTION)).click()
        selected = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.TO_FIELD))
        print("Selected To:", selected.text)

    def click_departure_date(self):

        date = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.DEPARTURE_DATE))
        date.click()
        print("Departure date clicked")

    def click_search(self):

        search = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search.click()
        print("Search button clicked")

    def verify_search_results(self):

        result = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.RESULT_PAGE))
        print("Search Result Page Displayed:", result.text)
        return result.is_displayed()
