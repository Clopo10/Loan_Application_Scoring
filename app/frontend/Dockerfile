# 1. Start with a lightning-fast, production-ready Nginx web server
FROM nginx:alpine

# 2. Delete the default "Welcome to Nginx" page that comes with the server
RUN rm -rf /usr/share/nginx/html/*

# 3. Copy files directly into the web server's public folder
COPY index.html /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# 4. Expose the standard web port
EXPOSE 80

# 5. Turn the Nginx server on (daemon off keeps the container running)
CMD ["nginx", "-g", "daemon off;"]