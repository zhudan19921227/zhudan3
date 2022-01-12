import json

import requests

from config import Host


class ApiCourse:
    def listCourse(self,session,inData):
        user_session = session
        url = f'{Host}/XX/XX'
        data = json.loads(inData)
        header = {}
        res = requests.post(url, data=data, header=header,cookise=user_session)
        res.encoding='unicode_escape'
        return res.text

    def addCourse(self, session,inData):
        user_session = session
        url = f'{Host}/XX/XX'
        data = json.loads(inData)
        header = {}
        res = requests.post(url, data=data, header=header, cookise=user_session)
        res.encoding = 'unicode_escape'
        return res.text

    def deleteCourse(self,session,inId):
        user_session = session
        url = f'{Host}/XX/XX'
        data = {'':int(inId)}
        header = {}
        res = requests.delete(url, data=data, header=header,cookise=user_session)
        res.encoding='unicode_escape'
        return res.text