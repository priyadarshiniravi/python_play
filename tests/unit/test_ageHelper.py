from datetime import datetime, timedelta
from unittest import TestCase

from app.age_helper import AgeHelper


class TestAgeHelper(TestCase):
    def test_get_days_diff(self):
        currentdate = datetime.now().date()
        tendayslater = currentdate + timedelta(days=10)
        ageHelper = AgeHelper(tendayslater)

        self.assertEquals('10',ageHelper.get_days_diff())



