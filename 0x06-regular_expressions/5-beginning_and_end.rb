#!/usr/bin/env ruby
# A regular expression that is matching a string which starts with h ends with n and can have any single character in between
puts ARGV[0].scan(/h.n/).join
