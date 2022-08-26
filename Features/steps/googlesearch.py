import re
import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@given(u'user is on google search page')
def launch_driver(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()));
    context.driver.get("https://google.com")
    context.driver.maximize_window()


@when(u'user executes the following query')
def step_impl(context):
    query = re.sub(r"[\n\r]"," ",context.text)
    print("this is a print from "+query.format(db_name='HR'))


@given(u'enters text to search')
def step_impl(context):
    context.driver.find_element_by_name("q").send_keys("selenium with python" + Keys.ENTER)
    time.sleep(3)


@then(u'Relavent results are displayed')
def step_impl(context):
    assert "selenium with python" in context.driver.title

@then(u'difference is {datediff}')
def step_impl(context,datediff):
    print("the date diff value is "+ datediff)
