FROM joyzoursky/python-chromedriver:3.9-selenium


RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip install allure-pytest
COPY . .

RUN python -m pytest Tests/test_2_login.py