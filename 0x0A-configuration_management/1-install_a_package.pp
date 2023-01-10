# make sure that flask version 2.1.0 is installed using pip3
package { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
}
