from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from os import mkdir

def pres_esc(browser):
    action = ActionChains(browser)
    action.key_down(Keys.ESCAPE)
    action.key_up(Keys.ESCAPE)
    action.perform()

def log_in(driver: Chrome):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/login"]')))
    driver.find_element(by=By.CSS_SELECTOR, value='a[href="/login"]').click()
    driver.find_element_by_id('login').send_keys("EDIT:<YOUR EMAIL HERE>")
    driver.find_element_by_id('password').send_keys("EDIT:<YOUR PASSWORD HERE>")
    driver.find_element(by=By.CLASS_NAME, value='btn btn-primary span4 block-center login-button auth').click()

def parse_html(html):
    return BeautifulSoup(html, 'html.parser')

def get_html(url, browser: Chrome, needs_login=False, already_logged_in=False):
    browser.get(url)
    browser.delete_all_cookies()
    try:
        if needs_login and not already_logged_in:
            log_in(browser)
        else:
            pres_esc(browser)
    except:
        ...
        # print(parse_html(browser.page_source))
    return browser.page_source

def get_browser():
    user_agent = UserAgent().random

    options = Options()
    options.add_argument('-headless')
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent={user_agent}')

    service = Service('EDIT:<PATH TO CHROMEDRIVER HERE>')

    return Chrome(service=service, options=options)

if __name__ == '__main__':
    logged_in = False
    browser = get_browser()
    problems_page = parse_html(get_html('https://noi.ph/past-problems/', browser))
    for problem in problems_page.find_all('a', class_='offset2'):
        problem_content = parse_html(get_html(problem['href'], browser, needs_login=True, already_logged_in=logged_in))
        logged_in = True
        mkdir(problem['href'].split("/")[-1])
        with open(f'{problem["href"].split("/")[-1]}/statement.html', 'w') as file:
            file.write(str(problem_content.find('div', class_='problem-statement')))
