import pandas as pd
import shap
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import RandomizedSearchCV
import pickle
import numpy as np

"""
여기서 리스트 형태의 데이터는 문자열로 읽어오게 되는데 다시 리스트 형식으로 만들어 주려면 ast.literal_eval()함수를 apply를 통해 해당 칼럼에 적용시켜주면 된다.
여기서는 리스트 데이터를 가지는 칼럼들은 모두 drop해줄 예정이므로 그대로 불러온다.
df = pd.read_csv('data.csv')

간단하게 확인
print(df.head())
print(df.shape)
print(df.info())

결측값 확인
print(df.isnull().sum())
0

중복값 확인
print(df.duplicated().sum())
0

타겟값 클래스 불균형 확인
print(df['result'].value_counts(normalize=True))
Victory    0.5505
Defeat     0.4430
Remake     0.0065
Remake는 '다시하기'로 불완전한 정보이므로 drop시키는게 좋을 것 같다.
클래스가 균형잡혀 있으므로 f1스코어로 평가할 필요는 없다. 그냥 정확도로 평가 에정

카테고리, 수치형 칼럼 분리
category = df.select_dtypes(include='object').columns
['summoners', 'game', 'result', 'time', 'champion', 'd_spell', 'f_spell', 'main_rune', 'sub_rune', 'items', 'p_kill', 'average_tier', 'team_champs', 'team', 'enemy_champ', 'enemy', 'side']
numerical = df.select_dtypes(exclude='object').columns
['level', 'kill', 'death', 'assist', 'pinkward', 'cs', 'cs_per_min']
여기서 time, p_kill의 경우 각각 초, 실수 단위로 카운트되는 수치형 변수로 바꿔줄 필요가 있다.
그리고 game 칼럼의 경우 종류에 따라 지표가 천차만별로 차이나니 명확한 기준을 위해 소환사의 협곡에서 솔로랭크, 자유랭크, 일반으로 진행되는 게임만 선별할 필요가 있다.
카테고리형 변수에서는 summoners, itmes, team_chapms, team, enemy_champs, enemy 칼럼들은 모두 drop해준다.
수치형 변수에서는 kill, death, assist를 종합한 kda칼럼을 새로 만들어준다. 상관관계를 갖는 칼럼을 생성시키는 것이지만 문제가 분류문제이고 부스팅 계열 모델을 사용할 예정이라 성능에 영향이 없다.

game 칼럼 클래스 확인
print(df['game'].value_counts(normalize=True))
Ranked Solo         0.8802
ARAM                0.0778
Normal              0.0153
Ultra Rapid Fire    0.0147
Flex 5:5 Rank       0.0118
Beginner            0.0002
Ranked Solo, Nomal, Flex 5:5 Rank만 남기고 모두 drop한다.
"""

# drop_data.csv로 불필요한 행 먼저 제거
def row_drop():
    df = pd.read_csv('data.csv')
    index = df[df['result']=='Remake'].index
    df = df.drop(index)
    index = df[df['game']=='ARAM'].index
    df = df.drop(index)
    index = df[df['game']=='Ultra Rapid Fire'].index
    df = df.drop(index)
    index = df[df['game']=='Beginner'].index
    df = df.drop(index)
    df.reset_index(drop=True, inplace=True)
    df.to_csv('drop_data.csv', index=False)
    return df

def preprocess():
    # 필요없는 칼럼들 drop
    df = pd.read_csv('drop_data.csv')
    df.drop(['summoners', 'items', 'team_champs', 'team', 'enemy_champ', 'enemy'], axis=1, inplace=True)

    # 시간을 초단위로 변환
    def toInt(arg):
        lst = arg.split()
        second = int(lst[0][:-1])*60 + int(lst[1][:-1])
        return second
    df['time'] = df['time'].apply(toInt)

    # 킬관여율 칼럼 p_kill을 실수로 변환
    def toFloat(arg):
        return int(arg[:-1])/100
    df['p_kill'] = df['p_kill'].apply(toFloat)

    # kda 칼럼 생성
    # kda = (kill+assist)/death
    # 이때, death가 0이면 zerodivisionerror가 나므로 기존의 death=0인 kda의 가중치 1.2와 최대하게 비슷하게 가중치를 줄 수 있도록 설계
    def toWeight(arg):
        if arg==0:
            arg=0.8
        else:
            arg=float(arg)
        return arg
    df['tmp'] = df['death'].apply(toWeight)
    df['kda'] = round((df['kill']+df['assist'])/df['tmp'], 2)
    df.drop('tmp', axis=1, inplace=True)

    # LabelEncoder로 카테고리형 변수들 인코딩
    for i in df.select_dtypes(include='object').columns:
        encoder = LabelEncoder()
        df[i] = encoder.fit_transform(df[i])

    # 타겟 변수 분리
    y = df['result']
    x = df.drop('result', axis=1)
    col = x.columns

    # train_test_split이 필요하지만 데이터 양도 적고 성능이 큰 의미가 아닌 shap를 통한 해석이 더 중요하므로 빠른 갱신을 위해 생략한다.

    # 스케일링
    scaler = MinMaxScaler()
    pro_x = scaler.fit_transform(x)
    pro_df = pd.DataFrame(pro_x, columns=col)

    return pro_x, y, pro_df

def boosting(pro_x, y):
    # 학습 및 하이퍼 파라미터 튜닝
    # gbm = GradientBoostingClassifier(random_state=42)

    # params = {
    #     "learning_rate" : [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],
    #     "n_estimators" : [100, 500]
    # }

    # model = RandomizedSearchCV(gbm, param_distributions=params, n_iter=5, scoring='accuracy', n_jobs=-1, cv=3, verbose=1, random_state=42)
    # model.fit(pro_x, y)

    # print('최적 하이퍼파라미터 :', model.best_params_)
    # print('최적 정확도 :', model.best_score_)
    # 최적 하이퍼파라미터 : {'n_estimators': 500, 'learning_rate': 0.05}
    # 최적 정확도 : 0.9089591690046142
    # 빠른 갱신을 위해 파라미터들을 최적의 하이퍼 파라미터로 고정시키기로 함.

    # 빠르게 boosting!!
    model = GradientBoostingClassifier(n_estimators=500, learning_rate=0.05, random_state=42)
    model.fit(pro_x, y)

    # 피클 파일로 저장
    with open("model.pickle", "wb") as fw:
        pickle.dump(model, fw)
    return model
    
def shap_plot(model, pro_df, index):
    row = pro_df.iloc[index,:]
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(row)

    shap.force_plot(
        base_value=explainer.expected_value, 
        shap_values=shap_values,
        features=row,
        show=False,
        matplotlib = True
    ).savefig('static/image/shap.png')
    return explainer, shap_values

# pro_x, y, pro_df = preprocess()
# model = boosting(pro_x, y)
# shap_plot(model, pro_df, 2)