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
        self.client.get("/api/v1/config/")
        self.client.get("/api/v1/oauth-clients/local")
        self.client.get('/api/v1/videos/languages')
        self.client.get('/api/v1/plugins/peertube-plugin-simplelogo/public-settings')
        self.client.get('/api/v1/plugins/peertube-plugin-matomo/public-settings')
        self.client.get('/api/v1/plugins/peertube-plugin-custom-links/public-settings')
        self.client.get('/api/v1/plugins/peertube-plugin-custom-links/public-settings')
        self.client.get('/api/v1/videos/?start=0&count=25&sort=-publishedAt&skipCount=true')
        self.client.get('/api/v1/plugins/peertube-plugin-topmenu/public-settings')
        self.client.get('/api/v1/plugins/peertube-plugin-topmenu/public-settings')

    @task(1)
    def performance_test(self):
        self._index_page()
