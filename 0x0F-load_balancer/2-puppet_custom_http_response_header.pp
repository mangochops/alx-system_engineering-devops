# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {\n\tlisten 80;\n\tserver_name localhost;\n\n\tlocation / {\n\t\tadd_header X-Served-By $hostname;\n\t\troot /var/www/html;\n\t\tindex index.html;\n\t}\n}",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
