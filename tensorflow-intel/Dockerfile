FROM clearlinux/python:3.7.5

RUN swupd bundle-add python-extras
RUN pip install -i https://pypi.douban.com/simple intel-tensorflow

ADD test.py /app/

CMD ["python3", "/app/test.py"]