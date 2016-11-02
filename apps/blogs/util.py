"""Utility for Parsing."""
import json
import datetime
from django.conf import settings
from pprint import pprint
from .models import Presentation
from usermanager.models import Profile


class ParseJson(object):
    """Parser Utility for data input."""

    def __init__(self, path=None):
        """Init method to get file path and prepare data out of the file."""
        if not path:
            self.path = settings.PARSE_FILE_PATH
        else:
            self.path = path
        self.prepare_json_data()

    def prepare_json_data(self):
        """Method to read the json file and import data into db."""
        with open(self.path) as json_file:
            self.json_data = json.load(json_file)

    def display_json_data(self):
        """Display Json data in formatted way."""
        pprint(self.json_data)

    def process_data(self):
        """Method to parse data into db."""
        # Running a loop on data to process.
        for data in self.json_data:
            # Get or Create a profile first
            temp, created = Profile.objects.get_or_create(
                username=data['creator']['name'],
                profile_url=data['creator']['profileUrl'])

            # Create the presentation
            Presentation.objects.create(
                id=data['id'], title=data['title'],
                thumbnail=data['thumbnail'], creator=temp,
                createdAt=datetime.datetime.strptime(
                    data['createdAt'], '%B %d, %Y'))
