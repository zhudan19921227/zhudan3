import os
import pytest
import json
from lib.Login import Login
from lib.lesson import ApiCourse
from data.loginData import getData
import allure
@allure.feature("课程模块")
@pytest.mark.course(order=2)
class TestCourse:
    def setup_class(self):
        self.session = Login.api_login('{"sss":"xx","dd":"xx"}')

    @allure.story("增加课程")
    @pytest.mark.add
    def test_add_course(self):
        inData = {}
        res = ApiCourse.addCourse(self.session,inData)
        assert json.loads(res)['retcode'] == 0

    @allure.story("展示课程")
    def test_list_course(self):
        assert 1 == 1

    @allure.story("删除课程")
    def test_delete_coures(self):
        assert 2 == 2

    @allure.story("修改课程")
    def test_update_course(self):
        assert 3 == 3
if __name__ == '__main__':
    pytest.main(['testcourse.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure generate  ../report/tmp  -o  ../report/report  --clean')