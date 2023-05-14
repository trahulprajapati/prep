#
# a = 'rahul prajapati'
#
# h = {}
# for i in range(len(a)):
#     if a[i] in h:
#         h[a[i]] += 1
#     else:
#         h[a[i]] = 1
#
# char = 0
# ch = ''
# for i, j in h.items():
#     if j > char:
#         char = j
#         ch = i
#
# print(char, ch)


#
# li = [{'expiryDateTime': '2023-06-02T00:00:00+06:00',
#   'offerID': 1563,
#   'offerState': 0,
#   'offerType': 2,
#   'startDateTime': '2023-05-03T00:00:00+06:00'},
#  {'expiryDate': '2023-05-09T12:00:00+00:00',
#   'offerID': 3857,
#   'offerType': 0,
#   'startDate': '2023-05-03T12:00:00+00:00'},
#  {'expiryDate': '9999-12-31T12:00:00+00:00',
#   'offerID': 10101,
#   'offerType': 0,
#   'startDate': '2022-06-21T12:00:00+00:00'},
#  {'expiryDate': '9999-12-31T12:00:00+00:00',
#   'offerID': 10102,
#   'offerType': 0,
#   'startDate': '2022-06-21T12:00:00+00:00'},
#  {'expiryDate': '9999-12-31T12:00:00+00:00',
#   'offerID': 10103,
#   'offerType': 0,
#   'startDate': '2022-06-21T12:00:00+00:00'},
#  {'expiryDate': '9999-12-31T12:00:00+00:00',
#   'offerID': 10105,
#   'offerType': 0,
#   'startDate': '2022-06-21T12:00:00+00:00'},
#  {'expiryDate': '2023-06-01T12:00:00+00:00',
#   'offerID': 21035,
#   'offerType': 0,
#   'startDate': '2023-05-03T12:00:00+00:00'}]

import datetime
import isodate

def _convert_start_date(start_date):
 """
 Fix year 1970 to month start date bill period
 """
 if '0000' == str(start_date)[:4]:
  today = datetime.datetime.utcnow()
  new_start = today.replace(
   day=1, hour=0, minute=0,
   second=0, microsecond=0)
  # is UTC
  return new_start.isoformat() + '+00:00'

 start_date = isodate.parse_datetime(str(start_date))
 return start_date.isoformat()[:-6] + '+00:00'
