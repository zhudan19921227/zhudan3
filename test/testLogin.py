import os

import pytest
import json
from lib.Login import Login
from data.loginData import getData
import allure
@allure.feature("登入模块")
@allure.story('登入测试用例')
@allure.severity('critical')
@pytest.mark.login(order=1)
@pytest.mark.parametrize('inData,rep',getData())
def test_login(inData,rep):
    res = Login.api_login(inData,getSession=False)
    assert json.loads(res)['recode'] == json.loads(rep)['recode']




if __name__ == '__main__':
    pytest.main(['testLogin.py','-s','--alluredir','../report/tmp'])
    os.system('allure generate  ../report/tmp  -o  ../report/report  --clean')