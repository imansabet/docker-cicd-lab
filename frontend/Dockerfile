FROM nginx:1.27-alpine 
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
HEALTHCHECK --interval=15s --timeout=3s --retries=3 \ 
  CMD wget -q --spider http://127.0.0.1/ || exit 1
