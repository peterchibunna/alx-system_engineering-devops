# make sure that flask version 2.1.0 is installed using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
