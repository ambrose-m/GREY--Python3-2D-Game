#!/usr/bin/env python3
import subprocess
import sys

emailMessage = '''
RESULTS OF REGRESSION TESTS: \n
Build - 
'''

# Run full build
command = 'python -m py_compile GREY.py'
buildSuccessful = True
try:
    subprocess.check_output(command, shell=True).decode('ascii')
except:
    buildSuccessful = False

if buildSuccessful:
    emailMessage += "SUCCESS\n"
else:
    emailMessage += "FAIL\n"

# Run unit tests
emailMessage += '''
Unit tests - 
'''
failedUnitTests = []                                         # keep track of failed unittests for output
unittestCommands = ['python -m unittest test_explosion.py -v', 'python -m unittest player_test.py -v', 'python -m unittest test_upgrade_anim.py -v', 'python -m unittest test_snow.py -v']
for cmd in unittestCommands:
    try:
        result = subprocess.check_output(cmd, shell=True).decode('ascii')
    except:
        failedUnitTests.append(cmd[18: -3])

if len(failedUnitTests) == 0: 
    emailMessage += "ALL PASSED\n"

else: 
    emailMessage += "TESTS FAILED: "
    for fail in failedUnitTests:
        emailMessage += fail + ", "
    emailMessage += "\n"

print(emailMessage)

# EMAIL:
import smtplib, ssl
from email.message import EmailMessage

port = 465  # For SSL
password = "regression5210"
sender = 'cpsc5210Regression@gmail.com'
receivers = sys.argv[1:]

msg = EmailMessage()
msg['Subject'] = 'Regression Testing Results'
msg['From'] = sender

msg.set_content(emailMessage)


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    for receiver in receivers:
        msg['To'] = receiver
        server.send_message(msg)