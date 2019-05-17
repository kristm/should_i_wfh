FROM debian:latest

WORKDIR /app

RUN apt-get update && apt-get -y install python3-pip git

COPY . .

RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]
