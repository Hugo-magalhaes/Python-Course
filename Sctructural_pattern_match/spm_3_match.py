def execute_command3(command: str):
    match command.split():
        case ['ls' | 'list' as the_cmd, path, *directories] as the_list \
                if len(the_list) > 1:
            for directory in directories:
                print('$ Listing directories from ', path, directory)
            print(f'{the_list=}, {the_cmd=}')

        case ['ls' | 'list', path, *directories] if len(directories) <= 1:
            print('$ Listing directory from ', path, directories)

        case ['cd' | 'change', path]:
            print('$ Changing directory to ', path)

        # -- Não obrigatório '_'
        case _:
            print('$ Command not impelmented')
    print('... rest of the code')
