"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    # numero de filas de la tabla tbl0
    filas = len(tbl0) 
    return filas


def pregunta_02():
    # numero de columnas de la tabla tbl0
    columnas = len(tbl0.columns)
    return columnas


def pregunta_03():
    # numero de registros por cada letra de la columna _c1 del archivo tbl0.tsv
    registros = tbl0.groupby('_c1').size()
    return registros

def pregunta_04():
    # promedio de la columna _c2 por cada letra de la columna _c1 del archivo tbl0.tsv
    promedio_c2 = tbl0.groupby('_c1')['_c2'].mean()
    return promedio_c2

def pregunta_05():
    # valor maximo de la columna _c2 por cada letra de la columna _c1 del archivo tbl0.tsv
    maximo_c2 = tbl0.groupby('_c1').max()['_c2']
    return maximo_c2

def pregunta_06():
    # valores unicos de la columna _c4 de del archivo tbl1.csv en mayusculas y ordenados alfabeticamente
    valores_unicos = tbl1['_c4'].unique()
    valores_unicos = [x.upper() for x in valores_unicos]
    valores_unicos.sort()
    return valores_unicos

def pregunta_07():
    # suma de la columna _c2 por cada letra de la columna _c1 del archivo tbl0.tsv
    suma_c2 = tbl0.groupby('_c1').sum()['_c2']
    return suma_c2

def pregunta_08():
    # Agregar una columna llamada suma con la suma de _c0 y _c2 al archivo tbl0.tsv
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0

def pregunta_09():
    # Agregar una columna llamada year con el año de la columna _c3 al archivo tbl0.tsv
    tbl0['year'] = tbl0['_c3'].str.split('-').str[0]
    return tbl0

def pregunta_10():
    tbl0.sort_values(by=['_c1', '_c2'], inplace=True)
    grouped = tbl0.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, x))).reset_index(name='_c0')
    return grouped


    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """


def pregunta_11():
    lista = tbl1.groupby('_c0', as_index=False)['_c4'].apply(lambda x: ','.join(sorted(x))).reset_index(drop=True)
    return  lista


def pregunta_12():
    tbl2.sort_values(by=['_c0', '_c5a', '_c5b'], inplace=True)
    tbl2['_c5'] = tbl2['_c5a'] + ':' + tbl2['_c5b'].astype(str)
    result = tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(x)).reset_index()

    return result


def pregunta_13():
    joined = pd.merge(tbl0, tbl2, on='_c0')
    result = joined.groupby('_c1')['_c5b'].sum()
    return result
