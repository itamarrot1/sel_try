from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (adjust the path to your WebDriver)
driver = webdriver.Chrome()  # Use webdriver.Firefox() for Firefox

try:
    # Open the login page
    driver.get("file:///path/to/your/login_page.html")  # Update this path

    # Wait for the page to load
    time.sleep(2)

    # Locate the username and password input fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter the username and password
    username_field.send_keys("your_username")  # Replace with your username
    password_field.send_keys("your_password")    # Replace with your password

    # Press Enter to submit the form
    password_field.send_keys(Keys.RETURN)

    # Optionally, wait to see the result
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
