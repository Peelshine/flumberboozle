import tomllib as toml

x = 'hi'

def read(
    path: str
) -> dict:
    with open(path, 'rb') as f:
        return toml.load(f)


defaultsettings = read('defaultsettings.toml')
usersettings = read('usersettings.toml')

# Merge usersettings on top of defaultsettings
settings = defaultsettings | usersettings

print(settings['meta']['name'])
