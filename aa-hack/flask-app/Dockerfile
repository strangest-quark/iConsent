FROM lambci/lambda:build-python3.8

# download libraries
RUN yum install -y yum-utils rpmdevtools
WORKDIR /tmp

WORKDIR /opt
ADD . .
RUN pipenv install -r req.txt
RUN mkdir -p python/lib/python3.8/site-packages
RUN pipenv lock -r > req.txt
RUN pip install -r req.txt --no-deps -t python/lib/python3.8/site-packages

# run test
WORKDIR /opt
COPY . .
RUN pipenv run python debug.py

# package lambda layer
WORKDIR /opt
RUN zip -r code.zip python