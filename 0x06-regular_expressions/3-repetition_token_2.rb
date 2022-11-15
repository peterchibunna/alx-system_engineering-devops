#!/usr/bin/env ruby
# htn hbtn hbbtn hbbbtn
# detect the words that contain the character `t` at least 1 time
puts ARGV[0].scan(/hbt{1,4}n/).join
