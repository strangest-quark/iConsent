FROM lambci/lambda:build-python3.7 AS py37
FROM lambci/lambda:build-python3.8

# download libraries
RUN yum install -y yum-utils rpmdevtools
WORKDIR /tmp
RUN yumdownloader --resolve \
    cairo \
    ImageMagick && \
    rpmdev-extract *rpm

# install libraries and set links
RUN mkdir /opt/lib
WORKDIR /opt/lib
RUN cp -P -R /tmp/*/usr/lib64/* /opt/lib
RUN ln libcairo.so.2 libcairo.so && \
    ln libpangocairo-1.0.so.0 pangocairo-1.0

# copy fonts and set environment variable
COPY --from=py37 /usr/share/fonts/default /opt/fonts/default
COPY --from=py37 /etc/fonts/fonts.conf /opt/fonts/fonts.conf
RUN sed -i s:/usr/share/fonts:/opt/fonts: /opt/fonts/fonts.conf
ENV FONTCONFIG_PATH="/opt/fonts"

WORKDIR /opt
ADD requirements.txt .
RUN pipenv install -r requirements.txt
RUN mkdir -p python/lib/python3.8/site-packages
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt --no-deps -t python/lib/python3.8/site-packages

# run test
WORKDIR /opt
COPY . .
RUN pipenv run python main.py

# package lambda layer
WORKDIR /opt
RUN zip -r code.zip fonts lib