# Import packages

from time import strftime, localtime
import requests

# Query the activity for the day from the API:
r = requests.get('https://www.boredapi.com/api/activity/')

r_json = r.json()
activity = r_json["activity"]
header = "The activity for the day is: " + activity

new_line = header+"\n"

# Save to a file:
file = open("activities.txt", 'a')

file.write(new_line)

file.close()

# Observe if needed:
# print("The activity for " + str(time.strftime("%a, %d %b %Y", time.localtime())) + " is: " + activity)