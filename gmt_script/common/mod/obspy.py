#!/usr/bin/env python3

from obspy import read,Stream,UTCDateTime
from obspy.geodetics import gps2dist_azimuth
from .science import *
from .toYearFraction import toYearFraction

def udt_to_floatyear(udt_time_string: str) -> str:
    udt_time = UTCDateTime(udt_time_string)
    float_year = toYearFraction(udt_time.datetime)
    return float_year