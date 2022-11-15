#!/usr/bin/env ruby
# htn hbtn hbbtn hbbbtn
# detect the words that contain the character `b` at most 1 time
puts ARGV[0].scan(/hb{0,1}tn/).join
