import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

opt_firefox = FirefoxOptions()
opt_chrome = ChromeOptions()

def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is headless mode, but you can set --browser_mode='gui'")
    parser.addoption('--browser_mode', action='store', default="chrome",
                     help="By default is headless mode, but you can set --browser_mode='firefox'")

# Параметризована фікстура для старту та закриття браузера
@pytest.fixture
def browser(request):
    browser_mode = request.config.getoption("browser_mode")
    browser_name = request.config.getoption("browser_name")
    if browser_mode == "gui":
        print(f"\nbrowser mode: {browser_mode}")
    elif browser_mode == "headless":
        opt_chrome.add_argument('--headless')
        opt_firefox.add_argument("--headless")
        print(f"\nbrowser mode: {browser_mode}")
    else:
        print("--browser_mode should be gui or headless!")

    if browser_name == "chrome":
        print(f"\nstart {browser_name} browser for test..")
        opt_chrome.add_argument('window-size=1920,1080')
        browser = webdriver.Chrome(options=opt_chrome)
    elif browser_name == "firefox":
        print(f"\nstart {browser_name} browser for test..")
        opt_firefox.add_argument('window-size=1920,1080')
        browser = webdriver.Firefox(options=opt_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()