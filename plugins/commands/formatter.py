from utils.colors import Colors


class Formatter:
    color_std = Colors.LIGHT_YELLOW.value
    color_info = Colors.LIGHT_BLUE.value
    color_error = Colors.RED.value
    color_highlight = Colors.WHITE.value
    
    # base

    def unknown_cmd(self, cmd: str):
        return f'{self.color_error}Unknown command {self.color_highlight}{cmd}'

    def bad_usage(self):
        return f'{self.color_error}Bad usage'

    # help

    def command_list(self, cmds: list):
        txt = ', '.join(cmds)
        return f'{self.color_info}Available commands: {self.color_std}{txt}'
    
    def command_not_found(self, cmd: str):
        return f'{self.color_error}Command {self.color_highlight}{cmd} {self.color_error}not found'

    def command_help(self, cmd: dict):
        return f'{self.color_info}PLOP'