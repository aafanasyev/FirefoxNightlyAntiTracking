
#
# https://wiki.mozilla.org/Security/Tracking_protection
# http://kb.mozillazine.org/Category:Preferences
#  
#

import os
from time import sleep
from selenium import __version__
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

sites = ["https://www.nu.nl/", "https://www.nos.nl/"]


print("This script capture and counts cookies. Different versions of Firefox") 
print("with different anti-tracking protection techniques enabled are used.")
print("Limitations are applied. Disk, memory, offline cache and history of") 
print("browsers are disabled. During browse session all cookies are accepted.")
print("Content of cookies is saved. However, on close browser is sanitized but")

print("Use cases:")

print("1 Firefox ESR Version 60.2.2")
print("2 Firefox Release 62.0.3")
print("3 Firefox Nightly Version 64.0a1")

print("4 Firefox ESR Version 60.2.2 with Tracking Protection")
print("5 Firefox Release 62.0.3 with Tracking Protection")
print("6 Firefox Nightly Version 64.0a1 with Tracking Protection") 
print("7 Firefox Nightly Version 64.0a1 with Tracking Protectionand and Content Blocking")

print("Experiment is about all cases above with waiting period\n for 10 minutes between each case ")

path_to_bin = os.path.dirname(os.path.realpath(__file__))
#binary = FirefoxBinary('/home/andrey/Documents/SSN/firefox-nightly/firefox')
#binary = FirefoxBinary('/home/andrey/Documents/SSN/firefox-release/firefox')
#binary = FirefoxBinary('/home/andrey/Documents/SSN/firefox-esr/firefox')
#if 




browsers = ['firefox-esr/firefox', 'firefox-release/firefox', 'firefox-nightly/firefox']

for i in browsers:
    # Firefox ESR Version 60.2.2"
    if browsers[i] == browsers[0]:
        #Case 


        path_to_browser = (('{0}/{1}').format(os.path.dirname(os.path.realpath(__file__)),browsers[i]))
        binary = FirefoxBinary(path_to_browser)
        
        profile = FirefoxProfile()

        #no tracking protection no cache, accept all cookies(Firefox 62.0.3 (64bit) default)

        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.disk_cache_ssl", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.cookie.cookieBehavior", 0)
        profile.set_preference("network.cookie.lifetimePolicy", 2)
        profile.set_preference("places.history.enabled",False)
        profile.set_preference("privacy.sanitize.sanitizeOnShutdown", True)

#profile.set_preference("privacy.trackingprotection.enabled", False)
#profile.set_preference("privacy.trackingprotection.introCount", 20)

#Nightly content blocking
profile.set_preference("privacy.trackingprotection.enabled", False)
profile.set_preference("privacy.trackingprotection.introCount", 20)

profile.set_preference("browser.contentblocking.enabled", False)
profile.set_preference("browser.contentblocking.introCount", 20)


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



options = Options()
#options.set_headless()

driver = Firefox(firefox_binary=binary, firefox_profile=profile, firefox_options=options)

print("{}: {}".format(driver.capabilities['browserName'],  driver.capabilities['browserVersion']))
print("geckodriver: {}".format(driver.capabilities['moz:geckodriverVersion']))
print("Selenium: {}".format(__version__))
print("================================")

for site in sites:
    print(site)
    driver.get(site)
    sleep (10)
    cookies = driver.get_cookies()

    print('Amount of loaded cookies: {}' .format(len(cookies)))


#FFclearCache.clear_firefox_cache(driver)
driver.close()
driver.quit()
