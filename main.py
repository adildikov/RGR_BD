from contextlib import closing

import psycopg2

from athletes import Athletes
from competitions import Competitions
from rewards import Rewards
from sport_types import SportTypes
from teams import Teams

with closing(psycopg2.connect(dbname='rgr', user='postgres', password='postgres', host='localhost')) as conn:
    with conn.cursor() as cursor:

        while True:
            table = input('Choose table (Athletes, Competitions, Rewards, SportTypes, Teams) or "end" for exit:')
            if table == 'end':
                break
            elif table not in ['Athletes', 'Competitions', 'Rewards', 'SportTypes', 'Teams']:
                print(f'Table {table} not exist')
                continue

            operation = input(f'Enter operation for table {table} (show_all, select, insert, update, delete):')
            if operation not in ['show_all', 'select', 'insert', 'update', 'delete']:
                print(f'Operation {operation} not exist')
                continue

            try:
                if operation == 'show_all':
                    query, props = eval(f'{table}.show_all()')
                    cursor.execute(query, props)
                    print('Results:')
                    for row in cursor:
                        print(row)

                elif operation == 'select':
                    query, props = eval(f'{table}.select()')
                    cursor.execute(query, props)
                    print('Results:')
                    for row in cursor:
                        print(row)

                elif operation == 'delete':
                    query, props = eval(f'{table}.delete()')
                    cursor.execute(query, props)
                    conn.commit()
                    print('Operation done. Good!')

                elif operation == 'update':
                    query, props = eval(f'{table}.update()')
                    cursor.execute(query, props)
                    conn.commit()
                    print('Operation done. Good!')

                elif operation == 'insert':
                    query, props = eval(f'{table}.insert()')
                    cursor.execute(query, props)
                    conn.commit()
                    print('Operation done. Good!')

            except Exception as e:
                print(e)
