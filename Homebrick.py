#!/usr/bin/env python

import requests
import time



def main():

	googleHome = "192.168.0.13"

	while True:
		
		homeURI = "http://" + googleHome + ":8008/setup/reboot"
		headers = {'content-type':'application/json'}
		data = '{"params":"now"}'
		request = requests.post(homeURI, headers=headers, data=data)
		time.sleep(60)





if __name__ == "__main__":
	main()
