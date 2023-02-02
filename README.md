# Image-Scraper-CVAT Combo

A library created to scrape Google Images. Credits to [ohyicong](https://github.com/ohyicong) for the Google Image Scraper Repo. You can download the original [here](https://github.com/ohyicong/Google-Image-Scraper/archive/refs/heads/master.zip)

## Pre-requisites

1. Google Chrome
1. Selenium (pip install Selenium)
1. Pillow (pip install Pillow)

## Usage

### Image Scraper (based on [Google Image Scraper](https://github.com/ohyicong/Google-Image-Scraper/archive/refs/heads/master.zip))
This project was created to bypass Google Chrome's new restrictions on web scraping from Google Images.

To use it, define your desired parameters in main.py and run through the command line, searches with a space in the middle should have an underscore.
```
python main.py --search <search_terms> -n <no.images> -miss <no_skips>
```

### CVAT

1. CD into cvat directory
2. Get your current IP or use default localhost:3950

To get the host IP
```cmd
ipconfig
IPv4 Address = <IP>
```

3. To create the labeling web server use the command, this will allow you to set a custom URL (eg current WAN IP (123.321.12.21) or if not set it will use the default local host as shown below)
```
set CVAT_HOST=<IP>
```

To start up the docker container use the command
```
docker-compose up -d
```

Connect to the set IP (or default) to start labeling ([localhost:3950](http://localhost:3950))
```
localhost:3950
```


## Setup for image scraper

1. Open command prompt at the current repo
2. Install Dependencies using (**Bash Script**)
   ```
   setup/pip_setup_venv.bat
   ```
   or **pip**
   ```
   pip install -r setup/requirements/requirements.txt
   ```
3. Edit your desired parameters in main.py if need be
   ```
   search_keys         = Strings that will be searched for
   number of images    = Desired number of images
   headless            = Chrome GUI behaviour. If True, there will be no GUI
   min_resolution      = Minimum desired image resolution
   max_resolution      = Maximum desired image resolution
   max_missed          = Maximum number of failed image grabs before program terminates. Increase this number to ensure large queries do not exit.
   number_of_workers   = Number of sectioned jobs created. Restricted to one worker per search term and thread.
   ```
4. To search the desired "SEARCH_1" and "SEARCH_2" for 100 images the run code is below
   ```
   python main.py --search SEARCH_1 SEARCH _2 -n 100
   ```
