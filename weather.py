#python

import atsd_client
from atsd_client.services import SeriesService
# from datetime import datetime


conn = atsd_client.connect()

svc = SeriesService(conn)

from atsd_client.models import Sample, Series
series = Series(entity='sensor123', metric='wind')
series.add_samples(
    Sample(value=1, time="2016-07-18T17:14:30Z"),
    Sample(value=2, time="2016-07-18T17:16:30Z")
)

svc.insert(series)
