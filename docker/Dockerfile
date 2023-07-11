# docker run -p 7077:7077 -p 8080:8080
FROM ubuntu:22.04

RUN apt update
RUN apt install -y wget python3.11 openjdk-11-jdk

RUN wget https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
RUN tar -xvzf spark-3.4.1-bin-hadoop3.tgz
RUN rm spark-3.4.1-bin-hadoop3.tgz

# to run stand alone instance in background:
# ENV SPARK_NO_DAEMONIZE=true
# docker run -d -p 8080:8080 -p7077:7077 <tag>

# 'true' prevents docker image from shutting down
#ENV SPARK_NO_DAEMONIZE=true

EXPOSE 8080 7077

#COPY entry.sh entry.sh
#CMD ["./entry.sh"]

#CMD ["/spark-3.4.1-bin-hadoop3/sbin/start-master.sh"]

#CMD ["/spark-3.4.1-bin-hadoop3/bin/spark-class", "org.apache.spark.deploy.master.Master"]
