#Sets custom header response

exec {'Update packages':
command  => 'sudo apt-get update',
provider => 'shell'
}

exec {'Install nginx':
command  => 'sudo apt-get -y install nginx',
provider => 'shell'
}

exec {'Add custom header in file':
command  => 'sudo sed -i "s/server_name _;/\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
provider => 'shell'
}

exec {'Restart nginx':
command  => 'sudo service nginx start',
provider => 'shell'
}