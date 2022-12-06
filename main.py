from flask import Flask
import pymysql

# 创建Flask应用实例
app = Flask(__name__)

# 查询指定的coupen字段是否在数据库中存在
@app.route("/api/check_coupen/<string:coupen>", methods=["GET"])
def check_coupen(coupen):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="user", password="password", db="my_database")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 查询指定的coupen字段是否在数据库中存在
    sql = "SELECT * FROM my_table WHERE column_name = %s"
    cursor.execute(sql, (coupen))

    # 获取查询结果
    results = cursor.fetchall()

    # 如果查询结果不为空，则说明数据库中有coupen的数据
    if results:
        return "存在"
    else:
        return "不存在"

    # 关闭数据库连接
    db.close()

# 启动Flask应用
if __name__ == "__main__":
    app.run()