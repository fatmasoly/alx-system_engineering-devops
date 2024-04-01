# Install Nginx
package { 'nginx':
  ensure => installed,
}

firewall { '100 allow http':
  port   => 80,
  proto  => tcp,
  action => accept,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

nginx::resource::server { 'default':
  ensure    => present,
  server_name => '_',
  add_header => { 'X-Served-By' => '$hostname' },
  rewrite   => {
    '^\/redirect_me' => 'https://github.com/fatmasoly permanent',
  },
  listen_options => 'default_server',
  error_page     => '404 /404.html',
  location       => {
    '= /404.html' => {
      root     => '/var/www/html',
      internal => true,
    },
  },
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.html', '/var/www/html/404.html'],
  require   => Package['nginx'],
}
