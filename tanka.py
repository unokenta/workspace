import random

#名詞フレーム
n_p_2=["日々","砂","月","夜","嘘","朝","恋","夢","海","鳥","空","声","雨","森","鍵","ネジ","波"]
n_p_3=["鼓動","明日","瞳","歪み","未来","光","心","とばり","あなた","掟","ロマン"]
n_p_4=["月光","片隅","岸壁","わびさび","旅人","魂","木漏れ日","綻び","企み","静寂","歯車","瞬き","足跡","心境","色彩"]
n_p_5=["クリスマス","アゲハ蝶","蝉時雨"]
n_p_6=["ひこうきぐも","登竜門","かみなり雲","桜吹雪"]

#述部フレーム
v_p_4=["を灯す","に陰る","が揺れる","がひかる","を照らす","が踊る","が凍る","が撫でる"]
v_p_5=["が残した","が囁く","へ歌った","を見下ろす","がきらめく","と移ろい","が滴る","を引き出す","を閉ざした","を遮る","を掴めば","に触れたい","が寄り添う"]
v_p_6=["に教わった","が届かない","を諦める","を待っている","がみつめてる","と話してる","が訪れる","が踊り出す"]

#修飾部フレーム
m_p_3=["時の","錆びた","欠けた","残る","陰る","朝の","荒れた"]
m_p_4=["佇む","優しい","壊れた","しおれた","訪ねた","仰いだ","隠した","きらめく","轟く","蠢く","冷たい","凍える","儚い"]
m_p_5=["唐突な","一粒の","ありふれた","一筋の","鮮やかな","大げさな","紅の"]

#構文テンプレート
s_f_1=[random.choice(n_p_4),random.choice(v_p_6),random.choice(n_p_2),random.choice(m_p_5),"\t",random.choice(n_p_2),random.choice(v_p_5),random.choice(m_p_3),random.choice(n_p_4)]
s_f_2=[random.choice(m_p_5),random.choice(n_p_2),random.choice(v_p_5),random.choice(m_p_3),random.choice(n_p_2),"\t",random.choice(m_p_4),random.choice(n_p_2),random.choice(v_p_4),random.choice(n_p_4)]
s_f_3=[random.choice(m_p_3),random.choice(n_p_2),random.choice(n_p_3),random.choice(v_p_4),random.choice(m_p_5),"\t",random.choice(m_p_4),random.choice(n_p_2),random.choice(v_p_4),random.choice(n_p_4)]
s_f_4=[random.choice(m_p_5),random.choice(n_p_6),random.choice(v_p_6),"\t",random.choice(m_p_3),random.choice(n_p_3),random.choice(v_p_6),random.choice(n_p_2)]

s_f=[s_f_1,s_f_2,s_f_3,s_f_4]


print("".join(random.choice(s_f)))
