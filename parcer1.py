from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
import sys
import csv

def scrape_stock(driver, ticker_symbol):
    # build the URL of the target page
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}'

    # visit the target page
    driver.get(url)

    try:
        # wait up to 3 seconds for the consent modal to show up
        consent_overlay = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.consent-overlay')))

        # click the 'Accept all' button
        accept_all_button = consent_overlay.find_element(By.CSS_SELECTOR, '.accept-all')
        accept_all_button.click()
    except TimeoutException:
        print('Cookie consent overlay missing')

    # initialize the dictionary that will contain
    # the data collected from the target page
    stock = { 'ticker': ticker_symbol }

    # scraping the stock data from the price indicators
    regular_market_price = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketPrice"]').text
    regular_market_change = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketChange"]').text
    regular_market_change_percent = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketChangePercent"]').text \
        .replace('(', '').replace(')', '')

    stock['regular_market_price'] = regular_market_price
    stock['regular_market_change'] = regular_market_change
    stock['regular_market_change_percent'] = regular_market_change_percent


    beta = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="BETA_5Y-value"]').text
    pe_ratio = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PE_RATIO-value"]').text
    eps = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EPS_RATIO-value"]').text

    stock['beta'] = beta
    stock['pe_ratio'] = pe_ratio
    stock['eps'] = eps

    return stock

# if there are no CLI parameters
if len(sys.argv) <= 1:
    print('Ticker symbol CLI argument missing!')
    sys.exit(2)

options = Options()
options.add_argument('--headless=new')

# initialize a web driver instance to control a Chrome window
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# set up the window size of the controlled browser
driver.set_window_size(1150, 1000)

# the array containing all scraped data
stocks = []

# scraping all market securities
for ticker_symbol in sys.argv[1:]:
    stocks.append(scrape_stock(driver, ticker_symbol))

for x in range(len(stocks)):
 print(stocks[x])
# close the browser and free up the resources
driver.quit()

# extract the name of the dictionary fields
# to use it as the header of the output CSV file

csv_header = stocks[0].keys()
#
# # export the scraped data to CSV
with open('stocks.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, csv_header)
    dict_writer.writeheader()
    dict_writer.writerows(stocks)
