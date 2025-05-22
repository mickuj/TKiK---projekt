# Generated from PythonMelody.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonMelodyParser import PythonMelodyParser
else:
    from PythonMelodyParser import PythonMelodyParser

# This class defines a complete listener for a parse tree produced by PythonMelodyParser.
class PythonMelodyListener(ParseTreeListener):

    # Enter a parse tree produced by PythonMelodyParser#program.
    def enterProgram(self, ctx:PythonMelodyParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#program.
    def exitProgram(self, ctx:PythonMelodyParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#stmt.
    def enterStmt(self, ctx:PythonMelodyParser.StmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#stmt.
    def exitStmt(self, ctx:PythonMelodyParser.StmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PythonMelodyParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PythonMelodyParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#compound_stmt.
    def enterCompound_stmt(self, ctx:PythonMelodyParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#compound_stmt.
    def exitCompound_stmt(self, ctx:PythonMelodyParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#func_def.
    def enterFunc_def(self, ctx:PythonMelodyParser.Func_defContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#func_def.
    def exitFunc_def(self, ctx:PythonMelodyParser.Func_defContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#if_stmt.
    def enterIf_stmt(self, ctx:PythonMelodyParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#if_stmt.
    def exitIf_stmt(self, ctx:PythonMelodyParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#while_stmt.
    def enterWhile_stmt(self, ctx:PythonMelodyParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#while_stmt.
    def exitWhile_stmt(self, ctx:PythonMelodyParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#for_stmt.
    def enterFor_stmt(self, ctx:PythonMelodyParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#for_stmt.
    def exitFor_stmt(self, ctx:PythonMelodyParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#block.
    def enterBlock(self, ctx:PythonMelodyParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#block.
    def exitBlock(self, ctx:PythonMelodyParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#assign_stmt.
    def enterAssign_stmt(self, ctx:PythonMelodyParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#assign_stmt.
    def exitAssign_stmt(self, ctx:PythonMelodyParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#assign_op.
    def enterAssign_op(self, ctx:PythonMelodyParser.Assign_opContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#assign_op.
    def exitAssign_op(self, ctx:PythonMelodyParser.Assign_opContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#expr_stmt.
    def enterExpr_stmt(self, ctx:PythonMelodyParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#expr_stmt.
    def exitExpr_stmt(self, ctx:PythonMelodyParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#print_stmt.
    def enterPrint_stmt(self, ctx:PythonMelodyParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#print_stmt.
    def exitPrint_stmt(self, ctx:PythonMelodyParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#import_stmt.
    def enterImport_stmt(self, ctx:PythonMelodyParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#import_stmt.
    def exitImport_stmt(self, ctx:PythonMelodyParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#return_stmt.
    def enterReturn_stmt(self, ctx:PythonMelodyParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#return_stmt.
    def exitReturn_stmt(self, ctx:PythonMelodyParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#param_list.
    def enterParam_list(self, ctx:PythonMelodyParser.Param_listContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#param_list.
    def exitParam_list(self, ctx:PythonMelodyParser.Param_listContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#expr.
    def enterExpr(self, ctx:PythonMelodyParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#expr.
    def exitExpr(self, ctx:PythonMelodyParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#dotted_name.
    def enterDotted_name(self, ctx:PythonMelodyParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#dotted_name.
    def exitDotted_name(self, ctx:PythonMelodyParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#function_call.
    def enterFunction_call(self, ctx:PythonMelodyParser.Function_callContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#function_call.
    def exitFunction_call(self, ctx:PythonMelodyParser.Function_callContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#arith_expr.
    def enterArith_expr(self, ctx:PythonMelodyParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#arith_expr.
    def exitArith_expr(self, ctx:PythonMelodyParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#bool_expr.
    def enterBool_expr(self, ctx:PythonMelodyParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#bool_expr.
    def exitBool_expr(self, ctx:PythonMelodyParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#logic_const.
    def enterLogic_const(self, ctx:PythonMelodyParser.Logic_constContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#logic_const.
    def exitLogic_const(self, ctx:PythonMelodyParser.Logic_constContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#list_expr.
    def enterList_expr(self, ctx:PythonMelodyParser.List_exprContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#list_expr.
    def exitList_expr(self, ctx:PythonMelodyParser.List_exprContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#elements.
    def enterElements(self, ctx:PythonMelodyParser.ElementsContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#elements.
    def exitElements(self, ctx:PythonMelodyParser.ElementsContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#dict_expr.
    def enterDict_expr(self, ctx:PythonMelodyParser.Dict_exprContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#dict_expr.
    def exitDict_expr(self, ctx:PythonMelodyParser.Dict_exprContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#kv_pairs.
    def enterKv_pairs(self, ctx:PythonMelodyParser.Kv_pairsContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#kv_pairs.
    def exitKv_pairs(self, ctx:PythonMelodyParser.Kv_pairsContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#module.
    def enterModule(self, ctx:PythonMelodyParser.ModuleContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#module.
    def exitModule(self, ctx:PythonMelodyParser.ModuleContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#alias.
    def enterAlias(self, ctx:PythonMelodyParser.AliasContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#alias.
    def exitAlias(self, ctx:PythonMelodyParser.AliasContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#name.
    def enterName(self, ctx:PythonMelodyParser.NameContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#name.
    def exitName(self, ctx:PythonMelodyParser.NameContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#rel_op.
    def enterRel_op(self, ctx:PythonMelodyParser.Rel_opContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#rel_op.
    def exitRel_op(self, ctx:PythonMelodyParser.Rel_opContext):
        pass


    # Enter a parse tree produced by PythonMelodyParser#log_op.
    def enterLog_op(self, ctx:PythonMelodyParser.Log_opContext):
        pass

    # Exit a parse tree produced by PythonMelodyParser#log_op.
    def exitLog_op(self, ctx:PythonMelodyParser.Log_opContext):
        pass



del PythonMelodyParser