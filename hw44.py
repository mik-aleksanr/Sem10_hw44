"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

coder = OneHotEncoder(handle_unknown='ignore')  # создаем кодировщик
cod_df = pd.DataFrame(coder.fit_transform(data[['whoAmI']]).toarray())  # выполняем горячее кодирование
# для столбца
print(data.join(cod_df))  # это для наглядности первоначальный столбец и кодированный
cod_df.columns = ['human', 'robot']  # добавляем название столбцов по названиям категориальных переменных
print(cod_df)
