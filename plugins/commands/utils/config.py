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
