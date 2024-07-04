import unittest
from crud_operations import *
from database import init_db, close_db

class TestCrudOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()

    @classmethod
    def tearDownClass(cls):
        close_db()

    def test_hotel_crud(self):
        hotel_id = create_hotel("Hotel Teste", "Localização Teste")
        hotel = read_hotel(hotel_id)
        self.assertIsNotNone(hotel)
        update_hotel(hotel_id, "Hotel Atualizado", "Nova Localização")
        hotel = read_hotel(hotel_id)
        self.assertEqual(hotel['h']['name'], "Hotel Atualizado")
        delete_hotel(hotel_id)
        hotel = read_hotel(hotel_id)
        self.assertIsNone(hotel)

    def test_room_crud(self):
        hotel_id = create_hotel("Hotel para Quarto", "Localização Teste")
        room_id = create_room(101, "Suite", hotel_id)
        room = read_room(room_id)
        self.assertIsNotNone(room)
        update_room(room_id, 102, "Deluxe")
        room = read_room(room_id)
        self.assertEqual(room['r']['number'], 102)
        delete_room(room_id)
        room = read_room(room_id)
        self.assertIsNone(room)
        delete_hotel(hotel_id)

    def test_client_crud(self):
        client_id = create_client("Cliente Teste", "cliente@teste.com")
        client = read_client(client_id)
        self.assertIsNotNone(client)
        update_client(client_id, "Cliente Atualizado", "cliente@atualizado.com")
        client = read_client(client_id)
        self.assertEqual(client['c']['email'], "cliente@atualizado.com")
        delete_client(client_id)
        client = read_client(client_id)
        self.assertIsNone(client)

    def test_reservation_crud(self):
        hotel_id = create_hotel("Hotel para Reserva", "Localização Teste")
        room_id = create_room(201, "Standard", hotel_id)
        client_id = create_client("Cliente Reserva", "cliente@reserva.com")
        reservation_id = create_reservation(client_id, room_id, "2024-07-01", "2024-07-10")
        reservation = read_reservation(reservation_id)
        self.assertIsNotNone(reservation)
        update_reservation(reservation_id, "2024-07-05", "2024-07-15")
        reservation = read_reservation(reservation_id)
        self.assertEqual(reservation['res']['start_date'], "2024-07-05")
        delete_reservation(reservation_id)
        reservation = read_reservation(reservation_id)
        self.assertIsNone(reservation)
        delete_client(client_id)
        delete_room(room_id)
        delete_hotel(hotel_id)

    def test_list_reservations_by_client(self):
        # Setup
        client_id = create_client("Cliente Teste Relatório", "cliente@teste.com")
        hotel_id = create_hotel("Hotel Relatório", "Localização Teste")
        room_id = create_room(301, "Suite", hotel_id)
        create_reservation(client_id, room_id, "2024-08-01", "2024-08-10")
        create_reservation(client_id, room_id, "2024-08-15", "2024-08-20")

        # Test
        reservations = list_reservations_by_client(client_id)
        self.assertEqual(len(reservations), 2)

        # Teardown
        delete_client(client_id)
        delete_room(room_id)
        delete_hotel(hotel_id)

    def test_list_available_rooms(self):
        # Setup
        hotel_id = create_hotel("Hotel Disponibilidade", "Localização Teste")
        room_id = create_room(401, "Standard", hotel_id)
        client_id = create_client("Cliente Teste Disponibilidade", "cliente@teste.com")
        create_reservation(client_id, room_id, "2024-09-01", "2024-09-10")

        # Test
        available_rooms = list_available_rooms("2024-09-11", "2024-09-20")
        self.assertEqual(len(available_rooms), 1)

        # Teardown
        delete_client(client_id)
        delete_room(room_id)
        delete_hotel(hotel_id)

    def test_list_clients_with_multiple_reservations(self):
        # Setup
        client_id1 = create_client("Cliente Multiplas Reservas 1", "cliente1@teste.com")
        client_id2 = create_client("Cliente Multiplas Reservas 2", "cliente2@teste.com")
        hotel_id = create_hotel("Hotel Multiplas Reservas", "Localização Teste")
        room_id1 = create_room(501, "Standard", hotel_id)
        room_id2 = create_room(502, "Suite", hotel_id)

        create_reservation(client_id1, room_id1, "2024-10-01", "2024-10-10")
        create_reservation(client_id1, room_id2, "2024-10-15", "2024-10-20")
        create_reservation(client_id2, room_id1, "2024-10-05", "2024-10-15")

        # Test
        clients = list_clients_with_multiple_reservations()
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0]['email'], "cliente1@teste.com")

        # Teardown
        delete_client(client_id1)
        delete_client(client_id2)
        delete_room(room_id1)
        delete_room(room_id2)
        delete_hotel(hotel_id)

if __name__ == '__main__':
    unittest.main()