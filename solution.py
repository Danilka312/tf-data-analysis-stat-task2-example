import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1119068275 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p 
    semians = 0 
    for i in range(len(x)): 
      semians += x[i] 
    left = (semians - 0.065*len(x))/(len(x)*(alpha)) + 0.065
    right = (semians - 0.065*len(x))/(len(x)*(1-alpha)) + 0.065

    return left, \
           right 
