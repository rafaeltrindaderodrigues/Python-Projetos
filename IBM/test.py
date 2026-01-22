from random import randint, choice

brazilian_names = [
    "Ana","Maria","João","José","Pedro","Paulo","Lucas","Bruno","Rafael","Daniel",
    "Carlos","Marcelo","André","Felipe","Eduardo","Gabriel","Matheus","Thiago","Diego","Guilherme",
    "Ricardo","Fernando","Roberto","Antônio","Marcos","Leonardo","Victor","Vinícius","Rodrigo","Alexandre",
    "Renan","Caio","Gustavo","Fábio","Leandro","Henrique","Miguel","Arthur","Bernardo","Davi",
    "Enzo","Otávio","Igor","Yuri","Renato","César","Wagner","Alessandro","Silvio","Samuel",
    "Murilo","Allan","Alan","Maurício","Nelson","Nilton","Jair","Patrick","Matias","Heitor",
    "Renata","Paula","Daniela","Camila","Carolina","Beatriz","Bruna","Larissa","Fernanda","Mariana",
    "Patrícia","Amanda","Gabriela","Natália","Bianca","Vanessa","Juliana","Raquel","Priscila","Tatiana"
]





# with open('./IBM/clients.txt', 'w+', encoding='utf-8') as f:
#     for user in users:
#         f.write(f'{user['User']}, {user['age']}, {user['departament']}, {user['salary']} \n')

#     f.seek(0)

#     content = f.read()

# print(content)

users = []

class File:
    standard_path = './IBM/clients.txt'

    def __init__(self, max_value = 0):
        self.max_value = max_value

    def creating_register(self):
        for x in range(0, self.max_value):
            users.append({
                            'User': choice(brazilian_names), 
                            'age': randint(16, 68), 
                            'departament': choice(['A', 'B', 'C']), 
                            'salary': randint(1600, 20001)  })

instance1 = File(100)
print(instance1.creating_register())
