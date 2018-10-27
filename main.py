#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Andrey Afanasyev"
__copyright__ = "Copyright 2018, FirefoxNightlyAntiTracking"
__license__ = "MIT"
__version__ = "0.0.2"
__email__ = "aafanasyev@os3.nl"
__status__ = "Prototype"



#
# https://wiki.mozilla.org/Security/Tracking_protection
# http://kb.mozillazine.org/Category:Preferences
#  

import os
import sys
import csv
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

print("Use usecases:")

print("1 Firefox ESR Version 60.2.2")
print("2 Firefox Release 62.0.3")
print("3 Firefox Nightly Version 64.0a1")

print("4 Firefox ESR Version 60.2.2 with Tracking Protection(TP)")
print("5 Firefox Release 62.0.3 with Tracking Protection(TP)")
print("6 Firefox Nightly Version 64.0a1 with Tracking Protection(TP)") 
print("7 Firefox Nightly Version 64.0a1 with Tracking Protectionand(TP) and Content Blocking(CB)")

print("Experiment is about all usecases above with waiting period\n for 10 minutes between each usecase ")


path_to_bin = os.path.dirname(os.path.realpath(__file__))
# Three browsers: 
# (0)Firefox ESR Version 60.2.2
# (1)Firefox Release 62.0.3
# (2)Firefox Nightly Version 64.0a1
browsers = ["firefox-esr/firefox", "firefox-release/firefox", "firefox-nightly/firefox"]
usecases = ["no TP","TP","TP and CB"]
sites = ["https://www.nu.nl/", "https://www.nos.nl/"]
experiments = 10
path_csv = "results.csv"

def browsersProfiles(usecase):
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
    # Tracking Protection
    if usecase == "TP":
        profile.set_preference("privacy.trackingprotection.enabled", True)
        # Disable guidance
        profile.set_preference("privacy.trackingprotection.introCount", 20)
        # Content Blocking
        profile.set_preference("browser.contentblocking.enabled", False)
        profile.set_preference("browser.contentblocking.introCount", 20)
    #Tracking Protection and Content Blocking
    elif usecase == "TP and CB":
        # Tracking Protection
        profile.set_preference("privacy.trackingprotection.enabled", True)
        # Disable guidance
        profile.set_preference("privacy.trackingprotection.introCount", 20)
        # Content Blocking
        profile.set_preference("browser.contentblocking.enabled", True)
        # Disable guidance
        profile.set_preference("browser.contentblocking.introCount", 20)
    # No Tracking Protection
    elif usecase == "no TP":
        profile.set_preference("privacy.trackingprotection.enabled", False)
        #disable guidance
        profile.set_preference("privacy.trackingprotection.introCount", 20)
        # Content Blocking
        profile.set_preference("browser.contentblocking.enabled", False)
        profile.set_preference("browser.contentblocking.introCount", 20)
    else:
        pass
    return profile

def browserBinary(browser):
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

def browserSession(binary, profile, usecase, experiment):
    #binary = browserBinary(browser)
    options = Options()
    #options.set_headless()

    driver = Firefox(firefox_binary=binary, firefox_profile=profile, options=options)

    print("{}: {}".format(driver.capabilities['browserName'],  driver.capabilities['browserVersion']))
    print("geckodriver: {}".format(driver.capabilities['moz:geckodriverVersion']))
    print("Selenium: {}".format(__version__))
    if usecase == "no TP":
        print("no Tracking Protection")
    elif usecase == "TP":
        print("Tracking Protection")
    elif usecase == "TP and CB":
        print("Tracking Protectionand and Content Blocking")
    print("================================")

    for site in sites:
        print(site)
        driver.get(site)
        # 10 seconds to load page
        sleep (10)
        cookies = driver.get_cookies()
        #print (cookies)
        print('Amount of loaded cookies: {}' .format(len(cookies)))
        print(experiment)
        write_measurements(path_csv, experiment, usecase, driver.capabilities['browserName'], driver.capabilities['browserVersion'], site, len(cookies))

    driver.close()
    driver.quit()
    #wait 10 minutes
    sleep(10)

def write_measurements(path_csv, experiment, usecase, browserName, browserVersion, site, cookiesAmount):
#writing results in to CSV
    if ((not os.path.isfile(path_csv)) or (os.path.isfile(path_csv) and os.stat(path_csv).st_size==0) and (experiment == 0)):
        with open(path_csv, 'w', encoding='utf-8') as results:
            writer = csv.writer(results)
            fields = ['Experiment', 'Use case', 'Browser Name', 'Browser Version', 'site', 'Amount of loaded cookies']
            writer.writerow(fields)

        with open(path_csv, 'a+', encoding='utf-8') as results:
            writer = csv.writer(results)
            fields = [experiment, usecase, browserName, browserVersion, site, cookiesAmount]
            writer.writerow(fields)
    else:
        with open(path_csv, 'a+', encoding='utf-8') as results:
            writer = csv.writer(results)
            fields = [experiment, usecase, browserName, browserVersion, site, cookiesAmount]
            writer.writerow(fields)

for experiment in range(experiments):
    for usecase in usecases:
        # usecase 0 no Tracking protection
        #profile = browsersProfiles(usecase)
        if usecase == "TP":
            # Browsers 
            for browser in browsers:
                #print("no Tracking Protection")
                browserSession(browserBinary(browser), browsersProfiles(usecase), usecase, experiment)

        elif usecase == "TP and CB":
            # Browsers 
            for browser in browsers:
                #print("Tracking Protectionand and Content Blocking")
                if browser == "firefox-nightly/firefox":
                    browserSession(browserBinary(browser), browsersProfiles(usecase), usecase, experiment)
                else:
                    pass
        elif usecase == "no TP":
            # Browsers 
            for browser in browsers:
                #print("no Tracking Protection")
                browserSession(browserBinary(browser), browsersProfiles(usecase), usecase, experiment)
        
        else:
            print("No usecase selected")
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
# 1st default usecase: private 
#profile.set_preference("browser.privacy.trackingprotection.menu", "private")
#>profile.set_preference("privacy.trackingprotection.enabled", False)
# 2nd usecase: always
#profile.set_preference("browser.privacy.trackingprotection.menu", "always")
#profile.set_preference("privacy.trackingprotection.enabled", True)
# Disable?
#>profile.set_preference("browser.privacy.trackingprotection.menu", "private")
#>profile.set_preference("privacy.trackingprotection.enabled", False)
#profile.set_preference("privacy.trackingprotection.pbmode.enabled", False)

# Third-Party Cookies

# 1st usecase: Trackers(recommended):
#profile.set_preference("network.cookie.cookieBehavior", 4)
# 2nd usecase (All third-party cookies)
#profile.set_preference("network.cookie.cookieBehavior", 1)
# Disable:
#profile.set_preference("network.cookie.cookieBehavior", 0)
