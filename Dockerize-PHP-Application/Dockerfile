FROM php:7.4-apache
RUN apt-get update && apt upgrade -y
RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable mysqli
ADD ./app /var/www/html
COPY ./app/my-site.conf /etc/apache2/sites-available/my-site.conf
RUN echo 'SetEnv MYSQL_DB_CONNECTION ${MYSQL_DB_CONNECTION}' >> /etc/apache2/conf-enabled/environment.conf
RUN echo 'SetEnv MYSQL_DB_NAME ${MYSQL_DB_NAME}' >> /etc/apache2/conf-enabled/environment.conf
RUN echo 'SetEnv MYSQL_USER ${MYSQL_USER}' >> /etc/apache2/conf-enabled/environment.conf
RUN echo 'SetEnv MYSQL_PASSWORD ${MYSQL_PASSWORD}' >> /etc/apache2/conf-enabled/environment.conf
RUN echo 'SetEnv SITE_URL ${SITE_URL}' >> /etc/apache2/conf-enabled/environment.conf
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf &&\
    a2enmod rewrite &&\
    a2enmod headers &&\
    a2enmod rewrite &&\
    a2dissite 000-default &&\
    a2ensite my-site &&\
    service apache2 restart
EXPOSE 80
EXPOSE 443