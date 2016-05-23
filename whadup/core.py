#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urlparse

class GithubStatus(object):

	def __init__(self, base_url='https://status.github.com/api/'):

		self._base_url = base_url
		self._opener = urllib2.build_opener()
		self._opener.addheaders.append(('Content-Type', 'application/json'))
		self._opener.addheaders.append(('User-agent', 'whadup - python wrapper \
		around status.github.com (github.com/mrsmn/whadup)'))

	def status(self):
		url = urlparse.urljoin(self._base_url, 'status.json')
		response = self._opener.open(url).read()
		return response

	def lastmessage(self):
		url = urlparse.urljoin(self._base_url, 'last-message.json')
		response = self._opener.open(url).read()
		return response

	def messages(self):
		url = urlparse.urljoin(self._base_url, 'messages.json')
		response = self._opener.open(url).read()
		return response
