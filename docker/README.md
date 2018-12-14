# Installation
## docker-compose

Install docker-compose by following [these](https://docs.docker.com/compose/install/#install-compose) directions:

    sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

## /etc/hosts

Append the following hosts to the hosts file for ease of local development:

    127.0.0.1 gbd.com
    127.0.0.1 api.gbd.com
    127.0.0.1 app.gbd.com
    127.0.0.1 www.gbd.com

Note that nginx is configured for development. 

# Development

Change directories into the docker dir to control containers through docker compose:

    cd docker
    sudo docker-compose up -d
    sudo docker-compose down
    etc.

Access the development environment at app.gbd.com while the reverse proxy and web app are running.
