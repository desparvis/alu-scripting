#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

input = ARGV[0]

matches = input.scan(/School/)

puts matches.join
