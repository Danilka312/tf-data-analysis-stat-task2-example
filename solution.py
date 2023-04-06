import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1119068275 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x) 
    Y = np.max(x)
    X_mean = np.mean(x)
    left = (2 * X_mean - Y + 0.13 - (0.065 * alpha)) / alpha
    right = (2 * X_mean - Y + 0.13) / (alpha - 1)

    return left, \
           right 
