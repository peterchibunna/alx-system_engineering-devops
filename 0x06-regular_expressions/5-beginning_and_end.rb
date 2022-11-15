#!/usr/bin/env ruby
# htn hbtn hbbtn hbbbtn
# detect the words that must start with h and end with n and any single character in between
puts ARGV[0].scan(/^h.n$/).join
