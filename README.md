# Create a developement workspace on your laptop
1. Run Terminal 
2. create directory
3. clone the Project git repository

```
Last login: Mon Mar 21 16:59:22 on ttys005
llcf6:~ $ pwd
/Users/
llcf6:~ $ mkdir relocaio
llcf6:~ $ cd relocaio
llcf6:relocaio$  git clone -b master https://github.com/dwojciec/dockerInfra.git && cd dockerInfra
Cloning into 'dockerInfra'...
Warning: Permanently added the RSA host key for IP address '192.30.252.129' to the list of known hosts.
remote: Counting objects: 65, done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 65 (delta 7), reused 0 (delta 0), pack-reused 44
Receiving objects: 100% (65/65), 83.89 KiB | 0 bytes/s, done.
Resolving deltas: 100% (18/18), done.
Checking connectivity... done.
llcf6:relocaio$ pwd
/Users/relocaio/dockerInfra
llcf6:dockerInfra $ ls
README.md		images			vagrant_getting_started
lcf6:dockerInfra $ cd vagrant_getting_started/
llcf6:vagrant_getting_started $ pwd
/Users/relocaio/dockerInfra/vagrant_getting_started
llcf6:vagrant_getting_started $ ls
DockerHostVagrantfile
Dockerfile
Setting up a development environment using Docker and Vagrant.md
Vagrantfile
readme.txt
```

## Creation of the VM hosting docker
 
  - using Docker-machine 


###  Using docker-machine to build VM

Build VM

```
docker-machine create --driver virtualbox <name_of_vm>

```
example

```
docker-machine create --driver virtualbox developpement

```

Set new environment. It's very important before running docker-compose

```
docker-machine env <name_of_vm> && \
eval "$(docker-machine env <name_of_vm>)"
```

Now we are ready to create our different docker containers.


# Installation
build images and containers using docker compose.
You are on your laptop directory where you dowloaded the GIT repository (Create a developement workspace).

Go to your workspace directory 
```bash
 cd /Users/<myWokspace>/dockerInfra/vagrant_getting_started/docker
```
Into this directory you will find a docker-compose.yml file and you will execute it from your Workspace directory.

```bash
$ eval "$(docker-machine env <name_of_vm>)"
$ pwd
/Users/<myWokspace>/dockerInfra/vagrant_getting_started/docker
$ls
aws			docker-compose.yml	nodejs
db			mongodb			web
$ docker-compose -f docker-compose.yml -p relocaio up -d
```

To access to the Docker VM

```bash
$ docker-machine ssh <name_of_vm>
```

To check docker images created by the docker-compose command:

```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
relocaio/nodejs     latest              907e83d52b84        3 minutes ago       489.9 MB
relocaio/eve        latest              f36e62da3cc7        6 minutes ago       334.1 MB
relocaio/mongodb    latest              2f7eadb88693        8 minutes ago       487.6 MB
centos              centos6             fc73b108c5ae        2 weeks ago         228.9 MB
centos              latest              778a53015523        2 weeks ago         196.7 MB
```

To validate the docker container running after the docker-compose command:

```bash
docker@developement:~$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                NAMES
410936b519f5        relocaio/nodejs     "npm start"              32 seconds ago      Up 32 seconds       0.0.0.0:49160->8080/tcp                              relocaio_nodejs_1
894b3cf61969        relocaio/eve        "python -u /app/run.p"   2 minutes ago       Up 2 minutes        0.0.0.0:80->80/tcp, 0.0.0.0:5000->5000/tcp, 81/tcp   relocaio_eve_1
1f3d0e8a2882        relocaio/mongodb    "/bin/mongod -f /etc/"   4 minutes ago       Up 4 minutes        0.0.0.0:27017->27017/tcp                             relocaio_mongo1_1
```


To check network created: 

```bash
docker@developement:~$ docker network ls
NETWORK ID          NAME                  DRIVER
b05af21b8db8        bridge                bridge              
1bcb0e75ba46        host                  host                
f0bcec8077eb        none                  null                
c8ab5918d5e3        relocaio_back-tier    bridge              
58c84efb4a57        relocaio_front-tier   bridge 
```


EVE REST/API server validation from local VM:

```bash
$ curl -i http://localhost:80
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 91
WWW-Authenticate: Basic realm="eve"
Cache-Control: max-age=20
Expires: Thu, 21 Apr 2016 09:30:26 GMT
Server: Eve/0.6.3 Werkzeug/0.11.3 Python/2.7.5
Date: Thu, 21 Apr 2016 09:30:06 GMT

{"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}}
```

To test it outside the VM. From your laptop you have to be sure that the port used by the EVE container (here 80) is forwarded by the VM (DOCKER_HOST IP) and you can use a browser or a application like PAW (MAC OSX) or Postman.

example :

```bash
$ docker-machine env developement
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.103:2376"
export DOCKER_CERT_PATH="/Users/.docker/machine/machines/developement"
export DOCKER_MACHINE_NAME="developement"
```

You can test the URL link http://192.168.99.103:80 

![image](https://github.com/dwojciec/dockerInfra/blob/master/images/Postman_eve.png)

To validate the nodejs container. You need to know the IP of your nodejs container using this command :

![image](https://github.com/dwojciec/dockerInfra/blob/master/images/Postman_eve.png)

```bash
docker@developement:~$ docker inspect relocaio_nodejs_1 | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.18.0.3",
                    
docker@developement:~$ curl -i http://172.18.0.3:8080
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 12
Date: Thu, 21 Apr 2016 10:27:40 GMT
Connection: keep-alive

Hello world
```
To access from your laptop you have to use the IP address of your DOCKER_HOST (here 192.168.99.103) and the port 49160
. http://192.168.99.103:49160

```bash
$ curl -i http://192.168.99.103:49160
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 12
Date: Thu, 21 Apr 2016 13:54:34 GMT
Connection: keep-alive

Hello world
```

From my Terminal session or from a browser  :

```bash
$ curl -i localhost:8080
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 66
Server: Eve/0.6.3 Werkzeug/0.11.3 Python/2.7.5
Date: Tue, 22 Mar 2016 11:29:12 GMT

{"_links": {"child": [{"href": "contacts", "title": "contacts"}]}}
```

## To connect to your Mongodb container
```bash
$ docker exec -it relocaio_mongo1_1 bash
bash-4.2# cd /var/log/mongodb
bash-4.2# ls
mongod.log
bash-4.2# tail -f mongod.log 
2016-03-22T11:13:23.175+0000 D STORAGE  [initandlisten] create collection local.startup_log { capped: true, size: 10485760 }
2016-03-22T11:13:23.175+0000 D STORAGE  [initandlisten] stored meta data for local.startup_log @ RecordId(1)
2016-03-22T11:13:23.176+0000 I NETWORK  [HostnameCanonicalizationWorker] Starting hostname canonicalization worker
2016-03-22T11:13:23.176+0000 D COMMAND  [PeriodicTaskRunner] BackgroundJob starting: PeriodicTaskRunner
2016-03-22T11:13:23.176+0000 D COMMAND  [ClientCursorMonitor] BackgroundJob starting: ClientCursorMonitor
2016-03-22T11:13:23.176+0000 D COMMAND  [TTLMonitor] BackgroundJob starting: TTLMonitor
2016-03-22T11:13:23.178+0000 D STORAGE  [initandlisten] local.startup_log: clearing plan cache - collection info cache reset
2016-03-22T11:13:23.178+0000 D STORAGE  [initandlisten] create uri: table:index-1-2701992292802169122 config: type=file,internal_page_max=16k,leaf_page_max=16k,checksum=on,prefix_compression=true,block_compressor=,,,,key_format=u,value_format=u,app_metadata=(formatVersion=6,infoObj={ "v" : 1, "key" : { "_id" : 1 }, "name" : "_id_", "ns" : "local.startup_log" }),
2016-03-22T11:13:23.182+0000 D STORAGE  [initandlisten] local.startup_log: clearing plan cache - collection info cache reset
2016-03-22T11:13:23.182+0000 I NETWORK  [initandlisten] waiting for connections on port 27017
```
or directly using this command

```bash
docker exec -it relocaio_mongo1_1 tail -f /var/log/mongodb/mongod.log
```


### Issue found with --volumes option for Mongodb :

```bash
2016-03-14T15:45:13.313+0000 E STORAGE  [initandlisten] WiredTiger (22) [1457970313:313814][1:0x7fd837f7ddc0], connection: : fsync: Invalid argument
2016-03-14T15:45:13.315+0000 I -        [initandlisten] Fatal Assertion 28561
2016-03-14T15:45:13.315+0000 I -        [initandlisten]
```

docker run --name mongodbtest -d --restart=always --publish 27018:27017 --volume /Users/RELOCA/mongodb:/var/lib/mongo reloca/mongodb

bug opened: 
see <https://github.com/mvertes/docker-alpine-mongo/issues/1>


## Inserting data into Mongodb database from the eve container 

```bash
docker exec -it relocaio_eve_1  sh -c 'exec python /app/mongoclientseeddata.py'
Connected successfully!!!
Database(MongoClient(host=['db01:27017'], document_class=dict, tz_aware=False, connect=True), u'relocaDB')
create user reloca
create row into restaurant collection
 create data into DB to execute some test
``` 
 
## Checking network rules associated with your VM

You can verify the port forwarded from your local VM. It's just a exemple using multiple Docker container.


```bash
$  VBoxManage list vms 
"default" {5a13f6e5-4ec3-4fe5-bf6e-01714ea5049f}
"relocaio" {bf447ecf-e747-43bf-a964-0722177f9961}
"relocaio2" {69d0806e-8d6b-4995-87b1-f576fffdbe19}
"developement" {1525a124-2864-48a9-b1df-3f4364f3e1d6}

$  VBoxManage showvminfo default  | grep "NIC 1"
NIC 1:           MAC: 080027D1C4C8, Attachment: NAT, Cable connected: on, Trace: off (file: none), Type: 82540EM, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
NIC 1 Settings:  MTU: 0, Socket (send: 64, receive: 64), TCP Window (send:64, receive: 64)
NIC 1 Rule(0):   name = 49152, protocol = udp, host ip = 127.0.0.1, host port = 49152, guest ip = , guest port = 49152
NIC 1 Rule(1):   name = docker, protocol = tcp, host ip = 127.0.0.1, host port = 4243, guest ip = , guest port = 4243
NIC 1 Rule(2):   name = gluster, protocol = tcp, host ip = 127.0.0.1, host port = 24007, guest ip = , guest port = 24007
NIC 1 Rule(3):   name = mongodb, protocol = tcp, host ip = 127.0.0.1, host port = 27017, guest ip = , guest port = 27017
NIC 1 Rule(4):   name = ssh, protocol = tcp, host ip = 127.0.0.1, host port = 55244, guest ip = , guest port = 22
NIC 1 Rule(5):   name = tcp1, protocol = tcp, host ip = 127.0.0.1, host port = 9345, guest ip = , guest port = 9345
NIC 1 Rule(6):   name = tcp2, protocol = tcp, host ip = 127.0.0.1, host port = 9346, guest ip = , guest port = 9346
NIC 1 Rule(7):   name = tcp3306, protocol = tcp, host ip = 127.0.0.1, host port = 3306, guest ip = , guest port = 3306
NIC 1 Rule(8):   name = tdp1, protocol = udp, host ip = 127.0.0.1, host port = 500, guest ip = , guest port = 500
NIC 1 Rule(9):   name = udp, protocol = udp, host ip = 127.0.0.1, host port = 24007, guest ip = , guest port = 24007
NIC 1 Rule(10):   name = udp2, protocol = udp, host ip = 127.0.0.1, host port = 4500, guest ip = , guest port = 4500
NIC 1 Rule(11):   name = udp24008, protocol = udp, host ip = 127.0.0.1, host port = 24008, guest ip = , guest port = 24008
NIC 1 Rule(12):   name = web, protocol = tcp, host ip = 127.0.0.1, host port = 5000, guest ip = , guest port = 5000
``` 

