# from flask import Flask, render_template, request
# from test import con_my_sql
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/")
# def login_page():
#     return render_template('login_page.html')

# @app.route("/register_page")
# def register_page():
#     return render_template('register_page.html')

# @app.route("/login", methods=["POST"])
# def login():
#     name = request.form.get("username")
#     pwd = request.form.get("password")

#     code = "select * from login_user where username='%s'"%(name)
#     cursor_ans = con_my_sql(code)
#     cursor_select = cursor_ans.fetchall()
#     if len(cursor_select) > 0:
#         if pwd == cursor_select[0]['password']:
#             return '登陆成功'
#         else:
#             return '密码错误 <a href="/">返回登陆</a>'
#     else:
#         return '用户不存在 <a href="/">返回登陆</a>'
    
# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form.get("username")
#     pwd = request.form.get("password")
    
#     code = "select * from login_user where username='%s'"%(name)
#     cursor_ans = con_my_sql(code)
#     cursor_select = cursor_ans.fetchall()
#     if len(cursor_select) > 0:
#         return '用户已存在 <a href="/">返回登陆</a>'
#     else:
#         code  = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')"%(name,pwd)
#         con_my_sql(code) 
#         return '注册成功 <a href="/">返回登陆</a>'



# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from test import con_my_sql

# app = Flask(__name__)
# CORS(app)

# @app.route("/login", methods=["POST"])
# def login():
#     name = request.form.get("username")
#     pwd = request.form.get("password")
#     code = "select * from login_user where username='%s'" % name
#     cursor_ans = con_my_sql(code)
#     cursor_select = cursor_ans.fetchall()
#     if len(cursor_select) > 0:
#         if pwd == cursor_select[0]['password']:
#             return jsonify({"status": "success", "msg": "登录成功"})
#         else:
#             return jsonify({"status": "error", "msg": "密码错误"})
#     else:
#         return jsonify({"status": "error", "msg": "用户不存在"})

# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form.get("username")
#     pwd = request.form.get("password")
#     code = "select * from login_user where username='%s'" % name
#     cursor_ans = con_my_sql(code)
#     cursor_select = cursor_ans.fetchall()
#     if len(cursor_select) > 0:
#         return jsonify({"status": "error", "msg": "用户已存在"})
#     else:
#         code = "INSERT INTO login_user (username, password) VALUES ('%s','%s')" % (name, pwd)
#         con_my_sql(code)
#         return jsonify({"status": "success", "msg": "注册成功"})

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from test import con_my_sql
# import os

# app = Flask(__name__)
# CORS(app)

# @app.route("/login", methods=["POST"])
# def login():
#     name = request.form.get("username")
#     pwd = request.form.get("password")
#     code = "select * from login_user where username='%s'" % name
#     cursor_ans = con_my_sql(code)
#     cursor_select = cursor_ans.fetchall()
#     if len(cursor_select) > 0:
#         if pwd == cursor_select[0]['password']:
#             return jsonify({"status": "success", "msg": "登录成功"})
#         else:
#             return jsonify({"status": "error", "msg": "密码错误"})
#     else:
#         return jsonify({"status": "error", "msg": "用户不存在"})

# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form.get("username")
#     pwd = request.form.get("password")
#     code = "select * from login_user where username='%s'" % name
#     cursor_ans = con_my_sql(code)
#     cursor_select = cursor_ans.fetchall()
#     if len(cursor_select) > 0:
#         return jsonify({"status": "error", "msg": "用户已存在"})
#     else:
#         code = "INSERT INTO login_user (username, password) VALUES ('%s','%s')" % (name, pwd)
#         con_my_sql(code)
#         return jsonify({"status": "success", "msg": "注册成功"})

# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))  # 使用环境变量PORT，默认5000
#     app.run(host='0.0.0.0', port=port, debug=True)  # 生产环境关闭debug


from flask import Flask, request, jsonify
from flask_cors import CORS
from test import con_my_sql
import os

app = Flask(__name__)
CORS(app)  # 允许所有跨域(简单但不太安全,生产环境建议限制)

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("username")
    pwd = request.form.get("password")
    
    code = "select * from login_user where username='%s'" % name
    cursor_select = con_my_sql(code)  # 现在直接返回结果列表
    
    if len(cursor_select) > 0:
        if pwd == cursor_select[0]['password']:
            return jsonify({"status": "success", "msg": "登录成功"})
        else:
            return jsonify({"status": "error", "msg": "密码错误"})
    else:
        return jsonify({"status": "error", "msg": "用户不存在"})

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("username")
    pwd = request.form.get("password")
    
    code = "select * from login_user where username='%s'" % name
    cursor_select = con_my_sql(code)
    
    if len(cursor_select) > 0:
        return jsonify({"status": "error", "msg": "用户已存在"})
    else:
        code = "INSERT INTO login_user (username, password) VALUES ('%s','%s')" % (name, pwd)
        con_my_sql(code)
        return jsonify({"status": "success", "msg": "注册成功"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)