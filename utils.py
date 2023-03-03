from selenium import webdriver
import geckodriver_autoinstaller
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By

import time
import json

def go_get_all_the_links(the_url_link="https://seshat.info/w/index.php?title=Special:AllPages"):
    geckodriver_autoinstaller.install()
    #PATH = "/home/majid/dev/selenium/"

    # /home/majid/.mozilla/firefox/qtgamvz4.default-release
    profile = webdriver.FirefoxProfile(
        '/home/majid/.mozilla/firefox/qtgamvz4.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired)
    driver.get("https://seshat.info")
    driver.implicitly_wait(5)

    login_btn = driver.find_element_by_css_selector('#mw-content-text > a:nth-child(1)')
    login_btn.click()
    time.sleep(5)

    #user_btn = driver.find_element_by_id("wpName1")
    #user_btn.send_keys("benamm")

    pass_btn = driver.find_element_by_id("wpPassword1")
    pass_btn.send_keys("5tr4%TR$")
    time.sleep(1)
    LOGIN_BTN = driver.find_element_by_id("wpLoginAttempt")
    LOGIN_BTN.click()
    time.sleep(2)
    dic_of_all = {}

    all_good_links_here = []
    last_page = False
    page_count = 0
    driver.get(the_url_link)
    #driver.get("https://seshat.info/w/index.php?title=Category:Conflict")
    while not last_page:
        #my_good_div = driver.find_element_by_id("mw-pages")
        my_good_ul = driver.find_element_by_class_name("mw-allpages-chunk")

        #html_div = my_good_div.get_attribute('innerHTML')
        html_div = my_good_ul.get_attribute('innerHTML')
        time.sleep(3)

        soup = BeautifulSoup(html_div)
        for link in soup.findAll('a'):
            a_link_0 = link.get('href')
            #a_link = a_link_0.split("=")[1]
            if "mw-pages" not in a_link_0:
                all_good_links_here.append(a_link_0)
            #print(link.get('href'))
        time.sleep(3)
        #next_button_list = driver.find_elements_by_xpath("//*[contains(text(),'Next Page')]")
        #next_button_list = driver.find_elements(By.CLASS_NAME, 'mw-allpages-nav')
        next_button_list = driver.find_elements(By.CLASS_NAME, "mw-allpages-nav")
        print(f"Length of found div is : {len(next_button_list)}")
        # Come to the bottom of the page
        next_buttons = next_button_list[1].find_elements_by_tag_name("a")


        if len(next_button_list) == 0:
            last_page = True
            break
        #next_button = next_button_list[0]
        if len(next_buttons) == 2:
            next_buttons[1].click()
            page_count+=1
        # click on the first page: 
        elif len(next_buttons) == 1 and page_count<8:
            next_buttons[0].click()
            page_count+=1
        # break out of last page
        elif len(next_buttons) == 1 and page_count >=8:
            #next_buttons[0].click()
            last_page = True
            break
    print("Alles gut.")
    return all_good_links_here


def download_the_contents_of_the_links(n, the_links_json, the_downloaded_links_json, dic_of_images_json):
    geckodriver_autoinstaller.install()
    #PATH = "/home/majid/dev/selenium/"

    # /home/majid/.mozilla/firefox/qtgamvz4.default-release
    profile = webdriver.FirefoxProfile(
        '/home/majid/.mozilla/firefox/qtgamvz4.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    with open(the_links_json, "r") as f1:
        all_good_links_here = json.load(f1)

    with open(the_downloaded_links_json, "r") as f2:
        already_downloaded_links = json.load(f2)

    # let's also keep track of images and where they are:
    with open(dic_of_images_json, "r") as f3:
        dic_of_images = json.load(f3)

    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired)
    driver.get("https://seshat.info")
    driver.implicitly_wait(5)

    login_btn = driver.find_element_by_css_selector('#mw-content-text > a:nth-child(1)')
    login_btn.click()
    time.sleep(5)

    pass_btn = driver.find_element_by_id("wpPassword1")
    pass_btn.send_keys("5tr4%TR$")
    time.sleep(1)
    LOGIN_BTN = driver.find_element_by_id("wpLoginAttempt")
    LOGIN_BTN.click()
    time.sleep(2)
    for a_link in all_good_links_here[0:n]:
        if a_link in already_downloaded_links:
            continue
        url = "https://seshat.info/w/index.php?title=" + a_link
        driver.get(url)
        time.sleep(3)
        html_content_selenium = driver.page_source
        images = driver.find_elements_by_tag_name("img")
        src_of_images_on_this_page = []
        for image in images:
            src = image.get_attribute("src")
            if "resources/assets/poweredby_mediawiki_88x31.png" in src:
                continue
            src_of_images_on_this_page.append(src)
        if src_of_images_on_this_page:
            dic_of_images[a_link] = src_of_images_on_this_page
        best_name = a_link.replace("%27", "'").replace("/", "_")
        my_file_address = "ALL_backup_html_seshat_info/" + best_name + ".html"
        with open (my_file_address, "w") as f:
            f.write(html_content_selenium)

        already_downloaded_links.append(a_link)
        with open(the_downloaded_links_json, "w") as f1:
            json.dump(already_downloaded_links, f1)
            print(len(already_downloaded_links), end=", ")

        with open(dic_of_images_json, "w") as f2:
            json.dump(dic_of_images, f2)
            print(f"images [{len(dic_of_images)}]", end=" ")
            #print(html_content)
    #print(driver.page_source)

def downlaod_all_images_from_links(images_json_file):
    geckodriver_autoinstaller.install()
    #PATH = "/home/majid/dev/selenium/"

    # /home/majid/.mozilla/firefox/qtgamvz4.default-release
    profile = webdriver.FirefoxProfile(
        '/home/majid/.mozilla/firefox/qtgamvz4.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired)
    driver.get("https://seshat.info")
    driver.implicitly_wait(5)

    login_btn = driver.find_element_by_css_selector('#mw-content-text > a:nth-child(1)')
    login_btn.click()
    time.sleep(5)

    pass_btn = driver.find_element_by_id("wpPassword1")
    pass_btn.send_keys("5tr4%TR$")
    time.sleep(1)
    LOGIN_BTN = driver.find_element_by_id("wpLoginAttempt")
    LOGIN_BTN.click()
    time.sleep(2)

    import urllib.request
    import os

    with open(images_json_file, "r") as f1:
        all_images_links_dic = json.load(f1)
    num_images = 0
    for k, v in all_images_links_dic.items():
        for num, my_image_url in enumerate(v):
            # extension
            my_extension = my_image_url.split(".")[-1]
            good_name_for_the_image = f"IMAGE_{num+1}_FOR_" + k.replace("/", "_") + my_extension
            dir_to_save = "ALL_IMAGE_BACKUPS/" + good_name_for_the_image
            #if os.path.exists(dir_to_save):
            urllib.request.urlretrieve(my_image_url, dir_to_save)
            time.sleep(3)
            num_images+=1
            print(num_images, end=", ")

