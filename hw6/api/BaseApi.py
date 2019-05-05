import ssl


class BaseApi:
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context
