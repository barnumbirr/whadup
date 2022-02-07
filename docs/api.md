<a href="../whadup/core.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
# <kbd>module</kbd> `whadup`

```python
from whadup import GithubStatus

gh = GithubStatus()
```

<a href="../whadup/core.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
## <kbd>class</kbd> `GithubStatus`

<a href="../whadup/core.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
### <kbd>method</kbd> `summary`

```python
summary()
```

Get a summary of the status page, including a status indicator, component
statuses, unresolved incidents, and any upcoming or in-progress scheduled
maintenances.

**Returns:**
  A dict representation of the JSON returned by the API.

**Example:**

```python
gh.summary()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T12:35:01.608Z"
  },
  "components": [
    {
      "id": "8l4ygp009s5s",
      "name": "Git Operations",
      "status": "operational",
      "created_at": "2017-01-31T20:05:05.370Z",
      "updated_at": "2022-01-29T21:09:15.078Z",
      "position": 1,
      "description": "Performance of git clones, pulls, pushes, and associated operations",
      "showcase": false,
      "start_date": null,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    ...
  ],
  "incidents": [],
  "scheduled_maintenances": [],
  "status": {
    "indicator": "none",
    "description": "All Systems Operational"
  }
}
```
<a href="../whadup/core.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
### <kbd>method</kbd> `status`

```python
status()
```

Get the status rollup for the whole page. This endpoint includes an
indicator - one of *none*, *minor*, *major*, or *critical*, as well as a human
description of the blended component status. Examples of the blended status
include "All Systems Operational", "Partial System Outage", and "Major Service
Outage".

**Returns:**
  A dict representation of the JSON returned by the API.

**Example:**

```python
gh.status()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T12:35:01.608Z"
  },
  "status": {
    "indicator": "none",
    "description": "All Systems Operational"
  }
}
```

<a href="../whadup/core.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
### <kbd>method</kbd> `components`

```python
components()
```

Get the components for the page. Each component is listed along with its
status - one of *operational*, *degraded_performance*, *partial_outage*, or
*major_outage*.

**Returns:**
  A dict representation of the JSON returned by the API.

**Example:**

```python
gh.components()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T12:35:01.608Z"
  },
  "components": [
    {
      "id": "8l4ygp009s5s",
      "name": "Git Operations",
      "status": "operational",
      "created_at": "2017-01-31T20:05:05.370Z",
      "updated_at": "2022-01-29T21:09:15.078Z",
      "position": 1,
      "description": "Performance of git clones, pulls, pushes, and associated operations",
      "showcase": false,
      "start_date": null,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    ...
  ]
}
```

<a href="../whadup/core.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
## <kbd>class (nested)</kbd> `Incidents`

Incidents are the cornerstone of any status page, being composed of many
incident updates. Each incident usually goes through a progression of
statuses listed below, with an impact calculated from a blend of
component statuses (or an optional override).

**Status**: *Investigating*, *Identified*, *Monitoring*, *Resolved*, or
*Postmortem*

**Impact**: None (black), Minor (yellow), Major (orange), or Critical (red)

```python
Incidents()
```

Get a list of the 50 most recent incidents. This includes all unresolved
incidents as well as those in the *Resolved* and *Postmortem* state.

**Returns:**
  A dict representation of the JSON returned by the API.

```python
gh.Incidents()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T12:35:01.608Z"
  },
  "incidents": [
    {
      "id": "vvthhf8gxt80",
      "name": "Incident with GitHub Actions, GitHub Pages, and Webhooks",
      "status": "resolved",
      "created_at": "2022-02-05T22:18:24.568Z",
      "updated_at": "2022-02-06T02:01:26.937Z",
      "monitoring_at": null,
      "resolved_at": "2022-02-06T02:01:26.920Z",
      "impact": "minor",
      "shortlink": "https://stspg.io/0s9sbhvrhw1v",
      "started_at": "2022-02-05T22:18:24.560Z",
      "page_id": "kctbh9vrtdwd",
      "incident_updates": [
        {
          "id": "4dq2zh8s0lwl",
          "status": "resolved",
          "body": "This incident has been resolved.",
          "incident_id": "vvthhf8gxt80",
          "created_at": "2022-02-06T02:01:26.920Z",
          "updated_at": "2022-02-06T02:01:26.920Z",
          "display_at": "2022-02-06T02:01:26.920Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "jsykhywmvm3m",
          "status": "investigating",
          "body": "Webhooks is operating normally.",
          "incident_id": "vvthhf8gxt80",
          "created_at": "2022-02-06T01:41:19.887Z",
          "updated_at": "2022-02-06T01:41:19.887Z",
          "display_at": "2022-02-06T01:41:19.887Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "tngtv4j9d24d",
          "status": "investigating",
          "body": "GitHub Pages is operating normally.",
          "incident_id": "vvthhf8gxt80",
          "created_at": "2022-02-06T01:33:32.768Z",
          "updated_at": "2022-02-06T01:33:32.768Z",
          "display_at": "2022-02-06T01:33:32.768Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "2m5z70vx9x4l",
          "status": "investigating",
          "body": "GitHub Pages is experiencing degraded performance. We are continuing to investigate.",
          "incident_id": "vvthhf8gxt80",
          "created_at": "2022-02-05T23:38:42.708Z",
          "updated_at": "2022-02-05T23:38:42.708Z",
          "display_at": "2022-02-05T23:38:42.708Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "dxbcpqy1rnt0",
          "status": "investigating",
          "body": "GitHub Actions is experiencing degraded performance. We are still investigating and will provide an update when we have one.",
          "incident_id": "vvthhf8gxt80",
          "created_at": "2022-02-05T22:25:30.070Z",
          "updated_at": "2022-02-05T22:25:30.070Z",
          "display_at": "2022-02-05T22:25:30.070Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "s9py5mz8sy0d",
          "status": "investigating",
          "body": "We are investigating reports of degraded performance for Webhooks.",
          "incident_id": "vvthhf8gxt80",
          "created_at": "2022-02-05T22:18:24.627Z",
          "updated_at": "2022-02-05T22:18:24.627Z",
          "display_at": "2022-02-05T22:18:24.627Z",
          "affected_components": [
            {
              "code": "4230lsnqdsld",
              "name": "Webhooks",
              "old_status": "operational",
              "new_status": "operational"
            }
          ],
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        }
      ],
      "components": [
        {
          "id": "4230lsnqdsld",
          "name": "Webhooks",
          "status": "operational",
          "created_at": "2019-11-13T18:00:24.256Z",
          "updated_at": "2022-02-06T01:41:20.874Z",
          "position": 3,
          "description": "Real time HTTP callbacks of user-generated and system events",
          "showcase": false,
          "start_date": null,
          "group_id": null,
          "page_id": "kctbh9vrtdwd",
          "group": false,
          "only_show_if_degraded": false
        }
      ]
    },
    ...
  ]
}
```

<a href=".../whadup/core.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
### <kbd>staticmethod</kbd> `unresolved`

```python
unresolved()
```

Get a list of any unresolved incidents. This endpoint will only return incidents
in the *Investigating*, *Identified*, or *Monitoring* state.

**Returns:**
  A dict representation of the JSON returned by the API.

**Example:**

```python
gh.Incidents.unresolved()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T12:35:01.608Z"
  },
  "incidents": []
}
```

<a href="../whadup/core.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
## <kbd>class (nested)</kbd> `Maintenances`

Scheduled maintenances are planned outages, upgrades, or general notices
that you're working on infrastructure and disruptions may occurr. A
close sibling of Incidents, each usually goes through a progression of
statuses listed below, with an impact calculated from a blend of
component statuses (or an optional override).

**Status**: *Scheduled*, *In Progress*, *Verifying*, or *Completed*

**Impact**: *None (black)*, *Minor (yellow)*, *Major (orange)*, or
*Critical (red)*

```python
Maintenances()
```

Get a list of the 50 most recent scheduled maintenances. This includes scheduled
maintenances as well as those in the *Completed* state.

**Returns:**
  A dict representation of the JSON returned by the API.

```python
gh.Maintenances()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T15:25:08.713Z"
  },
  "scheduled_maintenances": [
    {
      "id": "6gpzw3mdnkwj",
      "name": "Sunsetting API Authentication via Query Parameters, and the OAuth Applications API",
      "status": "completed",
      "created_at": "2021-06-29T07:14:25.286Z",
      "updated_at": "2021-08-13T14:00:29.907Z",
      "monitoring_at": null,
      "resolved_at": "2021-08-13T14:00:29.892Z",
      "impact": "maintenance",
      "shortlink": "https://stspg.io/vrtrk0fyhy25",
      "started_at": "2021-06-29T07:14:25.282Z",
      "page_id": "kctbh9vrtdwd",
      "incident_updates": [
        {
          "id": "c8v1x93xjtw5",
          "status": "completed",
          "body": "The scheduled maintenance has been completed.",
          "incident_id": "6gpzw3mdnkwj",
          "created_at": "2021-08-13T14:00:29.892Z",
          "updated_at": "2021-08-13T14:00:29.892Z",
          "display_at": "2021-08-13T14:00:29.892Z",
          "affected_components": [
            {
              "code": "brv1bkgrwx7q",
              "name": "API Requests",
              "old_status": "under_maintenance",
              "new_status": "operational"
            }
          ],
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "3mq6tpklgj45",
          "status": "in_progress",
          "body": "Scheduled maintenance is currently in progress. We will provide updates as necessary.",
          "incident_id": "6gpzw3mdnkwj",
          "created_at": "2021-08-11T14:00:34.154Z",
          "updated_at": "2021-08-11T14:00:34.154Z",
          "display_at": "2021-08-11T14:00:34.154Z",
          "affected_components": [
            {
              "code": "brv1bkgrwx7q",
              "name": "API Requests",
              "old_status": "operational",
              "new_status": "under_maintenance"
            }
          ],
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "71qpnpnfyvmd",
          "status": "scheduled",
          "body": "Maintenance will begin as scheduled in 60 minutes.",
          "incident_id": "6gpzw3mdnkwj",
          "created_at": "2021-08-11T13:00:33.008Z",
          "updated_at": "2021-08-11T13:00:33.008Z",
          "display_at": "2021-08-11T13:00:33.008Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "8309j5bg0z53",
          "status": "scheduled",
          "body": "We will be removing <a href=\"https://developer.github.com/changes/2020-02-10-deprecating-auth-through-query-param/\">API Authentication via Query Parameters</a> and <a href=\"https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint\">OAuth Application API</a> during these hours as part of a planned deprecation cycle. For more information, please read our <a href=\"https://github.blog/changelog/2021-04-19-sunsetting-api-authentication-via-query-parameters-and-the-oauth-applications-api/\">blog post</a>.",
          "incident_id": "6gpzw3mdnkwj",
          "created_at": "2021-06-29T07:14:25.330Z",
          "updated_at": "2021-06-29T07:14:25.330Z",
          "display_at": "2021-06-29T07:14:25.330Z",
          "affected_components": [
            {
              "code": "brv1bkgrwx7q",
              "name": "API Requests",
              "old_status": "operational",
              "new_status": "operational"
            }
          ],
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        }
      ],
      "components": [
        {
          "id": "brv1bkgrwx7q",
          "name": "API Requests",
          "status": "operational",
          "created_at": "2017-01-31T20:01:46.621Z",
          "updated_at": "2021-11-27T23:31:00.090Z",
          "position": 2,
          "description": "Requests for GitHub APIs",
          "showcase": false,
          "start_date": null,
          "group_id": null,
          "page_id": "kctbh9vrtdwd",
          "group": false,
          "only_show_if_degraded": false
        }
      ],
      "scheduled_for": "2021-08-11T14:00:00.000Z",
      "scheduled_until": "2021-08-13T14:00:00.000Z"
    },
    ...
  ]
}
```

<a href=".../whadup/core.py#L141"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
### <kbd>staticmethod</kbd> `upcoming`

```python
upcoming()
```

Get a list of any upcoming maintenances. This endpoint will only return
scheduled maintenances still in the *Scheduled* state.

**Returns:**
  A dict representation of the JSON returned by the API.

**Example:**

```python
gh.Maintenances.upcoming()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T15:25:08.713Z"
  },
  "scheduled_maintenances": []
}
```

<a href=".../whadup/core.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>
### <kbd>staticmethod</kbd> `active`

```python
active()
```

Get a list of any active maintenances. This endpoint will only return scheduled
maintenances in the In *Progress* or *Verifying* state.

**Returns:**
  A dict representation of the JSON returned by the API.

**Example:**

```python
gh.Maintenances.active()
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2022-02-07T15:25:08.713Z"
  },
  "scheduled_maintenances": []
}
```
