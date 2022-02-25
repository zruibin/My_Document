

# bash <(curl -L -s https://install.direct/go.sh)

#firewall-cmd --zone=public --add-port=5672/tcp --permanent
#firewall-cmd --zone=public --remove-port=5672/tcp --permanent
#firewall-cmd --reload
#firewall-cmd --zone=public --list-ports




/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf


systemctl enable v2ray
systemctl start v2ray

