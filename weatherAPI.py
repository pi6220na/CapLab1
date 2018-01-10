# Capstone Lab 1
# Use an API
# Jeremy Wolfe

import pprint
from urllib.request import urlopen
import json

# code base copied from: https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1

f = urlopen('http://api.wunderground.com/api/b27dbdfdaafdef52/geolookup/conditions/q/MN/Minneapolis.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print("Current temperature in %s is: %s" % (location, temp_f))
f.close()

#A better view by Jeremy -
#prints json in a "more" formatted format
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(parsed_json)
