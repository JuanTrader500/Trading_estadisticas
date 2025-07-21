import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

# Configurar fechas para el último año
fecha_fin = datetime.now()
fecha_inicio = datetime(2005, 1, 1)

print(f"Obteniendo datos desde {fecha_inicio.strftime('%Y-%m-%d')} hasta {fecha_fin.strftime('%Y-%m-%d')}")

def procesar_datos_yfinance(data, nombre_activo):
    try:
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        df = pd.DataFrame()
        df['date'] = data.index
        df['open'] = data['Open'].values
        df['high'] = data['High'].values
        df['low'] = data['Low'].values
        df['close'] = data['Close'].values
        if 'Volume' in data.columns:
            df['volume'] = data['Volume'].values

        df = df.dropna().reset_index(drop=True)
        return df
    except Exception as e:
        print(f"Error procesando datos de {nombre_activo}: {e}")
        return None