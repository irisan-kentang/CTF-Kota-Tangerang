limit_req_zone $binary_remote_addr zone=admin_panel:10m rate=200r/m;

server {
    listen 80;
    index index.php index.html;
    error_log  /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www;
    location ~ \.php$ {
        limit_req zone=admin_panel burst=20 nodelay;
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass admin-panel-app:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
    location / {
        limit_req zone=admin_panel burst=20 nodelay;
        try_files $uri $uri/ /index.php?$query_string;
        gzip_static on;
    }
}