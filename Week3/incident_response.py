#!/usr/bin/env python3
import subprocess
import json

result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)

raw_output = result.stdout

# Turn the text block into a list of individual lines
lines = raw_output.split('\n')

# Create an empty list to hold attacker IPs
attacker_ips = []

# Loop through each line
for line in lines:

    # Only process lines that have content
    if line:

        # Split by spaces, grab the IP at index 10
        ip = line.split(" ")[10]
        attacker_ips.append(ip)
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": attacker_ips
}
with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)
