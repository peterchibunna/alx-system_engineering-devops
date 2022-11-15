#!/usr/bin/env ruby
# hbn hbtn hbttn hbtttn hbttttn hbtttttn hbttttttn
# detect the words that contain the repeated `t`s
puts ARGV[0].scan(/hbt{2,5}n/).join
