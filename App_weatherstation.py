#!/usr/bin/python

import json
import sys
import time
import datetime
from datetime import date, datetime

from json import dumps

# libraries
import sys
import urllib.request as urllib2
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from sense_emu import SenseHat

# Oauth JSON File
GDOCS_OAUTH_JSON       = 'sensehat2cloud-6738621d80d1.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'D to C'

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 10


def login_open_sheet(oauth_key_file, spreadsheet):
	"""Connect to Google Docs spreadsheet and return the first worksheet."""
	try:
		scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

		json_key = json.load(open(oauth_key_file))
		credentials = SignedJwtAssertionCredentials(json_key['client_email'],json_key['private_key'],scope)
													
													
		#below line doesn't work anymore so commented, and use the other way to authorize											
		#gc = gspread.authorize(credentials)
		#instead, use one of the 2 below lines
		#gc = gspread.service_account(filename='D:\Online Classes\edureka\Edureka materials\S3\code\iotsheets-276804-a20f837deb72.json')
		gc = gspread.service_account(GDOCS_OAUTH_JSON)
		
		worksheet = gc.open(spreadsheet).sheet1
		return worksheet
	except Exception as ex:
		print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
		print('Google sheet login failed with error:', ex)
		sys.exit(1)


sense = SenseHat()
sense.clear()		
print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None
while True:
	# Login if necessary.
	if worksheet is None:
		worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

	# Attempt to get sensor reading.
	temp = sense.get_temperature()
	temp = round(temp, 1)
	humidity = sense.get_humidity()
	humidity = round(humidity, 1)
	pressure = sense.get_pressure()
	pressure = round(pressure, 1)
	
	# 8x8 RGB
	sense.clear()
	info = 'Temperature (C): ' + str(temp) + 'Humidity: ' + str(humidity) + 'Pressure: ' + str(pressure)
	sense.show_message(info, text_colour=[255, 0, 0])
	
	# Print
	print("Temperature (C): ", temp)
	print("Humidity: ", humidity)
	print("Pressure: ", pressure, "\n")


	def json_serial(obj):
		"""JSON serializer for objects not serializable by default json code"""

		if isinstance(obj,(datetime, date)):
			return obj.isoformat()
		raise TypeError ("Type %s not serializable" % type(obj))

	# Append the data in the spreadsheet, including a timestamp
	
	worksheet.append_row((dumps(datetime.now(), default=json_serial), temp,humidity,pressure)) 



	# Wait 30 seconds before continuing
	print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
	time.sleep(FREQUENCY_SECONDS)
