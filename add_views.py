from common import QueryExecutor
from templates import createViewMutation
import sys

if __name__ == '__main__':
    queryExecutor = QueryExecutor()

    query = createViewMutation.format(
        personId=sys.argv[1], adId=sys.argv[2], viewTime=sys.argv[3])
    print(query)
    addResult = queryExecutor.execute(query)
    print(addResult)
