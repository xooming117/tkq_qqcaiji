FROM frolvlad/alpine-python3
WORKDIR /opt/tbk/qqcaiji
COPY ./requirements.txt /opt/tbk/qqcaiji/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/tbk/qqcaiji

# 暴露 80 端口
#EXPOSE 80

CMD ["python", "cqsdk.py"]
