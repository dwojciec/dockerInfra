1. AWS Command Line Interface
2. s3fs-container (inspired from https://github.com/childsb/s3fs-container)


# AWS Command Line Interface 
The [AWS Command Line Interface (CLI)](http://docs.aws.amazon.com/cli/latest/reference/) is a unified tool to manage your AWS services.

# Install awscli as a container


### Create the aws cli docker container

```bash 
$ docker build -t relocaio/awscli -f Dockerfileawscli .
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
relocaio/infra      latest              b7dbbfdbbfea        5 days ago          495.8 MB
relocaio/s3fs       latest              b7dbbfdbbfea        5 days ago          495.8 MB
relocaio/awscli     latest              9c1fe9de54db        5 days ago          486.2 MB
```




AWSCLI can also be run __inside a container__, from a small bash script wrapper. To install AWSCLI as a container run :


```bash
$ curl -L https://github.com/dwojciec/dockerInfra/releases/download/1.0/run.sh  > /usr/local/bin/aws
$ chmod +x /usr/local/bin/aws
```

# Usage 
export your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environnement variables 
and you can use aws command like :

Example:
```bash
$ export AWS_ACCESS_KEY_ID=long_generated_id
$ export AWS_SECRET_ACCESS_KEY=long_gernated_secret
$ aws s3 ls
2016-02-05 13:09:37 cf-templates-1kyyl1pl5ag0r-eu-west-1
2015-10-28 09:42:32 cf-templates-1kyyl1pl5ag0r-us-east-1
2016-03-31 09:28:40 ebs-staging
2016-02-05 09:58:02 sandbox1-stormio
$ aws s3 ls s3://ebs-staging --region eu-central-1
                           PRE test/
2016-03-30 16:31:22          0 -
2016-03-30 16:24:28      10240 aws-test.tar.gz
2016-04-04 09:57:25          0 juju
2016-04-04 16:24:57    8815410 osxfuse-2.8.3.dmg
2016-04-04 09:57:28          0 qwerty
2016-04-04 09:57:30          0 toto
2016-04-05 08:59:15          0 tuesday
2016-04-04 09:57:33          0 tutu
2016-04-04 09:58:28          0 zuzu
2016-04-04 10:12:23          0 zzzz
```
 
 
# s3fs-container
This docker container uses the s3fs packge to FUSE mount s3 buckets.  The container is setup to export the s3 mount to host.  Just run the container, and mount your s3 bucket with no extra packages!

# Usage
This container uses a new feature in Docker 1.10 which allows a container to share the hosts mount namespace.  Once docker is up and running you can build the container with __b.sh__.

```bash
docker build -t relocaio/s3fs -f Dockerfilefuse .
```


You'll need to set your s3 username and secret.  Either modify mount.sh or add the following to your ~/.bashrc:
```bash
export S3User=long_generated_id
export S3Secret=long_gernated_secret
```
To mount a s3 bucket run:
```bash
./mount.sh bucket mountpoint
```

_Example:_
```bash
./mount.sh ebs-staging /mnt/ec2
```
The docker container launches and remains running.  To stop you can ctrl+c.  While the container is running the bucket remains mounted.  You can now access the s3 bucket as a local directory!

# Example

```bash
$ sudo mkdir -p /mnt/ec2
sudo mount --bind /mnt/ec2 /mnt/ec2
sudo mount --make-shared /mnt/ec2
export S3User=.............
export S3Secret=.............
./mount_debug.sh ebs-staging /mnt/ec2
FUSE library version: 2.9.2
nullpath_ok: 0
nopath: 0
utime_omit_ok: 0
unique: 1, opcode: INIT (26), nodeid: 0, insize: 56, pid: 0
INIT: 7.23
flags=0x0003f7fb
max_readahead=0x00020000
* About to connect() to ebs-staging.s3.amazonaws.com port 80 (#0)
*   Trying 54.231.194.44...
* Connected to ebs-staging.s3.amazonaws.com (54.231.194.44) port 80 (#0)
> GET / HTTP/1.1
Accept: */*
```

Open another __Terminal__ window session 

```bash
$ ls -ltr /mnt/ec2
total 8624
----------    1 root     root         10240 Mar 30 16:24 aws-test.tar.gz
----------    1 root     root             0 Mar 30 16:31 -
-rw-r--r--    1 docker   staff            0 Apr  4 09:37 toto
drwxr-xr-x    1 docker   staff            0 Apr  4 09:38 test/
-rw-r--r--    1 docker   staff            0 Apr  4 09:48 tutu
-rw-r--r--    1 docker   staff            0 Apr  4 09:50 qwerty
-rw-r--r--    1 docker   staff            0 Apr  4 09:56 juju
-rw-r--r--    1 docker   staff            0 Apr  4 09:58 zuzu
-rw-r--r--    1 root     root             0 Apr  4 10:12 zzzz
-rw-r--r--    1 root     root       8815410 Apr  4 16:24 osxfuse-2.8.3.dmg
-rw-r--r--    1 docker   staff            0 Apr  5 08:59 tuesday
$ touch /mnt/ec2/wednesday
$ ls -ltr /mnt/ec2
total 8625
----------    1 root     root         10240 Mar 30 16:24 aws-test.tar.gz
----------    1 root     root             0 Mar 30 16:31 -
-rw-r--r--    1 docker   staff            0 Apr  4 09:37 toto
drwxr-xr-x    1 docker   staff            0 Apr  4 09:38 test/
-rw-r--r--    1 docker   staff            0 Apr  4 09:48 tutu
-rw-r--r--    1 docker   staff            0 Apr  4 09:50 qwerty
-rw-r--r--    1 docker   staff            0 Apr  4 09:56 juju
-rw-r--r--    1 docker   staff            0 Apr  4 09:58 zuzu
-rw-r--r--    1 root     root             0 Apr  4 10:12 zzzz
-rw-r--r--    1 root     root       8815410 Apr  4 16:24 osxfuse-2.8.3.dmg
-rw-r--r--    1 docker   staff            0 Apr  5 08:59 tuesday
-rw-r--r--    1 docker   staff            0 Apr  5 15:05 wednesday
```

# s3fs-fuse
The container uses s3fs-fuse found here: https://github.com/s3fs-fuse/s3fs-fuse

# Notes
If you have any issue with the :shared inside the docker run command associated to the volume -v you have to check if the host mountpoint is __shared__. 

To share it (mountpoint.sh /mnt/ec2)

```bash
sudo mount --bind /mnt/ec2 /mnt/ec2 
sudo mount --make-shared /mnt/ec2
```

If you are receiving this error :
__Transport endpoint is not connected__

try :

```bash
sudo fusermount -uz /mountpoint
``` 

Tests *done and validated* on OSX through a Virtualbox docker-machine and on AWS EC2 using 14.04 Trusty Ubuntu AMI
