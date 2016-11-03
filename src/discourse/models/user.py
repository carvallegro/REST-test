import json

class Badge:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.type = json['badge_type_id']
        self.icon = json['icon']
        self.image = json['image']

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class User:
    def __init__(self, json):
        self.badges = list(map(lambda badge : Badge(badge), json['badges']))

        user = json['user']
        self.id = user['id']
        self.name = user['name']
        self.username = user['username']
        self.admin = user['admin']
        self.avatar_url_suffix = user['avatar_template']
        self.last_posted = user['last_posted_at']
        self.last_seen = user['last_seen_at']
        self.location = user['location']
        if self.avatar_url_suffix is None:
            self.avatar_url_suffix = user['system_avatar_template']
        self.avatar_url_suffix = self.avatar_url_suffix.format(size=32)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)