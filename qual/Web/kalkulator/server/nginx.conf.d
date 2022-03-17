limit_req_zone $binary_remote_addr zone=kalkulator_zone:10m rate=200r/m;

upstream kalkulator {
  server    kalkulator-app:5000;
}

server {
    listen 80;
    error_log  /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    location / {
        limit_req zone=kalkulator_zone burst=20 nodelay;
        proxy_pass http://kalkulator;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}