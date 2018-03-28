schema='(A,C)'
filename=$1
dates=$2
col_name='date_quote'
echo $filename
echo $dates
sed  '1 d' $filename | sed 's/[^[:alnum:]]\+$//;s/ \{1,\}/,/g' | sed 's/,/-/2g' | sed '1i A,C' | sed $'s/\r$//' | sed '/^$/d' | PGPASSFILE=~/.pgpass psql -h rds-postgresql.clahixkkwlcw.us-east-1.rds.amazonaws.com --port=5432 --username administrator --dbname stockdata -c "COPY temporal_quote ${schema} FROM stdin CSV HEADER;"

PGPASSFILE=~/.pgpass psql -h rds-postgresql.clahixkkwlcw.us-east-1.rds.amazonaws.com --port=5432 --username administrator --dbname stockdata -f populate_temporal_quote_data.sql -v d=$dates



