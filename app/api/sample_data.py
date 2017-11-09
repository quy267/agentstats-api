# -*- coding: utf-8 -*-
__author__ = 'huydq17'

MINION_SAMPLE_DATA = {
  "count": 4434,
  "minions": [
    {
      "_id": "10.58.4.65",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "os_family": "RedHat",
        "ossec": "OK: Installed"
      },
      "connection": True,
      "group": "vtt",
      "os": "RedHat",
      "ossec": True
    },
    {
      "_id": "10.58.42.123",
      "agent": True,
      "cmdlog": True,
      "comment": [
        "All connections are OK"
      ],
      "connection": True,
      "group": "vtnet",
      "os": "RedHat",
      "ossec": True
    },
    {
      "_id": "10.60.105.243",
      "agent": False,
      "comment": {
        "filebeat": "NOK: Not installed",
        "kav": "NOK: Not installed",
        "oa": "NOK: Not installed",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": False,
      "group": "vtnet",
      "kav": False,
      "oa": False,
      "os": "Windows"
    },
    {
      "_id": "10.60.106.34",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "filebeat": "OK: Installed, Running",
        "os_family": "RedHat"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "os": "RedHat"
    },
    {
      "_id": "10.60.32.167",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "10.60.32.182",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "os_family": "RedHat",
        "ossec": "OK: Installed"
      },
      "connection": False,
      "connection_data": "10.30.160.41:5044",
      "group": "vtt",
      "os": "RedHat",
      "ossec": True
    },
    {
      "_id": "10.60.32.19",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "os_family": "RedHat",
        "ossec": "OK: Installed"
      },
      "group": "vtnet",
      "os": "RedHat",
      "ossec": True
    },
    {
      "_id": "10.60.32.39",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "os_family": "RedHat",
        "ossec": "OK: Installed"
      },
      "group": "vtnet",
      "os": "RedHat",
      "ossec": True
    },
    {
      "_id": "10.60.96.118",
      "agent": True,
      "cmdlog": True,
      "comment": [
        "All connections are OK"
      ],
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "os": "RedHat"
    },
    {
      "_id": "10.60.96.119",
      "comment": [
        "All connections are OK"
      ],
      "connection": True,
      "group": "vtnet"
    },
    {
      "_id": "192.168.131.37",
      "agent": False,
      "comment": {
        "error": "Not support os_family redhat-",
        "os_family": "redhat-"
      },
      "connection": True,
      "group": "vtnet",
      "os": "redhat-"
    },
    {
      "_id": "Windows_10.0.0.4",
      "agent": True,
      "comment": [
        "All connections are OK"
      ],
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_10.0.0.5",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_10.0.8.1",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_10.0.8.3",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_192.168.10.150",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_192.168.10.204",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_192.168.10.206",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_192.168.10.207",
      "agent": True,
      "comment": [
        "All connections are OK"
      ],
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_192.168.203.3",
      "agent": True,
      "comment": {
        "filebeat": "OK: Installed, Running",
        "kav": "OK: Installed, Running",
        "oa": "OK: Installed, Running",
        "os_family": "Windows"
      },
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "Windows_192.168.203.4",
      "agent": True,
      "comment": [
        "All connections are OK"
      ],
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "kav": True,
      "oa": True,
      "os": "Windows"
    },
    {
      "_id": "anm_centos_10.10.0.65",
      "agent": False,
      "cmdlog": False,
      "comment": {
        "cmdlog": "NOK: Not installed",
        "filebeat": "NOK: Not installed",
        "os_family": "RedHat"
      },
      "connection": False,
      "connection_data": "10.30.160.44:80,10.30.160.44:443,10.30.160.44:4505,10.30.160.44:4506,10.30.160.44:6379,10.30.160.41:5044",
      "filebeat": False,
      "group": "vtnet",
      "os": "RedHat"
    },
    {
      "_id": "anm_centos_10.10.0.87",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "filebeat": "OK: Installed, Running",
        "os_family": "RedHat"
      },
      "connection": False,
      "connection_data": "10.30.160.41:5044",
      "filebeat": True,
      "group": "vtnet",
      "os": "RedHat"
    },
    {
      "_id": "anm_centos_10.60.105.165",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "filebeat": "OK: Installed, Running",
        "os_family": "RedHat"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "os": "RedHat"
    },
    {
      "_id": "anm_centos_10.60.105.166",
      "agent": True,
      "cmdlog": True,
      "comment": {
        "cmdlog": "OK: Installed",
        "filebeat": "OK: Installed, Running",
        "os_family": "RedHat"
      },
      "connection": True,
      "filebeat": True,
      "group": "vtnet",
      "os": "RedHat"
    }
  ]
}