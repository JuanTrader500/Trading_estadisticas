import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Extraction_libreri import procesar_datos_yfinance

warnings.filterwarnings('ignore')

# Configurar fechas para el último año
fecha_fin = datetime.now()
fecha_inicio = datetime(2005, 1, 1)

try:
    # Descargar datos
    sp500_df = procesar_datos_yfinance(
    yf.download("^GSPC", start=fecha_inicio, end=fecha_fin, progress=False),
    "S&P 500")
    
    
    vix_df = procesar_datos_yfinance(
    yf.download('^VIX',start=fecha_inicio, end=fecha_fin, progress=False),
    'VIX')
    vix_df = vix_df.iloc[:-1]

except:
    print("Algo salio mal al crear los data frame")
   
try:
    
    sp500_df.to_csv("C:/Users/juana/OneDrive/Escritorio/Datos_del_mercado/sp500_data_daily.csv",index=False)
    vix_df.drop(vix_df.index[-1])
    vix_df.to_csv("C:/Users/juana/OneDrive/Escritorio/Datos_del_mercado/vix_data_daily.csv",index=False)
    
    print("Se exporto con exito el csv")
except:
    print("No se pudo exportar el data_frame a un archivo csv")
