import pytest
import numpy as np
from geopy.distance import geodesic


#def CalsulateDist(firstPoint, secondPoint):
#    dist = np.sqrt(np.power((firstPoint[0] - secondPoint[0]), 2) + np.power((firstPoint[1] - secondPoint[1]), 2));
#    return dist;


def test_funk():
     #"Входной массив точек: "
    localMatrix=[[55.711481, 37.5862452], # метро лен. проспект
                 [55.68755262707189, 37.57358551025391], # метро академическая
                 [55.67768120209928,37.563285827636726],# профсоюзная
                 [55.6699855694748, 37.55444526672364],# новые черемушки
                 [55.65710773006344,37.54045486450196], #калужская
                [55.48566263468206,37.54062652587891] # Старосырово
                ]
     # считаем расстояние
    distanceS=[(geodesic(localMatrix[row], localMatrix[row + 1]).km) for row in range(len(localMatrix) - 1)]
     # находим медиану
    median = np.median(distanceS) * 10
     # ищем точки разрыва
    for row in range(len(localMatrix) - 1):
        assert not (distanceS[row] > median), "есть точки разрыва"

