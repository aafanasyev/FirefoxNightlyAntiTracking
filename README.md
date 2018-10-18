# FirefoxNightlyAntiTracking
This research (September 24 - October 26, 2018) focuses on examining new anti-tracking approach related to cookies of Firefox Nightly(64.0.1a) against most recent Firefox ESR (60.2.2esr) and Firefox Release (62.0.3)

# Environment
For this research was used an Uuntu 18.04.1 with most recent updates. Test script is written with python 3.6.6

```
user - script - firefox
       ^   v                   
   sites   data                
```

Selenium 3.14.1 and geckodriver 0.23.0 are required.


# Installation
use ```git clone https://github.com/aafanasyev/FirefoxNightlyAntiTracking.git``` 
Get into directory and run install.sh. It has all required and optional components



Python modules:
```bash
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py 
sudo python -m pip install pytest multiprocess pillow tblib selenium mini-amf bs4 publicsuffix pyvirtualdisplay tabulate plyvel boto3 pandas pyarrow s3fs psutil
```

