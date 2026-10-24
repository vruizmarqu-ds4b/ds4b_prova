# Script para analizar abandonos de clientes
df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto'])