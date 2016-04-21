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
llcf6:relocaio$  git clone -b master git@github.com:dwojciec/dockerInfra.git && cd dockerInfra
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
```bash

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

EVE REST/API server validation:

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
```
$ docker exec -it relocaio_db_1 bash
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

```
docker exec -it relocaio_db_1 tail -f /var/log/mongodb/mongod.log
```

### access to the mongodb

docker exec -it relocaio_db_1 mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT"

### Issue found with --volumes option for Mongodb :

``` 2016-03-14T15:45:13.313+0000 E STORAGE  [initandlisten] WiredTiger (22) [1457970313:313814][1:0x7fd837f7ddc0], connection: : fsync: Invalid argument
2016-03-14T15:45:13.315+0000 I -        [initandlisten] Fatal Assertion 28561
2016-03-14T15:45:13.315+0000 I -        [initandlisten]
```

docker run --name mongodbtest -d --restart=always --publish 27018:27017 --volume /Users/RELOCA/mongodb:/var/lib/mongo reloca/mongodb

bug opened: 
see <https://github.com/mvertes/docker-alpine-mongo/issues/1>


## Inserting data into Mongodb database
docker inspect --format="{{.Config.Hostname}}" reloca_db_1

docker exec -it reloca_db_1 sh -c 'exec mongo "1417768a7c2c:27017/relocadb"'

### To identify hostname of our container 
dockhostname() {
  docker inspect --format='{{.Config.Hostname}}' "$@"
}

dockhostname reloca_db_1
