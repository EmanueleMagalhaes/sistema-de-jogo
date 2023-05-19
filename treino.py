lista_produtos = ["faca","garfo","colher","prato"]
for produto in lista_produtos:
    print(produto)

lista_precos = [10, 30, 200, 50]
for preco in lista_precos:
    imposto = preco * 0.10
    print(imposto)

for val in range(50, 100, 5):
    print(val)
    
print("*********--tabuada--***********")
tabuada  = int(input("qual tabuada fazer: "))

for i in range(1, 11):
    print(tabuada*i)