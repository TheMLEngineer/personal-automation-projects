#!/usr/bin/env python3


import time

import os

import subprocess as s

import webbrowser

def sound():
    os.system('spd-say "Really Great Job , Keep Going"')


    
def send_notification():
    s.call(['notify-send','\t\t\tAnother 30 minutes in Productivity','\t\t\t\t     Keep Hustling Champ'])


url_list_window1 = ['http://localhost:8888/tree?' , 
           'https://mail.google.com/mail/u/0/#inbox' , 
           'https://asoftmurmur.com/?lang=en']


url_list_window2 = ['https://wipro.udemy.com/organization/home/' , 
                    'https://www.coursera.org/' , 
                    'https://developers.google.com/machine-learning/crash-course' , 
                    'https://www.hackerrank.com/dashboard' , 
                   'https://codingbat.com/python' , 
                   'https://www.codingame.com/home' , 
                   'https://www.codewars.com/dashboard' , 
                   'https://www.codechef.com/' , 
                   'https://exercism.io/my/tracks' , 
                   'https://www.spoj.com/']


for link in url_list_window1:
    webbrowser.open_new_tab(link)

webbrowser.open_new('')

for link in url_list_window2:
    webbrowser.open_new_tab(link)

os.chdir('/home/karthikeyan/Documents')

f = open('test_scheduler_success.txt' , 'w+')
f.write('Success')
f.close()

while True:
    send_notification()
    sound()
    time.sleep(1800)
