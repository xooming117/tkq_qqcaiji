FROM frolvlad/alpine-python3
WORKDIR /opt/tkq/qqcaiji
COPY ./requirements.txt /opt/tkq/qqcaiji/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/tkq/qqcaiji

# 暴露 80 端口
#EXPOSE 80

CMD ["python", "cqsdk.py"]
