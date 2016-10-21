import yaml

from src.configuration.Configuration import Configuration

current_configuration = None


def load(path):
    with open(path, "r") as stream:
        try:
            global current_configuration
            current_configuration = generate(stream)
            print(current_configuration)
        except yaml.YAMLError as exc:
            print(exc)


def generate(stream):
    yaml_conf = yaml.load(stream)
    websites = [parse_website(w) for w in yaml_conf.get("websites")]
    return Configuration(websites)

def parse_website(website):
    website_configuration = Configuration.Website(
        name=website.get("name"),
        url=website.get("url"),
        category=website.get("category"))
    authentication = website.get("authentication")
    if authentication:
        website_configuration.login = authentication.get("login")
        website_configuration.password = authentication.get("password")
    return website_configuration
