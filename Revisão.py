#1
'''
def verificar_numero(numero):
    if numero > 0:
        print('O número é positivo')
    elif numero < 0:
        print('O número é negativo')
    else:
        print('O número é zero')

numero = float(input('Digite um número: '))
verificar_numero(numero)
'''
#2
'''
numeros = []

def adicionar():
    numero = float(entrada_numero.get())
    numeros.append(numero)
    numeros.sort()

    lista.delete(0, tk.END)
    for n in numeros:
        lista.insert(tk.END, n)

    entrada_numero.delete(0, tk.END)

def buscar_maior():
    limite = float(entrada_limite.get())

    indice = -1
    for posicao in range(len(numeros)):
        if numeros[posicao] > limite:
            indice = posicao
            break

    if indice == -1:
        resultado.config(text='Resultado: -1\nNenhum elemento é maior que o limite')
    else:
        resultado.config(text=f'Resultado: índice {indice}\nValor: {numeros[indice]}')

def limpar():
    numeros.clear()
    lista.delete(0, tk.END)
    resultado.config(text='Resultado: ')

janela = tk.Tk()
janela.title('Maior que o Limite')
janela.geometry('600x400')

tk.Label(janela, text='Número: ', font='Verdana 10 bold').grid(row=0, column=0, padx=10, pady=5)
entrada_numero = tk.Entry(janela)
entrada_numero.grid(row=0, column=1)
tk.Button(janela, text='Adicionar', width=12, command=adicionar).grid(row=0, column=2, padx=10)

tk.Label(janela, text='Limite: ', font='Verdana 10 bold').grid(row=1, column=0, padx=10, pady=5)
entrada_limite = tk.Entry(janela)
entrada_limite.grid(row=1, column=1)
tk.Button(janela, text='Verificar', width=12, fg='white', bg='#4CAF50',
          command=buscar_maior).grid(row=1, column=2, padx=10)

tk.Label(janela, text='Lista ordenada:').grid(row=2, column=0, columnspan=3)
lista = tk.Listbox(janela, width=30, height=8)
lista.grid(row=3, column=0, columnspan=3)

tk.Button(janela, text='Limpar lista', width=12, fg='white', bg='red',
          command=limpar).grid(row=4, column=0, columnspan=3, pady=5)

resultado = tk.Label(janela, text='Resultado: ', font='Verdana 12 bold')
resultado.grid(row=5, column=0, columnspan=3)

janela.mainloop()
'''
#3
'''
numeros = []
 
def adicionar():
    numero = float(entrada.get())
    numeros.append(numero)
    lista.insert(tk.END, f'Índice {len(numeros) - 1}: {numero}')
    entrada.delete(0, tk.END)
 
def analisar():
    if len(numeros) == 0:
        resultado.config(text='Adicione pelo menos um número')
        return
 
    maior = max(numeros)
    menor = min(numeros)
 
    resultado.config(text=f'Maior valor: {maior} - índice {numeros.index(maior)}' +
                     f'\nMenor valor: {menor} - índice {numeros.index(menor)}')
 
def limpar():
    numeros.clear()
    lista.delete(0, tk.END)
    resultado.config(text='Resultado: ')
 
janela = tk.Tk()
janela.title('Maior e Menor')
janela.geometry('600x400')
 
tk.Label(janela, text='Digite um número: ', font='Verdana 10 bold').pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack()
 
tk.Button(janela, text='Adicionar', width=15, command=adicionar).pack(pady=5)
 
lista = tk.Listbox(janela, width=30, height=8)
lista.pack()
 
tk.Button(janela, text='Analisar', width=15, fg='white', bg='#4CAF50',
          command=analisar).pack(pady=5)
tk.Button(janela, text='Limpar lista', width=15, fg='white', bg='red',
          command=limpar).pack()
 
resultado = tk.Label(janela, text='Resultado: ', font='Verdana 12 bold')
resultado.pack(pady=5)
 
janela.mainloop()
'''
#4

numeros = []
 
def adicionar():
    numero = float(entrada_numero.get())
    numeros.append(numero)
    lista.insert(tk.END, f'Índice {len(numeros) - 1}: {numero}')
    entrada_numero.delete(0, tk.END)
 
def buscar():
    busca = float(entrada_busca.get())
 
    posicoes = []
    for posicao in range(len(numeros)):
        if numeros[posicao] == busca:
            posicoes.append(posicao)
 
    if len(posicoes) == 0:
        resultado.config(text='Número não encontrado')
    else:
        resultado.config(text=f'O número {busca} está na lista' +
                         f'\nPosição(ões): {posicoes}')
 
def limpar():
    numeros.clear()
    lista.delete(0, tk.END)
    resultado.config(text='Resultado: ')
 
janela = tk.Tk()
janela.title('Buscar Número')
janela.geometry('600x400')
 
tk.Label(janela, text='Número: ', font='Verdana 10 bold').grid(row=0, column=0, padx=10, pady=5)
entrada_numero = tk.Entry(janela)
entrada_numero.grid(row=0, column=1)
tk.Button(janela, text='Adicionar', width=12, command=adicionar).grid(row=0, column=2, padx=10)
 
tk.Label(janela, text='Buscar: ', font='Verdana 10 bold').grid(row=1, column=0, padx=10, pady=5)
entrada_busca = tk.Entry(janela)
entrada_busca.grid(row=1, column=1)
tk.Button(janela, text='Buscar', width=12, fg='white', bg='#4CAF50',
          command=buscar).grid(row=1, column=2, padx=10)
 
lista = tk.Listbox(janela, width=30, height=8)
lista.grid(row=2, column=0, columnspan=3, pady=10)
 
tk.Button(janela, text='Limpar lista', width=12, fg='white', bg='red',
          command=limpar).grid(row=3, column=0, columnspan=3)
 
resultado = tk.Label(janela, text='Resultado: ', font='Verdana 12 bold')
resultado.grid(row=4, column=0, columnspan=3, pady=5)
 
janela.mainloop()