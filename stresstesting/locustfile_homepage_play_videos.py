import datetime
import random
import uuid

from locust import HttpUser, task, between
from locust.contrib.fasthttp import FastHttpUser

class RealityTubeUser(FastHttpUser):
    wait_time = lambda *args, **kwargs: 0
    userId = None
    email = ''
    headers = None
    host = 'https://reality-tube.net/'

    def _index_page(self):
        urls_to_load = [
            "/static/streaming-playlists/hls/6336d361-65f4-4a3a-9df3-a1eef3937371/6336d361-65f4-4a3a-9df3-a1eef3937371-360-fragmented_for_perfomancetesting.mp4",
            '/static/streaming-playlists/hls/59287452-96e0-4448-9080-81fd54408756/59287452-96e0-4448-9080-81fd54408756-360-fragmented_for_perfomancetesting.mp4',
            '/static/streaming-playlists/hls/93c04c1c-70da-4307-acff-208b26c94dde/93c04c1c-70da-4307-acff-208b26c94dde-360-fragmented_for_perfomancetesting.mp4',
            '/static/streaming-playlists/hls/947f5d5a-5675-4691-ae8e-4fba926142dc/947f5d5a-5675-4691-ae8e-4fba926142dc-360-fragmented_for_perfomancetesting.mp4',
            '/static/streaming-playlists/hls/b7d37f3f-0054-4269-b751-57942e1a5133/b7d37f3f-0054-4269-b751-57942e1a5133-360-fragmented_for_performancetesting.mp4',
            '/static/streaming-playlists/hls/1dd8247e-c5d5-41a4-8b28-135471a6d972/1dd8247e-c5d5-41a4-8b28-135471a6d972-360-fragmented_for_performancetesting.mp4'
        ]
        self.client.get(random.choice(urls_to_load))

    @task(1)
    def performance_test(self):
        self._index_page()
