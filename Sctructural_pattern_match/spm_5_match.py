from dataclasses import dataclass


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command4(command: Command):
    # -- Isso funciona como um if, se o primeiro for mais gen
    match command:
        case Command(command='ls'):
            for directory in command.directories:
                print('listing all directories from', directory)

        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('changing all directories from', directory)

        # -- Não obrigatório '_'
        case _:
            print('$ Command not impelmented')
    print('... rest of the code')
