https://staging.tetrainsights.com/signin

pip freeze > requirements.txt

py.test Tests/ --alluredir ./result/ --browser chromehidden

python -m pytest Tests/test_2_login.py --browser chromehidden --so windows

allure serve ./result


docker build -t python .


py.test Tests/test_2_login.py --browser chromehidden

pip install pytest-rerunfailures

RUN