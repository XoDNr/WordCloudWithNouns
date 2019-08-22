# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
from konlpy.tag import Mecab
from collections import Counter
from wordcloud import WordCloud

fontFilePath = './font.ttf';

parser = Mecab()
string = """
현대중공업이 창사 40주년을 맞아 ‘2015년 매출 100조원 달성’이라는 목표를 세웠다. 현대중공업은 창사기념일을 하루 앞둔 22일 울산 본사에서 이재성 사장과 김진필 노조위원장 등 임직원 5000>여명이 참석한 가운데 창사 40주년 기념식을 열었다. 이재성 사장은 “우리는 이 자리에서 미래를 향한 새로운 도전을 약속하고, 현대중공업을 더욱 위대한 회사로 발전시켜 나가야 한다”며 “창사 40주년을 새로운 도약의
 원년으로 삼아 앞으로의 40년, 또 그 너머를 향해 전 임직원이 지혜와 의지를 모아 혼신의 노력을 기울여나가야 한다”고 밝혔다. 김진필 노조위원장은 “노사가 함께 하지 않으면 기업이든 노동자든 미래를 설계할 수 없
다”며 “노동조합도 새로운 100년을 향해 도약하는 한 해를 만드는데 적극 동참하겠다”고 말했다. 현대중공업은 1972년 3월23일 고 정주영 창업자를 비롯해 현대중공업 임직원과 울산시민 등 5000여명이 참석한 가운데 울
산조선소 기공식을 열며 시작됐다. 당시만해도 국내 조선사업은 세계 시장점유율이 1%에도 미치지 못할 정도로 영세했다. 하지만 이후 현대중공업은 가파르게 성장해 1983년 건조량을 기준으로 세계 1위 기업에 선정됐으
며, 한국도 조선 강국 대열에 올라 1993년 처음으로 일본을 제치고 수주량 기준으로 세계 1위에 올랐다. 현대중공업은 불황 타개를 위해 VLCC(초대형 유조선) 외 다목적 화물선, 벌크선, 목재운반선 등으로 선종을 다변>화시키는 한편 1975년 수리조선소인 현대미포조선을 설립하고, 같은 해 각종 육·해상 구조물을 제작하는 철구사업부를 신설하는 등 사업영역을 확대했다. 현재는 조선 외에도 해양, 플랜트, 엔진기계, 전기전자, 건설장>비, 그린에너지의 7개 사업본부를 갖추고 있으며 그룹 내에 자원·에너지, 금융·서비스 등을 아우르는 계열사를 지닌 국내 최대의 종합중공업 그룹이다. 현대중공업은 2015년까지 매출 100조원을 달성해 글로벌 종합중공>업 그룹으로 한 단게 도약한다는 중기(中期) 성장 비전도 밝혔다. 매출 100조원은 2011년 66조원보다 50% 가량 증가한 수치다. 사업다각화를 통한 성장동력 확보, 글로벌 경쟁에 선제적으로 대응할 수 있는 글로벌 경영>체계의 구축, 계열사 간 시너지 극대화 등을 중점추진전략으로 내세웠다.
"""
nounsList = parser.nouns(string)

nounsCount = Counter(nounsList)
nounsCountTags = nounsCount.most_common(20)
print(nounsCountTags)

wc = WordCloud(font_path=fontFilePath, background_color='#FFF', width=800, height=600)
cloudTags = wc.generate_from_frequencies(dict(nounsCountTags))

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloudTags)
plt.show()
