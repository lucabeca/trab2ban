from database import db

def create_hotel(name, location):
    with db.driver.session() as session:
        result = session.run("""
        CREATE (h:Hotel {name: $name, location: $location})
        RETURN elementId(h) AS id, h.name AS name, h.location AS location
        """, {"name": name, "location": location})
        record = result.single()
        print(f"Hotel criado com sucesso: ID={record['id']}, Name={record['name']}, Location={record['location']}")
        return record['id']

def read_hotel(hotel_id):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (h:Hotel)
        WHERE elementId(h) = $hotel_id
        RETURN h
        """, {"hotel_id": hotel_id})
        return result.single()

def update_hotel(hotel_id, new_name, new_location):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (h:Hotel)
        WHERE elementId(h) = $hotel_id
        SET h.name = $new_name, h.location = $new_location
        RETURN h
        """, {"hotel_id": hotel_id, "new_name": new_name, "new_location": new_location})
        record = result.single()
        print(f"Hotel atualizado com sucesso: ID={hotel_id}, Name={record['h']['name']}, Location={record['h']['location']}")

def delete_hotel(hotel_id):
    with db.driver.session() as session:
        session.run("""
        MATCH (h:Hotel)
        WHERE elementId(h) = $hotel_id
        DETACH DELETE h
        """, {"hotel_id": hotel_id})
    print(f"Hotel deletado com sucesso: ID={hotel_id}")

def list_all_hotels():
    with db.driver.session() as session:
        result = session.run("""
        MATCH (h:Hotel)
        RETURN elementId(h) AS id, h.name AS name, h.location AS location
        """)
        records = list(result)
        for record in records:
            print(f"ID={record['id']}, Name={record['name']}, Location={record['location']}")

# Quartos
def create_room(number, type, hotel_id):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (h:Hotel)
        WHERE elementId(h) = $hotel_id
        CREATE (r:Room {number: $number, type: $type})-[:BELONGS_TO]->(h)
        RETURN elementId(r) AS id, r.number AS number, r.type AS type
        """, {"number": number, "type": type, "hotel_id": hotel_id})
        record = result.single()
        print(f"Quarto criado com sucesso: ID={record['id']}, Number={record['number']}, Type={record['type']}")
        return record['id']

def read_room(room_id):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (r:Room)
        WHERE elementId(r) = $room_id
        RETURN r
        """, {"room_id": room_id})
        return result.single()

def update_room(room_id, new_number, new_type):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (r:Room)
        WHERE elementId(r) = $room_id
        SET r.number = $new_number, r.type = $new_type
        RETURN r
        """, {"room_id": room_id, "new_number": new_number, "new_type": new_type})
        record = result.single()
        print(f"Quarto atualizado com sucesso: ID={room_id}, Number={record['r']['number']}, Type={record['r']['type']}")

def delete_room(room_id):
    with db.driver.session() as session:
        session.run("""
        MATCH (r:Room)
        WHERE elementId(r) = $room_id
        DETACH DELETE r
        """, {"room_id": room_id})
    print(f"Quarto deletado com sucesso: ID={room_id}")

def list_all_rooms():
    with db.driver.session() as session:
        result = session.run("""
        MATCH (r:Room)
        RETURN elementId(r) AS id, r.number AS number, r.type AS type
        """)
        records = list(result)
        for record in records:
            print(f"ID={record['id']}, Number={record['number']}, Type={record['type']}")

# Clientes
def create_client(name, email):
    with db.driver.session() as session:
        result = session.run("""
        CREATE (c:Client {name: $name, email: $email})
        RETURN elementId(c) AS id, c.name AS name, c.email AS email
        """, {"name": name, "email": email})
        record = result.single()
        print(f"Cliente criado com sucesso: ID={record['id']}, Name={record['name']}, Email={record['email']}")
        return record['id']

def read_client(client_id):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (c:Client)
        WHERE elementId(c) = $client_id
        RETURN c
        """, {"client_id": client_id})
        return result.single()

def update_client(client_id, new_name, new_email):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (c:Client)
        WHERE elementId(c) = $client_id
        SET c.name = $new_name, c.email = $new_email
        RETURN c
        """, {"client_id": client_id, "new_name": new_name, "new_email": new_email})
        record = result.single()
        print(f"Cliente atualizado com sucesso: ID={client_id}, Name={record['c']['name']}, Email={record['c']['email']}")

def delete_client(client_id):
    with db.driver.session() as session:
        session.run("""
        MATCH (c:Client)
        WHERE elementId(c) = $client_id
        DETACH DELETE c
        """, {"client_id": client_id})
    print(f"Cliente deletado com sucesso: ID={client_id}")

def list_all_clients():
    with db.driver.session() as session:
        result = session.run("""
        MATCH (c:Client)
        RETURN elementId(c) AS id, c.name AS name, c.email AS email
        """)
        records = list(result)
        for record in records:
            print(f"ID={record['id']}, Name={record['name']}, Email={record['email']}")

# Reservas
def create_reservation(client_id, room_id, start_date, end_date):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (c:Client)
        WHERE elementId(c) = $client_id
        MATCH (r:Room)
        WHERE elementId(r) = $room_id
        CREATE (res:Reservation {start_date: $start_date, end_date: $end_date})-[:MADE_BY]->(c), (res)-[:BOOKS]->(r)
        RETURN elementId(res) AS id, res.start_date AS start_date, res.end_date AS end_date
        """, {"client_id": client_id, "room_id": room_id, "start_date": start_date, "end_date": end_date})
        record = result.single()
        print(f"Reserva criada com sucesso: ID={record['id']}, Start Date={record['start_date']}, End Date={record['end_date']}")
        return record['id']

def read_reservation(reservation_id):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (res:Reservation)
        WHERE elementId(res) = $reservation_id
        RETURN res
        """, {"reservation_id": reservation_id})
        return result.single()

def update_reservation(reservation_id, new_start_date, new_end_date):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (res:Reservation)
        WHERE elementId(res) = $reservation_id
        SET res.start_date = $new_start_date, res.end_date = $new_end_date
        RETURN res
        """, {"reservation_id": reservation_id, "new_start_date": new_start_date, "new_end_date": new_end_date})
        record = result.single()
        print(f"Reserva atualizada com sucesso: ID={reservation_id}, Start Date={record['res']['start_date']}, End Date={record['res']['end_date']}")

def delete_reservation(reservation_id):
    with db.driver.session() as session:
        session.run("""
        MATCH (res:Reservation)
        WHERE elementId(res) = $reservation_id
        DETACH DELETE res
        """, {"reservation_id": reservation_id})
    print(f"Reserva deletada com sucesso: ID={reservation_id}")

def list_all_reservations():
    with db.driver.session() as session:
        result = session.run("""
        MATCH (res:Reservation)
        RETURN elementId(res) AS id, res.start_date AS start_date, res.end_date AS end_date
        """)
        records = list(result)
        for record in records:
            print(f"ID={record['id']}, Start Date={record['start_date']}, End Date={record['end_date']}")

# Outras Operações

def list_reservations_by_client(client_id):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (c:Client)-[:MADE_BY]->(res:Reservation)-[:BOOKS]->(r:Room)
        WHERE elementId(c) = $client_id
        RETURN res, r
        """, {"client_id": client_id})
        records = list(result)
        return [record['res'] for record in records]

def list_available_rooms(start_date, end_date):
    with db.driver.session() as session:
        result = session.run("""
        MATCH (r:Room)
        WHERE NOT EXISTS {
            MATCH (r)<-[:BOOKS]-(res:Reservation)
            WHERE res.start_date < $end_date AND res.end_date > $start_date
        }
        RETURN r
        """, {"start_date": start_date, "end_date": end_date})
        records = list(result)
        return [record['r'] for record in records]

def list_clients_with_multiple_reservations():
    with db.driver.session() as session:
        result = session.run("""
        MATCH (c:Client)-[:MADE_BY]->(res:Reservation)
        WITH c, count(res) AS num_reservations
        WHERE num_reservations > 1
        RETURN c, num_reservations
        """)
        records = list(result)
        return [record['c'] for record in records]