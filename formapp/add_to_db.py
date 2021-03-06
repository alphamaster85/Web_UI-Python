# from . import models
import psycopg2
import datetime
from django.db import models
# from form_project.formapp.models import AnswerModel, QuestionModel

def insert_table_ones(table, first_place, name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO "{}"({}) VALUES('{}');""".format(table, first_place, name)
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect('dbname=formbase2 user=postgres password=root')
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_table_users(table, place1st, place2nd, place3th, place4th, dat1st, data2nd, data3th):
    sql = """INSERT INTO "{}"({}, {}, {}, {}) VALUES('{}', '{}', '{}', '{}');""".format(table, place1st, place2nd, place3th, place4th, dat1st, data2nd, data3th, datetime.date.today())
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect('dbname=formbase2 user=postgres password=root')
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the databasecd
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_table_usersdata(table, place1st, place2nd, place3th, place4th, place5th, dat1st, data2nd, data3th, data4th, data5th):
    sql = """INSERT INTO "{}"({}, {}, {}, {}, {})
             VALUES('{}', '{}', '{}', '{}', '{}');""".format(table, place1st, place2nd, place3th, place4th, place5th, dat1st, data2nd, data3th, data4th, data5th)
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect('dbname=formbase2 user=postgres password=root')
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the databasecd
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_from_file():
    sql_que_tlt = """INSERT INTO "question"(title, course_id, stage_id, tooltip) VALUES(%s, 1, %s, %s);"""
    sql_stg = """INSERT INTO "stage"(name, department) VALUES(%s, %s) RETURNING id;"""
    sql_que = """INSERT INTO "question"(title, course_id, stage_id) VALUES(%s, 1, %s);"""
    conn = None
    try:
        conn = psycopg2.connect('dbname=formbase2 user=postgres password=root')
        cur = conn.cursor()

        file = open('questions.txt', 'r')
        flag = 'Skills'
        flag_dict = {'Skills':'Activities', 'Activities':'Skills'}
        stage_id = 0
        for row in file:
            row = row.replace('\n', '')#.replace("'", "''")
            if row[0] is '#' and row[1] is '#':
                flag = flag_dict[flag]
            elif row[0] is '#':
                cur.execute(sql_stg, (row[1:], flag))
                conn.commit()
                stage_id = cur.fetchone()[0]
            else:
                if flag is 'Activities':
                    if row[0] is not '*':
                        sql = row
                        continue
                    cur.execute(sql_que_tlt, (sql, stage_id, row[1:]))
                    conn.commit()
                    continue
                cur.execute(sql_que, (row, stage_id))
                conn.commit()

        cur.close()
        file.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_answers_user():
    USER_ID = 1

    sql_insert = """INSERT INTO answer(user_id, question_id) VALUES(%s, %s);"""
    sql_select = """SELECT id FROM question;"""
    conn = None
    try:
        conn = psycopg2.connect('dbname=formbase2 user=postgres password=root')
        cur_select = conn.cursor()

        cur_select.execute(sql_select)
        columns = ('id',)
        results = []
        for row in cur_select.fetchall():
            results.append(dict(zip(columns, row)))
        cur_select.close()

        cur_insert = conn.cursor()
        for row in results:
            cur_insert.execute(sql_insert, (USER_ID, row['id']))
            conn.commit()
        cur_insert.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    insert_table_ones('course', 'name', 'Python')
    insert_table_ones('course', 'name', '.NET')
    insert_table_ones('course', 'name', 'Java')
    insert_table_ones('role', 'name', 'Admin')
    insert_table_ones('role', 'name', 'User')
    insert_table_ones('role', 'name', 'Expert')
    insert_table_ones('role', 'name', 'Recruiter')
    insert_table_ones('grade', 'name', 'None')
    insert_table_ones('grade', 'name', 'Beginner')
    insert_table_ones('grade', 'name', 'Good')
    insert_table_ones('grade', 'name', 'Strong')
    # insert_table_users('users', 'login', 'password', 'role_id', 'date', 'admin', 'admin', '1')
    # insert_table_users('users', 'login', 'password', 'role_id', 'date', 'andrii', '0000', '4')
    # insert_table_usersdata('usersdata', 'name', 'last', 'age', 'email', 'user_id', 'Andre', 'UA', 33, 'admin@ss.com', 1)
    # insert_table_usersdata('usersdata', 'name', 'last', 'age', 'email', 'user_id', 'Andrii', 'Ukrainets', 33, 'andre.ukrainets@gmail.com', 2)
    insert_from_file()
    # insert_answers_user()
    pass
