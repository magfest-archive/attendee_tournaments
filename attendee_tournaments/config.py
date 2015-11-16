from attendee_tournaments import *

at_config = parse_config(__file__)
c.include_plugin_config(at_config)

c.TOURNAMENT_AVAILABILITY_OPTS = []
_val = 0
for _day in range((c.ESCHATON - c.EPOCH).days):
    for _when in ['Morning (8am-12pm)', 'Afternoon (12pm-6pm)', 'Evening (6pm-10pm)', 'Night (10pm-2am)']:
        c.TOURNAMENT_AVAILABILITY_OPTS.append([
            _val,
            _when + ' of ' + (c.EPOCH + timedelta(days=_day)).strftime('%A %B %d')
        ])
        _val += 1
c.TOURNAMENT_AVAILABILITY_OPTS.append([_val, 'Morning (8am-12pm) of ' + c.ESCHATON.strftime('%A %B %d')])
