FROM python:3.8
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > /requirements.txt && pip install -r /requirements.txt
COPY simplify.py psimpl.py /
ENTRYPOINT ["python3.8", "/simplify.py"]
