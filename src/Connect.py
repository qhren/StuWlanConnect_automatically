import requests
import settings

header = {
    "Host": "10.255.44.33",
    "Referer": "http://10.255.44.33/srun_portal_pc.php",
    "Cookie": "login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYpuUwed%252FKvJiJytciND"
              "vNwBuZ0x09Oq24rxSlgZoySV1HXt1Y%252BNMpebTWWwCN2RXBaPE1V5IXtzvC"
              "ZeIts5mN8k%252F0IwRGgQ9VoKnXNhF1Ed4GE%252B6Ehu2ot05eO8LP7byWFYgr8"
              "jqRMLLOw%252FIvkPqcduHlA%253D%253D"
}

Data = {
    "action": "login",
    "ac_id": 1,
    "username": "%s" % settings.User_Name,
    "password": "%s" % settings.Pass_Word
}

requests.post("%s" % settings.Web_Url, data=Data, headers=header)
