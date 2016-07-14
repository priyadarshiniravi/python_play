from datetime import datetime


class AgeHelper(object):
    def __init__(self,date):
        self.date = date
    def get_days_diff(self):
        return str((self.date - datetime.now().date()).days)




