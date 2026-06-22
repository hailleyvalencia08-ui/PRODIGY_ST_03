import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Fixture to set up and tear down browser
@pytest.fixture
def setup():
    driver = webdriver.Chrome()   # You can use Firefox() or Edge() too
    driver.maximize_window()
    driver.get("https://example.com/login")  # Replace with your demo site
    yield driver
    driver.quit()

# ✅ Positive Test Case
def test_valid_login(setup):
    setup.find_element(By.ID, "username").send_keys("validUser")
    setup.find_element(By.ID, "password").send_keys("validPass")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Dashboard" in setup.page_source

# ❌ Negative Test Cases
def test_invalid_username(setup):
    setup.find_element(By.ID, "username").send_keys("wrongUser")
    setup.find_element(By.ID, "password").send_keys("validPass")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Invalid credentials" in setup.page_source

def test_invalid_password(setup):
    setup.find_element(By.ID, "username").send_keys("validUser")
    setup.find_element(By.ID, "password").send_keys("wrongPass")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Invalid credentials" in setup.page_source

def test_empty_username(setup):
    setup.find_element(By.ID, "password").send_keys("validPass")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Please enter username" in setup.page_source

def test_empty_password(setup):
    setup.find_element(By.ID, "username").send_keys("validUser")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Please enter password" in setup.page_source

def test_both_fields_empty(setup):
    setup.find_element(By.ID, "loginBtn").click()
    assert "Please enter credentials" in setup.page_source

def test_case_sensitivity(setup):
    setup.find_element(By.ID, "username").send_keys("VALIDUSER")
    setup.find_element(By.ID, "password").send_keys("VALIDPASS")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Invalid credentials" in setup.page_source

def test_special_characters(setup):
    setup.find_element(By.ID, "username").send_keys("user!@#")
    setup.find_element(By.ID, "password").send_keys("pass!@#")
    setup.find_element(By.ID, "loginBtn").click()
    assert "Invalid credentials" in setup.page_source
