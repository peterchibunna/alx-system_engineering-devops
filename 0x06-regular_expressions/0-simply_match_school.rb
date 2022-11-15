#!/usr/bin/env ruby
#regular expression that must match the word `School`
puts ARGV[0].scan(/School/).join
