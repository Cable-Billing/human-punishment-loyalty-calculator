FROM node:20.14.0-alpine as node-build
RUN rm -fr /app
WORKDIR /app
COPY ../app/package*.json ./
RUN npm install
COPY ../app ./
RUN npm run build

FROM nginx:1.26.1-alpine as nginx-setup

# Remove the detault Nginx site
RUN rm -fr /usr/share/nginx/html
RUN rm -fr /etc/nginx/conf.d/default.conf

# Copy custom Nginx config
COPY ../web-server/nginx.conf /etc/nginx/nginx.conf

# Vue App
RUN rm -fr /usr/share/nginx/app
COPY --from=node-build /app/dist /usr/share/nginx/app

# API
