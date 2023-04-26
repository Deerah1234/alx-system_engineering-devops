# SSH client configuration exercise

exec {'SSH configuration':
    command => "echo 'Host 35.237.86.168\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
    path    => '/usr/bin'
}
