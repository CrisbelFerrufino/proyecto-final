## Limitaciones del experimento, métodos y código


### Limitaciones del experimento

**1.Errores instrumentales en las mediciones**
Los sensores utilizados poseen incertidumbres fijas:

- 𝑡𝑒 = 0.001s en tiempo

- 𝑥𝑒 = 0.001m en posición

- 𝑣𝑒 = 0.001m/s en velocidad

Estas incertidumbres se propagan en todos los cálculos posteriores, especialmente en la obtención de la constante elástica y el período.

**2.Cantidad limitada de datos experimentales**
Cada conjunto cuenta con solo 6 puntos de medición. Este número es reducido para capturar adecuadamente la forma completa de una oscilación, lo que dificulta estimar con precisión parámetros como frecuencia o fase. Con más puntos, el ajuste sería significativamente más robusto.

**3. Posible desgaste del resorte**
La ley de Hooke solo es estrictamente válida dentro del rango lineal del resorte. Con el uso, los resortes tienden a perder rigidez, modificar su constante elástica y presentar pequeñas deformaciones permanentes.

**4. No se considera el amortiguamiento real**
El experimento asume un sistema ideal sin rozamiento. Sin embargo, existe fricción con el aire, rozamiento interno en la estructura y pérdida de energía en cada oscilación. Esto puede modificar tanto la amplitud como los parámetros ajustados.

**5. Falta de repetibilidad del experimento**
No se realizaron múltiples corridas independientes para cada masa. Sin promediar resultados, pequeñas fluctuaciones pueden generar discrepancias en los ajustes.

### Limitaciones del modelo teórico

**1. Modelo idealizado del Movimiento Armónico Simple**
El MAS asume que la fuerza es estrictamente proporcional al desplazamiento. En sistemas reales, esta proporcionalidad se cumple solo aproximadamente.

**2. Se desprecia la masa del resorte**
Se considera únicamente la masa colgante, pero en la práctica el resorte también tiene masa distribuida que participa del movimiento. Esto altera los tiempos característicos del sistema.

**3. Suposición de oscilaciones pequeñas**
El MAS es válido principalmente para oscilaciones de baja amplitud. Si la amplitud crece, aparecen términos no lineales en la dinámica.

**4. Linealización obligatoria para aplicar Mínimos Cuadrados**
La ecuación original del MAS no es lineal. Para ajustar los datos es necesario aplicar transformaciones matemáticas, lo cual introduce nuevas fuentes de error y limita la interpretación directa del ajuste.

### Limitaciones del método de Mínimos Cuadrados

**1. Sensibilidad al ruido**
El método de Mínimos Cuadrados es particularmente sensible a datos ruidosos. Un solo punto atípico puede sesgar significativamente los parámetros del ajuste.

**2. Ajuste basado en transformaciones**
Linearizar datos implica aplicar funciones como logaritmos o cuadrados. Estas funciones no preservan los errores de manera lineal, generando propagación de incertidumbre más compleja.

**3. Poca estabilidad con datos escasos**
Con únicamente seis puntos por masa, el ajuste puede variar notablemente si uno de ellos presenta un error sistemático.

### Limitaciones del código desarrollado

**1. Dependencia del formato de los archivos de datos**
El código depende de que los archivos .csv o .txt tengan la misma estructura. Cambios menores en los encabezados o formato pueden hacer que falle la lectura.

**2. Falta de validación de errores y excepciones**
El código no incorpora manejo robusto de errores. Si un archivo no existe, una columna está vacía o aparece un valor no numérico, el programa puede fallar silenciosamente.

**3. Ausencia de filtrado de datos**
No se implementaron funciones para eliminar valores fuera de rango o detectar outliers, lo que puede afectar el ajuste final.

**4. Modularidad limitada**
Algunas funciones podrían dividirse en módulos más pequeños para mejorar.