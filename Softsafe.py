# More of reading and writing files
# The use of close, read, readline, truncate, write
# This software can be used to save and retrieve files. 
# Softsafe.py does that function. Add other writings to it adn save it
# Test16.py writes to only files does not append or continue.


from sys import argv

script, filename = argv

print "We're going to write data to %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input(">>>")

print "File loading..."
target = open(filename, 'a') # The 'w' mode writes new user data into the file. Existing ones writes off.
			     # The 'a' mode writes to a file and even add to it
			     # The 'r' + 'U' mode does same function as 'w'. It seems 'r' cant be used alone.
print "File ready..."
target.truncate()

print "What do you have for me please?"

line1 = raw_input(">>> ")
line2 = raw_input(">>> ")
line3 = raw_input(">>> ")

print "Writing to file..."

target.write(line1) # This jumps to first line
target.write("\n")  # This write write the line1 input from (raw_input)
target.write(line2) # This jumps to second line
target.write("\n")  # This write the line2 input from (raw_input)
target.write(line3) # This jumps to line3
target.write("\n")  # This write the line3 input from (raw_inpt)


print "Writing completed. Saved '%s'." % filename
target.close()
