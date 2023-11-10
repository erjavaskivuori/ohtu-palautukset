from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)

        details = parsed_toml['tool']['poetry']
        name = details['name']
        desc = details['description']
        license = details['license']
        authors = details['authors']
        dep = details['dependencies']
        dev_dep = details['group']['dev']['dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, license, authors, dep, dev_dep)
