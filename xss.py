from playwright.sync_api import sync_playwright
import pyfiglet

with sync_playwright() as pr :
    logo = pyfiglet.figlet_format("forms")
    print(logo)
    
    url = input("Enter the url : ")
    browser = pr.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    forms = page.query_selector_all("form")
    for x in forms :
        print(x.inner_html())
