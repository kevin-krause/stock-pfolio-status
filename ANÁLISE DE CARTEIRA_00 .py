#!/usr/bin/env python
# coding: utf-8

# In[]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as pld


# In[]:


tickers = ['EGIE3.SA', 'WEGE3.SA', 'B3SA3.SA', 'SLCE3.SA',
           'TAEE11.SA', 'BBSE3.SA', 'IVVB11.SA']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source = 'yahoo', start = '2011-01-01')['Adj Close']


# In[]:


weights = np.array([0.1428, 0.1428, 0.1428, 0.1428, 0.1428, 0.1428, 0.1428])


# In[]:


sec_returns = np.log(sec_data / sec_data.shift(1))


# In[]:


retorno_med = sec_returns[['EGIE3.SA', 'WEGE3.SA', 'B3SA3.SA', 'SLCE3.SA',
           'TAEE11.SA', 'BBSE3.SA', 'IVVB11.SA']].mean() * 250
print ((str(round((retorno_med * 100), 4))) + "%")


# In[]:


portifolio_retorno = str(np.dot(sec_returns[['EGIE3.SA', 'WEGE3.SA', 'B3SA3.SA', 'SLCE3.SA',
           'TAEE11.SA', 'BBSE3.SA', 'IVVB11.SA']].mean() * 250, weights))
print ('retorno médio da carteira =', (portifolio_retorno))

portifolio_std = str(np.dot(sec_returns[['EGIE3.SA', 'WEGE3.SA', 'B3SA3.SA', 'SLCE3.SA',
           'TAEE11.SA', 'BBSE3.SA', 'IVVB11.SA']].std() * 250 ** 0.5, weights))
print ('desvio padrão da carteira =', (portifolio_std))

desvio_padrao_pfolio = sec_returns[['EGIE3.SA', 'WEGE3.SA', 'B3SA3.SA', 'SLCE3.SA',
           'TAEE11.SA', 'BBSE3.SA', 'IVVB11.SA']].std() * 250 ** 0.5
print (desvio_padrao_pfolio)


# # covariancia e correlação

# COVARIANCIA

# In[]:


pfolio_var = sec_returns[['EGIE3.SA', 'WEGE3.SA', 'B3SA3.SA', 'SLCE3.SA',
           'TAEE11.SA', 'BBSE3.SA', 'IVVB11.SA']].var() * 250
print (pfolio_var)


# In[]:


cov_matrix = sec_returns.cov() * 250
cov_matrix


# CORRELAÇÃO

# In[]:


corr_matrix = sec_returns.corr()
corr_matrix


# # covariancia e correlação do portfólio

# equal weighting scheme

# In[]:


weights = np.array([0.1428, 0.1428, 0.1428, 0.1428, 0.1428, 0.1428, 0.1428])


# portfólio variância

# In[]:


pfolio_var = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights)))
print ("portifólio variância =", (str(round((pfolio_var * 100), 4))) + "%")


# portfólio volatilidade

# In[]:


pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
print ("portifólio volatilidade =", (str(round((pfolio_vol * 100), 4))) + "%")


#  # riscos diversificáveis e não diversificáveis

# risco diversificável

# In[]:


ativo_1_var = sec_returns['EGIE3.SA'].var() * 250
float(ativo_1_var)


# In[ ]:


ativo_2_var = sec_returns['WEGE3.SA'].var() * 250
ativo_2_var


# In[ ]:


dr = pfolio_var - (weights[0] ** 2 * ativo_1_var) - (weights[1] ** 2 * ativo_2_var)
print ("risco diversificável =", (str(round(dr * 100, 4)) + ' %'))


# risco não diversificável

# plot all positions

#In[]:
sec_data.iloc[0]
