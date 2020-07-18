from tableauhyperapi import HyperProcess, Telemetry, Connection, CreateMode, NOT_NULLABLE, NULLABLE, SqlType, TableDefinition, Inserter, escape_name, escape_string_literal, HyperException,  TableName

with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    with Connection(endpoint=hyper.endpoint, database='drinks.hyper') as connection:
        tables = connection.catalog.get_table_names("public")
        print(tables)

        with connection.execute_query('SELECT * FROM drinks') as result:
            for row in result:
                print(row)
