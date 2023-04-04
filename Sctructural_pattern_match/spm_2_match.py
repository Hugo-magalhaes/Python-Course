def execute_command2(command: str):
    match command.split():
        case ['ls' | 'list', path, *_]:
            print('$ Listing files from ', path)

        case ['cd' | 'change', path]:
            print('$ Changing directory to ', path)

        # -- Não obrigatório '_'
        case _:
            print('$ Command not impelmented')
    print('... rest of the code')
