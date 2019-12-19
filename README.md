# 인공 지능 최종 과제_League of legend 상황별 승패 예측하기

교수님 수업시간에 강의자료로 사용하였던 prediction_Util 사용하였습니다.

data 출처 : League of legend 프로게임단 T1소속 Faker선수 최근 전적 30판을 데이터로 사용하였습니다.

- kill = 상대를 죽인 횟수
- tower = 파괴된 포탑 수
- totalgold = 획득 골드 차이
- Burf = 용, 바론 버프 획득한 총 횟수
- winlose = 승패 (승일때는 1, 패일때는 0으로 설정하였습니다.)
<hr/>

```
from mllib.prediction_util import PredictionUtil
UT = PredictionUtil()
```

prediction_util에 있는 모듈을 불러 온 뒤 객체를 만듭니다..

```
UT.read("data_set.csv")
```
![read](https://user-images.githubusercontent.com/54824935/71181483-94430080-22b7-11ea-9287-8d29417557f9.PNG)

data_set.csv 파일을 읽습니다.

```
UT.show_unique_column()
```
![Unique](https://user-images.githubusercontent.com/54824935/71181540-ade44800-22b7-11ea-9c2e-904ed37c8a04.PNG)

컬럼별 유니크한 값을 표시합니다.

```
UT.plot_3d('kill', 'Burf', 'Totalgold')
```
![Figure_1](https://user-images.githubusercontent.com/54824935/71181583-c5233580-22b7-11ea-9e96-14b3b0c6dd87.png)

```
UT.boxplot('kill','Totalgold')
```
![Figure_2](https://user-images.githubusercontent.com/54824935/71181605-d53b1500-22b7-11ea-9921-9b834169a69f.png)

```
UT.heatmap(['kill','tower','Totalgold','Burf','winlose']) #상관관계 파악
```
![Figure_3](https://user-images.githubusercontent.com/54824935/71181651-eab03f00-22b7-11ea-81c0-bad8da032bc9.png)

```
UT.run_all(['kill','Burf'],'winlose')
```
![run_all](https://user-images.githubusercontent.com/54824935/71181689-fac81e80-22b7-11ea-896d-c00af7e055c3.PNG)

```
UT.run_all(['kill','Totalgold','tower','Burf'],'winlose')
```
![run_all2](https://user-images.githubusercontent.com/54824935/71181696-fdc30f00-22b7-11ea-81ff-96c814c3a4ec.PNG)
