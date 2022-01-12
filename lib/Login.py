import json
from config import Host
import requests


class Login:
    def api_login(self,inData,getSession=True):
        url = f'{Host}/XX/XX'
        data = json.loads(inData)
        header = {}
        res = requests.post(url,data=data,header=header)
        if getSession:
           return res.cookies['sessionId']
        else:
            return res.text