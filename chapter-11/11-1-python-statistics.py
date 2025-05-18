import numpy as np
import matplotlib.pyplot as plt

# 假設參數
lambda_visits = 20   # 主動拜訪次數的均值
lambda_leads = 5     # 主動找上門的客戶數均值
alpha = 0.3          # 主動拜訪轉換率
beta = 0.5           # 主動找上門轉換率

# 蒙地卡羅模擬
num_simulations = 10000
simulated_cases = []

for _ in range(num_simulations):
    # 模擬泊松分布的拜訪和詢問數量
    active_visits = np.random.poisson(lambda_visits)
    in_bounds = np.random.poisson(lambda_leads)
    
    # 計算接案數量
    N = alpha * active_visits + beta * in_bounds
    simulated_cases.append(N)

# 繪製模擬結果分佈
plt.hist(simulated_cases, bins=50, color='skyblue', edgecolor='black')
plt.xlabel('接案數量')
plt.ylabel('模擬次數')
plt.title('蒙地卡羅模擬接案數量分佈')
plt.show()

# 顯示模擬結果的統計資訊
print("平均接案數量:", np.mean(simulated_cases))
print("接案數量標準差:", np.std(simulated_cases))
print("接案數量範圍 (95%信賴區間):", np.percentile(simulated_cases, [2.5, 97.5]))
