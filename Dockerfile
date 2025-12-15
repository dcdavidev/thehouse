FROM python:3.14.2-alpine3.22

COPY thehouse /thehouse

CMD ["python", "-m", "thehouse"]