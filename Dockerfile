FROM python:3.9
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP fizzbuzz.py
ENTRYPOINT ["python", "-m", "flask", "run", "-h", "fizzbuzz", "-p", "5000"]