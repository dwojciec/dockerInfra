# Mongodb container 
# Using Centos base image  and mongodb  
# Version 1
FROM centos:latest
USER root
MAINTAINER didier wojciechowski <didier@reloca.io>

# copy mongodb repo
COPY mongodb-org-3.2.repo /etc/yum.repos.d/mongodb-org-3.2.repo

# Update image
RUN yum -y update; yum clean all 

# Install Mongodb
RUN yum -y install mongodb-org which wget; yum clean all
RUN mkdir -p /var/lib/mongo 

# Create riouser user
RUN mkdir -p /home/riouser && \
groupadd -r riouser -g 433 && \
useradd -u 431 -r -g riouser -d /home/riouser -s /sbin/nologin -c "Docker image user" riouser && \
chown -R riouser:riouser /home/riouser

RUN echo "riouser:riouser" | chpasswd

RUN mkdir -p /home/riouser/.ssh; chown riouser /home/riouser/.ssh; chmod 700 /home/riouser/.ssh
#ADD ./authorized_keys /home/riouser/.ssh/
#ADD ./authorized_keys /root/.ssh/


RUN mkdir -p /home/mongodb && \
groupadd -r mongodb -g 65534 && \
useradd -u 102 -r -g mongodb -d /home/mongodb -s /bin/bash -c "mongodb image user" mongodb && \
chown -R mongodb:mongodb /home/mongodb

RUN echo "riouser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 
RUN chown -R mongodb:mongodb /var/lib/mongo
# Copy config mongodb
ADD etc/ /etc/

# User
#USER mongodb

# Mountable directories
VOLUME ["/var/lib/mongo"]

# Set the environment variables
ENV HOME /var/lib/mongo

# Working directory
WORKDIR /var/lib/mongo

ENTRYPOINT ["/bin/mongod"]
CMD ["-f", "/etc/mongod.conf"]

# Expose ports.

EXPOSE 27017/tcp
