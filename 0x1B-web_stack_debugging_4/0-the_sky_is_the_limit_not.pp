# Fix the limit of requests

exec {'Set the limit to 5000':
  onlyif  => 'test -f /etc/default/nginx',
  path    => '/bin:/sbin:/usr/bin',
  command => 'sed -i "s/15/5000/" /etc/default/nginx && sudo service nginx restart'
}
