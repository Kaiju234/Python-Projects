
# chai_extension.py

import os
from datetime import datetime

class ChaiExtension:
    def __init__(self, chai_interpreter):
        self.interpreter = chai_interpreter
        self.extend_language()

    def extend_language(self):
        # Adding new built-in functions
        self.interpreter.global_symbol_table.set("SAVE_FILE", self.builtin_save_file())
        self.interpreter.global_symbol_table.set("LOAD_FILE", self.builtin_load_file())
        self.interpreter.global_symbol_table.set("DATE", self.builtin_date())

    def builtin_save_file(self):
        def save_file(exec_ctx):
            filename = exec_ctx.symbol_table.get("filename")
            content = exec_ctx.symbol_table.get("content")

            if not isinstance(filename, str) or not isinstance(content, str):
                return self.interpreter.RTError(
                    self.pos_start, self.pos_end,
                    "Arguments must be strings",
                    exec_ctx
                )
            
            try:
                with open(filename, "w") as file:
                    file.write(content)
                return self.interpreter.RTResult().success(self.interpreter.Number.null)
            except Exception as e:
                return self.interpreter.RTError(
                    self.pos_start, self.pos_end,
                    f"Failed to save file: {e}",
                    exec_ctx
                )
        save_file.arg_names = ["filename", "content"]
        return save_file

    def builtin_load_file(self):
        def load_file(exec_ctx):
            filename = exec_ctx.symbol_table.get("filename")

            if not isinstance(filename, str):
                return self.interpreter.RTError(
                    self.pos_start, self.pos_end,
                    "Argument must be a string",
                    exec_ctx
                )
            
            try:
                with open(filename, "r") as file:
                    content = file.read()
                return self.interpreter.RTResult().success(self.interpreter.String(content))
            except Exception as e:
                return self.interpreter.RTError(
                    self.pos_start, self.pos_end,
                    f"Failed to load file: {e}",
                    exec_ctx
                )
        load_file.arg_names = ["filename"]
        return load_file

    def builtin_date(self):
        def date(exec_ctx):
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return self.interpreter.RTResult().success(self.interpreter.String(current_date))
        date.arg_names = []
        return date

    # Add more extensions as needed

# Usage:
# After initializing the chai interpreter, you can load this extension like so:
# extension = ChaiExtension(chai_interpreter_instance)
