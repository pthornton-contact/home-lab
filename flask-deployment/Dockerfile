FROM  python:alpine3.7  
RUN  pip install -r reqirements.txt
COPY  secret_token.py .
CMD  gunicorn -b 0.0.0.0:8000 secret_token:app