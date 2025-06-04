from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self, interpreter):
        super().__init__()
        self.interpreter = interpreter

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_type = "default"
        if "mismatched input" in msg:
            error_type = "mismatched"
        elif "extraneous input" in msg:
            error_type = "extraneous"
        elif "missing" in msg:
            error_type = "missing"
        elif "no viable alternative" in msg:
            error_type = "no_viable"

        self.interpreter._add_error_notes(error_type)
        print(f"[INFO] Niedopasowany token w linii {line}:{column} — używam __default_{error_type}__")
