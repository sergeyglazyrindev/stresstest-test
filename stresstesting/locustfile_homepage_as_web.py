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
        self.client.get("/")
        self.client.get("/client/en-US/runtime-es2015.e6ae81b736a450eb0283.js")
        self.client.get('/client/en-US/polyfills-es2015.b41cc4738c9a1b0170ba.js')
        self.client.get('/client/en-US/main-es2015.0b2423ab22d57a9ada18.js')
        self.client.get('/client/en-US/SourceSansPro-Regular.ttf.f963ed837d6e84c7f143.woff2')
        self.client.get('/client/en-US/SourceSansPro-Semibold.ttf.acbf737b5bfddd31d0f6.woff2')
        self.client.get('/client/en-US/SourceSansPro-Bold.ttf.2f5f78b01bf8ea38446d.woff2')
        self.client.get('/client/en-US/menu.1350325a50f233cc9067.svg')
        self.client.get('/client/en-US/24-es2015.ee4404d514308a3a5404.js')
        self.client.get('/client/en-US/common-es2015.39bf09d74599681c1be1.js')
        self.client.get('/client/en-US/8-es2015.e1d78c02af7627b2acce.js')
        self.client.get('/client/assets/images/icons/icon-144x144.png')
        self.client.get('/static/thumbnails/03e65b5a-a850-4fa1-894d-be40524790f1.jpg')
        self.client.get('/static/thumbnails/e928155f-05e6-48c8-8607-944d69cb1bec.jpg')
        self.client.get('/static/thumbnails/ab7aa242-19f4-4fbf-b66d-37283f12ec5d.jpg')
        self.client.get('/static/thumbnails/3d6f85ca-82d1-492a-8a2b-f128a3289c7e.jpg')
        self.client.get('/static/thumbnails/27b1726d-7971-4feb-9f34-a7039d6b8338.jpg')
        self.client.get('/static/thumbnails/7b60e9a3-3e5a-4e21-954c-c202f01db0f6.jpg')
        self.client.get('/static/thumbnails/9fb72a3d-c458-44ec-954d-ae714bd7a4bc.jpg')
        self.client.get('/static/thumbnails/05591a22-de8f-4732-9089-5a49a9510d94.jpg')
        self.client.get('/static/thumbnails/71dfd52b-264f-4cbf-9287-943708cea1b6.jpg')
        self.client.get('/plugins/custom-links/0.0.10/client-scripts/dist/common-client-plugin.js')
        self.client.get('/plugins/webapp-manifest/0.1.3/client-scripts/dist/common-client-plugin.js')
        self.client.get('/plugins/simplelogo/0.0.4/client-scripts/client/common-client-plugin.js')
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
