from mllib.prediction_util import PredictionUtil
UT = PredictionUtil()

UT.read("data_set.csv") # 파일 읽기
UT.show_unique_column() #컬럼 별 유니크한 값

UT.plot_3d('kill', 'Burf', 'Totalgold')
UT.boxplot('kill','Totalgold')
UT.heatmap(['kill','tower','Totalgold','Burf','winlose']) #상관관계 파악
UT.run_all(['kill','Burf'],'winlose')
print('------------------------------------------------------------------------')
UT.run_all(['kill','Totalgold','tower','Burf'],'winlose')