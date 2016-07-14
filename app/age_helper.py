from datetime import datetime


class AgeHelper(object):
    def __init__(self,date):
        self.date = date
    def get_age(self):
        days = (self.date - datetime.now().date()).days
        if (days/365) == 0:
            return str(days % 365) + " days"
        return str(days/365) + " years" + str(days%365) + " days"




