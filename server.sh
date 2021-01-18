npx postgraphile \
  -c postgres://postgres:postgres@localhost:5432/postgres \
  --schema zad5 \
  --append-plugins @graphile-contrib/pg-simplify-inflector,postgraphile-plugin-connection-filter,@graphile/postgis \
  --enhance-graphiql \
  --allow-explain \
  --watch
  