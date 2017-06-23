FROM python:3-slim

ADD test.py main.py server.py requirements.txt /capio-ai/src/

# RUN apk add --update python3 py3-pip

# RUN apk add --update sudo

# RUN apk add --update gcc

# RUN apk add --update libxml2-dev libxslt-dev python3-dev

RUN pip install -r /capio-ai/src/requirements.txt

# RUN pip install requests
# RUN pip install python-docx
# RUN pip install bottle

EXPOSE 8080
# CMD echo $API
# CMD echo $trans
# CMD python server.py $ip $port
# CMD cd /capio-ai/src/
# CMD python3 main.py $trans $API
CMD ["python","/capio-ai/src/server.py","0.0.0.0","8080"]