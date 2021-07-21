FROM python

MAINTAINER github.com/Milesfeng

RUN apt-get update

RUN apt-get -y install git ffmpeg libsm6 libxext6 

RUN git clone https://github.com/Milesfeng/OCR.git

WORKDIR /OCR

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD python3 run.py




