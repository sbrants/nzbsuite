import os

def create_api_key():
    """ Return a new randomized API_KEY
    """
    import time
    try:
        from hashlib import md5
    except ImportError:
        from md5 import md5
    import random
    # Create some values to seed md5
    t = str(time.time())
    r = str(random.random())
    # Create the md5 instance and give it the current time
    m = md5(t)
    # Update the md5 instance with the random variable
    m.update(r)

    # Return a hex digest of the md5, eg 49f68a5c8493ec2c0bf489821c21fc3b
    return m.hexdigest()

if not os.path.exists("/config/sabnzbd.ini"):
    with open("/config/sabnzbd.ini", "w") as sabnzbd:
        api_key = create_api_key()
        sabnzbd.write("[misc]\n")
        sabnzbd.write("api_key = {}\n".format(api_key))
        sabnzbd.write("download_dir = /data/incomplete\n")
        sabnzbd.write("complete_dir = /data/complete\n")
        sabnzbd.write("""[servers]
[[0.0.0.0]]
username = ""
enable = 0
name = 0.0.0.0
fillserver = 0
connections = 2
ssl = 0
host = 0.0.0.0
timeout = 120
password = ""
optional = 0
port = 119
retention = 0
""")
        sabnzbd.write("""[categories]\n
[[tv]]
priority = 1
pp = ""
name = tv
script = Default
newzbin = ""
dir = tv""")

def finSabKey():
    with open("/config/sabnzbd.ini") as sabnzbd:
        for line in sabnzbd:
            items = line.strip().split("=")
            if len(items) == 2:
                if items[0].strip() == "api_key":
                    return items[1].strip()

if not os.path.exists("/config/config.ini"):
    with open("/config/config.ini", "w") as sickbeard:
        sickbeard.write("[General]\n")
        sickbeard.write("config_version = 6\n")
        sickbeard.write('web_root = "/sickbeard"\n')
        sickbeard.write("nzb_method = sabnzbd\n")
        sickbeard.write("root_dirs = 0|/tv\n")
        sickbeard.write("tv_download_dir = /data/complete/tv\n")
        sickbeard.write("git_path = /usr/bin/git\n")
        sickbeard.write("[SABnzbd]\n")
        if "api_key" not in locals():
            api_key = finSabKey()
        sickbeard.write("sab_apikey = {}\n".format(api_key))
        sickbeard.write("sab_category = tv\n")
        sickbeard.write("sab_host = http://sabnzbd:8080/\n")