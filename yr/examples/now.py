#!/usr/bin/env python3

from yr.libyr import Yr

weather = Yr(location_name=u'Norge/Telemark/Skien/Skien')
now = weather.now()

print now
