# create a developement workspace
1. Run Terminal 
2. create directory
3. clone the git repository

```
Last login: Mon Mar 21 16:59:22 on ttys005
llcf6:~ $ pwd
/Users/
llcf6:~ $ mkdir relocaio
llcf6:~ $ cd relocaio
llcf6:relocaio$  git clone git@github.com:dwojciec/dockerInfra.git
Cloning into 'dockerInfra'...
Warning: Permanently added the RSA host key for IP address '192.30.252.129' to the list of known hosts.
remote: Counting objects: 65, done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 65 (delta 7), reused 0 (delta 0), pack-reused 44
Receiving objects: 100% (65/65), 83.89 KiB | 0 bytes/s, done.
Resolving deltas: 100% (18/18), done.
Checking connectivity... done.
llcf6:relocaio$ pwd
/Users/relocaio
llcf6:relocaio$ ls
dockerInfra
llcf6:relocaio $ cd dockerInfra/
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
llcf6:vagrant_getting_started $ vagrant up
```


# Setting up a development environment using __vagrant up__
Read [Setting up a development environment using Docker and Vagrant](https://github.com/dwojciec/dockerInfra/blob/master/vagrant_getting_started/Setting%20up%20a%20development%20environment%20using%20Docker%20and%20Vagrant.md) to provision your VM with docker installed 

## Connect to the vagrant VM
```
llcf6:vagrant_getting_started$ vagrant global-status
id       name                provider   state              directory                                                 
---------------------------------------------------------------------------------------------------------------------
976955c  dockerhostvm        virtualbox running            /Users/relocaio/dockerInfra/vagrant_getting_started 
8e134e7  reloca-container    docker     preparing          /Users/relocaio/dockerInfra/vagrant_getting_started
```

```
llcf6:vagrant_getting_started $ vagrant ssh 976955c
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-83-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Mon Mar 21 18:48:17 UTC 2016

  System load:  0.44              Processes:              87
  Usage of /:   4.5% of 39.34GB   Users logged in:        0
  Memory usage: 31%               IP address for eth0:    10.0.2.15
  Swap usage:   0%                IP address for docker0: 172.17.0.1

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud


vagrant@vagrant-ubuntu-trusty-64:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
<none>              <none>              129fa92c9eb9        About a minute ago   188 MB
ubuntu              14.04               97434d46f197        3 days ago           188 MB
vagrant@vagrant-ubuntu-trusty-64:~$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                          PORTS               NAMES
7ec181e6384d        129fa92c9eb9        "ping '-c 10' 127.0.0"   About a minute ago   Exited (0) About a minute ago                       reloca-container
vagrant@vagrant-ubuntu-trusty-64:~$ docker logs 7ec181e6384d
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.045 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.053 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.047 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.044 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.040 ms
64 bytes from 127.0.0.1: icmp_seq=6 ttl=64 time=0.060 ms
64 bytes from 127.0.0.1: icmp_seq=7 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=8 ttl=64 time=0.045 ms
64 bytes from 127.0.0.1: icmp_seq=9 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=10 ttl=64 time=0.037 ms

--- 127.0.0.1 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9000ms
rtt min/avg/max/mdev = 0.033/0.043/0.060/0.011 ms
vagrant@vagrant-ubuntu-trusty-64:~

```
 Our VM image is READY to use Docker container for our Development.
 
 Go to /vagrant directory.
 This directory /vagrant is mapped with the Workspace directory. 

## Installation

docker compose up

```
vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$ docker-compose -f docker-compose.yml -p relocaio up -d

vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
reloca/eve          latest              0ad471c67842        42 minutes ago      299.8 MB
reloca/mongodb      latest              1cab766b67f9        44 minutes ago      446.4 MB
<none>              <none>              f6fa19250713        48 minutes ago      188 MB
ubuntu              14.04               97434d46f197        3 days ago          188 MB
centos              latest              d0e7f81ca65c        2 weeks ago         196.6 MB
docker/compose      1.6.2               d2d56dd5ed11        3 weeks ago         57.96 MB

vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                NAMES
69ec8a1ffb4d        reloca/eve          "python -u /app/app.p"   9 minutes ago       Up 9 minutes        0.0.0.0:80->80/tcp, 0.0.0.0:5000->5000/tcp, 81/tcp   relocaio_web_1
31823ec17b31        reloca/mongodb      "/bin/mongod -f /etc/"   11 minutes ago      Up 11 minutes       0.0.0.0:27017->27017/tcp                             relocaio_db_1

vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$ curl -i http://localhost:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 66
Server: Eve/0.6.3 Werkzeug/0.11.3 Python/2.7.5
Date: Tue, 22 Mar 2016 11:25:11 GMT

{"_links": {"child": [{"href": "contacts", "title": "contacts"}]}}vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$ 
vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$
```

From my Terminal session or from a browser  :

```
llcf6: $ curl -i localhost:8080
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 66
Server: Eve/0.6.3 Werkzeug/0.11.3 Python/2.7.5
Date: Tue, 22 Mar 2016 11:29:12 GMT

{"_links": {"child": [{"href": "contacts", "title": "contacts"}]}}
```

## To connect to your Mongodb container
```
vagrant@vagrant-ubuntu-trusty-64:/vagrant/docker$ docker exec -it relocaio_db_1 bash
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
