# Web Socket programming example

Control client's computer from the server!

To achieve this, run [client.py](client.py) on the client's server and run [server.py](server.py) file on the server.

Then type the commands from the server to execute them on the client's computer.

---

# To run server.py file in AWS EC2 instance:
 
* Create and launch an EC2 instance. (linux, windows...any)
* Edit the Security Group and add all traffic with source 0.0.0.0/0. (There might be a specific protocol..I'll mention later)
* Open terminal for instance. (Maybe using PuTTY)
* Install python3 if not installed.
* Now save and run the [server.py](server.py) file in the instance.


Run to check is python3 is installed

```bash
[ec2-user ~]$ yum list installed | grep -i python3
```

If python3 is not installed then you'll see the following

```bash
[ec2-user ~]$ yum list installed | grep -i python3
[ec2-user ~]$

[ec2-user ~]$ python3
-bash: python3: command not found
```

Python 3 already installed output example:

```bash
[ec2-user ~]$ yum list installed | grep -i python3

python3.x86_64                        3.7.4-1.amzn2.0.4              @amzn2-core
python3-libs.x86_64                   3.7.4-1.amzn2.0.4              @amzn2-core
python3-pip.noarch                    9.0.3-1.amzn2.0.1              @amzn2-core
python3-setuptools.noarch             38.4.0-3.amzn2.0.6             @amzn2-core

[ec2-user ~]$ whereis python3
python3: //usr/bin/python3 /usr/bin/python3.7 /usr/bin/python3.7m /usr/lib/python3.7 /usr/lib64/python3.7 /us
```

If Python 3 isn't already installed, then install the package using the yum package manager.

```bash
[ec2-user ~]$ sudo yum install python3 -y
```