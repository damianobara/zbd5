from common import QueryExecutor, DataGenerator
from templates import existsAdQuery, createAdMutation, updateAdMutation

if __name__ == '__main__':
    dataGenerator = DataGenerator()
    queryExecutor = QueryExecutor()

    for i in range(10):
        ad = dataGenerator.getRandomAd()
        query = existsAdQuery.format(id=ad["id"])
        existsResult = queryExecutor.execute(query)

        if existsResult["ad"] == None:
            query = createAdMutation.format(
                id=ad["id"], color=ad["color"], hight=ad["hight"], width=ad["width"], texts=ad["width"])
            addResult = queryExecutor.execute(query)
            print(addResult)
        else:
            query = updateAdMutation.format(
                id=ad["id"], color=ad["color"], hight=ad["hight"], width=ad["width"], texts=ad["width"])
            updateResult = queryExecutor.execute(query)
            print(updateResult)