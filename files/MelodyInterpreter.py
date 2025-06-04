from PythonMelodyListener import PythonMelodyListener
from melody_map import melody_map


class MelodyInterpreter(PythonMelodyListener):
    def __init__(self):
        self.notes = []
        self.background_notes = []

    def _add_notes(self, rule_name):
        if rule_name not in melody_map:
            entry = melody_map["__default__"]
            print(
                f"[Ostrzeżenie] Token '{rule_name}' nie istnieje w melody_map. Używam domyślnej melodii '__default__'.")
        else:
            entry = melody_map.get(rule_name)
        melody = entry.get("melody", [])
        background = entry.get("background", [])
        self.notes += melody
        for chord, dur in background:
            for note in chord:
                self.background_notes.append((note, dur))

    def _add_error_notes(self, error_type):
        key = f"__default_{error_type}__"
        if key not in melody_map:
            key = "__default__"
        entry = melody_map[key]
        self.notes += entry.get("melody", [])
        for chord, dur in entry.get("background", []):
            for note in chord:
                self.background_notes.append((note, dur))

    # Produkcje główne
    def enterProgram(self, ctx):
        self._add_notes("program")

    def enterStmt(self, ctx):
        self._add_notes("stmt")

    def enterSimple_stmt(self, ctx):
        self._add_notes("simple_stmt")

    def enterCompound_stmt(self, ctx):
        self._add_notes("compound_stmt")

    # Instrukcje złożone
    def enterFunc_def(self, ctx):
        self._add_notes("func_def")

    def enterIf_stmt(self, ctx):
        self._add_notes("if_stmt")

    def enterWhile_stmt(self, ctx):
        self._add_notes("while_stmt")

    def enterFor_stmt(self, ctx):
        self._add_notes("for_stmt")

    def enterBlock(self, ctx):
        self._add_notes("block")

    # Instrukcje proste
    def enterAssign_stmt(self, ctx):
        self._add_notes("assign_stmt")

    def enterAssign_op(self, ctx):
        self._add_notes("assign_op")

    def enterExpr_stmt(self, ctx):
        self._add_notes("expr_stmt")

    def enterPrint_stmt(self, ctx):
        self._add_notes("print_stmt")

    def enterImport_stmt(self, ctx):
        self._add_notes("import_stmt")

    def enterReturn_stmt(self, ctx):
        self._add_notes("return_stmt")

    # Wyrażenia i wywołania
    def enterParam_list(self, ctx):
        self._add_notes("param_list")

    def enterFunction_call(self, ctx):
        self._add_notes("function_call")

    def enterDotted_name(self, ctx):
        self._add_notes("dotted_name")

    # Wyrażenia ogólne
    def enterExpr(self, ctx):
        self._add_notes("expr")

    def enterArith_expr(self, ctx):
        self._add_notes("arith_expr")

    def enterBool_expr(self, ctx):
        self._add_notes("bool_expr")

    def enterLogic_const(self, ctx):
        self._add_notes("logic_const")

    # Struktury danych
    def enterList_expr(self, ctx):
        self._add_notes("list_expr")

    def enterDict_expr(self, ctx):
        self._add_notes("dict_expr")

    def enterElements(self, ctx):
        self._add_notes("elements")

    def enterKv_pairs(self, ctx):
        self._add_notes("kv_pairs")

    # Moduły i aliasy
    def enterModule(self, ctx):
        self._add_notes("module")

    def enterAlias(self, ctx):
        self._add_notes("alias")

    def enterName(self, ctx):
        self._add_notes("name")

    # Operatory
    def enterRel_op(self, ctx):
        self._add_notes("rel_op")

    def enterLog_op(self, ctx):
        self._add_notes("log_op")

    def finish(self):
        pass