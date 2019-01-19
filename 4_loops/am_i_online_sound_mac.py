from urllib import request
from time import sleep
import os

# A URL for a website that we expect to be available, if we are online
url = 'https://www.google.com'

seconds_to_sleep_between_checks = 3

while True:
    print('Checking if you are online...')
    try:
        # Open the URL. This will error/fail if you are not online.
        request.urlopen(url).read()
        print('You seem to be online')
        # Shout out to the user! This only works on Macs
        os.system('say hey user, you are online')
    except:
        print('You are NOT online')

    print(f'Sleeping for {seconds_to_sleep_between_checks} seconds...')
    print()
    sleep(seconds_to_sleep_between_checks)



