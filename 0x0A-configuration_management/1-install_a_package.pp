#!/usr/bin/puppet

# Update Python packages including Flask
package { 'python3-pip':
  ensure => latest,
}

package { 'python3-setuptools':
  ensure => latest,
}

# Install an specific version of Flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3-pip'], Package['python3-setuptools']],
}
