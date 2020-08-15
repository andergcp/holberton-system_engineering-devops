#Sets custom header response

exec {'Update packages':
command  => 'apt-get update',
provider => 'shell'
}

exec {'Install nginx':
command  => 'apt-get -y install nginx',
provider => 'shell'
}

exec {'Add custom header in file':
command  => 'sed -i "s/server_name _;/\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
provider => 'shell'
}

exec {'Restart nginx':
command  => 'service nginx start',
provider => 'shell'
}