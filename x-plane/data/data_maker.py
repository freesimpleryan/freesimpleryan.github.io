def do_load(in_file, mem_dict, ignore_flags, index_callsign, gps_index):
	f = open(in_file)
	for line in f:
		if line == "" or line is None:
			continue
		data = line.split()
		if len(data) is 0 or data[0] in ignore_flags:
			continue
		coordinates = "%s %s "%(data[gps_index], data[gps_index + 1])
		callsign = data[index_callsign]
		mem_dict[callsign] = coordinates
	f.close()

def make_js_file(file_name, file_dict, var_name):
	out_file = open(file_name, 'w+')
	line = ["var %s = ["%var_name]
	last_entry = file_dict.keys()[-1]
	for coordinate in file_dict:
		line.append("{'%s':'%s %s'}"%(coordinate, file_dict[coordinate][0], file_dict[coordinate][1]))
		if coordinate != last_entry:
			line.append(",")
	line.append("];")
	out_file.write(''.join(line));
	out_file.close()

if __name__ == "__main__":
	earth_fix_file = "data/earth_fix.dat"
	earth_fix = {}
	earth_nav_file = "data/earth_nav.dat"
	earth_nav = {}
	print "Loading %s..."%earth_fix_file
	do_load(earth_fix_file, earth_fix, ("I", "600", "99"), 2, 0)
	print "Earth fix file loaded"
	print "%s waypoints found"%len(earth_fix)
	make_js_file("earth_fix.js", earth_fix, "earth_fix")
	print "Loading %s..."%earth_nav_file
	do_load(earth_nav_file, earth_nav, ("I", "810", "99"), 7, 1)
	print "Earth nav file loaded"
	print "%s waypoints found"%len(earth_nav)
	make_js_file("earth_nav.js", earth_nav, "earth_nav")
	
		
	
