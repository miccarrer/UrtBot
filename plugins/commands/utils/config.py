from utils.yaml import load_yaml

commands_help = load_yaml('config/commands.yaml')


def get_cmd_list():
    cmds = []
    for cmd_key in commands_help:
        cmd = commands_help[cmd_key]
        cmd_name = cmd['command']
        if(cmd_name not in cmds):
            cmds.append(cmd_name)
    cmds.sort()
    return ', '.join(cmds)


def get_cmd(name):
    lines = []
    for cmd_key in commands_help:
        cmd = commands_help[cmd_key]
        cmd_name = cmd['command']
        cmd_shortcut = cmd['shortcut']
        if(cmd_name == name or cmd_shortcut == name):
            if(len(lines) > 0):
                lines.append('or')

            if cmd_shortcut == None:
                lines.append(f'{cmd_name}')
            else:
                lines.append(f'{cmd_name} ({cmd_shortcut})')

            cmd_description = cmd['description']
            cmd_usage = cmd['usage']

            lines.append(f'Description: {cmd_description}')
            lines.append(f'Usage: {cmd_usage}')
    return '\n'.join(lines)
