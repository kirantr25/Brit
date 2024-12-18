from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search_ifrs17(driver):
    driver.get("https://www.britinsurance.com/")

    search_icon = driver.find_element(By.CSS_SELECTOR, "[aria-label='Search']")
    search_icon.click()

    search_bar = driver.find_element(By.ID, "searchBar")
    search_bar.send_keys("IFRS 17")
    search_bar.submit()

    results = driver.find_elements(By.CSS_SELECTOR, ".search-result-item h3")

    assert len(results) == 5, f"Expected 5 results, got {len(results)}"
    assert "Interim results for the six months ended 30 June 2022" in [r.text for r in results], "Expected title not found"