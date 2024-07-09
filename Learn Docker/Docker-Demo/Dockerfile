# #starting from an existing templete which is ubuntu
# #this base image gets pull down from the cloud
FROM ubuntu:latest 

# #installing dependencies to our image
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && apt-get update \
    && apt-get install -y sl

# #terminal command to run environmental variables
ENV PORT=8080

# #Default command that executed when we start the container
CMD [ "echo", "Learning Docker is fun, as of now 😊" ]

