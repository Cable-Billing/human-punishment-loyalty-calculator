FROM nginx:1.27-alpine

# Remove the detault Nginx site
RUN rm -fr /usr/share/nginx/html
RUN rm -fr /etc/nginx/conf.d/default.conf

# Copy custom Nginx config
COPY ../app/app.conf /etc/nginx/conf.d/app.conf
COPY ../api/api.conf /etc/nginx/conf.d/api.conf
COPY ../web-server/nginx.conf /etc/nginx/nginx.conf

# Vue App
COPY ../app/dist /usr/share/nginx/app

# API
