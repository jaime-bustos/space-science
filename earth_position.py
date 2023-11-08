"""
Kernel Information:
spk contain trajectory information of planetary bodies, spacecraft, etc.
pck contain physical parameters of bodies like the size or orientation
ik contain instrument-specific information that are e.g., mounted on a spacecraft
ck contain information regarding the orientation of a spacecraft in space
fk contain reference frame information that is needed to calculate positions in a less common reference system
lsk contain time information that is crucial to convert e.g., the UTC time into ephemeris time ET (a standard time format that is being used in space science and astronomy)

"""


import spiceypy
import datetime


spiceypy.furnsh('naif0012.tls')

#get today's date
DATE_TODAY = datetime.datetime.today()

DATE_TODAY.strftime('%d-%m-%YT00:00:00')


ET_MIDNIGHT = spiceypy.utc2et(DATE_TODAY)

print(ET_MIDNIGHT)