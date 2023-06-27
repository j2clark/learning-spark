# learning-spark
Capture various steps to create a PySpark virtual machine

We will install VirtualBox on a Windows 11 Host.

We then create a virtual machine using Ubuntu 22.04, with Guest Additions. Guest Additions enables better screen scaling, as well as copy/paste between host<->guest

We install Python 3 (comes preinstalled), Jupyter Notebook, Java, and Spark 

Finally, we create some port forwarding entries to enable access to Jupyter and Spark dashboards from the Host machine

## VirtualBox

[Download](https://www.virtualbox.org/wiki/Downloads) and install the latest VirtualBox release. 7.0 at the time this was written.

## Ubuntu 22.04 LTS

[Download](https://ubuntu.com/download/desktop) Ubuntu Desktop 22.04 LTS 

For visual learners (like me), here is An excellent short video on [Installing Ubuntu 22.04 on VirtualBox](https://www.youtube.com/watch?v=rJ9ysibH768&ab_channel=GEEKrar)

### Create VirtualBox Machine

In VirtualBox, create a New instance.

Give it a name (e.g. spark), and the location of the Ubuntu ISO you just downloaded:
* Name: `spark`   
* ISO Image: `ubuntu-22.04.2-desktop-amd64.iso`
* Select `Skip Unattended Installation`

Select Next and provide compute requirements:
* Base Memory: `4096 MB` (min)
* Processors: `2` (min)
* Select `Enable EFI`

Select Next and provide the Hard Disk requirements:
* Disk Size: `25 GB` (min)
* Select `Preallocate Full Size`

Select Next and Finish to create the machine config and return to the VirtualBox console.

We need to make one modification before instantiating. From the console select the newly created machine and choose `Settings`
* Select Display
* Video Memory: `32 GB` (min)
* Select `OK` to exit back to the VirtualBox console

### Install Ubuntu on VirtualBox machine

Select machine entry and select `Start`

This will spin up machine and begin the Ubuntu installation.
This process and the installation process as a whole, can take a while.

Step through the Installation Dialogs, paying closer attention to the following:
* Updates and Software: What apps would you like to install to start with? `Minimal installation`

When asked select `Restart Now` (and `press ENTER` when asked) and complete final installation questions

### Install Guest Additions

Guest Additions help with scaling display plus provides copy/paste between host and guest machines

Open a terminal and run the following:
```shell
sudo apt update
sudo apt install -y build-essential linux-headers-$(uname -r)
```

Once completed, from the Machine Menu select `Devices > Insert Guest Additions CD image...`

Once the CD is mounted and CD icon appears in Ubuntu menu, click to open 

Right click and select `Open in Terminal`

```shell
./autorun.sh
```

Once complete, restart machine for changes to take effect.

You should now be able to scale window size as desired.

To enable copy/paste between hoist and machine select `Devices > Shared Clipboard > Bidirectional`

## Jupyter Notebook

To install Jupyter we first need to ensure python3 and pip3 are installed

For visual learners, here is an excellent video on [Installing Jupyter Notebook on Ubuntu 22.04](https://www.youtube.com/watch?v=Zua1g79e5yY&ab_channel=Abstractprogrammer)

Open a terminal and run:
```shell
sudo apt update
sudo apt install python3 -y
sudo apt install python3-pip -y
```

Now we can install Jupyter:
```shell
pip3 install jupyter
```

Note: on my work computer I always have issues with pip and SSL thanks to our firewall solution. The unfortunate workaround is to run the following:
```shell
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org jupyter
```

Restart machine for changes to take effect.

From a terminal:
```shell
mkdir ~/python-workspace
cd python-workspace/
jupyter notebook
```

Jupyter should start, and a Firefox browser will eventually open and resolve to `http://localhost:8888/tree` 

Create a new Notebook (`Python3`), click on Untitled to give it a name (`test`) 

In `In []`, enter `1+1` then Shift+Enter
If all is well, you should see `Out[1]: 2`

In the next `In []`, enter `1/2` then Shift+Enter
If all is well, you should see `Out[2]: 0.5`

Select `File > Save and Checkpoint`, and close browser

Open a new terminal:
```shell
cd pythone-workspace/
ls
```

You should see your notebook `test.ipynb` listed.

## Spark

For visual learners, here is a short video on [Installing Spark](https://www.youtube.com/watch?v=YanzUI-30pI&ab_channel=BigTechTalk)

### The EASY installation method is simply:
```shell
pip install pyspark
```

Once complete you can verify installation via the following:

PySpark:
```shell
pyspark
```
type `quit()` to exit

spark-shell (Scala):
```shell
spark-shell
```
Ctrl+C to exit

Note that java was installed for us:
```shell
java -version
```

### Manual Installation

The overall steps for installing spark are:
* install Java
* download and install Spark
* update environment path

#### Install Java

From a terminal:
```shell
sudo apt update
sudo apt install -y default-jdk
```

Ensure java is installed:
```shell
java -version
```

Should produce something like:
```shell
openjdk version "11.0.19" 2023-04-18
OpenJDK Runtime Environment (build 11.0.19+7-post-Ubuntu-0ubuntu122.04.1)
OpenJDK 64-Bit Server VM (build 11.0.19+7-post-Ubuntu-0ubuntu122.04.1, mixed mode, sharing)
```

#### Download and Install Spark
Next we download and install Spark. Below I selected the latest spark and hadoop versions

Go to [Spark downloads](https://spark.apache.org/downloads.html):
* 1 Choose a Spark release: `3.4.1 (Jun 23 2023)` 
* 2 Choose a package type: `Pre-built for Apache Hadoop 3.3 and later`
* Copy the download url from 3. Download Spark: [spark-3.4.1-bin-hadoop3.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz) 

Open a terminal (Note we log in as super-user)
```shell
sudo su -
mkdir -p /opt/spark
cd /opt/spark
wget https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
tar -xvf spark-3.4.1-bin-hadoop3.tgz
rm spark-3.4.1-bin-hadoop3.tgz
```

Note: on my work computer I always have issues with SSL thanks to our firewall solution. The unfortunate workaround is to run the following:
```shell
wget --no-check-certificate https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
```

Open a new terminal and update your .bashrc:
```shell
nano ~/.bashrc
```

Add the follow to the bottom of the file:
```shell
SPARK_HOME=/opt/spark/spark-3.4.1-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
```

Save, close and `source` the changes:
```shell
source ~/.bashrc
```

### Verify Installation
Once complete you can verify installation via the following:

PySpark:
```shell
pyspark
```
type `quit()` to exit

spark-shell (Scala):
```shell
spark-shell
```
Ctrl+C to exit

### Spark Console

With either pyspark or spark-shell running, open a browser on ubuntu machine and go to [http://localhost:4040](http://localhost:4040)

## VirtualBox Port Forwarding

We can access Jupyter Notebook and Spark consoles from the HOST machine, but we need to add port forward rules to our VirtualBox instance.

For visual learners, here is an excellent short video on [VirtualBox Port Forwarding](https://www.youtube.com/watch?v=SK_7AhHNZ0M&ab_channel=Abstractprogrammer)

### Find Ubuntu IP Address
Before you can add port forwarding rule, you will need to know the IP address of the Ubuntu instance.

On all my instances, it has always been `10.0.2.15`

The easiest way is to run either pyspark or spark-shell: both report the IP address in the URL

Or you can run:
```shell
ip a
```

### Add Port Forward Rules
From the Machine Menu select `Devices > Network > Network Settings...`

Under Adapter 1, select Advanced > Port Forwarding

Add a new rule (the green + on the right)

| Name    | Protocol | Host IP   | Host Port | Guest IP  | Guest Port |
|---------|----------|-----------|-----------|-----------|------------|
| Jupyter | TCP      | 127.0.0.1 | 8888      | 10.0.2.15 | 8888       |
| Spark   | TCP      | 127.0.0.1 | 4040      | 10.0.2.15 | 4040       |

Click OK to save and close, OK again to close Network dialog

Jupyter requires additional steps to enable external access, whereas Spark should now be accessible from the Host machine.

### Configure Jupyter for External Access

In this step we will create a config file for jupyter, add required parameters to config file, and finally generate and add a password hash to the config file

#### Create Jupyter Config File

```shell
jupyter notebook --generate-config
```

Take note of the location of the file: e.g. `/home/<username>/.jupyter/jupyter_notebook_config.py` 

Open the file for editing:
```shell
nano /home/<username>/.jupyter/jupyter_notebook_config.py
```

Add the following lines just below the line `c = get_config()`
```shell
c.IPKernelApp.pylab = 'inline' # if you want plotting support always in your notebook
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'password-hash'
c.NotebookApp.port = 8888
```

Leave the editor open, we still need to update the password-hash

#### Generate a Password Hash

In a new terminal run:
```shell
ipython -c "from notebook.auth import passwd; passwd()"
```

Answer the prompts, and copy the response: e.g. `'argon2:$argon2id$v=19$m=10240,t=10,p=8$+KB0t20KQobWiUSHzx8eww$AKqxzE07Ox9OQpCuRErwaseKqiOXAVotH4kZTMKCHUw'`

Past the response into the jupyter config: Take care about preserving the single quotes
```shell
c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$+KB0t20KQobWiUSHzx8eww$AKqxzE07Ox9OQpCuRErwaseKqiOXAVotH4kZTMKCHUw'
```

Save config and exit

#### Verify Access

Run jupyter:
```shell
cd ~/python-workspace
jupyter notebook
```

From the Host machine, open a browser and enter [http://127.0.0.1:8888](http://127.0.0.1:8888) (or the host port you configured above)

You will be prompted for the password you just generated for the config

You should now have access to the notebooks on the Ubuntu instance