from datetime import date

class Session:
    def __init__(self):
        self.date = date.today().strftime("%B %d, %Y")

