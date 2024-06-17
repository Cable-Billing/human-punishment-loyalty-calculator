FROM node:lts as node-build
WORKDIR /app
COPY ../app/package*.json ./
RUN npm install
COPY ../app ./
RUN npm run build

FROM nginx:stable-alpine as nginx-setup

# Remove the detault Nginx site
RUN rm -fr /usr/share/nginx/html
RUN rm -fr /etc/nginx/conf.d/default.conf

# Copy custom Nginx config
COPY ../web-server/nginx.conf /etc/nginx/nginx.conf

# Vue App
COPY --from=node-build /app/dist /usr/share/nginx/app

# API
