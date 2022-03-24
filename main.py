from card import Card
from database import database_connection


def main(data, context):
    Card.instantiate_from_json()
    database_connection.insert_card_details(Card.convert_to_db_list())
    Card.archive_all_cards()

    database_connection.connection.close()


if __name__ == '__main__':
    main('', '')
