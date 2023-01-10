file { '/tmp/school':
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love puppet',
  group   => 'www-data',
  owner   => 'www-data'
}
