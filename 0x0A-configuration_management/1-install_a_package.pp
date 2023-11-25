# 1-install_a_package.pp

# Define a package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',  # Specify the desired version
  provider => 'pip3',   # Use pip3 as the package provider
  require  => Package['python3-pip'],  # Ensure pip3 is installed before Flask
}

# Ensure that python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}
