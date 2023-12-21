'''
Variables

path = "server.conf

key = "TIMEOUT"

value = "10"

Onece the program is runned, the value of TIMEOUT will change from 40 to 10.

'''




# update servser config file
def update_config_file(path , key , value):

    # open server.conf file in read mode
    with open(path , "r") as file:
        # read content of the file line by line
        lines = file.readlines()

    # open server.conf file in write mode
    with open(path , "w") as file:

        for line in lines:
            # check if the line starts with that key
            if key in line:
                # update the line with the key and new value
                file.write(key + "=" + value + "\n")
            else:
                # keep the same line
                file.write(line)

update_config_file("YOUR_PATH", "YOUR_KEY", "YOUR_VALUE")