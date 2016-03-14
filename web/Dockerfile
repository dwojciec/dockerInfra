# EVE container 
# Using Centos base image and EVE REST API Framework  
# Version 1
FROM centos:latest
USER root
MAINTAINER didier wojciechowski <didier@reloca.io>


# Update image
RUN yum -y update; yum clean all && \
 yum -y install epel-release; yum clean all

RUN INSTALL_PKGS="gcc python-devel.x86_64 python-pip python-yaml sudo" && \
    yum install -y $INSTALL_PKGS && \
    yum clean all 

# Create riouser user
RUN mkdir -p /home/riouser && \
groupadd -r riouser -g 433 && \
useradd -u 431 -r -g riouser -d /home/riouser -s /sbin/nologin -c "Docker image user" riouser && \
chown -R riouser:riouser /home/riouser

RUN echo "riouser:riouser" | chpasswd

RUN mkdir -p /home/riouser/.ssh; chown riouser /home/riouser/.ssh; chmod 700 /home/riouser/.ssh
#ADD ./authorized_keys /home/riouser/.ssh/
#ADD ./authorized_keys /root/.ssh/

RUN echo "riouser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


COPY ./app /app

# Install EVE REST API Framework
RUN pip install eve

EXPOSE 5000 80 81
