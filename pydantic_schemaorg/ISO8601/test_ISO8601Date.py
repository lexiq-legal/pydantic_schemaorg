#    Year:
#       YYYY (eg 1997)
#    Year and month:
#       YYYY-MM (eg 1997-07)
#    Complete date:
#       YYYY-MM-DD (eg 1997-07-16)
#    Complete date plus hours and minutes:
#       YYYY-MM-DDThh:mmTZD (eg 1997-07-16T19:20+01:00)
#    Complete date plus hours, minutes and seconds:
#       YYYY-MM-DDThh:mm:ssTZD (eg 1997-07-16T19:20:30+01:00)
#    Complete date plus hours, minutes, seconds and a decimal fraction of a
# second
#       YYYY-MM-DDThh:mm:ss.sTZD (eg 1997-07-16T19:20:30.45+01:00)
from pydantic import BaseModel

from ISO8601.ISO8601Date import ISO8601Date

class TestModel(BaseModel):
    testDate: ISO8601Date


test_dates = {'1997', '1997-07', '1997-07-16', '1997-07-16T19:20+01:00', '1997-07-16T19:20:30+01:00',
              '1997-07-16T19:20:30.45+01:00'}
for test_date in test_dates:
    TestModel(testDate=test_date)
