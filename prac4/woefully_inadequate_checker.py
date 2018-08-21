def main():


    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    user_choice = input(">>> ")
    if user_choice in usernames:
        print("Access Granted")

    else:
        print("Access Denied")

main()
