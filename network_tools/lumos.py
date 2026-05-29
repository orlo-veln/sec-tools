# imports
import re

# data
logfile = '/home/manjushri/scripts/test_data/fake_auth.log'

# functions
def rate_threat(count):
    if count > 100:
        return 'HIGH'
    elif count > 10:
        return 'MEDIUM'
    else:
        return 'LOW'

def lumos(logfile):
    with open(logfile, 'r') as f:
        lines = f.readlines()

    failed = []
    pattern = r'Failed password for (\S+) from (\S+)'

    for line in lines:
        match = re.search(pattern, line)
        if match:
            failed.append(match)

    ip_counts = {}
    user_counts = {}
    for match in failed:
        ip = match.group(2)
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1
        user = match.group(1)
        if user in user_counts:
            user_counts[user] += 1
        else:
            user_counts[user] = 1

    print(f"Total lines read: {len(lines)}")
    print(f"Failed attempts found: {len(failed)}")
    print(f"Unique IPs: {len(ip_counts)}")
    print()
    for ip, count in ip_counts.items():
        rating = rate_threat(count)
        print(f"{ip:<20} attempts: {count:<5} threat: {rating}")
    print()
    print("Usernames tried:")
    for user, count in user_counts.items():
        print(f"  {user:<20} attempts:  {count}")     
# run
lumos(logfile)
