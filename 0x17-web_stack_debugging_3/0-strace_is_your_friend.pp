# This Puppet manifest installs the missing PHP module and restarts Apache to fix the 500 error

package { 'php5-mysql':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => Package['php5-mysql'],
}

exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => Package['php5-mysql'],
}
