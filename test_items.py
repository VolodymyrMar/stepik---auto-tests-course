import time, pytest
from selenium import webdriver

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button>0 , "Button not found."

