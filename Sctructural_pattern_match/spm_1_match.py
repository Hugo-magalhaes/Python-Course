def execute_command1(command):
    match command:
        case 'ls':
            print('$ Listing files')

        case 'cd':
            print('$ Changing directory')

        # -- Não obrigatório '_'
        case _:
            print('$ Command not impelmented')
    print('... rest of the code')
