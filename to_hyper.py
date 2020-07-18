from tableauhyperapi import HyperProcess, Telemetry, Connection, CreateMode, NOT_NULLABLE, NULLABLE, SqlType, TableDefinition, Inserter, escape_name, escape_string_literal, HyperException,  TableName

with HyperProcess(telemetry=Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU) as hyper:

         # Creates a new Hyper file or
         # replaces the file if it already exists.
    with Connection(
            endpoint=hyper.endpoint,
            database="drinks.hyper",
            create_mode=CreateMode.CREATE_AND_REPLACE) as connection:

        # default schema name is "public"
        # define table
        drinks_table = TableDefinition(
            table_name="drinks",
            columns=[
                TableDefinition.Column(
                    "country", SqlType.text(), NOT_NULLABLE),
                TableDefinition.Column(
                    "beer_servings", SqlType.big_int(), NOT_NULLABLE),
                TableDefinition.Column(
                    "spirit_servings", SqlType.big_int(), NOT_NULLABLE),
                TableDefinition.Column(
                    "wine_servings", SqlType.big_int(), NOT_NULLABLE),
                TableDefinition.Column(
                    "total_litres_of_pure_alcohol", SqlType.double(), NOT_NULLABLE),
                TableDefinition.Column(
                    "continent", SqlType.text(), NOT_NULLABLE)
            ]
        )

        # create tables
        connection.catalog.create_table(drinks_table)

        path_to_csv = "drinks.csv"
        print(drinks_table.table_name)

        count_in_drinks_table = connection.execute_command(
            command=f"COPY drinks FROM 'drinks.csv' (format csv, delimiter ',', header)"
            # f"(format csv, NULL 'NULL', delimiter ',', header)"
        )
        print(
            f"The number of rows in table {drinks_table.table_name} is {count_in_drinks_table}.")
