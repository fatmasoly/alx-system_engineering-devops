#!/usr/bin/env ruby
# A regular expression which only matching: capital letters
#must match School
puts ARGV[0].scan(/[A-Z]/).join
