# Spark on Docker

We manually install spark onto docker instance (instead of pip install).
Doing so gives us ability to run in various scenarios:
1. as a service: `/spark-3.4.1-bin-hadoop3/sbin/start-master.sh`
2. spark-shell: `/spark-3.4.1-bin-hadoop3/bin/spark-shell`
3. pyspark: `/spark-3.4.1-bin-hadoop3/bin/pyspark`

Several ports are exposed: 8080 and 7077.
To map those ports to local, use -p <HOST>:<IMAGE>
```shell
docker run -p 8080:8080 -p 7077:7077 <tag> 
```

To create a spark service image, modify [docker](./docker/Dockerfile) image to include `SPARK_NO_DAEMONIZE=true` and a CMD to execute `start-master.sh`:  
```dockerfile
ENV SPARK_NO_DAEMONIZE=true

CMD ["/spark-3.4.1-bin-hadoop3/sbin/start-master.sh"]
```

Run image in detached mode:
```shell
docker run -d -p 8080:8080 -p 7077:7077 <tag>
```