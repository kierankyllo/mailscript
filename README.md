### Basic Mailscript With Firstname Formatting

This script iterate over the csv file in the folder and sends emails to each recipient. 

It will also format the text and html message bodies with the first names of the recipients into the first {} that it encounters.

Currently it has a sleep of three seconds after each message, which can be removed if your provider does not rate limit.

#### Requires:

Python3  
SMTP account