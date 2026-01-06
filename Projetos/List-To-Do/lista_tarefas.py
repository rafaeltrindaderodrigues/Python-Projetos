# Objetivo é fazer uma lista de tarefas

"""
Passos: 
 
 1 - Gerar uma estrutura de repetição para ele escolher entre adicionar tarefa, listar ou excluir
 2 - Salvar um arquivo com base nas alterações feitas
 
 
 """

import sys 
import os 
import json 
import time

lista_tarefas = []


while True:
    tarefa = input('\na[dicionar], d[eletar], [l]istar e [m]odificar tarefa: ').lower()

    # Trabalhando com a parte de adicionar a tarefa, mas dentro de cada tarefa deve ter a etapa de 
    # pendente, realizando ou concluida
    if tarefa == 'a':
        os.system('clear')
        adicionar = input('Valor: ').capitalize()

        print('\nAdicionando...')
        time.sleep(1)

        lista_tarefas.append({adicionar: "Pendente ⏱️"})
    
    elif tarefa == 'm':
        os.system('clear')

        for i, itens in enumerate(lista_tarefas):
            print(i, itens, sep='-')
        
        try:
            i = int(input('\nIndice para modificar: '))
    
        except ValueError: 
            print('Digite um número')
            continue

        # Pegando a key para acessar o valor e modificar
        try:
            os.system('clear')
            valor_chave = list(lista_tarefas[i].keys())[0]

            modificacao = input('p[endente], r[ealizando] e c[oncluida]: ').lower()

            print('\nModificando...')
            time.sleep(1)

            if modificacao == 'p':
                lista_tarefas[i][valor_chave] = "Pendente ⏱️"
            
            elif modificacao == 'r':
                lista_tarefas[i][valor_chave] = "Realizando 📝"
            
            elif modificacao == 'c': 
                lista_tarefas[i][valor_chave] = "Concluída ✅"
            
            else: 
                print('Digite corretamente')
                continue
    
        except IndexError: 
            print('O index digitado não está na lista')
            continue

    elif tarefa == 'd':
        os.system('clear')

        for i, itens in enumerate(lista_tarefas):
            print(i, itens, sep='-')

        try:
            i = int(input('Indice para modificar: '))
        
        except ValueError: 
            print('Digite um número')
            continue

        try:
            print('Deletando...')
            time.sleep(1)
            del lista_tarefas[i]

        except IndexError:
            print('O index digitado não está na lista')
            continue
    
    elif tarefa == 'l':
        os.system('clear')
        for i, itens in enumerate(lista_tarefas):
            print(i, itens, sep='-')
    
    else: 
        print('Digite corretamente')
        continue
     

# melhorias no código, eu pego o index duas vezes em deletar e modificar. Poderia fazer uma function para
# pegar o index e colocar nas duas condiçoes

        
        

        

