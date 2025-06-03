🔐 New Script Idea: SSH Brute-Force Blocker
This script will automatically detect repeated failed SSH login attempts from the same IP address and block that IP using ufw (firewall).

✅ Step-by-Step Logic in Plain English:

Read the system's auth log (usually /var/log/auth.log or /var/log/secure).
Search for lines that show "Failed password" attempts.
Extract the IP addresses from those failed attempts.
Count how many times each IP address failed to log in.
If any IP has more than 5 failed attempts, block that IP using the ufw firewall.
Log what was blocked, when, and why — in a separate log file.
Optionally: send yourself a notification email or message (optional bonus later).
Run this script from cron every hour or daily.
