import pymysql

# 数据库连接配置
connection = pymysql.connect(
    host='testone-public02.rdsmgk9da2t7z4x.rds.bj.baidubce.com',
    user='hztest001_admin',
    port=13307,
    password='mw4LgXl*rciT1gCrB+G',
    database='hanzhongtest_001',
    charset='utf8mb4'
)

# 批量插入数据
def insert_data():
    try:
        with connection.cursor() as cursor:
            # 构造测试数据
            data = [(f"user_{i}", f"user_{i}@example.com") for i in range(500000)]
            # SQL 语句
            sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
            
            # 分批插入数据（每次插入 10,000 行）
            batch_size = 10000
            for i in range(0, len(data), batch_size):
                cursor.executemany(sql, data[i:i + batch_size])
                connection.commit()  # 提交事务
                print(f"Inserted rows: {i + batch_size}")
                
    finally:
        connection.close()

# 执行插入
insert_data()
