import json
from lesson import ApiCourse
from Login import Login
import pytest
@pytest.fixture(scope='module',autouse=True)
def delete_all_course(request):
    session = Login.api_login('')
    inData = {}
    res = json.loads(ApiCourse.listCourse(session,inData))['reslist']
    for one in res:
        ApiCourse.deleteCourse(session,one['id'])
    for one in range(1,7):
        courseData = {'name':f'aa{one:0>3}','des':'middle'}
        ApiCourse.addCourse(session,courseData)
    def fin():
        print("end")
    request.addfinalizer(fin)
