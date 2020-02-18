# TinderBot
Tinder automate swipe.

### Getting Started
 - download chromedriver, unzip, move to `/usr/local/bin`
 - `virtualenv -p python3 venv`
 - `source venv/bin/activate`
 - `pip install -r requirements.txt`


- create a config_local.py file with variables:
  ``` 
   fb_email = 'your_email'
   fb_password = 'your_password'
   negitive_filter = ['instagram', 'insta', 'ig', 'follow']
   positive_filter = ['foodie', 'sports']
  ```

  Note : Add things you hate and things you love in a tinder bio to negitive_filter and positive_filter


### Runing the Bot
 - `python run.py`
 
 Original repository : https://github.com/aj-4/tinder-swipe-bot
