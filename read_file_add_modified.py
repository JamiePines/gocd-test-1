write_file_name = "hello_world_mod.txt"
read_file_name = "hello_world.txt"
read_file = open(read_file_name, "r")
read_file_lines = read_file.readlines()
line = read_file_lines[0]
modded_line = line + " modded...!"
write_file =  open(write_file_name, "w+")
write_file.write(modded_line)