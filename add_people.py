from common import QueryExecutor, DataGenerator
from templates import existsPersonQuery, createPersonMutation, updatePersonMutation

if __name__ == '__main__':
    dataGenerator = DataGenerator()
    queryExecutor = QueryExecutor()

    for i in range(10):
        person = dataGenerator.getRandomPerson()
        query = existsPersonQuery.format(id=person["id"])
        existsResult = queryExecutor.execute(query)
        print(existsResult)

        if existsResult["person"] == None:
            query = createPersonMutation.format(
                id=person["id"], gender=person["gender"],
                birth=person["birth"], income=person["income"],
                interests=person["interests"], longitude=person["longitude"], latitude=person["latitude"])
            addResult = queryExecutor.execute(query)
            print(addResult)
        else:
            query = updatePersonMutation.format(
                id=person["id"], gender=person["gender"],
                birth=person["birth"], income=person["income"],
                interests=person["interests"], longitude=person["longitude"], latitude=person["latitude"])
            updateResult = queryExecutor.execute(query)
            print(updateResult)