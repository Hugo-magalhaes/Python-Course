def execute_command3(command: str):
    match command:
        # -- Colocar _, *_ obriga que o match tenha ao menos um objeto
        case {'command': 'ls', 'directory': [_, *_]}:
            # ! Isso funciona, não sei pq esta acusando
            for directory in command['directory']:  # type: ignore
                print('$ Listing directories from ', directory)

        # -- Não obrigatório '_'
        case _:
            print('$ Command not impelmented')
    print('... rest of the code')
