# FirefoxNightlyAntiTracking
This research (September 24 - October 26, 2018) focuses on examining new anti-tracking approach of Firefox Nightly(64.0.1a) against most recent release of Firefox(62.0.3)

# Environment
For this research was used an ubuntu 18.04.1 with most recent updates. OpenWPM works better with python 2.7.+

```
user - script - Firefox - mitmproxy
        ^                    v
       sites               logs
       list                data
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
sudo python get-pip.py 
sudo python -m pip install pytest multiprocess pillow tblib selenium mini-amf bs4 publicsuffix pyvirtualdisplay tabulate plyvel boto3 pandas pyarrow s3fs psutil
```

