## Setting up a development environment using Docker and Vagrant

![image](https://github.com/dwojciec/dockerInfra/blob/master/images/docker%2Bvagrant.jpg)

Docker and Vagrant can be used together to build isolated and repeatable development environments. 
![image](https://github.com/dwojciec/dockerInfra/blob/master/images/vagrant-docker.png)

### Run Docker containers in a custom Docker host

Create the VM host called _dockerhostvm_ file __DockerHostVagrantfile__

```
Vagrant.configure("2") do |config| 
 config.vm.provision "docker"  
  config.vm.provision "shell", inline:
   "ps aux | grep 'sshd:' | awk '{print $2}' | xargs kill" 
     config.vm.define "dockerhostvm"
     config.vm.box = "ubuntu/trusty64" 
     config.vm.provider :virtualbox do |vb|
     vb.name = "dockerhostvm"
  end  
 end 
```

Create docker container called _reloca-container_ file __Vagrantfile__. I will create and run a very simple Docker container, based on the Ubuntu 14.04 image. The container will do very little of interest: it pings localhost 10 times and exits. 

```
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
DOCKER_HOST_NAME = "dockerhostvm"
DOCKER_HOST_VAGRANTFILE = "./DockerHostVagrantfile"
 
Vagrant.configure("2") do |config|
 
 config.vm.synced_folder ".", "/user/local/src"
 config.vm.define "reloca-container" do |m|
 
        m.vm.provider :docker do |d|
          d.name = 'reloca-container'
          d.build_dir = "."
          d.cmd = ["ping", "-c 10", "127.0.0.1"]
          d.remains_running = true
          d.vagrant_machine = "#{DOCKER_HOST_NAME}"
          d.vagrant_vagrantfile = "#{DOCKER_HOST_VAGRANTFILE}"
        end
 end
end
```

The dockerfile used by the _reloca-container_ is 

```
FROM ubuntu:14.04
 
RUN mkdir /u01 && \
chmod a+xr /u01
COPY readme.txt /u01/
```

### The command to get things started is :  _vagrant up_ 

The vagrant logging show the creation of the _dockerhostvm_ Virtual Box VM:

```
t:vagrant_getting_started $ vagrant up
Bringing machine 'reloca-container' up with 'docker' provider...
==> reloca-container: Docker host is required. One will be created if necessary...
    reloca-container: Vagrant will now create or start a local VM to act as the Docker
    reloca-container: host. You'll see the output of the `vagrant up` for this VM below.
    reloca-container:  
    dockerhostvm: Importing base box 'ubuntu/trusty64'...
    dockerhostvm: Matching MAC address for NAT networking...
    dockerhostvm: Checking if box 'ubuntu/trusty64' is up to date...
    dockerhostvm: Setting the name of the VM: dockerhostvm
    dockerhostvm: Clearing any previously set forwarded ports...
    dockerhostvm: Clearing any previously set network interfaces...
    dockerhostvm: Preparing network interfaces based on configuration...
    dockerhostvm: Adapter 1: nat
    dockerhostvm: Forwarding ports...
    dockerhostvm: 22 (guest) => 2222 (host) (adapter 1)
    dockerhostvm: Booting VM...
    dockerhostvm: Waiting for machine to boot. This may take a few minutes...
    dockerhostvm: SSH address: 127.0.0.1:2222
    dockerhostvm: SSH username: vagrant
    dockerhostvm: SSH auth method: private key
    dockerhostvm: 
    dockerhostvm: Vagrant insecure key detected. Vagrant will automatically replace
    dockerhostvm: this with a newly generated keypair for better security.
    dockerhostvm: 
    dockerhostvm: Inserting generated public key within guest...
    dockerhostvm: Removing insecure key from the guest if it's present...
    dockerhostvm: Key inserted! Disconnecting and reconnecting using new SSH key...
    dockerhostvm: Machine booted and ready!
    dockerhostvm: Checking for guest additions in VM...
    dockerhostvm: The guest additions on this VM do not match the installed version of
    dockerhostvm: VirtualBox! In most cases this is fine, but in rare cases it can
    dockerhostvm: prevent things such as shared folders from working properly. If you see
    dockerhostvm: shared folder errors, please make sure the guest additions within the
    dockerhostvm: virtual machine match the version of VirtualBox you have installed on
    dockerhostvm: your host and reload your VM.
    dockerhostvm: 
    dockerhostvm: Guest Additions Version: 4.3.36
    dockerhostvm: VirtualBox Version: 5.0
    dockerhostvm: Mounting shared folders...
    dockerhostvm: /vagrant => /Users/RELOCA/vagrant_getting_started
    dockerhostvm: Running provisioner: docker...
    dockerhostvm: Installing Docker onto machine...
    dockerhostvm: Running provisioner: shell...
    dockerhostvm: Running: inline script
    dockerhostvm: stdin: is not a tty
==> reloca-container: Syncing folders to the host VM...
    dockerhostvm: Mounting shared folders...
    dockerhostvm: /var/lib/docker/docker_1458578330_7526 => /Users/RELOCA/vagrant_getting_started
    dockerhostvm: /var/lib/docker/docker_build_64af429a682c74964811f5489a51f192 => /Users/RELOCA/vagrant_getting_started
==> reloca-container: Building the container from a Dockerfile...
    reloca-container: Sending build context to Docker daemon 50.69 kB
    reloca-container: Step 1 : FROM ubuntu:14.04
    reloca-container: 14.04: Pulling from library/ubuntu
    reloca-container: 203137e8afd5: Pulling fs layer
    reloca-container: 2ff1bbbe9310: Pulling fs layer
    reloca-container: 933ae2486129: Pulling fs layer
    reloca-container: a3ed95caeb02: Pulling fs layer
    reloca-container: a3ed95caeb02: Waiting
    reloca-container: 933ae2486129: Verifying Checksum
    reloca-container: 933ae2486129: Download complete
    reloca-container: 2ff1bbbe9310: Verifying Checksum
    reloca-container: 2ff1bbbe9310: Download complete
    reloca-container: a3ed95caeb02: Verifying Checksum
    reloca-container: a3ed95caeb02: Download complete
    reloca-container: 203137e8afd5: Verifying Checksum
    reloca-container: 203137e8afd5: Download complete
    reloca-container: 203137e8afd5: Pull complete
    reloca-container: 203137e8afd5: Pull complete
    reloca-container: 2ff1bbbe9310: Pull complete
    reloca-container: 2ff1bbbe9310: Pull complete
    reloca-container: 933ae2486129: Pull complete
    reloca-container: 933ae2486129: Pull complete
    reloca-container: a3ed95caeb02: Pull complete
    reloca-container: a3ed95caeb02: Pull complete
    reloca-container: Digest: sha256:1c8b813b6b6656e9a654bdf29a7decfcc73b92a62b934adc4253b0dc2be9d0a2
    reloca-container: Status: Downloaded newer image for ubuntu:14.04
    reloca-container:  ---> 97434d46f197
    reloca-container: Step 2 : RUN mkdir /u01 && chmod a+xr /u01
    reloca-container:  ---> Running in 6afc331328fc
    reloca-container:  ---> 27e720dcb669
    reloca-container: Removing intermediate container 6afc331328fc
    reloca-container: Step 3 : COPY readme.txt /u01/
    reloca-container:  ---> c99be0f85471
    reloca-container: Removing intermediate container fd6bc0a93bc7
    reloca-container: Successfully built c99be0f85471
    reloca-container: 
    reloca-container: Image: c99be0f85471
==> reloca-container: Warning: When using a remote Docker host, forwarded ports will NOT be
==> reloca-container: immediately available on your machine. They will still be forwarded on
==> reloca-container: the remote machine, however, so if you have a way to access the remote
==> reloca-container: machine, then you should be able to access those ports there. This is
==> reloca-container: not an error, it is only an informational message.
==> reloca-container: Creating the container...
    reloca-container:   Name: reloca-container
    reloca-container:  Image: c99be0f85471
    reloca-container:    Cmd: ping -c 10 127.0.0.1
    reloca-container: Volume: /var/lib/docker/docker_1458578330_7526:/user/local/src
    reloca-container:  
    reloca-container: Container created: 6dfb37dc45c01c3a
==> reloca-container: Starting container...
==> reloca-container: Provisioners will not be run since container doesn't support SSH.
```

With vagrant global-status, we can check on the machines that Vagrant controls. The result from our recent activities is that two entries have been added: the _dockerhostvm_ (created by the virtualbox provider) and the _reloca-container_ , provided through the docker provider (inside the dockerhostvm – although we cannot tell that fact from this listing).


```
llcf6:vagrant_getting_started$ vagrant global-status
id       name                provider   state              directory                                                 
---------------------------------------------------------------------------------------------------------------------
0870deb  dockerhostvm        virtualbox running            /Users//RELOCA/vagrant_getting_started 
026d781  reloca-container    docker     stopped            /Users//RELOCA/vagrant_getting_started 
```

If you want vagrant to act on the VirtualBox machine _dockerhostvm_ , the command need to make use of the id of the VM - for example __vagrant ssh 0870deb__ 
```(vagrant ssh <machine id for dockerhostvm>)```

```
llcf6:vagrant_getting_started $ vagrant ssh 0870deb
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-83-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Mon Mar 21 16:40:22 UTC 2016

  System load:  0.36              Processes:              86
  Usage of /:   5.0% of 39.34GB   Users logged in:        0
  Memory usage: 37%               IP address for eth0:    10.0.2.15
  Swap usage:   0%                IP address for docker0: 172.17.0.1

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud


*** System restart required ***
Last login: Mon Mar 21 16:40:22 2016 from 10.0.2.2

vagrant@vagrant-ubuntu-trusty-64:~$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                         PORTS               NAMES
2bbd026f888a        c99be0f85471        "/bin/bash"              About an hour ago   Exited (0) About an hour ago                       sick_meitner
75aa81af6cab        c99be0f85471        "/bash"                  About an hour ago   Created                                            insane_meninsky
6dfb37dc45c0        c99be0f85471        "ping '-c 10' 127.0.0"   About an hour ago   Exited (0) About an hour ago                       reloca-container
vagrant@vagrant-ubuntu-trusty-64:~$ docker start -i reloca-container
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.030 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.072 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.049 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=6 ttl=64 time=0.053 ms
64 bytes from 127.0.0.1: icmp_seq=7 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=8 ttl=64 time=0.046 ms
64 bytes from 127.0.0.1: icmp_seq=9 ttl=64 time=0.045 ms
64 bytes from 127.0.0.1: icmp_seq=10 ttl=64 time=0.050 ms

--- 127.0.0.1 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9010ms
rtt min/avg/max/mdev = 0.030/0.044/0.072/0.014 ms
vagrant@vagrant-ubuntu-trusty-64:~$ 



```

