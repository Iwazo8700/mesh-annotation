# Pull base image.
FROM ubuntu:latest


USER root


ENTRYPOINT ["python3"]

# Install.

#python
RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv


# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

#pysolr
RUN apt-get install -y libmemcached-dev gosu && \
  pip install --no-cache-dir social-auth-app-django "gunicorn==19.3.0" "psycopg2==2.6" pylibmc pysolr "elasticsearch==2.4.1" && \

#wgets  
RUN  apt-get install -y wget


#java
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

#comandos no terminal pra busca
RUN apt-get update && apt-get install -y unzip

RUN wget http://ftp.unicamp.br/pub/apache/lucene/solr/8.2.0/solr-8.2.0.zip -q

RUN unzip -qq solr-8.2.0.zip && rm solr-8.2.0.zip



COPY mesh.py /Downloads/mesh-docker/mesh.py
COPY c2020.bin /Downloads/mesh-docker/c2020.bin

CMD ./solr-8.2.0/bin/solr start -c
CMD ./solr-8.2.0/bin/solr create -c mesh -p 8983
CMD python3 Downloads/mesh.py