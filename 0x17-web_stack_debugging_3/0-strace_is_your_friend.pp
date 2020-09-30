# Fixing an error in a Wordpress Apache server
exec {'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php;,
  path    => ['/usr/bin', '/bin']
}