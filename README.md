# learning-spark
Capture various steps to get up to speed on spark


## Environment Setup

Install and configure The following:  
* [VirtualBox](#virtualbox)
* [Ubuntu 22.04 LTS](#ubuntu-22.04-lts)
* [Jupyter Notebook](#jupyter-notebook)
* [(Py)Spark](#spark)
* [Network Mapping](#create-a-network-mapping-in-virtualbox)

### VirtualBox

[Download](https://www.virtualbox.org/wiki/Downloads) and install Version (I chose latest version, 7.0.4)

### Ubuntu 22.04 LTS

Excellent short video on [Installing Ubuntu 22.04 on VirtualBox](https://www.youtube.com/watch?v=rJ9ysibH768&ab_channel=GEEKrar)

1. Create a new machine in VirtualBox with the following settings:
   * Select `Skip unattended installation`
   * 2 CPUs (min)
   * 4 GB RAM (min)
   * 32GB Video memory recommend 
   * 25 GB Disk, fixed
  
   * Ubuntu Install Settings: 
     * Choose minimal install

2. Install Guest Additions:

  After initial install of OS, RESTART

3. Open Terminal and run the following:
  ```shell
  sudo apt update
  sudo apt-get install -y build-essential linux-headers-$(uname -r)
  ```
4. Select Devices from Menu, and choose `Insert Guest Additions CD image...`

5. Once mounted, open CD and right click on autorun.sh and choose `Run as a Program`

6. Once completed, restart machine for changes to take effect.

7. To enable copying to/from host machine, select Devices menu, and choose `Shared Clipboard` and `Drag and Drop` to `Bidirectional`

### Jupyter Notebook

Excellent short video on [Installing Jupyter Notebook on Ubuntu 22.04](https://www.youtube.com/watch?v=Zua1g79e5yY&ab_channel=Abstractprogrammer)

1. From Ubuntu terminal, run the following:
    ```shell
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    
    #pip3 install jupyter
    pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org jupyter
    ```

2. Restart computer

3. From Ubuntu terminal, run the following:
    ```shell
    cd
    mkdir python-workspace
    cd python-workspace/ 
    jupyter notebook
    ```

### Enable Access to Jupyter Notebook from HOST machine:

1. Install the following packages:
      ```shell
      sudo apt-get update -y
      #sudo apt-get install build-essential -y
      sudo apt-get install libssl-dev libpq-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip -y
      #sudo apt-get install python3-pip -y
      sudo apt-get install python3-dev python3-venv -y
      sudo apt-get install nano -y
      sudo apt-get install git -y
    ```
   
2. Create a Jupyter Configuration file:
    ```shell
    jupyter notebook --generate-config
    ```
    Make a note of the file location, it will be something like: `/home/<username>/.jupyter/jupyter_notebook_config.py`

3. Create a password for our configuration file:
    ```shell
    ipython -c "from notebook.auth import passwd; passwd()"
    ```
    e.g. `'argon2:$argon2id$v=19$m=10240,t=10,p=8$KPyiNB6rhfP9w/PcO6DbwQ$YMbtB3vxizi1k7/1XlyKKUWMUpX1cZfn9ALQtog0PhQ'`

4.  Edit the configuration file:
    ```shell
    nano /home/<username>/.jupyter/jupyter_notebook_config.py
    ``` 
  
5.  Add the following lines to the file (just below `c = get_config()`):
    ```shell
    c.IPKernelApp.pylab = 'inline' # if you want plotting support always in your notebook
    c.NotebookApp.allow_origin = '*' # put your public IP Address here
    c.NotebookApp.ip = '*'
    c.NotebookApp.allow_remote_access = True
    c.NotebookApp.open_browser = False
    c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$KPyiNB6rhfP9w/PcO6DbwQ$YMbtB3vxizi1k7/1XlyKKUWMUpX1cZfn9ALQtog0PhQ'
    c.NotebookApp.port = 8888
    ```

6.  Start Jupyter Notebook (from the correct directory):
    ```shell
    cd
    cd python-workspace/
    jupyter notebook
    ```

In a browser on the GUEST machine, enter http://localhost:8888

### Spark

Short video on setting [Installing Spark](https://www.youtube.com/watch?v=YanzUI-30pI&ab_channel=BigTechTalk)

1. Install Java
    ```shell
    sudo apt-get install default-jdk
    ```

2. Download Spark: [Downloads](https://spark.apache.org/downloads.html)

    Version https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz

    ```shell
    sudo su -
    mkdir -p /opt/spark
    cd /opt/spark
    wget --no-check-certificate https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
    tar -xvf spark-3.4.1-bin-hadoop3.tgz
   ```
    
    Add Spark and PySpark to the PATH:
    ```shell
    nano ~/.bashrc
    # Add to end of file
    SPARK_HOME=/opt/spark/spark-3.4.1-bin-hadoop3
    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
    export PYSPARK_PYTHON=/usr/bin/python3
    # save and exit
    source ~/.bashrc
    ```

###  Create a Network Mapping in VirtualBox:

In order to access the Jupyter Notebook and Spark console from the HOST machine, we need to create a network mapping in VirtualBox.

Excellent short video on VirtualBox [Port Forwarding](https://www.youtube.com/watch?v=SK_7AhHNZ0M&ab_channel=Abstractprogrammer)

You will need to identify the IP address of the guest machine in order to complete the mapping.
In my case, the guest IP is `10.0.2.15`
```shell
~$ ip a
```

* Open Devices menu, and choose `Network` and `Network Settings`
* Select `Advanced` and `Port Forwarding`
* Click the `+` icon to add a new rule

| Name | Protocol | Host IP | Host Port | Guest IP | Guest Port |
| --- | --- | --- | --- | --- | --- |
| Jupyter | TCP |`127.0.0.1`|`8888`|`10.0.2.15`|`8888`|
| Spark | TCP |`127.0.0.1`| `4040`   |`10.0.2.15`| `4040`     |

* Click `OK` to save the rule

Start Jupyter and/or Spark to access from HOST
