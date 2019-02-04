# import json
# import psycopg2
#
# conn = psycopg2.connect('dbname=formbase user=postgres password=root')
# cur = conn.cursor()
#
# cur.execute("""SELECT id, part, stage FROM stages WHERE part='Activities';""")
# columns = ('id', 'part', 'stage')
# results = []
# for row in cur.fetchall():
#     results.append(dict(zip(columns, row)))
#
# cur.close()
# conn.close()
#
# print(results)
# # print(json.dumps(results, indent=2))

from .models import StageModel

if __name__ == "__main__":
    a = StageModel.objects.all()
    print(a)
