from datetime import datetime, timedelta
from unittest import TestCase

from app.age_helper import AgeHelper


class TestAgeHelper(TestCase):
    def test_get_days_diff(self):
        currentdate = datetime.now().date()
        tendayslater = currentdate + timedelta(days=10)
        ageHelper = AgeHelper(tendayslater)

        self.assertEquals('10 days', ageHelper.get_age())

    def test_get_year_diff(self):
        currentdate = datetime.now().date()
        tendayslater = currentdate + timedelta(days=375)
        ageHelper = AgeHelper(tendayslater)

        self.assertEquals("1 year 10 days", ageHelper.get_age())





