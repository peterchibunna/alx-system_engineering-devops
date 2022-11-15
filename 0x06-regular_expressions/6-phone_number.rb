#!/usr/bin/env ruby
# detect the words that must contain 10 digits only and always
puts ARGV[0].scan(/^\d{10}$/).join
