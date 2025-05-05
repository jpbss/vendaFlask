from controle.conectarbanco import *
import json
import datetime

class ControleGenerico:

    def __init__(self):
        self.ob = Banco()
        self.ob.configura(ho="177.190.74.69",
                          db="tpc10",
                          us="trabtpc",
                          se="trabtpc",
                          po=65004)

    def incluir(self,objeto):
        self.ob.abrirConexao()
        sql = "insert into {} ".format(objeto.tabelaBanco)+'('
        sql+= '{}'.format(objeto.lista)
        sql+= ') values ({})'.format(objeto.dadosInserir)
        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()

    def alterar(self,objeto):
        self.ob.abrirConexao();
        sql = "update {} ".format(objeto.tabelaBanco)
        sql += 'set {}'.format(objeto.dadosUpdate)

        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()

    def delete(self, objeto):
        self.ob.abrirConexao();
        sql = "delete from {} ".format(objeto.tabelaBanco)
        sql += objeto.dadosDelete

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def procuraRegistro(self,objeto):
        self.ob.abrirConexao()
        objeto = self.ob.selectQuery(objeto.dadosPesquisa)
        return objeto

    def apagar(self,entrada):
        self.ob.abrirConexao();
        sql = "delete from aluno where idaluno = {}".format(entrada)
        self.ob.execute(sql)
        self.ob.gravar()

    def listarTodos(self,objeto):
        self.ob.abrirConexao()
        dados = self.ob.selectQuery("select * from {}".format(objeto.tabelaBanco))
        return dados




