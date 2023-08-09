import random

def barganhar(personagem):
    return personagem

def comprar_item(personagem, item):
    if "Ouro" in personagem and personagem["Ouro"] >= item["Preço"]:
        personagem["Ouro"] -= item["Preço"]
        if "Itens" not in personagem:
            personagem["Itens"] = []
        personagem["Itens"].append(item)
        print(f"{personagem['Nome']} comprou {item['Nome']}.")
    else:
        print("Você não tem ouro suficiente para comprar este item.")

def abrir_bau(personagem, bau):
    premio = None
    for premio_info in bau["bau"]:
        if random.randint(1, 100) <= premio_info["probabilidade"]:
            premio = premio_info
            break
    
    if premio:
        if "Ouro" in premio:
            personagem["Ouro"] += premio["Ouro"]
            print(f"{personagem['Nome']} encontrou {premio['Ouro']} de ouro!")
        else:
            print(f"{personagem['Nome']} encontrou {premio['premio']}!")
            if "Itens" not in personagem:
                personagem["Itens"] = []
            personagem["Itens"].append(premio)
    else:
        print(f"{personagem['Nome']} abriu o baú, mas não encontrou nada.")

personagem = {
    "Nome": "Heroi Victor",
    "Ouro": 50
}

itens = [
     {
        "Nome": "Espada de ferro",
        "Preço": 7,
        "Dano": 25
    },
    {
        "Nome": "Poção de Força",
        "Preço": 10,
        "Dano": 5
    },
    {
        "Nome": "Escudo de ferro",
        "Preço": 15,
        "Defesa": 10
    },
    {
        "Nome": "Armadura de Ferro Completa",
        "Preço": 35,
        "Defesa": 30
    },
    {
        "Nome": "Espada Mágica de Fogo",
        "Preço": 30,
        "Dano": 40
    },
    {
        "Nome": "Poção de vida",
        "Preço": 5,
        "Cura": 25
    },
    {
        "Nome": "Poção do sono",
        "Preço": 10,
        "Dano": 30
    },
    {
        "Nome": "Mjolnir martelo de Thor",
        "Preço": 250,
        "Dano": 400
    },
    {
        "Nome": "Bau misterioso",
        "Preço": 20,
        "bau": [
            {
                "premio": 500,
                "probabilidade": 20
            },
            {
                "premio": 250,
                "probabilidade": 40
            },
            {
                "premio": 100,
                "probabilidade": 60
            },
            {
                "premio": 50,
                "probabilidade": 90
            }
        ]
    },
    {
        "Nome": "Bau de Armas",
        "Preço": 15,
        "bau": [
            {
                "premio": "Cajado do trovão",
                "dano": 200,
                "probabilidade": 30
            },
            {
                "premio": "Espada de obsidiana",
                "dano": 100,
                "probabilidade": 50
            },
            {
                "premio": "Escudo com Espinhos",
                "defesa": 50,
                "dano": 10,
                "probabilidade": 80
            }
        ]
    }
]

while True:
    print("1 - Comprar Item")
    print("2 - Abrir Baú Misterioso")
    print("3 - Abrir Baú de Armas")
    print("4 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Itens disponíveis para compra:")
        for i, item in enumerate(itens):
            print(f"{i+1} - {item['Nome']} - Preço: {item['Preço']} Ouro")
        
        item_escolhido = int(input("Escolha o número do item que deseja comprar: ")) - 1
        if 0 <= item_escolhido < len(itens):
            comprar_item(personagem, itens[item_escolhido])
        else:
            print("Opção inválida.")
    elif escolha == "2":
        abrir_bau(personagem, itens[-2])  # Último item é o baú misterioso
    elif escolha == "3":
        abrir_bau(personagem, itens[-1])  # Último item é o baú de armas
    elif escolha == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")
