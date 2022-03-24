from datetime import datetime
import requests
import constants
from pytz import timezone


class Card:
    surplus_cards = []

    def __init__(self, card_id: str, name: str, writer: str, ):
        self.card_id = card_id
        self.name = name
        self.title = 'Surplus ' + self.name
        self.wordcount = 0
        self.client = -1
        self.writer = writer
        now = datetime.now(timezone('Asia/Kolkata'))
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        self.submitted_date = now
        self.status = -1
        self.set_card_custom_field()

        Card.surplus_cards.append(self)

    @staticmethod
    def instantiate_from_json():
        url = f"https://api.trello.com/1/lists/{constants.SURPLUS_LIST}/cards"

        response = requests.request(
            "GET",
            url,
            headers=constants.HEADERS,
            params=constants.PARAMS
        )

        for card_json in response.json():
            Card(card_json['id'], card_json['name'], card_json['idMembers'][0])

    def set_card_custom_field(self):
        proofreading_field_url = 'https://api.trello.com/1/cards' + f'/{self.card_id}/customFieldItems'

        response = requests.request(
            "GET",
            proofreading_field_url,
            params=constants.PARAMS,
            headers=constants.HEADERS
        )

        for custom_field_json in response.json():
            try:
                self.wordcount = int(custom_field_json['value']['number'])
                if self.wordcount < 0:
                    self.title = 'Deficit ' + self.name
            except:
                print('Could not find custom field.')

    @staticmethod
    def convert_to_db_list():
        values = []
        for card in Card.surplus_cards:
            values.append([card.card_id, card.title, card.wordcount, card.client,
                           card.writer, card.submitted_date, card.status])

        return values

    @staticmethod
    def archive_all_cards():
        url = f"https://api.trello.com/1/lists/{constants.SURPLUS_LIST}/archiveAllCards"

        response = requests.request(
            "POST",
            url,
            headers=constants.HEADERS,
            params=constants.PARAMS
        )

        print(response.status_code)
