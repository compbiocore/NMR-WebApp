FROM python:3.9
ENV PYTHONUNBUFFERED 1
# Install ssh 
RUN sudo apt-get -y install openssh-server \\ 
&& apt-get -y inotify-tools
# Start service
RUN sudo service ssh start
# start the daemon
RUN sudo /usr/sbin/sshd -D &
RUN useradd -m --no-log-init --system  --uid 1000 foobob -s /bin/bash -g sudo -G root

#change password
RUN echo 'foobob:foobob' | chpasswd

WORKDIR /app
COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt 
COPY . /app
RUN chmod +x wait-for-it.sh
# Expose not needed because that is in docker-compose.yml 
CMD ["./wait-for-it.sh", "db:3306", "--", "python3", "manage.py", "runserver", "0.0.0.0:8000"]