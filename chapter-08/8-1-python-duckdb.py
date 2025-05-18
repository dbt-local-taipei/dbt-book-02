import duckdb

# 建立一個記憶體中的 DuckDB 資料庫連接
con = duckdb.connect(database=':memory:')

# 建立表格並插入測試資料
con.execute("""
CREATE TABLE sales (
    id INTEGER,
    product VARCHAR,
    amount DECIMAL(10, 2)
)
""")

con.execute("""
INSERT INTO sales (id, product, amount) VALUES
(1, 'Apple', 10.5),
(2, 'Banana', 8.75),
(3, 'Cherry', 12.0),
(4, 'Date', 6.25),
(5, 'Elderberry', 15.0)
""")

# 執行一個 SQL 查詢來計算總銷售額
result = con.execute("SELECT SUM(amount) AS total_sales FROM sales").fetchall()

# 顯示查詢結果
print(f'Total Sales: ${result[0][0]:.2f}')
