#!/bin/bash

#set -e

echo "This script installs a Python 3 based environment (main.py) to test a new Firefox Nightly(64.0.1a) Anti-tracking approach."

OperatingSystem=$(uname -o)
HardwarePlatform=$(uname -i)


if [ $OperatingSystem != "GNU/Linux" ] || [ $HardwarePlatform != "x86_64" ];then
   echo "Only Debian-based 64-bit distributions are supported, preferably Ubunutu 18.04 LTS"
   exit 1
fi
# UPDATE operating system (OS):

sudo apt-get update; sudo apt-get upgrade -y; sudo apt-get dist-upgrade -y; sudo apt-get autoremove --purge -y; sudo apt-get autoclean -y;


# INSTALL OS packages:

sudo apt-get install -y firefox htop git python3-dev python3-pip libxml2-dev libxslt-dev libffi-dev libssl-dev build-essential xvfb libleveldb-dev libjpeg-dev sqlite3 sqlitebrowser curl wget


# Python 3 modules:
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install --upgrade selenium matplotlib pylint

# INSTALL geckodriver
sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
echo "Extracting:"
sudo tar -zxf geckodriver-v0.23.0-linux64.tar.gz --checkpoint=.100
echo "\n Done \n"
sudo mv geckodriver /usr/local/bin
sudo rm geckodriver-v0.23.0-linux64.tar.gz


# INSTALL Firefox ESR (60.2.2esr)
sudo wget https://ftp.mozilla.org/pub/firefox/releases/60.2.2esr/linux-x86_64/en-US/firefox-60.2.2esr.tar.bz2
echo "Extracting:"
sudo tar -jxf firefox-60.2.2esr.tar.bz2 --checkpoint=.100
echo "\n Done \n"
sudo rm -rf firefox-esr
sudo mv firefox firefox-esr
sudo rm firefox-60.2.2esr.tar.bz2


# INSTALL Firefox Release (62.0.3)
sudo wget https://ftp.mozilla.org/pub/firefox/releases/62.0.3/linux-x86_64/en-US/firefox-62.0.3.tar.bz2
echo "Extracting:"
sudo tar -jxf firefox-62.0.3.tar.bz2 --checkpoint=.100
echo "\n Done \n"
sudo rm -rf firefox-release
sudo mv firefox firefox-release
sudo rm firefox-62.0.3.tar.bz2

# INSTALL Firefox Nightly (64.0a1)
sudo wget https://ftp.mozilla.org/pub/firefox/nightly/latest-mozilla-central-l10n/firefox-64.0a1.en-US.linux-x86_64.tar.bz2
echo "Extracting:"
sudo tar -jxf firefox-64.0a1.en-US.linux-x86_64.tar.bz2 --checkpoint=.100
echo "\n Done \n"
sudo rm -rf firefox-nightly
sudo mv firefox firefox-nightly
sudo rm firefox-64.0a1.en-US.linux-x86_64.tar.bz2


#INSTALL Microsoft Visual Code for development (OPTIONAL)

if [[ $# -gt 1 ]]; then
    echo "Usage: install.sh [--vscode | --no-vscode]" >&2
    exit 1
fi

if [[ $# -gt 0 ]]; then
    case "$1" in
        "--vscode")
            vscode=true
            ;;
        "--no-vscode")
            vscode=false
            ;;
        *)
            echo "Usage: install.sh [--vscode | --no-vscode]" >&2
            exit 1
            ;;
    esac
else
    echo "Would you like to install Microsoft Visual Studio Code? (Only required if no other IDE is installed) [y,N]"
    read -s -n 1 response
    if [[ $response = "" ]] || [ $response == 'n' ] || [ $response == 'N' ]; then
        vscode=false
        echo "Not installing Microsoft Visual Studio Code"
    elif [ $response == 'y' ] || [ $response == 'Y' ]; then
        vscode=true
        echo "Installing Microsoft Visual Studio Code"
    else
        echo "Unrecognized response, exiting"
        exit 1
    fi
fi

if [ "$vscode" = true ]; then
    sudo wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" 
    sudo apt install code -y
    code --install-extension ms-python.python 
    code --install-extension streetsidesoftware.code-spell-checker
fi
