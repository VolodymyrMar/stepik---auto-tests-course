from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x))

    button2 = browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(10)
    browser.quit()
