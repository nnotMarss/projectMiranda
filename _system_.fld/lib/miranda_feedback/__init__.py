import os
import sys
import json
import requests
import random


def parent(directory=os.getcwd(), levels=1):
    parent_dir = os.path.abspath(os.path.join(directory, *([os.pardir] * levels)))
    return parent_dir


sys.path.append(parent())
import miranda_folder as folder  # noqa
import miranda_language as lang  # noqa
from miranda_logger import log  # noqa
locale = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), 'r').read()


def send_message(content):
    sender_id = random.randint(10000000, 99999999)
    machine = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "MACHINEID.var"), 'r')
    data = {
        'content': "## New <:cc:1242123467470409799><:oo:1242123471253798962><:dd:1242123472956821696><:ee:1242123469290733639> submit was sent <@1171734246067544137>!",
        "embeds": [{
            "color": 16711422,
            "title": "From: ***%s***!" % (machine.read()),
            "description": "```\nMessage ID: %s\n\n%s\n```" % (sender_id, content),
        }],
        "author": {
            "icon_url": "https://cdn.ntmrs.xyz/@WEBSERVER/web/ASSETS/icon_v1.jpg",
            "name": "Miranda - Feedback",
            "url": "https://example.com"
        },
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://discord.com/api/webhooks/1241820361604206643/e5I94GyU-YPPQhCgMqKBLQZcnDxM3gcz3gztSKc0gHESL3G3Q3Uir3lPMWJHPbVluogr",
        data=json.dumps(data), headers=headers)

    if response.status_code == 204:
        print(":: %s" % (lang.lang(locale, "feedback_sent") % sender_id))
    else:
        print(":: %s\n:: '%s'" % (lang.lang(locale, "feedback_fail_module"), response.status_code))