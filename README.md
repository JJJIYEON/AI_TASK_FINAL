# 인공 지능 최종 과제_League of legend 상황별 승패 예측하기

교수님 수업시간에 강의자료로 사용하였던 prediction_Util 사용하였습니다.

data 출처 : League of legend 프로게임단 T1소속 Faker선수 최근 전적 30판을 데이터로 사용하였습니다.

- kill = 상대를 죽인 횟수
- tower = 파괴된 포탑 수
- totalgold = 획득 골드 차이
- Burf = 용, 바론 버프 획득한 총 횟수
- winlose = 승패 (승일때는 1, 패일때는 0으로 설정하였습니다.)
<hr/>

```from mllib.prediction_util import PredictionUtil
UT = PredictionUtil()```

prediction_util에 있는 모듈을 불러 온 뒤 객체를 만듭니다..

```UT.read("data_set.csv")```

data_set.csv 파일을 읽습니다.

```UT.show_unique_column()```

컬럼별 유니크한 값을 표시합니다.

```UT.plot_3d('kill', 'Burf', 'Totalgold')```

```UT.boxplot('kill','Totalgold')```

```UT.heatmap(['kill','tower','Totalgold','Burf','winlose']) #상관관계 파악```

```UT.run_all(['kill','Burf'],'winlose')```

```UT.run_all(['kill','Totalgold','tower','Burf'],'winlose')```
