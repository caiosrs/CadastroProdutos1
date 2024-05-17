import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=ISPD-DP062\\SQLEXPRESS01;"
    "Database=DatabaseTeste;"
    "Trusted_Connection=yes;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

cursor = conexao.cursor()

nomeProduto = ""
descricaoProduto = ""
corProduto = ""
precoProduto = ""

comando = f"""INSERT INTO Produtos (Nome, Descricao, Cor, Preco)
Values ('{nomeProduto}', '{descricaoProduto}', '{corProduto}', {precoProduto})"""

cursor.execute(comando)
cursor.commit()

#cd ".\Cadastro de produtos\Pyodbc\"