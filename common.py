from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client, gql
import random, string
from datetime import datetime
import time
import json
from randomtimestamp import randomtimestamp

class QueryExecutor:
    def __init__(self):
        self.transport = AIOHTTPTransport(url="http://localhost:5000/graphql")
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def execute(self, query):
        return self.client.execute(gql(query))

class DataGenerator:
    def __init__(self):
        pass

    def _getRandomHash(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))


    def _getRandomGender(self):
        return random.choice(["M", "F", "O"])

    def _getRandomColor(self):
        r = lambda: random.randint(0, 255)
        return ('#%02X%02X%02X' % (r(), r(), r()))

    def _getRandomHight(self):
        return random.randrange(10000)

    def _getRandomWidth(self):
        return random.randrange(10000)

    def _getRandomTexts(self):
        iterations = random.randrange(20)
        words = []
        for _ in range (iterations):
            words.append("".join(random.choices(string.ascii_lowercase, k=10)))
        return json.dumps(words)

    def _getRandomDate(self):
        d = random.randint(1, int(time.time()))
        return datetime.fromtimestamp(d).strftime('%Y-%m-%d')

    def _getRandomIncome(self):
        return random.randrange(10000)

    def _getRandomCoordinates(self):
        return random.uniform(-180,180)

    def _getRandomTimestamp(self):
        return randomtimestamp()

    def getRandomAd(self):
        return {
            "id": self._getRandomHash(),
            "color": self._getRandomColor(),
            "hight": self._getRandomHight(),
            "width": self._getRandomWidth(),
            "texts": self._getRandomTexts()
        }

    def getRandomPerson(self):
        return {
            "id": self._getRandomHash(),
            "gender": self._getRandomGender(),
            "birth": self._getRandomDate(),
            "income": self._getRandomIncome(),
            "interests": self._getRandomTexts(),
            "longitude": self._getRandomCoordinates(),
            "latitude": self._getRandomCoordinates()
        }

    def getRandomView(self):
        return {
            "personId": self._getRandomHash(),
            "adId": self._getRandomHash(),
            "viewTime": self._getRandomTimestamp()
        }

if __name__ == '__main__':
    data_generator = DataGenerator()
    print(data_generator._getRandomTimestamp())
