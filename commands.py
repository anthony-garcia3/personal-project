
from inquirer.themes import Theme, term

class PrettyTheme(Theme):
    def __init__(self):
        super().__init__()
        self.Question.mark_color = term.green
        self.Question.brackets_color = term.normal
        self.Question.default_color = term.normal
        self.Editor.opening_prompt_color = term.bright_black
        self.Checkbox.selection_color = term.blue
        self.Checkbox.selection_icon = ">"
        self.Checkbox.selected_icon = "[X]"
        self.Checkbox.selected_color = term.yellow + term.bold
        self.Checkbox.unselected_color = term.normal
        self.Checkbox.unselected_icon = "[ ]"
        self.Checkbox.locked_option_color = term.gray50
        self.List.selection_color = term.green
        self.List.selection_cursor = ">"
        self.List.unselected_color = term.normal

