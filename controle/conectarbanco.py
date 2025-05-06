import mysql.connector
class Banco:

   def __init__(self):
       self.servidor=""
       self.usuario=""
       self.senha=""
       self.banco=""
       self.porta=3306
       self.ponteiro =""

   def abrirConexao(self):
      self.con = mysql.connector.connect(host=self.servidor,
                                 database=self.banco,
                                 user=self.usuario,
                                 passwd=self.senha,
                                 port=self.porta)
      self.ponteiro=self.con.cursor()

   def selectQuery(self,entrada):
      self.ponteiro.execute(entrada)
      resposta = self.ponteiro.fetchall()
      return resposta

   def executeQuery(self, entrada,dados):
       self.ponteiro.execute(entrada,dados)

   def execute(self, entrada):
       self.ponteiro.execute(entrada)

   def gravar(self):
      self.con.commit()

   def descarte(self):
      self.con.rollback()

   def configura(self,ho,us,se,db,po=3306):
       self.servidor = ho
       self.usuario = us
       self.senha = se
       self.banco = db
       self.porta = po

   def mostraResultado(self,entrada):
       for i in entrada:
           print(i)