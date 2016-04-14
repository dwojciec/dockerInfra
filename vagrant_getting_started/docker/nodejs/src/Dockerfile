FROM    centos:centos6
MAINTAINER reloca.io
# Enable Extra Packages for Enterprise Linux (EPEL) for CentOS
RUN     yum install -y epel-release

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV RLB_DATABASE_URI=mongodb://mongo/nodejsapp \ 
    RLB_HTTP_HOST=0.0.0.0 \
    RLB_HTTP_PORT=8080 

# Install Node.js and npm
RUN     yum install -y nodejs npm

# Create user node
RUN groupadd -r node \
&&  useradd -r -g node node

# Install app dependencies
COPY package.json ./package.json
RUN set -x \
&& npm install --production \
&& npm dedupe \
&& npm cache clean \
&& rm -rf /tmp/npm* 

# Bundle app source
COPY . . 

USER node
EXPOSE  8080
# Switch to app user to start process
CMD ["npm", "start"]
