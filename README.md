# learning-spark

## Setting up local dev environment

A PAIN in the ass to get right...

Primary issues:
* Python3 PIP on Ubuntu - could not get it to install properly on Ubuntu 16.04 

Set Up Windows System:
1. Install VirtualBox
2. Create an Ubuntu 20.04 VirtualBox instance (latest stable?)
   * Select `Skip Unattended Installation`
   * 2 CPU/4GB Memory
   * 25GiB Disk - FIXED
   * Enable EFI (helps with video display)
3. Watched the following video to (finally) get jupyter working: [How to Setup Jupyter Notebook in Any Cloud Server in under 7 minutes! - Ubuntu 20.04](https://www.youtube.com/watch?v=Dq1phGV-7fI&ab_channel=TheLinuxOS)
4. Installation (Shell Steps):    
   ```shell
    sudo apt-get update -y
    sudo apt-get upgrade -y
    sudo apt-get install build-essentials libssl-dev libpq-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip -y
    sudo apt-get install supervisor -y
    sudo apt-get install python3-pip python3-dev python3-venv -y
    sudo apt-get install nano -y
    sudo apt-get install git -y
    sudo apt-get install ngnix curl -y
    sudo apt-get autoremove -y 
    
    sudo python3 -m pip install jupyter
    jupyter notebook --generate-config
    ```

5. Run Jupyter! `jupyter notebook`

## PySpark