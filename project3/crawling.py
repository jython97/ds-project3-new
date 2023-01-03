from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import multiprocessing

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

#랭킹 500등 유저들 리스트
def top_500_list():
    lst = []
    for i in range(1, 6):
        url = f"https://www.op.gg/leaderboards/tier?page={i}&region=kr"
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        p = soup.find_all('strong', 'summoner-name')
        for j in p:
            lst.append(j.text)
    return lst

#각 유저들의 최근 20게임 크롤링
def make_data(ranker):
    lst_name = []
    lst_game = []
    lst_result = []
    lst_time = []
    lst_champion = []
    lst_level = []
    lst_dspell = []
    lst_fspell = []
    lst_mainrune = []
    lst_subrune = []
    lst_item = []
    lst_kill = []
    lst_death = []
    lst_assist = []
    lst_kda = []
    lst_pkill = []
    lst_ward = []
    lst_cs = []
    lst_mincs = []
    lst_tier = []
    lst_participants_champ = []
    lst_participants = []
    lst_enemy = []
    lst_enemy_champ = []
    lst_side = []

    for name in ranker:
        lst_name += [name]*20
        url = f'https://www.op.gg/summoners/kr/{name}'
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        #게임 종류 칼럼
        p = soup.find_all('div', 'type')
        for j in p:
            lst_game.append(j.text)

        #승패여부 칼럼
        p = soup.find_all('div', 'result')
        for j in p:
            lst_result.append(j.text)

        #게임시간 칼럼
        p = soup.find_all('div', 'length')
        for j in p:
            lst_time.append(j.text)

        #챔피언, 스펠들, 룬들, 레벨 칼럼
        p = soup.find_all('div', 'champion')
        for j in p:
            find = j.find_all('img')
            lst_champion.append(find[0]['alt'])
            lst_dspell.append(find[1]['alt'])
            lst_fspell.append(find[2]['alt'])
            lst_mainrune.append(find[3]['alt'])
            lst_subrune.append(find[4]['alt'])
            lst_level.append(j.find('span', 'champion-level').text)

        #사용 아이템들 칼럼
        p = soup.find_all('div', 'items')
        for j in p:
            lst2 = []
            find = j.find_all('img')
            for k in find:
                lst2.append(k['alt'])
            lst_item.append(lst2)

        #킬, 데스, 어시스트 칼럼
        p = soup.find_all('div', 'k-d-a')
        for j in p:
            k = j.text.split(' / ')
            lst_kill.append(k[0])
            lst_death.append(k[1])
            lst_assist.append(k[2])

        #킬 관여율, 핑크와드 수, cs, 분당 cs, 평균 티어 칼럼
        p = soup.find_all('div', 'stats')
        for j in p:
            lst_pkill.append(j.find('div', 'p-kill').text.split()[-1])
            lst_ward.append(j.find('div', 'ward').text.split()[-1])
            lst_cs.append(j.find('div', 'cs').text.split()[1])
            lst_mincs.append(j.find('div', 'cs').text.split()[2][1:-1])
            lst_tier.append(j.find('div', 'average-tier').text)

        #아군, 적군 조합 및 플레이어 칼럼
        p = soup.find_all('div', 'participants')
        for j in p:
            lst2 = []
            lst3 = []
            arg1 = j.find_all('img')
            arg2 = j.find_all('div', 'name')
            for k in arg1:
                lst2.append(k['alt'])
            for k in arg2:
                lst3.append(k.text)

            #레드진영, 블루진영 판별리스트
            if name in lst3[:5]:
                lst_side.append('blue')
                lst_participants_champ.append(lst2[:5])
                lst_participants.append(lst3[:5])
                lst_enemy.append(lst2[5:])
                lst_enemy_champ.append(lst3[5:])
            else:
                lst_side.append('red')
                lst_participants_champ.append(lst2[5:])
                lst_participants.append(lst3[5:])
                lst_enemy_champ.append(lst2[:5])
                lst_enemy.append(lst3[:5])

    #데이터 프레임화
    df = pd.DataFrame({'summoners' : lst_name, 
                        'game' : lst_game,
                        'result': lst_result,
                        'time' : lst_time,
                        'champion' : lst_champion,
                        'level' : lst_level,
                        'd_spell' : lst_dspell,
                        'f_spell' : lst_fspell,
                        'main_rune' : lst_mainrune,
                        'sub_rune' : lst_subrune,
                        'items' : lst_item,
                        'kill' : lst_kill,
                        'death' : lst_death,
                        'assist' : lst_assist,
                        'p_kill' : lst_pkill,
                        'pinkward' : lst_ward,
                        'cs': lst_cs,
                        'cs_per_min': lst_mincs,
                        'average_tier': lst_tier,
                        'team_champs' : lst_participants_champ,
                        'team' : lst_participants,
                        'enemy_champ' : lst_enemy_champ,
                        'enemy' : lst_enemy,
                        'side': lst_side})

    return df

#한번에 많은 정보를 스크래핑 하려하면 OP GG에서 접속을 끊어버려서 어쩔 수 없이 시간차를 두고 데이터를 수집한다.
def concat_data():
    ranker = top_500_list() # 500위 랭커 리스트 구하기
    df1 = make_data(ranker[:250]) # 1~250위까지 20게임씩 스크래핑
    time.sleep(180) # 3분 딜레이
    df2 = make_data(ranker[250:]) # 251~500위까지 20게임씩 스크래핑
    df = pd.concat([df1, df2], ignore_index=True)
    df.to_csv('data.csv', index=False) # csv파일로 저장

    return df

# def concat_data():
#     multiprocessing.freeze_support()

#     #랭킹 500위 유저들의 리스트
#     ranker = top_500_list()

#     #랭킹 250위 유저들까지 크롤링하여 Dataframe으로 변환
#     start = time.time()
#     pool = multiprocessing.Pool(processes=5)
#     results = [
#         pool.apply_async(make_data, args=(ranker[:50],)),
#         pool.apply_async(make_data, args=(ranker[50:100],)),
#         pool.apply_async(make_data, args=(ranker[100:150],)),
#         pool.apply_async(make_data, args=(ranker[150:200],)),
#         pool.apply_async(make_data, args=(ranker[200:250],))]
#     df1, df2, df3, df4, df5 = [result.get() for result in results]
#     pool.close()
#     pool.join()
#     end = time.time()
#     print('time1 : {0}'.format(end - start))
#     df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

#     #OP.GG의 블락을 감당하기 위해 3분 기다리기
#     time.sleep(180)

#     #랭킹 250위~500위 유저들까지 크롤링하여 Dataframe으로 변환
#     start = time.time()
#     pool = multiprocessing.Pool(processes=5)
#     results = [
#         pool.apply_async(make_data, args=(ranker[250:300],)),
#         pool.apply_async(make_data, args=(ranker[300:350],)),
#         pool.apply_async(make_data, args=(ranker[350:400],)),
#         pool.apply_async(make_data, args=(ranker[400:450],)),
#         pool.apply_async(make_data, args=(ranker[450:500],))]
#     df1, df2, df3, df4, df5 = [result.get() for result in results]
#     pool.close()
#     pool.join()
#     end = time.time()
#     print('time2 : {0}'.format(end - start))
#     df = pd.concat([df, df1, df2, df3, df4, df5], ignore_index=True)

#     df.to_csv('data.csv', index=False)
    
#     return df

# if __name__=="__main__":
#     concat_data()
#     print(multiprocessing.cpu_count())