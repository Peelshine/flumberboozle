'''
The silliest parser of all time
'''
import glob
from sys import exit
import codes



extension = 'subaru'
tokens = {
    'comment_start': '[',
    'comment_end': ']',
    'braces_start': '{',
    'braces_end': '}',
}



config_files = glob.glob(f'**/*.{extension}', recursive=True)


def parse(

) -> None:

    converted_lines = []
    in_comment = False
    in_braces = False
    active_category = ''

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
                for character in line:

                    # Handle comments
                    if (in_comment and
                    character in tokens['comment_end']
                    ):
                        in_comment = False
                        continue

                    elif (not in_comment and
                    character in tokens['comment_start']
                    ):
                        in_comment = True

                    if in_comment:
                        continue



                    # Handle category
                    #
                    # Unlike handling comments, it is important we do
                    # not handle what happens if inside a category
                    # after determining if inside of a category,
                    # otherwise the category name will include the
                    # braces.g


                    if (in_braces and
                    character in tokens['braces_end']
                    ):
                        in_category = False

                    if in_braces:
                        active_category += character

                    elif (not in_braces and
                    character in tokens['braces_start']
                    ):
                        in_braces = True



                    print(character)

                old_line = line # i go at the end


def write(
) -> None:
    with open('dev_config.py') as f:
        pass



def panic(
    problem
) -> None:
    print(f'{codes.red_bold}! PANIC !{codes.reset}'
        f'\n{problem}')
    exit()



parse()
write()
