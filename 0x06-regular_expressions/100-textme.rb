#!/usr/bin/env ruby
# script extract the `from:`, `to:`, and the `flags:` parts of the string and print them as:
# [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/(?<=from:|to:|flags:)(.+?)(?=\])/).join(",")
