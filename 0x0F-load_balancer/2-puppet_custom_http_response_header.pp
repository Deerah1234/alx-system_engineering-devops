# Configure our servers with puppet

exec { 'update apt':
    command => 'sudo apt update -y',
    path    => '/usr/bin/'
}

exec { 'install Nginx':
    command => 'sudo apt install -y nginx',
    path    => '/usr/bin/'
}

exec { 'update firewall':
    command => "sudo ufw allow 'Nginx http'",
    path    => '/usr/bin/:/usr/sbin/'
}

exec { 'index page return':
    command => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html',
    path    => '/usr/bin/'
}

exec { '404 page':
    command => 'echo "Ceci n\'est pas une page" | sudo tee /usr/share/nginx/html/custom_404.html',
    path    => '/usr/bin/'
}

$new_header = "\n\tadd_header X-Served-By \$hostname;"
$redirect="server_name _;\n\trewrite ^/redirect_me google.com permanent;"
$not_found="\n\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}"
exec { 'change the default configuration':
    command => 'sudo sed -i "s/server_name _;/$redirect$new_header$not_found/" /etc/nginx/sites-enabled/default',
    path    => '/usr/bin'
}

exec { 'restart nginx':
    command => 'sudo service nginx restart',
    path    => '/usr/bin/:/usr/sbin/'
}
