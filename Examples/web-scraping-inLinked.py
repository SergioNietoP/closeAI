from bs4 import BeautifulSoup
from selenium import webdriver

# Path to GeckoDriver executable
geckodriver_path = 'Examples/geckodriver.exe'

# URL of the profile you want to scrape
url = ""

# Create a new instance of a browser driver
driver = webdriver.Firefox(executable_path=geckodriver_path)

# Use the driver to navigate to the URL
driver.get(url)

# Get the HTML of the page
html = driver.page_source

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(html, 'html.parser')

# Now you can use BeautifulSoup to find elements on the page
# Note: LinkedIn's actual HTML structure will differ, so you'll need to inspect it and adjust your BeautifulSoup code accordingly
experience_section = soup.find(id='experience')
experience_paragraphs = experience_section.find_all('p')

for paragraph in experience_paragraphs:
    print(paragraph.get_text())

# Don't forget to close the driver when you're done with it
driver.quit()
