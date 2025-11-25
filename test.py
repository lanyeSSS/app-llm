# import  pymysql

# conn = pymysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="g5e5a7v4",
#     database="flask_demo",
#     charset="utf8mb4"
# )

# def con_my_sql(sql_code):
#     try:
#         conn.ping(reconnect=True)  # 确保数据库连接可用
#         print(sql_code)

#         cursor = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象，结果以字典返回
#         cursor.execute(sql_code)  # 执行传入的 SQL

#         conn.commit()  # 提交事务（例如 INSERT、UPDATE、DELETE）
#         conn.close()   # 关闭连接
#         return cursor  # 返回结果

#     except pymysql.MySQLError as err_message:
#         conn.rollback()  # 发生错误时回滚
#         conn.close()
#         return type(err_message), err_message  # 返回错误类型和内容



# username = "Lanye"
# pwd = '123456'
# code  = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')"%(username,pwd)
# print(con_my_sql(code)) # 插入测试

# username = "Lanye"
# code = "select * from login_user where username='%s'" % (username)
# cursor_ans = con_my_sql(code)
# print(cursor_ans.fetchall())  # 查询测试

# import pymysql
# import os

# def get_db_config():
#     """获取数据库配置，支持环境变量"""
#     if os.environ.get('MYSQLHOST'):  # 如果存在Railway的环境变量
#         return {
#             "host": os.environ.get('MYSQLHOST'),
#             "port": int(os.environ.get('MYSQLPORT', 3306)),
#             "user": os.environ.get('MYSQLUSER'),
#             "password": os.environ.get('MYSQLPASSWORD'),
#             "database": os.environ.get('MYSQLDATABASE'),
#             "charset": "utf8mb4"
#         }
#     else:
#         # 开发环境配置
#         return {
#             "host": "localhost",
#             "port": 3306,
#             "user": "root",
#             "password": "g5e5a7v4",
#             "database": "flask_demo",
#             "charset": "utf8mb4"
#         }

# def create_connection():
#     """创建新的数据库连接"""
#     db_config = get_db_config()
#     return pymysql.connect(**db_config)

# def con_my_sql(sql_code):
#     try:
#         # 每次执行SQL都创建新的连接，避免连接超时问题
#         conn = create_connection()
#         print(sql_code)

#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute(sql_code)
#         conn.commit()  # 提交事务
        
#         return cursor  # 返回cursor，调用者需要处理关闭

#     except pymysql.MySQLError as err_message:
#         if 'conn' in locals():
#             conn.rollback()  # 发生错误时回滚
#             conn.close()
#         return f"数据库错误: {err_message}"

import pymysql
import os

def get_db_config():
    """获取数据库配置"""
    if os.environ.get('MYSQLHOST'):  # 云平台
        return {
            "host": os.environ.get('MYSQLHOST'),
            "port": int(os.environ.get('MYSQLPORT', 3306)),
            "user": os.environ.get('MYSQLUSER'),
            "password": os.environ.get('MYSQLPASSWORD'),
            "database": os.environ.get('MYSQLDATABASE'),
            "charset": "utf8mb4"
        }
    else:  # 本地
        return {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "g5e5a7v4",
            "database": "flask_demo",
            "charset": "utf8mb4"
        }

def con_my_sql(sql_code):
    conn = None
    try:
        conn = pymysql.connect(**get_db_config())
        print(sql_code)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql_code)
        conn.commit()
        
        # 关键修复: 先获取结果,再关闭连接
        result = cursor.fetchall()
        return result  # 直接返回结果列表
        
    except pymysql.MySQLError as err:
        if conn:
            conn.rollback()
        print(f"数据库错误: {err}")
        return []
    finally:
        if conn:
            conn.close()