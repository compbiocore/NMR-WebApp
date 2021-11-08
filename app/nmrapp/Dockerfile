FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN  pip install -r requirements.txt 
COPY . /app
RUN chmod +x wait-for-it.sh
# No expose needed because that is in docker-compose.yml 
CMD ["./wait-for-it.sh", "db:3306", "--", "python3", "manage.py", "runserver", "0.0.0.0:8000"]