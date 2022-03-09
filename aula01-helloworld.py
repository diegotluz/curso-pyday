#print("Hello World") comentario por linha
"""
comentário em multiplas linhas
"""

#Trabalhando com listas
pessoas = [] #Lista vazia  ****tem que declarar vazio pra começar a usar
pessoas = {"nome": "", "sobrenome":"", "idade":"", "sexo":""} #preenchendo nossa tupula com os campos vazios *declarar

#criando nossa lista dentro da lista pessoas com lista de (nome, sobrenome, idade e sexo)
pnomes=["Tiago","Vinivius","Marina","João","Maria"]
psobrenomes = ["oliveira","santos","sousa","silva","oliveira"] 
pidades = ["23","25","25","26","28"]
psexos =["f","f","f","m","m"]

#loop para perguntar se add um novo usuário a nossa lista
while "s" == input("Deseja adcionar novo usuário s(sim),n(não)?"):
    #solicitando ao usuário os dados pra ser adcionado a lista 
    pnomes.append(input("Digite o seu primeiro nome: ")) 
    psobrenomes.append(input("Digite o seu sobrenome: "))
    pidades.append(str(input("Digite o sua idade: ")))
    psexos.append(input("Digite o seu sexo: "))
    print("########################################################################################################################")

    #concatenando nossa lista
    pessoas = {"nome" : pnomes},{"sobrenome":psobrenomes},{"idade" : pidades},{"sexo" : psexos }
    #percorrendo a lista e mostranso nossos usuários cadastrados 

    for i in range(len(pessoas[0]["nome"])):
        print(pessoas[0]["nome"][i],pessoas[1]["sobrenome"][i],pessoas[2]["idade"][i],pessoas[3]["sexo"][i])