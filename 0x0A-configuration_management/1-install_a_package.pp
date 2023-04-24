# install puppet-lint

package {'puppet-lint':
    ensure => '2.5.0',
    source => 'gem',
    name   => 'puppet-lint'
}
