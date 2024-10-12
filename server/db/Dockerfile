# Use the official MySQL 8.0 image as a base
FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=superSecretPassword
ENV MYSQL_DATABASE=killteam
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=admin

# Expose the MySQL port
EXPOSE 3306

# Mount the volume for persistent data storage
VOLUME /var/lib/mysql

# Start the MySQL service
CMD ["mysqld_safe"]