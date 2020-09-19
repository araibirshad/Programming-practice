# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:08:33 2020

@author: Araib Irshad
"""


#>>>>>>>>>>>INTERNET TIME<<<<<<<<<<
#uses NTPLIB query to get time from an NTP server
#option for changing ntp server
import ntplib
from time import ctime

def gettime():
    
    server = 'time.google.com'
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request(server,version=3)
   
    
    return ctime(response.tx_time)
