'''
The silliest parser of all time
'''
import glob
from sys import exit
import codes



extension = 'subaru'



config_files = glob.glob(f'**/*.{extension}', recursive=True)


def parse(

) -> None:
    converted_lines = []

    for file_name in config_files:
        # Get the current file as a string
        with open(file_name) as file:
            file = str(file.read()).lower().splitlines()
            print(file)

            # Iterate over every line in the file
            for line in file:

                # Catch any simple errors
                if line.count('=') > 1:
                    panic('More than one equals sign!'
                        f'\nLine: {line}')

                # Iterate over every character in the line

                old_line = line # i go at the end


def write(
) -> None:
    with open('dev_config.py') as f:
        pass



def panic(
    problem
) -> None:
    print(f'{codes.red_bold}PANIC!{codes.reset}'
        f'\n{problem}')
    exit()



parse()
write()
