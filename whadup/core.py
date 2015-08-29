#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import urllib2
import urlparse

class GithubStatus(object):

	def __init__(self, base_url='https://status.github.com/api/'):

		self.base_url = base_url
		self.opener = urllib2.build_opener()
		self.opener.addheaders.append(('Content-Type', 'application/json'))

	def status(self):
		url = urlparse.urljoin(self.base_url, 'status.json')
		response = self.opener.open(url).read()
		return response

	def lastmessage(self):
		url = urlparse.urljoin(self.base_url, 'last-message.json')
		response = self.opener.open(url).read()
		return response

	def messages(self):
		url = urlparse.urljoin(self.base_url, 'messages.json')
		response = self.opener.open(url).read()
		return response
