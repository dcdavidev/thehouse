FROM python:3.12-alpine

COPY thehouse /thehouse

CMD ["python", "-m", "thehouse"]
