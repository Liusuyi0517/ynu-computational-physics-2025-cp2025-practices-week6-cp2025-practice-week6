import numpy as np
import matplotlib.pyplot as plt

def setup_parameters():
    """
    设置模拟牛顿环所需的参数
    
    返回:
    tuple: 包含激光波长(lambda_light,单位m)、透镜曲率半径(R_lens,单位m)的元组
    """
    # 氦氖激光波长 (m)
    lambda_light = 632.8e-9
    # 透镜曲率半径 (m)
    R_lens = 0.1
    return lambda_light, R_lens

def generate_grid():
    """
    生成模拟所需的网格坐标
    
    返回:
    tuple: 包含网格坐标X、Y以及径向距离r的元组
    """
    # 在此生成x和y方向的坐标网格
    pass

def calculate_intensity(r, lambda_light, R_lens):
    """
    计算干涉强度分布
    
    参数:
    r (np.ndarray): 径向距离数组
    lambda_light (float): 激光波长(m)
    R_lens (float): 透镜曲率半径(m)
    
    返回:
    np.ndarray: 干涉强度分布数组
    """
    # 在此实现光强计算
    pass

def plot_newton_rings(intensity):
    """
    绘制牛顿环干涉条纹图像
    
    参数:
    intensity (np.ndarray): 干涉强度分布数组
    """
    # 在此实现图像绘制
    pass

if __name__ == "__main__":
    # 1. 设置参数
    lambda_light, R_lens = setup_parameters()
    
    # 2. 生成网格坐标
    X, Y, r = generate_grid()
    
    # 3. 计算干涉强度分布
    intensity = calculate_intensity(r, lambda_light, R_lens)
    
    # 4. 绘制牛顿环
    plot_newton_rings(intensity)






import numpy as np
import matplotlib.pyplot as plt

def newton_rings_intensity(R, lamda, r):
    d = R - np.sqrt(R**2 - r**2)
    I = 4 * np.sin((2 * np.pi / lamda) * (R - np.sqrt(R**2 - r**2)))**2
    return I

# 参数设置
R = 1000  # 凸透镜曲率半径
lamda = 0.0005  # 光的波长
r = np.linspace(0, 10, 1000)  # 圆环半径范围

# 计算光强分布
I = newton_rings_intensity(R, lamda, r)

# 绘制牛顿环干涉图样
plt.plot(r, I)
plt.xlabel('圆环半径 r')
plt.ylabel('光强 I')
plt.title('牛顿环干涉图样')
plt.show()

# 分析不同参数对干涉图样的影响
# 改变凸透镜曲率半径
R_list = [500, 1000, 1500]
for R in R_list:
    I = newton_rings_intensity(R, lamda, r)
    plt.plot(r, I, label=f'R={R}')

plt.xlabel('圆环半径 r')
plt.ylabel('光强 I')
plt.title('不同曲率半径对牛顿环干涉图样的影响')
plt.legend()
plt.show()

# 改变光的波长
lamda_list = [0.0004, 0.0005, 0.0006]
for lamda in lamda_list:
    I = newton_rings_intensity(R, lamda, r)
    plt.plot(r, I, label=f'λ={lamda}')

plt.xlabel('圆环半径 r')
plt.ylabel('光强 I')
plt.title('不同波长对牛顿环干涉图样的影响')
plt.legend()
plt.show()



