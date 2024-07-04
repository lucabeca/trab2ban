from crud_operations import *
from database import init_db, close_db

def main_menu():
    while True:
        print("\nGerenciamento de Hotel")
        print("1. Gerenciar Hotéis")
        print("2. Gerenciar Quartos")
        print("3. Gerenciar Clientes")
        print("4. Gerenciar Reservas")
        print("5. Outras Operações")
        print("6. Executar Testes")
        print("7. Sair")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            manage_hotels()
        elif choice == '2':
            manage_rooms()
        elif choice == '3':
            manage_clients()
        elif choice == '4':
            manage_reservations()
        elif choice == '5':
            other_operations()
        elif choice == '6':
            run_tests()
        elif choice == '7':
            close_db()
            break
        else:
            print("Opção inválida, tente novamente.")

def manage_hotels():
    while True:
        print("\nMenu de Hotéis:")
        print("1 - Criar Hotel")
        print("2 - Ler Hotel")
        print("3 - Atualizar Hotel")
        print("4 - Deletar Hotel")
        print("5 - Listar Todos os Hotéis")
        print("6 - Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            name = input("Nome do Hotel: ")
            location = input("Localização do Hotel: ")
            create_hotel(name, location)
        elif choice == '2':
            hotel_id = input("ID do Hotel: ")
            hotel = read_hotel(hotel_id)
            if hotel:
                print(hotel)
            else:
                print("Hotel não encontrado.")
        elif choice == '3':
            hotel_id = input("ID do Hotel: ")
            new_name = input("Novo Nome do Hotel: ")
            new_location = input("Nova Localização do Hotel: ")
            update_hotel(hotel_id, new_name, new_location)
        elif choice == '4':
            hotel_id = input("ID do Hotel: ")
            delete_hotel(hotel_id)
        elif choice == '5':
            list_all_hotels()
        elif choice == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

def manage_rooms():
    while True:
        print("\nMenu de Quartos:")
        print("1 - Criar Quarto")
        print("2 - Ler Quarto")
        print("3 - Atualizar Quarto")
        print("4 - Deletar Quarto")
        print("5 - Listar Todos os Quartos")
        print("6 - Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            hotel_id = input("ID do Hotel: ")
            number = input("Número do Quarto: ")
            type = input("Tipo do Quarto: ")
            create_room(number, type, hotel_id)
        elif choice == '2':
            room_id = input("ID do Quarto: ")
            room = read_room(room_id)
            if room:
                print(room)
            else:
                print("Quarto não encontrado.")
        elif choice == '3':
            room_id = input("ID do Quarto: ")
            new_number = input("Novo Número do Quarto: ")
            new_type = input("Novo Tipo do Quarto: ")
            update_room(room_id, new_number, new_type)
        elif choice == '4':
            room_id = input("ID do Quarto: ")
            delete_room(room_id)
        elif choice == '5':
            list_all_rooms()
        elif choice == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

def manage_clients():
    while True:
        print("\nMenu de Clientes:")
        print("1 - Criar Cliente")
        print("2 - Ler Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Deletar Cliente")
        print("5 - Listar Todos os Clientes")
        print("6 - Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            name = input("Nome do Cliente: ")
            email = input("Email do Cliente: ")
            create_client(name, email)
        elif choice == '2':
            client_id = input("ID do Cliente: ")
            client = read_client(client_id)
            if client:
                print(client)
            else:
                print("Cliente não encontrado.")
        elif choice == '3':
            client_id = input("ID do Cliente: ")
            new_name = input("Novo Nome do Cliente: ")
            new_email = input("Novo Email do Cliente: ")
            update_client(client_id, new_name, new_email)
        elif choice == '4':
            client_id = input("ID do Cliente: ")
            delete_client(client_id)
        elif choice == '5':
            list_all_clients()
        elif choice == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

def manage_reservations():
    while True:
        print("\nMenu de Reservas:")
        print("1 - Criar Reserva")
        print("2 - Ler Reserva")
        print("3 - Atualizar Reserva")
        print("4 - Deletar Reserva")
        print("5 - Listar Todas as Reservas")
        print("6 - Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            client_id = input("ID do Cliente: ")
            room_id = input("ID do Quarto: ")
            start_date = input("Data de Início (YYYY-MM-DD): ")
            end_date = input("Data de Fim (YYYY-MM-DD): ")
            create_reservation(client_id, room_id, start_date, end_date)
        elif choice == '2':
            reservation_id = input("ID da Reserva: ")
            reservation = read_reservation(reservation_id)
            if reservation:
                print(reservation)
            else:
                print("Reserva não encontrada.")
        elif choice == '3':
            reservation_id = input("ID da Reserva: ")
            new_start_date = input("Nova Data de Início (YYYY-MM-DD): ")
            new_end_date = input("Nova Data de Fim (YYYY-MM-DD): ")
            update_reservation(reservation_id, new_start_date, new_end_date)
        elif choice == '4':
            reservation_id = input("ID da Reserva: ")
            delete_reservation(reservation_id)
        elif choice == '5':
            list_all_reservations()
        elif choice == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

def other_operations():
    while True:
        print("\nOutras Operações:")
        print("1 - Listar Reservas por Cliente")
        print("2 - Listar Quartos Disponíveis")
        print("3 - Listar Clientes com Múltiplas Reservas")
        print("4 - Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            client_id = input("ID do Cliente: ")
            list_reservations_by_client(client_id)
        elif choice == '2':
            start_date = input("Data de Início (YYYY-MM-DD): ")
            end_date = input("Data de Fim (YYYY-MM-DD): ")
            list_available_rooms(start_date, end_date)
        elif choice == '3':
            list_clients_with_multiple_reservations()
        elif choice == '4':
            break
        else:
            print("Opção inválida, tente novamente.")

def run_tests():
    import unittest
    import test_crud_operations
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_crud_operations)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    init_db()
    main_menu()
    close_db()