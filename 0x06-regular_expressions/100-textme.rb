#!/usr/bin/env ruby
from = ARGV[0].scan(/from:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
puts [from, to, flags].join(',')
