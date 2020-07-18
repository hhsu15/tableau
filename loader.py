import tableauserverclient as TSC
import os

tableau_auth = TSC.TableauAuth(
    os.getenv("USER"), os.getenv("PASSWORD"), os.getenv('SITE'))

server = TSC.Server('https://prod-useast-a.online.tableau.com/')

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(
        pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])

    # get projects
    projects = TSC.Pager(server.projects)
    for p in projects:
        print(p.name)
        print(p.id)

    # upload file
    project_id = "e2db3b78-d90c-42cb-8ec9-3375dd2e3254"
    file_path = "drinks.hyper"

    new_datasource = TSC.DatasourceItem(project_id)

    new_datasource = server.datasources.publish(
        new_datasource, file_path, "CreateNew"
    )
