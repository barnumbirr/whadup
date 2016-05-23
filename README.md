<img src="https://raw.githubusercontent.com/mrsmn/whadup/master/doc/whadup.jpg" height=250 alt="whadup" title="whadup">

[![PyPi Version](http://img.shields.io/pypi/v/whadup.svg)](https://pypi.python.org/pypi/whadup/)   [![Downloads](http://img.shields.io/pypi/dm/whadup.svg)](https://pypi.python.org/pypi/whadup/)
[![Code Health](https://landscape.io/github/mrsmn/whadup/master/landscape.svg)](https://landscape.io/github/mrsmn/whadup/master)

**whadup** is an APACHE licensed library written in Python providing an easy to use wrapper around https://status.github.com.

## Installation:

From source use

	$ python setup.py install

or install from PyPi

	$ pip install whadup

## Documentation:

- **`GET /api/status.json`**
```python
>>> from whadup import GithubStatus
>>> gh = GithubStatus()
>>> gh.status()
{"status":"good","last_updated":"2015-08-29T15:59:44Z"}
```

- **`GET /api/last-message.json`**
```python
>>> gh.lastmessage()
{"status":"good","body":"Everything operating normally.","created_on":"2015-08-25T13:49:29Z"}
```

- **`GET /api/messages.json`**
```python
>>> gh.messages()
[
	{
		"status": "good", 
		"body": "Everything operating normally.", 
		"created_on": "2015-08-25T13:49:29Z"
	}, 
	{
		"status": "good", 
		"body": "Service has been restored. We continue to monitor the situation closely.", 
		"created_on": "2015-08-25T12:52:30Z"
	}, 
	{
		"status": "minor", 
		"body": "We are restoring service as we mitigate a DDoS attack. Response times may be slower while this work continues.", 
		"created_on": "2015-08-25T12:08:21Z"
	}, 
	{
		"status": "minor", 
		"body": "We are restoring service as we mitigate a DDoS attack.", 
		"created_on": "2015-08-25T11:27:21Z"
	}, 
	{
		"status": "major", 
		"body": "We are continuing to work to mitigate an ongoing DDoS attack.", 
		"created_on": "2015-08-25T11:06:09Z"
	}, 
	{
		"status": "major", 
		"body": "The connectivity problems have been identified as a DDoS attack. We're working to mitigate now.", 
		"created_on": "2015-08-25T10:38:32Z"
	}, 
	{
		"status": "minor", 
		"body": "We're continuing to diagnose reports of connectivity problems.", 
		"created_on": "2015-08-25T10:07:20Z"
	}, 
	{
		"status": "minor", 
		"body": "We are investigating reports of connectivity problems.", 
		"created_on": "2015-08-25T09:39:12Z"
	}, 
	{
		"status": "good", 
		"body": "Everything operating normally.", 
		"created_on": "2015-08-24T16:08:32Z"
	}, 
	{
		"status": "minor", 
		"body": "We're investigating a brief capacity overload. Systems are recovering.", 
		"created_on": "2015-08-24T15:58:07Z"
	}, 
	{
		"status": "minor", 
		"body": "Minor service outage.", 
		"created_on": "2015-08-24T15:47:02Z"
	}
]
```

## License:

	Apache v2.0 License
	Copyright 2015-2016 Martin Simon

	 Licensed under the Apache License, Version 2.0 (the "License");
	 you may not use this file except in compliance with the License.
	 You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

	 Unless required by applicable law or agreed to in writing, software
	 distributed under the License is distributed on an "AS IS" BASIS,
	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	 See the License for the specific language governing permissions and
	 limitations under the License.


## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
