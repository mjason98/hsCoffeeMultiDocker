from services.connect import create_conn


def get_best_coffee(userid):
    best_coffee = ''

    try:
        conn = create_conn()

        query = f'''
            SELECT c1 from coffee.UserCoffee
            WHERE UserId='{userid}'
        '''

        conn.execute(query)
        result = conn.fetchone()
        best_coffee = result[0]

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise 'Connection error'

    return best_coffee


def get_top3_leaderboard():
    best_coffee = []

    try:
        conn = create_conn()

        query = '''
            select t2.cn from
            (select t.c1 as cn, COUNT(*) as co from
            (select c1 from coffee.usercoffee
            union all
            select c2 from coffee.usercoffee
            union ALL
            select c3 from coffee.usercoffee) as t
            group by t.c1) as t2
            order by t2.co desc
            limit 3
        '''

        conn.execute(query)
        result = conn.fetchall()
        best_coffee = list(map(lambda x: x[0], result))

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise 'Connection error'

    return best_coffee


def get_top3_coffee(userid):
    best_coffee = ''

    try:
        conn = create_conn()

        query = f'''
            SELECT c1,c2,c3 from coffee.UserCoffee
            WHERE UserId='{userid}'
        '''

        conn.execute(query)
        result = conn.fetchone()
        best_coffee = result

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise 'Connection error'

    return best_coffee


def set_top3_coffee(userid, list3):
    try:
        assert len(list3) == 3, 'the list of coffees most be of size 3'

        conn = create_conn()

        query = f'''
            UPDATE coffee.UserCoffee
            SET c1='{list3[0]}',c2='{list3[1]}',c3='{list3[2]}'
            WHERE UserId={userid}
        '''

        conn.execute(query)
        conn.execute('commit')
        conn.close()
    except Exception as e:
        conn.execute('rollback')
        print(f"An error occurred: {str(e)}")
        raise 'An error ocurred'
