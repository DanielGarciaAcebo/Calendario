import json
import os
import random
import time
from datetime import datetime
from typing import Dict, List, Optional, cast

from flask import current_app

import constants as constants
from gregorian_calendar import GregorianCalendar

class CalendarData:

    REPETITION_TYPE_WEEKLY = "w"
    REPETITION_TYPE_MONTHLY = "m"
    REPETITION_SUBTYPE_WEEK_DAY = "w"
    REPETITION_SUBTYPE_MONTH_DAY = "m"

    def __init__(self, data_folder: str, first_weekday: int = constants.WEEK_START_DAY_MONDAY) -> None:
        self.data_folder = data_folder
        self.gregorian_calendar = GregorianCalendar
        self.gregorian_calendar.setfirstweekday(first_weekday)

    def load_calendar(self, filename: str) -> Dict:
        with open(os.path.join("../flask-calendar/flask_calendar", self.data_folder, "{}.json".format(filename))) as file:
            contents = json.load(file)
        if type(contents) is not dict:
            raise ValueError("Error loading calendar from file '{}'".format(filename))
        return contents


