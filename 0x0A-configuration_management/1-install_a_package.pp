package {
  'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Exec['apt-get update'],
}

exec {
  'apt-get update':
    command => '/usr/bin/apt-get update',
    onlyif  => '/usr/bin/apt-get update',
    path    => ['/usr/bin', '/bin'],
}
