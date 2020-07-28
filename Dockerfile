FROM lambci/lambda:build-python3.8

# download libraries
RUN yum install -y yum-utils rpmdevtools
WORKDIR /tmp

WORKDIR /opt
ADD video-generator .
RUN pipenv install -r requirements.txt
RUN mkdir -p python/lib/python3.8/site-packages
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt --no-deps -t python/lib/python3.8/site-packages

# run test
# WORKDIR /opt
# COPY video-generator .
# RUN pipenv run python debug.py

# package lambda layer
WORKDIR /opt
RUN zip -r code.zip python