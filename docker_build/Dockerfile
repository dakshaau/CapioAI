FROM python:3

ADD test.py main.py server.py requirements.txt /

RUN pip install -r requirements.txt

# EXPOSE 8080
# CMD echo $API
# CMD echo $trans
# CMD python server.py $ip $port
CMD python main.py $trans $API