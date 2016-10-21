class Configuration(object):
    websites = []

    def __init__(self, websites=[]):
        super().__init__()
        self.websites = websites

    def __str__(self, *args, **kwargs):
        # return super().__str__(*args, **kwargs)
        return ", ".join([str(w) for w in self.websites])

    class Website(object):
        name = ""
        url = ""
        category = ""
        login = ""
        password = ""

        def __init__(self, name, url, category, login="", password=""):
            super().__init__()
            self.name = name
            self.url = url
            self.category = category
            self.login = login
            self.password = password

        def __str__(self, *args, **kwargs):
            # return super().__str__(*args, **kwargs)
            return self.name + " - " + self.url