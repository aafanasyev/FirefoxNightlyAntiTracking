# FirefoxNightlyAntiTracking
This research (September 24 - October 26, 2018) focuses on examining new anti-tracking approach of Firefox Nightly(64.0.1a) against most recent release of Firefox(62.0.3)

# Environment
For this research was used an ubuntu 18.04.1 with most recent updates. Test script is written with python 3.6.6

```
user - script - Firefox - mitmproxy
        ^                    v
       sites               logs
       list                data
```


# Installation

Python modules:
```bash
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py 
sudo python -m pip install pytest multiprocess pillow tblib selenium mini-amf bs4 publicsuffix pyvirtualdisplay tabulate plyvel boto3 pandas pyarrow s3fs psutil
```

