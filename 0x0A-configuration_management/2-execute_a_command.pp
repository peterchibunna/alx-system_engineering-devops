# kill the `killmenow` process
exec { 'pkill':
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'pkill killmenow',
  returns  => [0, 1],
  provider => 'shell',
  timeout  => 300
}
