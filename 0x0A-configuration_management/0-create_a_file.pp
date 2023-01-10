# make sure the /tmp/school exists with the attributes given
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data'
}
