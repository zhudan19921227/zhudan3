cd D:\6\example
pytest -sq --alluredir=../report/tmp
allure generate  ../report/tmp -o ../report/report --clean