FROM nginx:latest
LABEL MAINTAINER = "AMIRMOHAMMAD | myme.ir"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
