import sqlite3

dbname = 'discord.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()


# 大文字部はSQL文。小文字でも問題ない。
#cur.execute('CREATE TABLE servers(id INTEGER ,name STRING)')

# データベースへコミット。これで変更が反映される。
#conn.commit()
conn.close()