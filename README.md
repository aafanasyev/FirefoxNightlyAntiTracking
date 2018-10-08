# FirefoxNightlyAntiTracking
This research (September 24 - October 26, 2018) focuses on examining new anti-tracking approach of Firefox Nightly by using OpenWPM framework.

# Environment
For this research was used an ubuntu 18.04.1 with most recent updates. OpenWPM works better with python 2.7.+

```
user - OpenWrt - Firefox - mitmproxy
```


# Installation

Before installation  OpenWPM following packages should be installed:

```bash
apt update && apt upgrade -y && apt dist-upgrade -y && apt autoremove --purge -y && apt autoclean -y
sudo apt install python python-pip npm
``` 

Python modules:
```bash
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py 
sudo python3 -m pip install pytest multiprocess pillow tblib selenium mini-amf bs4 publicsuffix pyvirtualdisplay tabulate plyvel boto3 pandas pyarrow s3fs psutil
```

Clone, extract and install some requirements of OpenWPM
```bash
git clone https://github.com/citp/OpenWPM.git
cd OpenWPM/
~/OpenWPM$ ls
automation      __init__.pyc        requirements-dev.txt
CHANGELOG       install-dev.sh      requirements.txt
demo.py         install-mac-dev.sh  run-on-osx-via-docker.sh
Dockerfile      install.sh          setup.cfg
Dockerfile-dev  LICENSE             test
firefox-bin     __pycache__         VERSION
__init__.py     README.md

sudo python3 -m pip install -r requirements-dev.txt
sudo sh install-dev.sh
```

Run tests:
```bash
:~/OpenWPM/test$ ls
conftest.py      __pycache__                      test_js_instrument.py
expected.py      pytest.ini                       test_pages
__init__.py      test_crawl.py                    test_profile.py
__init__.pyc     test_custom_function_command.py  test_simple_commands.py
manual_test.py   test_env.py                      test_storage_vectors.py
openwpmtest.py   test_extension.py                utilities.py
openwpmtest.pyc  test_http_instrumentation.py     utilities.pyc
:~/OpenWPM/test$ py.test -vv
```

Output:

