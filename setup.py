# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='whadup',
    version='0.2.0',
    author='Martin Simon',
    author_email='me@martinsimon.me',
    description='A python wrapper around githubstatus.com.',
    keywords=['Github', 'Github status', 'API', 'wrapper', 'api'],
    url='https://github.com/barnumbirr/whadup',
    download_url='https://github.com/barnumbirr/whadup/archive/refs/heads/master.zip',
    packages=['whadup'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
)
