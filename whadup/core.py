# -*- coding: utf-8 -*-

import json
import requests

class GithubStatus:

    def __init__(self):
        from . import API_BASE_URL, API_VERSION
        self.api_base_url = API_BASE_URL
        self.api_base_url += f"{API_VERSION}/"

    def _request(self, method, path, params=None, payload=None):
        params = params or {}

        response = requests.request(
            method,
            self.api_base_url + path,
            params=params,
            data=json.dumps(payload) if payload else payload,
            headers={
                "User-Agent": f"whadup - github.com/barnumbirr/whadup",
                "Content-Type": "application/json"},
        )

        response.encoding = "utf-8"
        return response.json()

    def _get(self, path, params=None):
        """ Read API resources. """
        return self._request('GET', path, params=params)

    def _post(self, path, params=None, payload=None):
        """ Create new API resources. """
        return self._request('POST', path, params=params, payload=payload)

    def _put(self, path, params=None, payload=None):
        """ Modify existing API resources. """
        return self._request('PUT', path, params=params, payload=payload)

    def _delete(self, path, params=None, payload=None):
        """ Remove API resources. """
        return self._request('DELETE', path, params=params, payload=payload)

    def summary(self, **kwargs):
        """
        Get a summary of the status page, including a status indicator,
        component statuses, unresolved incidents, and any upcoming or
        in-progress scheduled maintenances.

        Returns:
            A dict representation of the JSON returned by the API.
        """
        return self._get("summary.json", kwargs)

    def status(self, **kwargs):
        """
        Get the status rollup for the whole page. This endpoint includes an
        indicator - one of none, minor, major, or critical, as well as a human
        description of the blended component status. Examples of the blended
        status include "All Systems Operational", "Partial System Outage", and
        "Major Service Outage".

        Returns:
            A dict representation of the JSON returned by the API.
        """
        return self._get("status.json", kwargs)


    def components(self, **kwargs):
        """
        Get the components for the page. Each component is listed along with its
         status - one of operational, degraded_performance, partial_outage, or
         major_outage.

        Returns:
            A dict representation of the JSON returned by the API.
        """
        return self._get("components.json", kwargs)

    class Incidents:
        """
        Incidents are the cornerstone of any status page, being composed of many
        incident updates. Each incident usually goes through a progression of
        statuses listed below, with an impact calculated from a blend of
        component statuses (or an optional override).

        Status: Investigating, Identified, Monitoring, Resolved, or Postmortem

        Impact: None (black), Minor (yellow), Major (orange), or Critical (red)
        """

        def __new__(cls, **kwargs):
            """
            Get a list of the 50 most recent incidents. This includes all
            unresolved incidents as well as those in the Resolved and Postmortem
            state.

            Returns:
                A dict representation of the JSON returned by the API.
            """
            return GithubStatus()._get("incidents.json", kwargs)

        @staticmethod
        def unresolved(**kwargs):
            """
            Get a list of any unresolved incidents. This endpoint will only
            return incidents in the Investigating, Identified, or Monitoring
            state.

            Returns:
                A dict representation of the JSON returned by the API.
            """
            return GithubStatus()._get("incidents/unresolved.json", kwargs)

    class Maintenances:
        """
        Scheduled maintenances are planned outages, upgrades, or general notices
        that you're working on infrastructure and disruptions may occurr. A
        close sibling of Incidents, each usually goes through a progression of
        statuses listed below, with an impact calculated from a blend of
        component statuses (or an optional override).

        Status: Scheduled, In Progress, Verifying, or Completed

        Impact: None (black), Minor (yellow), Major (orange), or Critical (red)
        """

        def __new__(cls, **kwargs):
            """
            Get a list of the 50 most recent scheduled maintenances. This
            includes scheduled maintenances as well as those in the Completed
            state.

            Returns:
                A dict representation of the JSON returned by the API.
            """
            return GithubStatus()._get("scheduled-maintenances.json", kwargs)

        @staticmethod
        def upcoming(**kwargs):
            """
            Get a list of any upcoming maintenances. This endpoint will only
            return scheduled maintenances still in the Scheduled state.

            Returns:
                A dict representation of the JSON returned by the API.
            """
            return GithubStatus()._get("scheduled-maintenances/upcoming.json", kwargs)

        @staticmethod
        def active(**kwargs):
            """
            Get a list of any active maintenances. This endpoint will only
            return scheduled maintenances in the In Progress or Verifying state.

            Returns:
                A dict representation of the JSON returned by the API.
            """
            return GithubStatus()._get("scheduled-maintenances/active.json", kwargs)
