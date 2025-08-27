from Clientes import Cliente
from Conta import Conta

print("testando projeto")

c1 = Cliente("João", 2132312)
conta = Conta(c1.nome, 432423, 0)

print(conta.titular,"numero:", conta.numero, "seu saldo:", conta.saldo)