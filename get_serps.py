import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
import time, os
from datetime import datetime
import csv
import sys


def get_serp_by_query(driver, query, serp_folder_path):
    """
    This function can search Google for query.
    Parameters:
    query - a string that contains the phrase that will be searched
    serp_folder_path - a path to folder where resulting serps are saved
    """
    # perform the search, because we need the location link to show
    url = f"https://google.com/search?q={query}"
    driver.get(url)
    sleep(2)
    # Access the content of the page
    htmlPage = driver.page_source
    filename = query.replace('/','')
    with open(f"{serp_folder_path}/{filename}.html", 'w', encoding='utf-8') as output:
        output.write(htmlPage)
    

def search_all_queries(queries_file_csv):
    # Set the driver path
    driverpath ='driver/chromedriver'
    chrome_options = webdriver.ChromeOptions()

    category_folder_path = queries_file_csv.split('_')[1].split('.')[0]
    serp_folder_path = str(datetime.now()).split()[0]
    
    if not os.path.isdir(category_folder_path):
        os.mkdir(f'{category_folder_path}')
    os.mkdir(f'{category_folder_path}/{serp_folder_path}')

    queries = []
    with open(queries_file_csv, 'r') as inputF:
        reader = csv.reader(inputF)
        for row in reader:
            queries.append(row[0])

    # Create a new instance of the driver for every search
    driver = webdriver.Chrome(executable_path=driverpath, options=chrome_options)
    for query in queries:
        get_serp_by_query(driver, query, f"{category_folder_path}/{serp_folder_path}")
    driver.close()

if __name__ == "__main__":
    search_all_queries(sys.argv[1]) #parameter is a path to a csv file with a query list, like 'list_Gender Identities.csv' 