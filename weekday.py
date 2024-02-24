# This program is giving you output whether today is a weekday or not.
# Resource 1: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# Resourse 2: https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,)%20to%206%20(Sunday).
 
# Author: Hyojin Kim
 
import datetime

# Use the date.weekday() method. Digits 0-6 represent the consecutive days of the week, starting from Monday.
weekno = datetime.datetime.today().weekday()


if weekno < 5: # 0 Mon , 1 Tue, 2 Wed, 3 Thur, 4 Fri
    print ("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print ("It is the weekend, yay!")