FROM nginx:alpine

RUN rm -f /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/nginx.conf

COPY website/public/ /usr/share/nginx/public/
COPY website/archive/ /usr/share/nginx/archive/

EXPOSE 80
