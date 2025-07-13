FROM redhat/ubi9:latest 

# Install packages of httpd server 
RUN yum install httpd -y 

# copy source code in /var/www/html 
COPY src/  /var/www/html 

# Default running port 
EXPOSE 80 

# start httpd service 
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]