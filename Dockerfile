FROM python:3.7.10-alpine3.13
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt

ARG DEFAULT_TITLE="Default"
ARG DEFAULT_CONTENT="Default content"

ENV TITLE=${DEFAULT_TITLE}
ENV CONTENT=${DEFAULT_CONTENT}

COPY . .

ENTRYPOINT ["python"]
CMD ["main.py"]