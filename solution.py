import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1119068275 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргумент
    alpha = 1 - p
    n = len(x) 
    Y = max(x)  
    left = ((Y-0.065)/(1-alpha)**(1/n))+0.065 - 0.01
    right = ((Y-0.065)/(alpha)**(1/n))+0.065 + 0.01

    return left, \
           right 
