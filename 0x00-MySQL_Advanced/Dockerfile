# Use the official Ubuntu 20.04 image
FROM ubuntu:20.04

# Update the package lists
RUN apt-get update

# Install MySQL Server
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server

# Install Python
RUN apt-get install -y python3

# Expose MySQL port
EXPOSE 3306

# Start MySQL service
CMD ["mysqld"]
