command_list = ("exit","help","")

while True:
    command = input("Hometerminal: ")
    if command in command_list:
        pass
    else:
        print("Command not found")