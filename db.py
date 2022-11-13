import psycopg2
import pandas as pd

df = pd.read_csv('project3/remake_data.csv')
con = psycopg2.connect(host='localhost',dbname="postgres", user="postgres", password="1234",port=5432)

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS data")
cur.execute("""CREATE TABLE data (
                id INT PRIMARY KEY,
                summoners VARCHAR(255),
                game VARCHAR(255),
                result VARCHAR(255),
                time VARCHAR(255),
                champion TEXT,
                level INT,
                d_spell TEXT,
                f_spell TEXT,
                main_rune TEXT,
                sub_rune TEXT,
                items TEXT,
                kill INT,
                death INT,
                assist INT,
                p_kill VARCHAR(255),
                pinkward INT,
                cs INT,
                cs_per_min INT,
                average_tier VARCHAR(255),
                team_champs TEXT,
                team TEXT,
                enemy_champs TEXT,
                enemy TEXT,
                side VARCHAR(255))""")



for i in range(len(df)):
    cur.execute(f"INSERT INTO data (id, summoners, game, result, time, champion, level, d_spell, f_spell, main_rune, sub_rune, items, kill, death, assist, p_kill, pinkward, cs, cs_per_min, average_tier, team_champs, team, enemy_champs, enemy, side) VALUES ({i}, '{df['summoners'][i]}', '{df['game'][i]}', '{df['result'][i]}', '{df['time'][i]}', '{df['champion'][i]}', {df['level'][i]}, '{df['d_spell'][i]}', '{df['f_spell'][i]}', '{df['main_rune'][i]}', '{df['sub_rune'][i]}', '{df['items'][i]}', {df['kill'][i]}, {df['death'][i]}, {df['assist'][i]}, '{df['p_kill'][i]}', {df['pinkward'][i]}, {df['cs'][i]}, {df['cs_per_min'][i]}, '{df['average_tier'][i]}', '{df['team_champs'][i]}', '{df['team'][i]}', '{df['enemy_champ'][i]}', '{df['enemy'][i]}', '{df['side'][i]}')")

con.commit()
cur.close()
con.close()
