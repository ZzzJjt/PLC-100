import numpy as np
import pandas as pd

# 假设我们有一个CSV文件，其中包含了历史数据
data = pd.read_csv('reactor_temperature_data.csv')
inputs = data[['coolant_flow', 'heating_power']].values
outputs = data['temperature'].values

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(32, input_dim=2, activation='relu'))  # 输入层
model.add(Dense(64, activation='relu'))              # 隐藏层
model.add(Dense(1, activation='linear'))             # 输出层
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(inputs, outputs, epochs=100, batch_size=10)
def reactor_simulation(temp_target, model, initial_conditions):
    temp_current = initial_conditions[0]
    coolant_flow = initial_conditions[1]
    heating_power = initial_conditions[2]
    
    # 模拟一段时间内的温度变化
    for _ in range(100):  # 假设100个时间步
        predicted_heating = model.predict(np.array([[coolant_flow, heating_power]]))
        
        # 更新冷却水流速和加热功率以接近目标温度
        if temp_current < temp_target:
            cooling_adjustment = -0.1 * (temp_target - temp_current)
            heating_adjustment = predicted_heating[0][0] + 0.1 * (temp_target - temp_current)
        else:
            cooling_adjustment = 0.1 * (temp_current - temp_target)
            heating_adjustment = predicted_heating[0][0] - 0.1 * (temp_current - temp_target)
        
        coolant_flow += cooling_adjustment
        heating_power += heating_adjustment
        
        # 更新当前温度
        temp_current += (predicted_heating[0][0] - temp_current) * 0.1
        
        print(f"Current Temperature: {temp_current}, Target: {temp_target}")
