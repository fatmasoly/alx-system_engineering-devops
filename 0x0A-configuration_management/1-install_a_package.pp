# Installing flask from pip3
# install flask
package { 'python3-pip':
  ensure   => installed,
}

exec { 'install-flask':
  command => 'pip3 install flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/usr/bin', '/usr/sbin'],
}
