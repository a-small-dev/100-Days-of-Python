from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Driver:
    def __init__(self):
        self.chrome_options = None
        self.get_options()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.google_forms_url = "Your google form goes here"

    def get_options(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        return

    def record_data(self, data_to_record):
        self.driver.get(url=self.google_forms_url)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".whsOnd.zHQkBf")))
        for data in data_to_record:
            input_fields = self.driver.find_elements(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, ".NPEfkd.RveJvd.snByac")
            input_fields[0].send_keys(data_to_record[data]["address"])
            input_fields[1].send_keys(data_to_record[data]["cost"])
            input_fields[2].send_keys(data_to_record[data]["bedrooms"])
            input_fields[3].send_keys(data_to_record[data]["bathrooms"])
            input_fields[4].send_keys(data_to_record[data]["url"])
            submit_button.click()
            another_submission = self.driver.find_element(By.CSS_SELECTOR, ".c2gzEf a")
            another_submission.click()
        return