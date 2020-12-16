#!/usr/bin/python3 -u

import os

TAG = os.environ['QBT_TAG']
HOST = os.environ['QBT_HOST']
USER = os.environ['QBT_USER']
PASS = os.environ['QBT_PASS']

from qbittorrentapi import Client
client = Client(host=HOST, username=USER, password=PASS)

for torrent in client.torrents.info():
  torrent_tags = torrent.tags.split(',')
  for status in torrent.trackers:
    if status.status == 4:
      if TAG not in torrent_tags:
        print('Tagging', torrent.name,'–',status.msg)
        torrent.addTags(TAG)
    else:
      if TAG in torrent_tags:
        print('Clearing', torrent.name)
        torrent.removeTags(TAG)

print('Done.')