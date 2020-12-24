#!/usr/bin/python3 -u

import os
from qbittorrentapi import Client

DEBUG = os.environ['QBT_DEBUG'] == 'true'
TAG = os.environ['QBT_TAG']
HOST = os.environ['QBT_HOST']
USER = os.environ['QBT_USER']
PASS = os.environ['QBT_PASS']

IGNORED_TRACKER_URLS = {'** [DHT] **', '** [PeX] **', '** [LSD] **'}

client = Client(host=HOST, username=USER, password=PASS)

for torrent in client.torrents.info():
	if DEBUG:
		print('---', torrent.name, '---')
		print('Tags:', torrent.tags)

	has_working_trackers = False
	for tracker in torrent.trackers:
		tracker_working = tracker.status != 4 and tracker.url not in IGNORED_TRACKER_URLS
		if DEBUG:
			print('Tracker:', tracker.url, tracker_working, tracker.status, tracker.msg)
		if tracker_working:
			has_working_trackers = True

	torrent_tags = torrent.tags.split(',')
	if has_working_trackers:
		if TAG in torrent_tags:
			print('Clearing', torrent.name)
			torrent.removeTags(TAG)
	else:
		if TAG not in torrent_tags:
			print('Tagging', torrent.name)
			torrent.addTags(TAG)
