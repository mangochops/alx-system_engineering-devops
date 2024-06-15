# This Puppet manifest tunes various Nginx settings for improved performance

# Increase worker processes for handling more concurrent requests
class { 'nginx':
  worker_processes => 4;  # Adjust based on your server's hardware
}

# Increase connections per worker to handle more concurrent connections
nginx::http {
  keepalive_timeout => 60;
  keepalive_requests => 100;
}

# Optimize buffer sizes for better memory usage
nginx::http::upstream {
  buffer_size => 8k;
  client_body_buffer_size => 4k;
}

# Enable gzip compression to reduce response sizes
nginx::module {
  gzip_on => 'on';
  gzip_min_length => 1024;
  gzip_comp_level => 4;
  gzip_types => (
    text/plain,
    text/css,
    text/javascript,
    text/xml,
    text/x-script,
    application/javascript,
    application/x-javascript,
    application/xml,
    application/x-font-ttf,
    image/svg+xml;
  );
}

# Increase connection timeout to handle slower clients
nginx::http {
  client_timeout => 30;
}

# Consider disabling unnecessary modules to reduce resource usage
# Uncomment the following line if applicable
# nginx::module { 'autoindex' => false; }
