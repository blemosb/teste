def show_tasks(tasks):
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Digite a nova tarefa: ")
    tasks.append(task)
    print(f"Tarefa '{task}' adicionada!")

def main():
    tasks = []
    while True:
        print("\nMenu:")
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Sair")
        print("4. TESTE")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            print("teste do git ***********.")
        elif choice == '4':
            print("teste do git 5.")
        elif choice == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
