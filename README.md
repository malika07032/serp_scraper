# Search Engine Result Page (SERP) Scraper
Part of my work for Cred Lab (Wellesley College)

Tools and Technologies: Python, Selenium, Beautiful Soup

My Python module for scraping Google search result pages that recognizes 90% of the available search page components.

This directory contains:
1. get_serps.py - Python script, which takes a csv with a list of query phrases as a parameter, and creates a folder
                      of html files that a gathered using Selenium.
2. driver (folder) - contains a web driver, which essential to run 'get_serps.py', as it uses Selenium
3. list_Gender Identities.csv - example csv file with a list of query phrases on the topic of Gender Identities
4. serp_scraper.py - Python script, which takes a search page html file as a parameter and creates a json files with all of the information scraped from a html search page.
    
    
How to run the Python script:
    ex: python get_serps.py 'list_Gender Identities.csv'
    ex: python serp_scraper.py your_folder your_html_file.html
