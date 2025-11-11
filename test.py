import  pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="g5e5a7v4",
    database="flask_demo",
    charset="utf8mb4"
)

def con_my_sql(sql_code):
    try:
        conn.ping(reconnect=True)  # 确保数据库连接可用
        print(sql_code)

        cursor = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象，结果以字典返回
        cursor.execute(sql_code)  # 执行传入的 SQL

        conn.commit()  # 提交事务（例如 INSERT、UPDATE、DELETE）
        conn.close()   # 关闭连接
        return cursor  # 返回结果

    except pymysql.MySQLError as err_message:
        conn.rollback()  # 发生错误时回滚
        conn.close()
        return type(err_message), err_message  # 返回错误类型和内容



# username = "Lanye"
# pwd = '123456'
# code  = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')"%(username,pwd)
# print(con_my_sql(code)) # 插入测试

# username = "Lanye"
# code = "select * from login_user where username='%s'" % (username)
# cursor_ans = con_my_sql(code)
# print(cursor_ans.fetchall())  # 查询测试

