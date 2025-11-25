import os
import psycopg2
import psycopg2.extras

def get_conn():
    """连接 Render Postgres 数据库"""
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise Exception("DATABASE_URL 环境变量未设置")

    return psycopg2.connect(db_url, cursor_factory=psycopg2.extras.DictCursor)


def init_db():
    """自动创建 login_user 表（如果不存在）"""
    conn = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS login_user (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        """)
        conn.commit()
    finally:
        if conn:
            conn.close()


def con_my_sql(sql, params=None):
    """执行 SQL 并返回结果"""
    conn = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()

        try:
            return cur.fetchall()
        except psycopg2.ProgrammingError:
            return []

    except Exception as err:
        print("数据库错误:", err)
        return []
    finally:
        if conn:
            conn.close()


# 让 Flask 启动时自动建表
init_db()
