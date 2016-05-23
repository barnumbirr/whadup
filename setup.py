#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
	name='whadup',
	version='0.1.2',
	url='https://github.com/mrsmn/whadup',
	download_url='https://github.com/mrsmn/whadup/archive/master.zip',
	author='Martin Simon',
	author_email='me@martinsimon.me',
	license='Apache v2.0 License',
	packages=['whadup'],
	description='A python wrapper around status.github.com',
	long_description=file('README.md','r').read(),
	keywords=['Github', 'Github status', 'API', 'wrapper'],
)