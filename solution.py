import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1119068275 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p 
    Y = max(x)  
    left = ((Y - 0.065)/(alpha) + 0.065)**(1/n)
    right = ((Y - 0.065)/(alpha-1) + 0.065)**(1/n)

    return left, \
           right 
