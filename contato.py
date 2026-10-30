import sqlite3

def conectar_banco():

    conn = sqlite3.connect('contatos.db')

    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL
            )'''
    cursor.execute(sql)
    conn.commit()
    return conn

def menu():
    print("### CONTATOS ###")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Atualizar contato")
    print("5 - Excluir contato")
    print("0 - Sair")

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conn.commit()
    conn.close()
    print("Contato adicionado com sucesso!")

def listar_contatos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conn.close()
    print("### LISTA DE CONTATOS ###")
    for contato in contatos:
        print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conn.close()
    if contatos:
        print("### RESULTADOS DA BUSCA ###")
        for contato in contatos:
            print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}")
    else:
        print("Nenhum contato encontrado.")

def atualizar_contato():
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    nome = input("Digite o novo nome do contato: ")
    telefone = input("Digite o novo telefone do contato: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE contatos SET nome = ?, telefone = ? WHERE id = ?", (nome, telefone, id_contato))
    conn.commit()
    conn.close()
    print("Contato atualizado com sucesso!")

def excluir_contato():
    id_contato = input("Digite o ID do contato que deseja excluir: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    conn.commit()
    conn.close()
    print("Contato excluído com sucesso!")




while True:  

        print("### CONTATOS ###")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Atualizar contato")
        print("5 - Excluir contato")
        print("0 - Sair")


        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            atualizar_contato()
        elif opcao == "5": 
            excluir_contato()
        elif opcao == "0":
            print("Saindo do programa...")
            break

        menu()