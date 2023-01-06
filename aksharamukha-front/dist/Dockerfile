# our base image
FROM httpd:alpine

# Copy Quasar src files
ADD ./spa-mat /usr/local/apache2/htdocs/
COPY .htaccess /usr/local/apache2/htdocs/.htaccess

RUN sed -i '/LoadModule rewrite_module/s/^#//g' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's#AllowOverride [Nn]one#AllowOverride All#' /usr/local/apache2/conf/httpd.conf

WORKDIR /usr/local/apache2/htdocs/

# tell the port number the container should expose
EXPOSE 80
