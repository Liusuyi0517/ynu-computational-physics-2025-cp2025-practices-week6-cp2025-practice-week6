import unittest
import numpy as np
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from solutions.newton_rings_solution import setup_parameters, generate_grid, calculate_intensity, plot_newton_rings
from src.newton_rings import setup_parameters, generate_grid, calculate_intensity, plot_newton_rings

class TestNewtonRingsSolution(unittest.TestCase):

    def test_setup_parameters(self):
        lambda_light, R_lens = setup_parameters()
        self.assertAlmostEqual(lambda_light, 632.8e-9)
        self.assertAlmostEqual(R_lens, 0.1)

    def test_generate_grid(self):
        X, Y, r = generate_grid()
        self.assertEqual(X.shape, (1000, 1000))
        self.assertEqual(Y.shape, (1000, 1000))
        self.assertEqual(r.shape, (1000, 1000))
        # 由于浮点数精度的原因，中心点的值可能不完全为0
        self.assertLess(r[500, 500], 1e-5)

    def test_calculate_intensity(self):
        lambda_light, R_lens = setup_parameters()
        _, _, r = generate_grid()
        intensity = calculate_intensity(r, lambda_light, R_lens)
        self.assertEqual(intensity.shape, (1000, 1000))
        # 由于干涉强度的计算特性，值可能会略大于4
        # 检查强度值是否在合理范围内
        self.assertTrue(np.all(intensity >= 0) and np.all(intensity <= 4.1))

if __name__ == '__main__':
    unittest.main()



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
