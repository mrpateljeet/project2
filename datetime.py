import datetime

class MyDatetime:

    def __init__(self, **kwargs):
        
        if "iso_8601" in kwargs:
            # Parse the ISO 8601 string.
            dt = datetime.datetime.fromisoformat(kwargs["iso_8601"])
            self.year = dt.year
            self.month = dt.month
            self.day = dt.day
            self.hour = dt.hour
            self.minute = dt.minute
            self.second = dt.second
        else:
            # Use the default date and time.
            self.year = kwargs.get("year", datetime.datetime.now().year)
            self.month = kwargs.get("month", datetime.datetime.now().month)
            self.day = kwargs.get("day", datetime.datetime.now().day)
            self.hour = kwargs.get("hour", 0)
            self.minute = kwargs.get("minute", 0)
            self.second = kwargs.get("second", 0)

    @property
    def iso_8601(self):
        """
        Get the datetime in ISO 8601 format.

        Returns:
            A string in ISO 8601 format.
        """

        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second).isoformat()

    @property
    def human_readable(self):
        """
        Get the datetime in a human-readable format.

        Returns:
            A string in a human-readable format.
        """

        return f"{self.month:02}/{self.day:02}/{self.year} {self.hour:02}:{self.minute:02}:{self.second:02}"

    @staticmethod
    def from_timestamp(timestamp):
        """
        Create a new MyDatetime object from a Unix timestamp.

        Args:
            timestamp: A Unix timestamp.

        Returns:
            A MyDatetime object.
        """

        return MyDatetime(year=datetime.datetime.fromtimestamp(timestamp).year,
                         month=datetime.datetime.fromtimestamp(timestamp).month,
                         day=datetime.datetime.fromtimestamp(timestamp).day,
                         hour=datetime.datetime.fromtimestamp(timestamp).hour,
                         minute=datetime.datetime.fromtimestamp(timestamp).minute,
                         second=datetime.datetime.fromtimestamp(timestamp).second)

    @classmethod
    def today(cls):
        """
        Create a new MyDatetime object representing today's date.

        Returns:
            A MyDatetime object representing today's date.
        """

        return MyDatetime(year=datetime.datetime.today().year,
                         month=datetime.datetime.today().month,
                         day=datetime.datetime.today().day)

