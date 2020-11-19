"""
    dataProcessing.py 
    데이터 전처리용 function 코드
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler

WALK_TYPE = "acc"
SENSOR_TYPE = ("acc", "hrm", "pre")  # 각각 가속도, 심박수, 압력
FRAME = 10
TOTAL_SUBJECT = 2


class Data:
    """
        데이터 처리하는 클래스
        input : folder (data)
        output : object (..?)
        
    """

    def __init__(self, folder):
        def _getDataFromFile(filename):
            with open(filename, "r") as f:
                lineData = f.readline().split(",")
                lineData = lineData[4:]  # 데이터 시작은 0,0,0,0  부터 시작해서 이 부분 버리기
                # lineData => list 형태
            return lineData

        self.data = {}  # data - down, up - sensors
        self.baseFolder = folder
        self.downstair = folder + "downstair/"
        self.upstair = folder + "upstair/"
        for sensor in SENSOR_TYPE:
            for numOfsubejct in range(TOTAL_SUBJECT):
                upFilename = self.upstair + sensor + str(numOfsubejct)
                upData = _getDataFromFile(upFilename)
                self.data["up"] = []
                print(len(upData))
                downFilename = self.downstair + sensor + str(numOfsubejct)
                downData = _getDataFromFile(downFilename)
                self.data["down"] = []
                print(len(downData))

    def _getSize(self):
        pass

    def _robustScaler(self):
        pass

    def _cutWindow(self):
        pass


if __name__ == "__main__":
    data = Data("data/")

