
#
# https://wiki.mozilla.org/Security/Tracking_protection
# http://kb.mozillazine.org/Category:Preferences
#  
#

import os
import sys
from time import sleep
from selenium import __version__
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary




print("This script capture and counts cookies. Different versions of Firefox") 
print("with different anti-tracking protection techniques enabled are used.")
print("Limitations are applied. Disk, memory, offline cache and history of") 
print("browsers are disabled. During browse session all cookies are accepted.")
print("Content of cookies is saved. However, on close browser is sanitized but")

print("Use cases:")

print("1 Firefox ESR Version 60.2.2")
print("2 Firefox Release 62.0.3")
print("3 Firefox Nightly Version 64.0a1")

print("4 Firefox ESR Version 60.2.2 with Tracking Protection(TP)")
print("5 Firefox Release 62.0.3 with Tracking Protection(TP)")
print("6 Firefox Nightly Version 64.0a1 with Tracking Protection(TP)") 
print("7 Firefox Nightly Version 64.0a1 with Tracking Protectionand(TP) and Content Blocking(CB)")

print("Experiment is about all cases above with waiting period\n for 10 minutes between each case ")

path_to_bin = os.path.dirname(os.path.realpath(__file__))
#binary = FirefoxBinary('/home/andrey/Documents/SSN/firefox-nightly/firefox')
#binary = FirefoxBinary('/home/andrey/Documents/SSN/firefox-release/firefox')
#binary = FirefoxBinary('/home/andrey/Documents/SSN/firefox-esr/firefox')
#if 

# Three browsers: 
# (0)Firefox ESR Version 60.2.2
# (1)Firefox Release 62.0.3
# (2)Firefox Nightly Version 64.0a1
browsers = ["firefox-esr/firefox", "firefox-release/firefox", "firefox-nightly/firefox"]

cases = ["no TP","TP","TP and CB"]

sites = ["https://www.nu.nl/", "https://www.nos.nl/"]

def browsersProfiles(case):
    profile = FirefoxProfile()
    # no cache, accept all cookies
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.disk_cache_ssl", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.cookie.cookieBehavior", 0)
    profile.set_preference("network.cookie.lifetimePolicy", 2)
    profile.set_preference("places.history.enabled",False)
    profile.set_preference("privacy.sanitize.sanitizeOnShutdown", True)
    # No Tracking Protection
    if case == "no TP":
        # No Tracking Protection
        profile.set_preference("privacy.trackingprotection.enabled", False)
        #disable guidance
        profile.set_preference("privacy.trackingprotection.introCount", 20)
    #Tracking Protection
    elif case == "TP":
        # Tracking Protection
        profile.set_preference("privacy.trackingprotection.enabled", True)
        # Disable guidance
        profile.set_preference("privacy.trackingprotection.introCount", 20)
        # Content Blocking
        profile.set_preference("browser.contentblocking.enabled", False)
        profile.set_preference("browser.contentblocking.introCount", 20)
    elif case == "TP and CB":
        # Tracking Protection
        profile.set_preference("privacy.trackingprotection.enabled", True)
        # Disable guidance
        profile.set_preference("privacy.trackingprotection.introCount", 20)
        # Content Blocking
        profile.set_preference("browser.contentblocking.enabled", True)
        # Disable guidance
        profile.set_preference("browser.contentblocking.introCount", 20)
    return profile

def browserVersion(browser):
    path_to_bin = os.path.dirname(os.path.realpath(__file__))
    path_to_browser = (('{0}/{1}').format(path_to_bin,browser))
    binary = FirefoxBinary(path_to_browser)

    return binary

def sitesCookies(driver):
    for site in sites:
        print(site)
        driver.get(site)
        # 10 seconds to load page
        sleep (10)
        cookies = driver.get_cookies()
        print (cookies)
        #print('Amount of loaded cookies: {}' .format(len(cookies)))
        return cookies




for case in cases:
    # Case 0 no Tracking protection
    profile = browsersProfiles(case)
    if case == "no TP":
        # Browsers 
        for browser in browsers:
            binary = browserVersion(browser)
            options = Options()
            #options.set_headless()

            driver = Firefox(firefox_binary=binary, firefox_profile=profile, firefox_options=options)

            print("{}: {}".format(driver.capabilities['browserName'],  driver.capabilities['browserVersion']))
            print("geckodriver: {}".format(driver.capabilities['moz:geckodriverVersion']))
            print("Selenium: {}".format(__version__))
            print("no Tracking Protection")
            print("================================")
            #print(sitesCookies(driver))
            print('Amount of loaded cookies: {}' .format(len(sitesCookies(driver))))

            driver.close()
            driver.quit()
            #wait 10 minutes
            sleep(10)
    elif case == "TP":
        # Browsers 
        for browser in browsers:
            binary = browserVersion(browser)
            options = Options()
            #options.set_headless()

            driver = Firefox(firefox_binary=binary, firefox_profile=profile, firefox_options=options)

            print("{}: {}".format(driver.capabilities['browserName'],  driver.capabilities['browserVersion']))
            print("geckodriver: {}".format(driver.capabilities['moz:geckodriverVersion']))
            print("Selenium: {}".format(__version__))
            print("no Tracking Protection")
            print("================================")
            print(sitesCookies(driver))
            print('Amount of loaded cookies: {}' .format(len(sitesCookies(driver))))

            driver.close()
            driver.quit()
            #wait 10 minutes
            sleep(600)
    elif case == "TP and CB":
        # Browsers 
        for browser in browsers:
            binary = browserVersion(browser)
            options = Options()
            #options.set_headless()

            driver = Firefox(firefox_binary=binary, firefox_profile=profile, firefox_options=options)

            print("{}: {}".format(driver.capabilities['browserName'],  driver.capabilities['browserVersion']))
            print("geckodriver: {}".format(driver.capabilities['moz:geckodriverVersion']))
            print("Selenium: {}".format(__version__))
            print("no Tracking Protection")
            print("================================")
            print(sitesCookies(driver))
            print('Amount of loaded cookies: {}' .format(len(sitesCookies(driver))))

            driver.close()
            driver.quit()
            #wait 10 minutes
            sleep(600)
    else:
        print("No case selected")
        sys.exit()

#Nightly content blocking
#profile.set_preference("privacy.trackingprotection.enabled", False)
#profile.set_preference("privacy.trackingprotection.introCount", 20)

#profile.set_preference("browser.contentblocking.enabled", False)
#456profile.set_preference("browser.contentblocking.introCount", 20)


#Slow-loading Trackers(By default enabled)
#profile.set_preference("browser.fastblock.enabled", True)

# Block Trackers (by default on if contentblocking enabled)
#>profile.set_preference("privacy.trackingprotection.enabled", True)
# 1st default case: private 
#profile.set_preference("browser.privacy.trackingprotection.menu", "private")
#>profile.set_preference("privacy.trackingprotection.enabled", False)
# 2nd case: always
#profile.set_preference("browser.privacy.trackingprotection.menu", "always")
#profile.set_preference("privacy.trackingprotection.enabled", True)
# Disable?
#>profile.set_preference("browser.privacy.trackingprotection.menu", "private")
#>profile.set_preference("privacy.trackingprotection.enabled", False)
#profile.set_preference("privacy.trackingprotection.pbmode.enabled", False)

# Third-Party Cookies

# 1st case: Trackers(recommended):
#profile.set_preference("network.cookie.cookieBehavior", 4)
# 2nd case (All third-party cookies)
#profile.set_preference("network.cookie.cookieBehavior", 1)
# Disable:
#profile.set_preference("network.cookie.cookieBehavior", 0)

