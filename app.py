def tv_command(command):
    output = ''
    while True:
        if command == "on":
            print('TV turned on')
        elif command =="off":
            print('TV Turned off')
        elif command =="quit":
            print('goodbye')
        break
    return output

command = input('input command:>>  ')
result = tv_command(command)
print(result)