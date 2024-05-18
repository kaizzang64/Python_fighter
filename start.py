import time
import tkinter as tk

name_window = None  # 전역 변수로 name_window 선언
prologue_window = None  # 전역 변수로 prologue_window 선언
prologue_index = 0  # 전역 변수로 prologue_index 선언


funds_label = None


funds = 10000
population = 10000
economy = 0
research = 0
military = 100
region = 2

# 이름 입력 화면을 생성하는 함수
def name_scene():
    global name_window  # name_window를 전역 변수로 사용하겠다고 선언
    name_window = tk.Tk()
    name_window.title("게임 시작")  # 윈도우 제목 설정
    name_window.geometry("1280x720")  # 윈도우 크기 설정

    # 게임 시작 버튼을 누를 때 호출되는 함수
    def start_game():
        user_name = user_name_entry.get()  # 사용자가 입력한 이름을 가져옴
        name_window.destroy()  # 이름 입력 윈도우 종료
        prologue_scene(user_name)  # 프롤로그 장면으로 이동하는 함수 호출

    # 사용자 이름을 입력하는 레이블 생성
    user_name_label = tk.Label(name_window, text="당신의 이름을 입력하세요:")
    user_name_label.pack()

    # 사용자 이름을 입력하는 입력창 생성
    user_name_entry = tk.Entry(name_window)
    user_name_entry.pack()

    # 게임 시작 버튼 생성
    start_button = tk.Button(name_window, text="게임 시작", command=start_game, width=20, height=5)
    start_button.pack()

    name_window.mainloop()  # Tkinter 이벤트 루프 시작

# 프롤로그 장면을 생성하고 업데이트하는 함수
def prologue_scene(user_name):
    global prologue_window, prologue_index

    prologue_texts = [
        """
        젤렌스키의 우크라이나가 붕괴했을때, 우크라이나인들은 
        러시아인들이 무너지고 패배했다고 생각했습니다.
        러시아 국기가 가장 중요한 지역이자 
        예전 우크라이나의 수도 한복판에 자리잡았습니다. 
        나약하고 겁에 질린 우크라이나 군대는 곧 무의미하게 해체되고, 
        푸틴 서기장이 다시한번 소비에트 연방을 재건하게 두었습니다.
        대만 전쟁은 충격 그 자체였습니다.치밀하게 계획된 계획이 
        중국과 러시아의 신무기와 함께 실행되었습니다. 
        과거 2차 세계대전의 중국군이 무색할정도로 대만섬 침공은 
        러시아가 비밀스럽게 제공한 '신무기'와 함께 이루어졌습니다.
        미국과 일본, 대한민국을 중심으로한 한미일 연합군은 
        초반에는 중국군을 강하게 밀어붙였습니다.
        잠시 동안이지만, 대만섬 전체를 완전히 되찾을것만 같았습니다.
        그 순간이 지나자, 전쟁의 비극이 시작되었습니다.연합 사령부 내부의 
        그 누구도 무엇이 그들의 주도권을 빼앗아갔는지 알아차리지 못하였습니다.
        중국의 스파이들? 지휘관의 무능함? 정치인들의 배반? 그 무엇이 원인이던간에,
        한미일 연합사령부의 공세는 중단되었습니다. 중국군은 필사적으로 
        한미일 연합군에 맞서며 서서히 전세를 뒤집기 시작했으며,
        미국의 항공모함을 거의 날려버린것을 시작으로. 중국 첩보원이 비밀리에 
        주도한 반전 시위 물결이 서울, 도쿄, 뉴욕의 거리를
        메우기 시작했습니다. 조금씩 조금씩 한미일 연합군은 
        밀려나기 시작했고, 끝내 완전히 붕괴해 버렸습니다.
        """,
        f"""
        \"D-3 전쟁의 서막\"


        지난 10년동안 어둠속을 헤쳐나가며 우린 계속 나아갔습니다.
        미국인들은 오만에 가득차 북태평양 조약기구는 무너져내렸으며
        역사의 쓰레기통 속으로 사라졌다고 생각했습니다.
        우리는 10년전 민주주의를 위해 싸워왔습니다.
        한국, 일본, 미국에서 젊고 용감한 이들이
        빨갱이들을 몰아내기 위한 위대한 시도를 향해 단결했습니다.
        현실에 안주하고 있던 중국인들은 전쟁속에서
        남중국해를 향해 진격하는 한미일 연합군에게 패배에 패배를 거듭하였습니다.
        허나 우리의 성공이 절정에 이르렀을때,
        우리는 바로 자기 자신들에게 배반당했습니다.
        무능한 지휘관들과 정치인들은
        승리의 안도감에 심취하여, '신무기'의 성능을 매우 간과하여
        중국군이 전세를 뒤집을때 까지 손을 놓고 있었습니다.
        그리고 우리의 먼 후방에서도, 극좌단체와 지하 간첩 조직들이 종전을 선동하며
        반전 시위가 이어졌습니다.
        그 결과, 세계의 경찰을 자처하던 미국은 졸지에 이빨빠진 호랑이로 전락하고.
        NATO(북대서양조약기구)회원국들의 탈퇴를 막을수 없었습니다.

        지난 전쟁으로 단련된 베테랑 {user_name}(와)과 오정훈 중장은 
        참여하는 전투마다 승전보를 울리며 엄청난 공을 세웠지만, 
        대만의 정부 인사를 탈출시키는 마지막 작전 도중 엄청난 전력 손실을 입고
        간신히 탈출하여 풍전등화 앞의 조국을 지키고 있습니다.
        비무장지대 너머에선, 
        중국과 러시아의 지원을 받은 괴뢰군들이 적화통일을 꿈꾸고있습니다. 
        끝내 대만 전쟁에서 살아남지 못한 베테랑 군인들을 모두 잃어버렸습니다.
        우리나라 에선, 인적 자원의 감소와 군 내부의 보수파들로 인해
        매년 수많은 국방비를 지출하는것에 비해 전력이 턱없이 모자란 상태입니다.
        정치인들은 서로를 헐뜯으며 연합군이 지난 전쟁속에서 치명적인 피해를 
        입게 만든 탁상공론을 지속하고 있습니다.
        어찌되었건, 전쟁은 곧 찾아올것 입니다. 지난 전쟁을 깊이 반성하여,
        더이상 대한민국의 국민들이 피눈물을 흘리지 않게 해야 합니다.
        더이상 물러설곳은 없으며,
        역사의 필연성은 폭군이나 빨갱이들에 의해 멈춰지지 않을것입니다.
        우린 죽음이 찾아오거나, 빨갱이의 총끝이 목끝까지 오더라도
        결코 투쟁을 멈추지 않을 것 입니다.

        러시아를 비롯한 공산주의 세력이 NATO를 무찌르고 승리하면서 
        세계에 신질서가 내려왔습니다. 유니언 잭과 성조기가
        있던 자리에는 오성홍기와 낫과 망치가 다시한번 
        휘날리고 있습니다. 한반도의 어두운 밤하늘에 희미한 
        빛이 깜빡이고 있습니다. 푸틴 서기장은 2차 세계대전 이후 80년만에
        찾아온 승리를 축하하고 있으며, 북한은 신 질서에 힘입어
        머지않아 한반도를 붉게 물들일 날을 꿈꾸고 있습니다.

        낙동강 방어선의 부대는 모두 연락이 끊겼으며, 마지막 남은 민주주의의
        잔해들은 자신의 운명을 실현할 준비를 하고 있습니다.
        """,
        f"""
        -------------------------------------------------------------
        (중략)
        -------------------------------------------------------------
        2033년 8월 12일, 총성이 멈췄습니다. 2차 한국전쟁은 끝났고,
        북한은 2년 동안의 진이 빠지는 전쟁 끝에 승전국이 되었습니다. 
        전세계 전쟁사에 길이남을 치열한 공방전 끝에 
        양측은 수백만명의 사상자를 내고 끝내 부산은 함락되었습니다.
        오정훈 사령관이 이끄는 해병대가 필사적으로 저항해 제주도에 망명정부를
        세웠지만. 제주도  심각한 경제적, 군사적 타격을 입었습니다.
        
        "국민여러분"
        
        {user_name}의 힘있는 목소리가 제주도에 가득 모인 군중들을 울렸다. 
        군인들, 피난민들, 기자들, 정부인사들. 모두 이곳에 있었고, 
        모두가 환영받았다. 
        \"우리 모두는 조선 민주주의 인민 공화국이라 불리는 
        파괴적인 괴물 때문에 이 자리에 있습니다. 그 안에 있는 무수한 악마들은 
        전세계를 충격에 빠뜨려 침묵에 잠기게 했습니다. 허나 더 이상은 안 됩니다! 
        김정은의 비도덕적인 이데올로기가 더 이상 퍼져나가서도, 
        더 많은 사람들을 죽여서도 안 됩니다!\" 
        광란의 환호소리가 터져나왔다. 그 잠깐 동안 절망과 처절함은 어딘가로 사라졌다. 
        \"여러분들 모두 들어보십시오. 여러분들의 증오를 잘 알고 있습니다. 
        모두 그럴만 합니다. 그럴만 해요! 저희 대한민국 정부가 저지른 잘못으로 그들을 
        바다속으로 쫓아버리고 싶겠죠. 하지만 부디, 들어주십시오. 
        제가 말하는 것을 들어주십시오! 우리는 여기서 당장 이 증오의 고리를 끊어버려야 합니다!\" 
        여전히 환호성은 강력했다. 하지만 방금 전보다는 약했다.
        \"저는 대한민국을 압니다. 진정한 대한민국을. 북한놈들이 뿌리를 뽑아버리려 했던 
        그런 대한민국을 말입니다.\"
        {user_name}는 깊게 숨을 들이마셨다. 
        "허나 대한민국은 결코 죽지 않았습니다! 민주 대한의 빛은 결코
        없어질 수 없습니다! 전세계를 위해서는 더 나은 미래가 있을 겁니다! 
        우리는 패배자와 승리자로, 여당과 야당으로 서지 않아야 합니다. 
        우리는 형제지간, 자매지간, 그리고 동등한 관계로서 존재해야 합니다! 
        그러니 부디, 대한민국을 위하여 간청합니다. 저희를 용서해주십시오. 
        저희는 최선을 다했습니다만, 국민여러분들의 생명과 재산을 지키지 못했습니다!" 
        그의 두 손은 주먹을 꽉 쥐었다. 그는 이빨을 더 세게 갈았다. 
        사람들은 침묵 속에서 그를 재판했다. "국민여러분, 
        우리를 용서해주십시오. 우리가 자그마한 동정조차 얻을 자격이 없다 하더라도, 
        교양있는 자들은 자유를 위해 계속해서 싸울 것입니다." 
        그의 목소리는 힘있게 깔렸고, 
        점점 갈라지기 시작했다. 분위기는 어두워졌다.{user_name}는 천천히 무릎을 
        꿇고 머리를 앞으로 숙였다. 수 초가 지났다. 아무도 말하지 않았다. 
        그들은 {user_name}의 몸이 흔들리는 것을 알아챘다. 흔들리는 몸 사이로, 
        두 방울의 눈물이 목조 연단에 떨어졌다. 그는 사람들이 이 숨 막힐 것 같은 
        침묵을 계속하리라 생각했다. 하지만 한 사람이 박수를 치기 시작했고, 
        10명이, 100명이, 1000명이 박수를 쳤다. 그가 자유를 위해 싸우기로 결심한 
        자들을 올려다봤을 때, {user_name}의 얼굴은 떨리는 미소를 지었다.
        """,
        f"""
        민경록 대통령의 편지


        {user_name}님에게,
        
        패배는 언제나 어렵습니다. 우리는 친절한 말로 패배의 쓰라림을 달래고
        공개적인 겸손을 보여 주려고 노력할 수 있지만, 그 쓰라림은 결코 사라지지 않습니다.
        그것은 우리 각자가 무덤까지 가지고 갈 상처입니다.        
        그런 의미에서 저는 당신이 비상 행정부 수장이 되는것이 상당히 다행이라고 생각합니다.
        사령관님처럼 정직하고 애국심이 강하며 헌신적인 군인으로서
        저는 여생을 '어떻게 했더라면', '어떻게 다르게 행동할 수 있었을까'를
        고민하며 보낼 것입니다. 제가 대통령에 당선된것이 우연인지, 역사의 긴 궤적에서
        벗어난 일탈인지, 아니면 완전히 다른 무언가인지 궁금해할 것입니다.       
        이 질문에 대한 답은 결코 알 수 없지만, 그것은 당신과 국민들이 짊어져야 할 짐입니다.
        {user_name}님, 제가 재임 기간에 해결하고자 했던 더 큰 문제들이 이제 사령관님에게 떠넘겨졌습니다.   
        현재 한반도에 남아있는 우리나라국민들은 더이상 저희가 보호해줄수 없는 상태입니다.
        1차 한국전쟁 이전의 삶에 대한 기억이 있는 사람들이 거의 없으며, 
        우리는 자유의 횃불이 잠시라도 이득이 된다면 부주의하게도 꺼버릴 수 있는 
        선동가와 급진주의자들이 점점 더 많아지는 나라에 살고 있습니다.
        저는 가끔 밤마다 창밖을 바라보며 사령관님이 이끄는 새로운 세대가 
        이러한 도전에 맞설 수 있을지 걱정합니다. 
        하지만 여러분은 할 수 있다고 믿어 의심치 않습니다.
        모든 측면을 살피고 신중한 접근 방식을 취함으로써, 저는 당신이 다시한번
        자유 민주주의를 되찾아 올것이라 굳게 믿습니다.
        이 나라를 자랑스럽게 만드십시오, 대통령님. 위대한 일을 마무리하십시오.
        영원히 당신의 것입니다,
        """
    ]

    button_texts = ['다음', '총원 최대 경계 상태로!', '감사합니다...', '편지는 정중하고 무뚝뚝하게 읽혔다.']

    def update_text():
        global prologue_index

        if prologue_index < len(prologue_texts):
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, prologue_texts[prologue_index])
            next_button.config(text=button_texts[prologue_index])  # 버튼 텍스트 변경
            prologue_index += 1
        else:
            prologue_index = 0
            prologue_window.destroy()
            Lobby()

    if prologue_window is None:
        prologue_window = tk.Toplevel()
        prologue_window.title("프롤로그")
        prologue_window.geometry("1280x720")

        text_widget = tk.Text(prologue_window, height=50, width=100)
        text_widget.pack()

        next_button = tk.Button(prologue_window, text="다음", command=update_text, width=30, height=5)
        next_button.pack(side=tk.BOTTOM)

        update_text()

def update_funds_label():
    global funds_label  # funds_label 변수를 전역 변수로 사용
    funds_label.config(text=f"자금 : {funds}")

def update_military_label():
    global military_label
    military_label.config(text=f"군사력 : {military}")

def update_population_label():
    global population_label
    population_label.config(text=f"인구 : {population}")

def update_economy_label():
    global economy_label
    economy_label.config(text=f"경제력 : {economy}")

def update_research_label():
    global research_label_label
    research_label.config(text=f"연구력 : {research}")

def update_region_label():
    global region_label
    region_label.config(text=f"지역수 : {region}")

def update_combat_power_label():
    global combat_power_label
    combat_power_label.config(text=f"전투력 : {military*0.1}")

#세금 징수 창 버튼
def on_jeju_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
     # region이 2 이상인 경우에만 함수 실행
    if region >= 1:
        funds += population * 0.07
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_jeolla_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 3:
        funds += population * 0.08
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_gyeongsang_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 6:
        funds += population * 0.15
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_chungcheong_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 15:
        funds += population * 0.20
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_gangwon_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 21:
        funds += population * 0.25
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_gyeonggi_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 54:
        funds += population * 0.45
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_hwanghae_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 49:
        funds += population * 0.35
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_pyongan_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 31:
        funds += population * 0.30
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)  # update_funds_label 함수 호출

def on_wonsan_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 26:
        funds += population * 0.25
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

def on_hamgyong_button_click():
    global funds
    global funds_label  # funds_label 변수를 전역 변수로 선언
    global population
    global region
    if region >= 44:
        funds += population * 0.20
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)

#군사력 개발 버튼
def buy_soldier():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>500 and research>=0:
        military = military + 1
        funds=funds-500
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def buy_Rifle():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>2000 and research>=20:
        military = military + 6
        funds=funds-2000
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def buy_RPG():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>6000 and research>=175:
        military = military + 25
        funds=funds-6000
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def buy_Artillery():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>50000 and research>=2200:
        military = military + 2200
        funds=funds-50000
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def buy_Artillery():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>50000 and research>=2200:
        military = military + 250
        funds=funds-50000
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def buy_Tank():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>500000 and research>=15000:
        military = military + 2600
        funds=funds-500000
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def buy_Fighter():
    global funds
    global military_label  # funds_label 변수를 전역 변수로 선언
    global military
    global research
    if funds>8000000 and research>=30000:
        military = military + 43000
        funds=funds-8000000
        update_funds_label()  # update_funds_label 함수 호출
        update_military_label()
        update_combat_power_label()

def research_1():
    global funds
    global research_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global research
    if funds>5000 and economy>=0:
        research = research + 1
        funds=funds-5000
        update_funds_label()  # update_funds_label 함수 호출
        update_research_label()

def research_2():
    global funds
    global research_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global research
    if funds>30000 and economy>=40:
        research = research + 6
        funds=funds-30000
        update_funds_label()  # update_funds_label 함수 호출
        update_research_label()

def research_3():
    global funds
    global research_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global research
    if funds>90000 and economy>=300:
        research = research + 20
        funds=funds-90000
        update_funds_label()  # update_funds_label 함수 호출
        update_research_label()

def research_4():
    global funds
    global research_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global research
    if funds>500000 and economy>=7500:
        research = research + 115
        funds=funds-500000
        update_funds_label()  # update_funds_label 함수 호출
        update_research_label()

def research_5():
    global funds
    global research_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global research
    if funds>5000000 and economy>=70000:
        research = research + 1200
        funds=funds-5000000
        update_funds_label()  # update_funds_label 함수 호출
        update_research_label()

def research_6():
    global funds
    global research_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global research
    if funds>80000000 and economy>=800000:
        research = research + 19300
        funds=funds-800000
        update_funds_label()  # update_funds_label 함수 호출
        update_research_label()

def facility_1():
    global funds
    global economy_label  # funds_label 변수를 전역 변수로 선언
    global population_label
    global economy
    global region
    global population
    if funds>2500 and region>=0:
        economy = economy + 1
        funds=funds-2500
        population=population+200
        update_funds_label()  # update_funds_label 함수 호출
        update_economy_label()
        update_population_label()

def facility_2():
    global funds
    global economy_label  # funds_label 변수를 전역 변수로 선언
    global population_label
    global economy
    global region
    global population
    if funds>10000 and region>=3:
        economy = economy + 5
        funds=funds-10000
        population=population+900
        update_funds_label()  # update_funds_label 함수 호출
        update_economy_label()
        update_population_label()

def facility_3():
    global funds
    global economy_label  # funds_label 변수를 전역 변수로 선언
    global population_label
    global economy
    global region
    global population
    if funds>50000 and region>=9:
        economy = economy + 27
        funds=funds-50000
        population=population+4600
        update_funds_label()  # update_funds_label 함수 호출
        update_economy_label()
        update_population_label()

def facility_4():
    global funds
    global economy_label  # funds_label 변수를 전역 변수로 선언
    global population_label
    global economy
    global region
    global population
    if funds>300000 and region>=15:
        economy = economy + 165
        funds=funds-300000
        population=population+28000
        update_funds_label()  # update_funds_label 함수 호출
        update_economy_label()
        update_population_label()

def facility_5():
    global funds
    global economy_label  # funds_label 변수를 전역 변수로 선언
    global population_label
    global economy
    global region
    global population
    if funds>2000000 and region>=24:
        economy = economy + 1100
        funds=funds-2000000
        population=population+190000
        update_funds_label()  # update_funds_label 함수 호출
        update_economy_label()
        update_population_label()

def facility_6():
    global funds
    global economy_label  # funds_label 변수를 전역 변수로 선언
    global economy
    global region
    global population
    if funds>30000000 and region>=39:
        economy = economy + 17000
        funds=funds-30000000
        population=population+2900000
        update_funds_label()  # update_funds_label 함수 호출
        update_economy_label()
        update_population_label()

def region_1(region_1_button, region_2_button):
    global military
    global enemy_military
    global region
    enemy_military = 200

    region_1_battle = tk.Toplevel()
    region_1_battle.title("해남 전투")
    region_1_battle.geometry("800x600")

    label = tk.Label(region_1_battle, text="해남 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_1_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_1_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_1_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_1_battle, text="돌아가기", command=region_1_battle.destroy)
            back_button.pack()
            button_states["region_2_button"] = "active"
            button_states["region_1_button"] = "disabled"
            region_2_button.config(state=button_states["region_2_button"])
            region_1_button.config(state=button_states["region_1_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_1_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_1_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_1_battle, text="돌아가기", command=region_1_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_1_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_1_battle.after(1250, perform_ally_attack)

def region_2(region_2_button, region_3_button):
    global military
    global enemy_military
    global region
    enemy_military = 500

    region_2_battle = tk.Toplevel()
    region_2_battle.title("여수 전투")
    region_2_battle.geometry("800x600")

    label = tk.Label(region_2_battle, text="여수 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_2_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_2_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_2_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_2_battle, text="돌아가기", command=region_2_battle.destroy)
            back_button.pack()
            button_states["region_3_button"] = "active"
            button_states["region_2_button"] = "disabled"
            region_3_button.config(state=button_states["region_3_button"])
            region_2_button.config(state=button_states["region_2_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_2_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_2_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_2_battle, text="돌아가기", command=region_2_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_2_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_2_battle.after(1250, perform_ally_attack)

def region_3(region_3_button, region_4_button):
    global military
    global enemy_military
    global region
    enemy_military = 1000

    region_3_battle = tk.Toplevel()
    region_3_battle.title("광주 전투")
    region_3_battle.geometry("800x600")

    label = tk.Label(region_3_battle, text="광주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_3_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_3_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_3_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_3_battle, text="돌아가기", command=region_3_battle.destroy)
            back_button.pack()
            button_states["region_4_button"] = "active"
            button_states["region_3_button"] = "disabled"
            region_3_button.config(state=button_states["region_3_button"])
            region_4_button.config(state=button_states["region_4_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_3_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_3_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_3_battle, text="돌아가기", command=region_3_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_3_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_3_battle.after(1250, perform_ally_attack)

def region_4(region_4_button, region_5_button):
    global military
    global enemy_military
    global region
    enemy_military = 2000

    region_4_battle = tk.Toplevel()
    region_4_battle.title("남원 전투")
    region_4_battle.geometry("800x600")

    label = tk.Label(region_4_battle, text="남원 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_4_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_4_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_4_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_4_battle, text="돌아가기", command=region_4_battle.destroy)
            back_button.pack()
            button_states["region_5_button"] = "active"
            button_states["region_4_button"] = "disabled"
            region_4_button.config(state=button_states["region_4_button"])
            region_5_button.config(state=button_states["region_5_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_4_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_4_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_4_battle, text="돌아가기", command=region_4_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_4_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_4_battle.after(1250, perform_ally_attack)

def region_5(region_5_button, region_6_button):
    global military
    global enemy_military
    global region
    enemy_military = 3200

    region_5_battle = tk.Toplevel()
    region_5_battle.title("전주 전투")
    region_5_battle.geometry("800x600")

    label = tk.Label(region_5_battle, text="전주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_5_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_5_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_5_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_5_battle, text="돌아가기", command=region_5_battle.destroy)
            back_button.pack()
            button_states["region_6_button"] = "active"
            button_states["region_5_button"] = "disabled"
            region_5_button.config(state=button_states["region_5_button"])
            region_6_button.config(state=button_states["region_6_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_5_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_5_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_5_battle, text="돌아가기", command=region_5_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_5_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_5_battle.after(1250, perform_ally_attack)

def region_6(region_6_button, region_7_button):
    global military
    global enemy_military
    global region
    enemy_military = 4500

    region_6_battle = tk.Toplevel()
    region_6_battle.title("군산 전투")
    region_6_battle.geometry("800x600")

    label = tk.Label(region_6_battle, text="군산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_6_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_6_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_6_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_6_battle, text="돌아가기", command=region_6_battle.destroy)
            back_button.pack()
            button_states["region_7_button"] = "active"
            button_states["region_6_button"] = "disabled"
            region_7_button.config(state=button_states["region_7_button"])
            region_6_button.config(state=button_states["region_6_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_6_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_6_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_6_battle, text="돌아가기", command=region_6_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_6_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_6_battle.after(1250, perform_ally_attack)

def region_7(region_7_button, region_8_button):
    global military
    global enemy_military
    global region
    enemy_military = 5800

    region_7_battle = tk.Toplevel()
    region_7_battle.title("진주 전투")
    region_7_battle.geometry("800x600")

    label = tk.Label(region_7_battle, text="진주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_7_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_7_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_7_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_7_battle, text="돌아가기", command=region_7_battle.destroy)
            back_button.pack()
            button_states["region_8_button"] = "active"
            button_states["region_7_button"] = "disabled"
            region_7_button.config(state=button_states["region_7_button"])
            region_8_button.config(state=button_states["region_8_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_7_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_7_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_7_battle, text="돌아가기", command=region_7_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_7_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_7_battle.after(1250, perform_ally_attack)

def region_8(region_8_button, region_9_button):
    global military
    global enemy_military
    global region
    enemy_military = 7500

    region_8_battle = tk.Toplevel()
    region_8_battle.title("합천 전투")
    region_8_battle.geometry("800x600")

    label = tk.Label(region_8_battle, text="합천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_8_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_8_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_8_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_8_battle, text="돌아가기", command=region_8_battle.destroy)
            back_button.pack()
            button_states["region_9_button"] = "active"
            button_states["region_8_button"] = "disabled"
            region_8_button.config(state=button_states["region_8_button"])
            region_9_button.config(state=button_states["region_9_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_8_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_8_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_8_battle, text="돌아가기", command=region_8_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_8_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_8_battle.after(1250, perform_ally_attack)

def region_9(region_9_button, region_10_button):
    global military
    global enemy_military
    global region
    enemy_military = 9000

    region_9_battle = tk.Toplevel()
    region_9_battle.title("울산 전투")
    region_9_battle.geometry("800x600")

    label = tk.Label(region_9_battle, text="울산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_9_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_9_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_9_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_9_battle, text="돌아가기", command=region_9_battle.destroy)
            back_button.pack()
            button_states["region_10_button"] = "active"
            button_states["region_9_button"] = "disabled"
            region_9_button.config(state=button_states["region_9_button"])
            region_10_button.config(state=button_states["region_10_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_9_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_9_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_9_battle, text="돌아가기", command=region_9_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_9_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_9_battle.after(1250, perform_ally_attack)

def region_10(region_10_button, region_11_button):
    global military
    global enemy_military
    global region
    enemy_military = 11000

    region_10_battle = tk.Toplevel()
    region_10_battle.title("부산 전투")
    region_10_battle.geometry("800x600")

    label = tk.Label(region_10_battle, text="부산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_10_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_10_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_10_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_10_battle, text="돌아가기", command=region_10_battle.destroy)
            back_button.pack()
            button_states["region_11_button"] = "active"
            button_states["region_10_button"] = "disabled"
            region_10_button.config(state=button_states["region_10_button"])
            region_11_button.config(state=button_states["region_11_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_10_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_10_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_10_battle, text="돌아가기", command=region_10_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_10_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_10_battle.after(1250, perform_ally_attack)


def region_11(region_11_button, region_12_button):
    global military
    global enemy_military
    global region
    enemy_military = 15000

    region_11_battle = tk.Toplevel()
    region_11_battle.title("논산 전투")
    region_11_battle.geometry("800x600")

    label = tk.Label(region_11_battle, text="논산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_11_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_11_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_11_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_11_battle, text="돌아가기", command=region_11_battle.destroy)
            back_button.pack()
            button_states["region_12_button"] = "active"
            button_states["region_11_button"] = "disabled"
            region_11_button.config(state=button_states["region_11_button"])
            region_12_button.config(state=button_states["region_12_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_11_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_11_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_11_battle, text="돌아가기", command=region_11_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_11_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_11_battle.after(1250, perform_ally_attack)

def region_12(region_12_button, region_13_button):
    global military
    global enemy_military
    global region
    enemy_military = 20000

    region_12_battle = tk.Toplevel()
    region_12_battle.title("세종 전투")
    region_12_battle.geometry("800x600")

    label = tk.Label(region_12_battle, text="세종 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_12_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_12_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_12_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_12_battle, text="돌아가기", command=region_12_battle.destroy)
            back_button.pack()
            button_states["region_13_button"] = "active"
            button_states["region_12_button"] = "disabled"
            region_12_button.config(state=button_states["region_12_button"])
            region_13_button.config(state=button_states["region_13_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_12_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_12_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_12_battle, text="돌아가기", command=region_12_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_12_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_12_battle.after(1250, perform_ally_attack)

def region_13(region_13_button, region_14_button):
    global military
    global enemy_military
    global region
    enemy_military = 28000

    region_13_battle = tk.Toplevel()
    region_13_battle.title("포항 전투")
    region_13_battle.geometry("800x600")

    label = tk.Label(region_13_battle, text="포항 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_13_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_13_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_13_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_13_battle, text="돌아가기", command=region_13_battle.destroy)
            back_button.pack()
            button_states["region_14_button"] = "active"
            button_states["region_13_button"] = "disabled"
            region_14_button.config(state=button_states["region_14_button"])
            region_13_button.config(state=button_states["region_13_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_13_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_13_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_13_battle, text="돌아가기", command=region_13_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_13_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_13_battle.after(1250, perform_ally_attack)

def region_14(region_14_button, region_15_button):
    global military
    global enemy_military
    global region
    enemy_military = 40000

    region_14_battle = tk.Toplevel()
    region_14_battle.title("영덕 전투")
    region_14_battle.geometry("800x600")

    label = tk.Label(region_14_battle, text="영덕 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_14_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_14_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_14_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_14_battle, text="돌아가기", command=region_14_battle.destroy)
            back_button.pack()
            button_states["region_15_button"] = "active"
            button_states["region_14_button"] = "disabled"
            region_14_button.config(state=button_states["region_14_button"])
            region_15_button.config(state=button_states["region_15_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_14_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_14_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_14_battle, text="돌아가기", command=region_14_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_14_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_14_battle.after(1250, perform_ally_attack)

def region_15(region_15_button, region_16_button):
    global military
    global enemy_military
    global region
    enemy_military = 52000

    region_15_battle = tk.Toplevel()
    region_15_battle.title("안동 전투")
    region_15_battle.geometry("800x600")

    label = tk.Label(region_15_battle, text="안동 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_15_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_15_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_15_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_15_battle, text="돌아가기", command=region_15_battle.destroy)
            back_button.pack()
            button_states["region_16_button"] = "active"
            button_states["region_15_button"] = "disabled"
            region_15_button.config(state=button_states["region_15_button"])
            region_16_button.config(state=button_states["region_16_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_15_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_15_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_15_battle, text="돌아가기", command=region_15_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_15_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_15_battle.after(1250, perform_ally_attack)

def region_16(region_16_button, region_17_button):
    global military
    global enemy_military
    global region
    enemy_military = 65000

    region_16_battle = tk.Toplevel()
    region_16_battle.title("김천 전투")
    region_16_battle.geometry("800x600")

    label = tk.Label(region_16_battle, text="김천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_16_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_16_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_16_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_16_battle, text="돌아가기", command=region_16_battle.destroy)
            back_button.pack()
            button_states["region_17_button"] = "active"
            button_states["region_16_button"] = "disabled"
            region_16_button.config(state=button_states["region_16_button"])
            region_17_button.config(state=button_states["region_17_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_16_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_16_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_16_battle, text="돌아가기", command=region_16_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_16_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_16_battle.after(1250, perform_ally_attack)

def region_17(region_17_button, region_18_button):
    global military
    global enemy_military
    global region
    enemy_military = 80000

    region_17_battle = tk.Toplevel()
    region_17_battle.title("대구 전투")
    region_17_battle.geometry("800x600")

    label = tk.Label(region_17_battle, text="대구 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_17_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_17_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_17_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_17_battle, text="돌아가기", command=region_17_battle.destroy)
            back_button.pack()
            button_states["region_18_button"] = "active"
            button_states["region_17_button"] = "disabled"
            region_17_button.config(state=button_states["region_17_button"])
            region_18_button.config(state=button_states["region_18_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_17_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_17_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_17_battle, text="돌아가기", command=region_17_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_17_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_17_battle.after(1250, perform_ally_attack)
    
def region_18(region_18_button, region_19_button):
    global military
    global enemy_military
    global region
    enemy_military = 100000

    region_18_battle = tk.Toplevel()
    region_18_battle.title("청주 전투")
    region_18_battle.geometry("800x600")

    label = tk.Label(region_18_battle, text="청주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_18_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_18_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_18_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_18_battle, text="돌아가기", command=region_18_battle.destroy)
            back_button.pack()
            button_states["region_19_button"] = "active"
            button_states["region_18_button"] = "disabled"
            region_18_button.config(state=button_states["region_18_button"])
            region_19_button.config(state=button_states["region_19_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_18_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_18_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_18_battle, text="돌아가기", command=region_18_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_18_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_18_battle.after(1250, perform_ally_attack)

def region_19(region_19_button, region_20_button):
    global military
    global enemy_military
    global region
    enemy_military = 125000

    region_19_battle = tk.Toplevel()
    region_19_battle.title("대전 전투")
    region_19_battle.geometry("800x600")

    label = tk.Label(region_19_battle, text="대전 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_19_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_19_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_19_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_19_battle, text="돌아가기", command=region_19_battle.destroy)
            back_button.pack()
            button_states["region_20_button"] = "active"
            button_states["region_19_button"] = "disabled"
            region_19_button.config(state=button_states["region_19_button"])
            region_20_button.config(state=button_states["region_20_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_19_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_19_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_19_battle, text="돌아가기", command=region_19_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_19_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_19_battle.after(1250, perform_ally_attack)

def region_20(region_20_button, region_21_button):
    global military
    global enemy_military
    global region
    enemy_military = 150000

    region_20_battle = tk.Toplevel()
    region_20_battle.title("충주 전투")
    region_20_battle.geometry("800x600")

    label = tk.Label(region_20_battle, text="충주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_20_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_20_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_20_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_20_battle, text="돌아가기", command=region_20_battle.destroy)
            back_button.pack()
            button_states["region_21_button"] = "active"
            button_states["region_20_button"] = "disabled"
            region_20_button.config(state=button_states["region_20_button"])
            region_21_button.config(state=button_states["region_21_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_20_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_20_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_20_battle, text="돌아가기", command=region_20_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_20_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_20_battle.after(1250, perform_ally_attack)

def region_21(region_21_button, region_22_button):
    global military
    global enemy_military
    global region
    enemy_military = 180000

    region_21_battle = tk.Toplevel()
    region_21_battle.title("원주 전투")
    region_21_battle.geometry("800x600")

    label = tk.Label(region_21_battle, text="원주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_21_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_21_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_21_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_21_battle, text="돌아가기", command=region_21_battle.destroy)
            back_button.pack()
            button_states["region_22_button"] = "active"
            button_states["region_21_button"] = "disabled"
            region_21_button.config(state=button_states["region_21_button"])
            region_22_button.config(state=button_states["region_22_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_21_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_21_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_21_battle, text="돌아가기", command=region_21_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_21_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_21_battle.after(1250, perform_ally_attack)

def region_22(region_22_button, region_23_button):
    global military
    global enemy_military
    global region
    enemy_military = 215000

    region_22_battle = tk.Toplevel()
    region_22_battle.title("평창 전투")
    region_22_battle.geometry("800x600")

    label = tk.Label(region_22_battle, text="평창 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_22_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_22_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_22_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_22_battle, text="돌아가기", command=region_22_battle.destroy)
            back_button.pack()
            button_states["region_23_button"] = "active"
            button_states["region_22_button"] = "disabled"
            region_22_button.config(state=button_states["region_22_button"])
            region_23_button.config(state=button_states["region_23_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_22_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_22_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_22_battle, text="돌아가기", command=region_22_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_22_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_22_battle.after(1250, perform_ally_attack)

def region_23(region_23_button, region_24_button):
    global military
    global enemy_military
    global region
    enemy_military = 250000

    region_23_battle = tk.Toplevel()
    region_23_battle.title("홍천 전투")
    region_23_battle.geometry("800x600")

    label = tk.Label(region_23_battle, text="홍천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_23_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_23_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_23_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_23_battle, text="돌아가기", command=region_23_battle.destroy)
            back_button.pack()
            button_states["region_24_button"] = "active"
            button_states["region_23_button"] = "disabled"
            region_23_button.config(state=button_states["region_23_button"])
            region_24_button.config(state=button_states["region_24_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_23_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_23_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_23_battle, text="돌아가기", command=region_23_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_23_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_23_battle.after(1250, perform_ally_attack)

def region_24(region_24_button, region_25_button):
    global military
    global enemy_military
    global region
    enemy_military = 290000

    region_24_battle = tk.Toplevel()
    region_24_battle.title("춘천 전투")
    region_24_battle.geometry("800x600")

    label = tk.Label(region_24_battle, text="춘천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_24_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_24_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_24_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_24_battle, text="돌아가기", command=region_24_battle.destroy)
            back_button.pack()
            button_states["region_25_button"] = "active"
            button_states["region_24_button"] = "disabled"
            region_24_button.config(state=button_states["region_24_button"])
            region_25_button.config(state=button_states["region_25_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_24_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_24_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_24_battle, text="돌아가기", command=region_24_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_24_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_24_battle.after(1250, perform_ally_attack)

def region_25(region_25_button, region_26_button):
    global military
    global enemy_military
    global region
    enemy_military = 335000

    region_25_battle = tk.Toplevel()
    region_25_battle.title("강릉 전투")
    region_25_battle.geometry("800x600")

    label = tk.Label(region_25_battle, text="강릉 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_25_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_25_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_25_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_25_battle, text="돌아가기", command=region_25_battle.destroy)
            back_button.pack()
            button_states["region_26_button"] = "active"
            button_states["region_25_button"] = "disabled"
            region_25_button.config(state=button_states["region_25_button"])
            region_26_button.config(state=button_states["region_26_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_25_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_25_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_25_battle, text="돌아가기", command=region_25_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_25_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_25_battle.after(1250, perform_ally_attack)

def region_26(region_26_button, region_27_button):
    global military
    global enemy_military
    global region
    enemy_military = 390000

    region_26_battle = tk.Toplevel()
    region_26_battle.title("속초 전투")
    region_26_battle.geometry("800x600")

    label = tk.Label(region_26_battle, text="속초 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_26_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_26_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_26_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_26_battle, text="돌아가기", command=region_26_battle.destroy)
            back_button.pack()
            button_states["region_27_button"] = "active"
            button_states["region_26_button"] = "disabled"
            region_26_button.config(state=button_states["region_26_button"])
            region_27_button.config(state=button_states["region_27_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_26_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_26_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_26_battle, text="돌아가기", command=region_26_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_26_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_26_battle.after(1250, perform_ally_attack)

def region_27(region_27_button, region_28_button):
    global military
    global enemy_military
    global region
    enemy_military = 450000

    region_27_battle = tk.Toplevel()
    region_27_battle.title("고성 전투")
    region_27_battle.geometry("800x600")

    label = tk.Label(region_27_battle, text="고성 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_27_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_27_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_27_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_27_battle, text="돌아가기", command=region_27_battle.destroy)
            back_button.pack()
            button_states["region_28_button"] = "active"
            button_states["region_27_button"] = "disabled"
            region_27_button.config(state=button_states["region_27_button"])
            region_28_button.config(state=button_states["region_28_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_27_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_27_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_27_battle, text="돌아가기", command=region_27_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_27_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_27_battle.after(1250, perform_ally_attack)

def region_28(region_28_button, region_29_button):
    global military
    global enemy_military
    global region
    enemy_military = 520000

    region_28_battle = tk.Toplevel()
    region_28_battle.title("철원 전투")
    region_28_battle.geometry("800x600")

    label = tk.Label(region_28_battle, text="철원 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_28_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_28_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_28_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_28_battle, text="돌아가기", command=region_28_battle.destroy)
            back_button.pack()
            button_states["region_29_button"] = "active"
            button_states["region_28_button"] = "disabled"
            region_28_button.config(state=button_states["region_28_button"])
            region_29_button.config(state=button_states["region_29_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_28_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_28_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_28_battle, text="돌아가기", command=region_28_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_28_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_28_battle.after(1250, perform_ally_attack)

def region_29(region_29_button, region_30_button):
    global military
    global enemy_military
    global region
    enemy_military = 600000

    region_29_battle = tk.Toplevel()
    region_29_battle.title("고산 전투")
    region_29_battle.geometry("800x600")

    label = tk.Label(region_29_battle, text="고산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_29_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_29_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_29_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_29_battle, text="돌아가기", command=region_29_battle.destroy)
            back_button.pack()
            button_states["region_30_button"] = "active"
            button_states["region_29_button"] = "disabled"
            region_29_button.config(state=button_states["region_29_button"])
            region_30_button.config(state=button_states["region_30_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_29_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_29_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_29_battle, text="돌아가기", command=region_29_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_29_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_29_battle.after(1250, perform_ally_attack)

def region_30(region_30_button, region_31_button):
    global military
    global enemy_military
    global region
    enemy_military = 690000

    region_30_battle = tk.Toplevel()
    region_30_battle.title("통천 전투")
    region_30_battle.geometry("800x600")

    label = tk.Label(region_30_battle, text="통천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_30_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_30_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_30_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_30_battle, text="돌아가기", command=region_30_battle.destroy)
            back_button.pack()
            button_states["region_31_button"] = "active"
            button_states["region_30_button"] = "disabled"
            region_30_button.config(state=button_states["region_30_button"])
            region_31_button.config(state=button_states["region_31_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_30_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_30_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_30_battle, text="돌아가기", command=region_30_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_30_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_30_battle.after(1250, perform_ally_attack)

def region_31(region_31_button, region_32_button):
    global military
    global enemy_military
    global region
    enemy_military = 850000

    region_31_battle = tk.Toplevel()
    region_31_battle.title("원산 전투")
    region_31_battle.geometry("800x600")

    label = tk.Label(region_31_battle, text="원산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_31_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_31_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_31_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_31_battle, text="돌아가기", command=region_31_battle.destroy)
            back_button.pack()
            button_states["region_32_button"] = "active"
            button_states["region_31_button"] = "disabled"
            region_31_button.config(state=button_states["region_31_button"])
            region_32_button.config(state=button_states["region_32_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_31_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_31_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_31_battle, text="돌아가기", command=region_31_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_31_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_31_battle.after(1250, perform_ally_attack)

def region_32(region_32_button, region_33_button):
    global military
    global enemy_military
    global region
    enemy_military = 950000

    region_32_battle = tk.Toplevel()
    region_32_battle.title("곡산 전투")
    region_32_battle.geometry("800x600")

    label = tk.Label(region_32_battle, text="곡산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_32_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_32_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_32_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_32_battle, text="돌아가기", command=region_32_battle.destroy)
            back_button.pack()
            button_states["region_33_button"] = "active"
            button_states["region_32_button"] = "disabled"
            region_32_button.config(state=button_states["region_32_button"])
            region_33_button.config(state=button_states["region_33_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_32_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_32_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_32_battle, text="돌아가기", command=region_32_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_32_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_32_battle.after(1250, perform_ally_attack)

def region_33(region_33_button, region_34_button):
    global military
    global enemy_military
    global region
    enemy_military = 1075000

    region_33_battle = tk.Toplevel()
    region_33_battle.title("연산 전투")
    region_33_battle.geometry("800x600")

    label = tk.Label(region_33_battle, text="연산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_33_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_33_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_33_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_33_battle, text="돌아가기", command=region_33_battle.destroy)
            back_button.pack()
            button_states["region_34_button"] = "active"
            button_states["region_33_button"] = "disabled"
            region_33_button.config(state=button_states["region_33_button"])
            region_34_button.config(state=button_states["region_34_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_33_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_33_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_33_battle, text="돌아가기", command=region_33_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_33_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_33_battle.after(1250, perform_ally_attack)

def region_34(region_34_button, region_35_button):
    global military
    global enemy_military
    global region
    enemy_military = 1225000

    region_34_battle = tk.Toplevel()
    region_34_battle.title("평양 전투")
    region_34_battle.geometry("800x600")

    label = tk.Label(region_34_battle, text="평양 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_34_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_34_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_34_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_34_battle, text="돌아가기", command=region_34_battle.destroy)
            back_button.pack()
            button_states["region_35_button"] = "active"
            button_states["region_34_button"] = "disabled"
            region_34_button.config(state=button_states["region_34_button"])
            region_35_button.config(state=button_states["region_35_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_34_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_34_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_34_battle, text="돌아가기", command=region_34_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_34_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_34_battle.after(1250, perform_ally_attack)

def region_35(region_35_button, region_36_button):
    global military
    global enemy_military
    global region
    enemy_military = 1400000

    region_35_battle = tk.Toplevel()
    region_35_battle.title("남포 전투")
    region_35_battle.geometry("800x600")

    label = tk.Label(region_35_battle, text="남포 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_35_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_35_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_35_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_35_battle, text="돌아가기", command=region_35_battle.destroy)
            back_button.pack()
            button_states["region_36_button"] = "active"
            button_states["region_35_button"] = "disabled"
            region_35_button.config(state=button_states["region_35_button"])
            region_36_button.config(state=button_states["region_36_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_35_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_35_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_35_battle, text="돌아가기", command=region_35_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_35_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_35_battle.after(1250, perform_ally_attack)

def region_36(region_36_button, region_37_button):
    global military
    global enemy_military
    global region
    enemy_military = 1600000

    region_36_battle = tk.Toplevel()
    region_36_battle.title("순천 전투")
    region_36_battle.geometry("800x600")

    label = tk.Label(region_36_battle, text="순천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_36_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_36_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_36_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_36_battle, text="돌아가기", command=region_36_battle.destroy)
            back_button.pack()
            button_states["region_37_button"] = "active"
            button_states["region_36_button"] = "disabled"
            region_36_button.config(state=button_states["region_36_button"])
            region_37_button.config(state=button_states["region_37_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_36_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_36_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_36_battle, text="돌아가기", command=region_36_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_36_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_36_battle.after(1250, perform_ally_attack)

def region_37(region_37_button, region_38_button):
    global military
    global enemy_military
    global region
    enemy_military = 1850000

    region_37_battle = tk.Toplevel()
    region_37_battle.title("라오산 전투")
    region_37_battle.geometry("800x600")

    label = tk.Label(region_37_battle, text="라오산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_37_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_37_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_37_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_37_battle, text="돌아가기", command=region_37_battle.destroy)
            back_button.pack()
            button_states["region_38_button"] = "active"
            button_states["region_37_button"] = "disabled"
            region_37_button.config(state=button_states["region_37_button"])
            region_38_button.config(state=button_states["region_38_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_37_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_37_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_37_battle, text="돌아가기", command=region_37_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_37_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_37_battle.after(1250, perform_ally_attack)

def region_38(region_38_button, region_39_button):
    global military
    global enemy_military
    global region
    enemy_military = 2100000

    region_38_battle = tk.Toplevel()
    region_38_battle.title("청양 전투")
    region_38_battle.geometry("800x600")

    label = tk.Label(region_38_battle, text="청양 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_38_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_38_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_38_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_38_battle, text="돌아가기", command=region_38_battle.destroy)
            back_button.pack()
            button_states["region_39_button"] = "active"
            button_states["region_38_button"] = "disabled"
            region_38_button.config(state=button_states["region_38_button"])
            region_39_button.config(state=button_states["region_39_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_38_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_38_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_38_battle, text="돌아가기", command=region_38_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_38_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_38_battle.after(1250, perform_ally_attack)

def region_39(region_39_button, region_40_button):
    global military
    global enemy_military
    global region
    enemy_military = 2400000

    region_39_battle = tk.Toplevel()
    region_39_battle.title("리창 전투")
    region_39_battle.geometry("800x600")

    label = tk.Label(region_39_battle, text="리창 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_39_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_39_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_39_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_39_battle, text="돌아가기", command=region_39_battle.destroy)
            back_button.pack()
            button_states["region_40_button"] = "active"
            button_states["region_39_button"] = "disabled"
            region_39_button.config(state=button_states["region_39_button"])
            region_40_button.config(state=button_states["region_40_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_39_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_39_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_39_battle, text="돌아가기", command=region_39_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_39_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_39_battle.after(1250, perform_ally_attack)

def region_40(region_40_button, region_41_button):
    global military
    global enemy_military
    global region
    enemy_military = 2750000

    region_40_battle = tk.Toplevel()
    region_40_battle.title("나호드카 전투")
    region_40_battle.geometry("800x600")

    label = tk.Label(region_40_battle, text="나호드카 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_40_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_40_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_40_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_40_battle, text="돌아가기", command=region_40_battle.destroy)
            back_button.pack()
            button_states["region_41_button"] = "active"
            button_states["region_40_button"] = "disabled"
            region_40_button.config(state=button_states["region_40_button"])
            region_41_button.config(state=button_states["region_41_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_40_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_40_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_40_battle, text="돌아가기", command=region_40_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_40_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_40_battle.after(1250, perform_ally_attack)

def region_41(region_41_button, region_42_button):
    global military
    global enemy_military
    global region
    enemy_military = 3250000

    region_41_battle = tk.Toplevel()
    region_41_battle.title("블라디보스토크 전투")
    region_41_battle.geometry("800x600")

    label = tk.Label(region_41_battle, text="블라디보스토크 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_41_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_41_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_41_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_41_battle, text="돌아가기", command=region_41_battle.destroy)
            back_button.pack()
            button_states["region_42_button"] = "active"
            button_states["region_41_button"] = "disabled"
            region_41_button.config(state=button_states["region_41_button"])
            region_42_button.config(state=button_states["region_42_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_41_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_41_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_41_battle, text="돌아가기", command=region_41_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_41_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_41_battle.after(1250, perform_ally_attack)

def region_42(region_42_button, region_43_button):
    global military
    global enemy_military
    global region
    enemy_military = 3800000

    region_42_battle = tk.Toplevel()
    region_42_battle.title("우수리스크 전투")
    region_42_battle.geometry("800x600")

    label = tk.Label(region_42_battle, text="우수리스크 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_42_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_42_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_42_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_42_battle, text="돌아가기", command=region_42_battle.destroy)
            back_button.pack()
            button_states["region_43_button"] = "active"
            button_states["region_42_button"] = "disabled"
            region_42_button.config(state=button_states["region_42_button"])
            region_43_button.config(state=button_states["region_43_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_42_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_42_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_42_battle, text="돌아가기", command=region_42_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_42_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_42_battle.after(1250, perform_ally_attack)

def region_43(region_43_button, region_44_button):
    global military
    global enemy_military
    global region
    enemy_military = 4400000

    region_43_battle = tk.Toplevel()
    region_43_battle.title("장진 전투")
    region_43_battle.geometry("800x600")

    label = tk.Label(region_43_battle, text="장진 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_43_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_43_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_43_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_43_battle, text="돌아가기", command=region_43_battle.destroy)
            back_button.pack()
            button_states["region_44_button"] = "active"
            button_states["region_43_button"] = "disabled"
            region_43_button.config(state=button_states["region_43_button"])
            region_44_button.config(state=button_states["region_44_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_43_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_43_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_43_battle, text="돌아가기", command=region_43_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_43_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_43_battle.after(1250, perform_ally_attack)

def region_44(region_44_button, region_45_button):
    global military
    global enemy_military
    global region
    enemy_military = 5000000

    region_44_battle = tk.Toplevel()
    region_44_battle.title("강계 전투")
    region_44_battle.geometry("800x600")

    label = tk.Label(region_44_battle, text="강계 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_44_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_44_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_44_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_44_battle, text="돌아가기", command=region_44_battle.destroy)
            back_button.pack()
            button_states["region_45_button"] = "active"
            button_states["region_44_button"] = "disabled"
            region_44_button.config(state=button_states["region_44_button"])
            region_45_button.config(state=button_states["region_45_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_44_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_44_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_44_battle, text="돌아가기", command=region_44_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_44_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_44_battle.after(1250, perform_ally_attack)

def region_45(region_45_button, region_46_button):
    global military
    global enemy_military
    global region
    enemy_military = 5700000

    region_45_battle = tk.Toplevel()
    region_45_battle.title("낭림 전투")
    region_45_battle.geometry("800x600")

    label = tk.Label(region_45_battle, text="낭림 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_45_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_45_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_45_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_45_battle, text="돌아가기", command=region_45_battle.destroy)
            back_button.pack()
            button_states["region_46_button"] = "active"
            button_states["region_45_button"] = "disabled"
            region_45_button.config(state=button_states["region_45_button"])
            region_46_button.config(state=button_states["region_46_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_45_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_45_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_45_battle, text="돌아가기", command=region_45_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_45_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_45_battle.after(1250, perform_ally_attack)

def region_46(region_46_button, region_47_button):
    global military
    global enemy_military
    global region
    enemy_military = 6450000

    region_46_battle = tk.Toplevel()
    region_46_battle.title("자성 전투")
    region_46_battle.geometry("800x600")

    label = tk.Label(region_46_battle, text="자성 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_46_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_46_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_46_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_46_battle, text="돌아가기", command=region_46_battle.destroy)
            back_button.pack()
            button_states["region_47_button"] = "active"
            button_states["region_46_button"] = "disabled"
            region_46_button.config(state=button_states["region_46_button"])
            region_47_button.config(state=button_states["region_47_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_46_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_46_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_46_battle, text="돌아가기", command=region_46_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_46_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_46_battle.after(1250, perform_ally_attack)

def region_47(region_47_button, region_48_button):
    global military
    global enemy_military
    global region
    enemy_military = 7200000

    region_47_battle = tk.Toplevel()
    region_47_battle.title("갑산 전투")
    region_47_battle.geometry("800x600")

    label = tk.Label(region_47_battle, text="갑산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_47_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_47_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_47_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_47_battle, text="돌아가기", command=region_47_battle.destroy)
            back_button.pack()
            button_states["region_48_button"] = "active"
            button_states["region_47_button"] = "disabled"
            region_47_button.config(state=button_states["region_47_button"])
            region_48_button.config(state=button_states["region_48_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_47_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_47_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_47_battle, text="돌아가기", command=region_47_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_47_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_47_battle.after(1250, perform_ally_attack)

def region_48(region_48_button, region_49_button):
    global military
    global enemy_military
    global region
    enemy_military = 8200000

    region_48_battle = tk.Toplevel()
    region_48_battle.title("함흥 전투")
    region_48_battle.geometry("800x600")

    label = tk.Label(region_48_battle, text="함흥 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_48_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_48_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_48_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_48_battle, text="돌아가기", command=region_48_battle.destroy)
            back_button.pack()
            button_states["region_49_button"] = "active"
            button_states["region_48_button"] = "disabled"
            region_48_button.config(state=button_states["region_48_button"])
            region_49_button.config(state=button_states["region_49_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_48_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_48_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_48_battle, text="돌아가기", command=region_48_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_48_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_48_battle.after(1250, perform_ally_attack)

def region_49(region_49_button, region_50_button):
    global military
    global enemy_military
    global region
    enemy_military = 9200000

    region_49_battle = tk.Toplevel()
    region_49_battle.title("단천 전투")
    region_49_battle.geometry("800x600")

    label = tk.Label(region_49_battle, text="단천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_49_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_49_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_49_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_49_battle, text="돌아가기", command=region_49_battle.destroy)
            back_button.pack()
            button_states["region_50_button"] = "active"
            button_states["region_49_button"] = "disabled"
            region_49_button.config(state=button_states["region_49_button"])
            region_50_button.config(state=button_states["region_50_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_49_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_49_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_49_battle, text="돌아가기", command=region_49_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_49_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_49_battle.after(1250, perform_ally_attack)

def region_50(region_50_button, region_51_button):
    global military
    global enemy_military
    global region
    enemy_military = 10300000

    region_50_battle = tk.Toplevel()
    region_50_battle.title("혜산 전투")
    region_50_battle.geometry("800x600")

    label = tk.Label(region_50_battle, text="혜산 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_50_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_50_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_50_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_50_battle, text="돌아가기", command=region_50_battle.destroy)
            back_button.pack()
            button_states["region_51_button"] = "active"
            button_states["region_50_button"] = "disabled"
            region_50_button.config(state=button_states["region_50_button"])
            region_51_button.config(state=button_states["region_51_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_50_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_50_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_50_battle, text="돌아가기", command=region_50_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_50_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_50_battle.after(1250, perform_ally_attack)

def region_51(region_51_button, region_52_button):
    global military
    global enemy_military
    global region
    enemy_military = 11500000

    region_51_battle = tk.Toplevel()
    region_51_battle.title("백암 전투")
    region_51_battle.geometry("800x600")

    label = tk.Label(region_51_battle, text="백암 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_51_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_51_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_51_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_51_battle, text="돌아가기", command=region_51_battle.destroy)
            back_button.pack()
            button_states["region_52_button"] = "active"
            button_states["region_51_button"] = "disabled"
            region_51_button.config(state=button_states["region_51_button"])
            region_52_button.config(state=button_states["region_52_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_51_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_51_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_51_battle, text="돌아가기", command=region_51_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_51_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_51_battle.after(1250, perform_ally_attack)

def region_52(region_52_button, region_53_button):
    global military
    global enemy_military
    global region
    enemy_military = 12800000

    region_52_battle = tk.Toplevel()
    region_52_battle.title("삼지연 전투")
    region_52_battle.geometry("800x600")

    label = tk.Label(region_52_battle, text="삼지연 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_52_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_52_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_52_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_52_battle, text="돌아가기", command=region_52_battle.destroy)
            back_button.pack()
            button_states["region_53_button"] = "active"
            button_states["region_52_button"] = "disabled"
            region_52_button.config(state=button_states["region_52_button"])
            region_53_button.config(state=button_states["region_53_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_52_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_52_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_52_battle, text="돌아가기", command=region_52_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_52_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_52_battle.after(1250, perform_ally_attack)

def region_53(region_53_button, region_54_button):
    global military
    global enemy_military
    global region
    enemy_military = 14300000

    region_53_battle = tk.Toplevel()
    region_53_battle.title("나선 전투")
    region_53_battle.geometry("800x600")

    label = tk.Label(region_53_battle, text="나선 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_53_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_53_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_53_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_53_battle, text="돌아가기", command=region_53_battle.destroy)
            back_button.pack()
            button_states["region_54_button"] = "active"
            button_states["region_53_button"] = "disabled"
            region_53_button.config(state=button_states["region_53_button"])
            region_54_button.config(state=button_states["region_54_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_53_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_53_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_53_battle, text="돌아가기", command=region_53_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_53_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_53_battle.after(1250, perform_ally_attack)

def region_54(region_54_button, region_55_button):
    global military
    global enemy_military
    global region
    enemy_military = 17000000

    region_54_battle = tk.Toplevel()
    region_54_battle.title("청진 전투")
    region_54_battle.geometry("800x600")

    label = tk.Label(region_54_battle, text="청진 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_54_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_54_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_54_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_54_battle, text="돌아가기", command=region_54_battle.destroy)
            back_button.pack()
            button_states["region_55_button"] = "active"
            button_states["region_54_button"] = "disabled"
            region_54_button.config(state=button_states["region_54_button"])
            region_55_button.config(state=button_states["region_55_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_54_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_54_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_54_battle, text="돌아가기", command=region_54_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_54_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_54_battle.after(1250, perform_ally_attack)

def region_55(region_55_button, region_57_button):
    global military
    global enemy_military
    global region
    enemy_military = 20000000

    region_55_battle = tk.Toplevel()
    region_55_battle.title("사리원 전투")
    region_55_battle.geometry("800x600")

    label = tk.Label(region_55_battle, text="사리원 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_55_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_55_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_55_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_55_battle, text="돌아가기", command=region_55_battle.destroy)
            back_button.pack()
            button_states["region_57_button"] = "active"
            button_states["region_55_button"] = "disabled"
            region_55_button.config(state=button_states["region_55_button"])
            region_57_button.config(state=button_states["region_57_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_55_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_55_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_55_battle, text="돌아가기", command=region_55_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_55_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_55_battle.after(1250, perform_ally_attack)

def region_56(region_56_button, region_57_button):
    global military
    global enemy_military
    global region
    enemy_military = 24000000

    region_56_battle = tk.Toplevel()
    region_56_battle.title("해주 전투")
    region_56_battle.geometry("800x600")

    label = tk.Label(region_56_battle, text="해주 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_56_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_56_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_56_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_56_battle, text="돌아가기", command=region_56_battle.destroy)
            back_button.pack()
            button_states["region_57_button"] = "active"
            button_states["region_56_button"] = "disabled"
            region_56_button.config(state=button_states["region_56_button"])
            region_57_button.config(state=button_states["region_57_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_56_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_56_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_56_battle, text="돌아가기", command=region_56_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_56_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_56_battle.after(1250, perform_ally_attack)

def region_57(region_57_button, region_58_button):
    global military
    global enemy_military
    global region
    enemy_military = 29000000

    region_57_battle = tk.Toplevel()
    region_57_battle.title("연천 전투")
    region_57_battle.geometry("800x600")

    label = tk.Label(region_57_battle, text="연천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_57_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_57_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_57_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_57_battle, text="돌아가기", command=region_57_battle.destroy)
            back_button.pack()
            button_states["region_58_button"] = "active"
            button_states["region_57_button"] = "disabled"
            region_57_button.config(state=button_states["region_57_button"])
            region_58_button.config(state=button_states["region_58_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_57_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_57_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_57_battle, text="돌아가기", command=region_57_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_57_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_57_battle.after(1250, perform_ally_attack)

def region_58(region_58_button, region_59_button):
    global military
    global enemy_military
    global region
    enemy_military = 35000000

    region_58_battle = tk.Toplevel()
    region_58_battle.title("개성 전투")
    region_58_battle.geometry("800x600")

    label = tk.Label(region_58_battle, text="개성 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_58_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_58_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_58_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_58_battle, text="돌아가기", command=region_58_battle.destroy)
            back_button.pack()
            button_states["region_59_button"] = "active"
            button_states["region_58_button"] = "disabled"
            region_58_button.config(state=button_states["region_58_button"])
            region_59_button.config(state=button_states["region_59_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_58_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_58_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_58_battle, text="돌아가기", command=region_58_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_58_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_58_battle.after(1250, perform_ally_attack)

def region_59(region_59_button, region_60_button):
    global military
    global enemy_military
    global region
    enemy_military = 42000000

    region_59_battle = tk.Toplevel()
    region_59_battle.title("이천 전투")
    region_59_battle.geometry("800x600")

    label = tk.Label(region_59_battle, text="이천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_59_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_59_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_59_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_59_battle, text="돌아가기", command=region_59_battle.destroy)
            back_button.pack()
            button_states["region_60_button"] = "active"
            button_states["region_59_button"] = "disabled"
            region_59_button.config(state=button_states["region_59_button"])
            region_60_button.config(state=button_states["region_60_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_59_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_59_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_59_battle, text="돌아가기", command=region_59_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_59_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_59_battle.after(1250, perform_ally_attack)

def region_60(region_60_button, region_61_button):
    global military
    global enemy_military
    global region
    enemy_military = 50000000

    region_60_battle = tk.Toplevel()
    region_60_battle.title("용인 전투")
    region_60_battle.geometry("800x600")

    label = tk.Label(region_60_battle, text="용인 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_60_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_60_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_60_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_60_battle, text="돌아가기", command=region_60_battle.destroy)
            back_button.pack()
            button_states["region_61_button"] = "active"
            button_states["region_60_button"] = "disabled"
            region_60_button.config(state=button_states["region_60_button"])
            region_61_button.config(state=button_states["region_61_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_60_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_60_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_60_battle, text="돌아가기", command=region_60_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_60_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_60_battle.after(1250, perform_ally_attack)

def region_61(region_61_button, region_62_button):
    global military
    global enemy_military
    global region
    enemy_military = 59000000

    region_61_battle = tk.Toplevel()
    region_61_battle.title("수원 전투")
    region_61_battle.geometry("800x600")

    label = tk.Label(region_61_battle, text="수원 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_61_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_61_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_61_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_61_battle, text="돌아가기", command=region_61_battle.destroy)
            back_button.pack()
            button_states["region_62_button"] = "active"
            button_states["region_61_button"] = "disabled"
            region_61_button.config(state=button_states["region_61_button"])
            region_62_button.config(state=button_states["region_62_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_61_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_61_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_61_battle, text="돌아가기", command=region_61_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_61_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_61_battle.after(1250, perform_ally_attack)

def region_62(region_62_button, region_63_button):
    global military
    global enemy_military
    global region
    enemy_military = 69000000

    region_62_battle = tk.Toplevel()
    region_62_battle.title("인천 전투")
    region_62_battle.geometry("800x600")

    label = tk.Label(region_62_battle, text="인천 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_62_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_62_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_62_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_62_battle, text="돌아가기", command=region_62_battle.destroy)
            back_button.pack()
            button_states["region_63_button"] = "active"
            button_states["region_62_button"] = "disabled"
            region_62_button.config(state=button_states["region_62_button"])
            region_63_button.config(state=button_states["region_63_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_62_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_62_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_62_battle, text="돌아가기", command=region_62_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_62_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_62_battle.after(1250, perform_ally_attack)

def region_63(region_63_button):
    global military
    global enemy_military
    global region
    enemy_military = 90000000

    region_63_battle = tk.Toplevel()
    region_63_battle.title("서울 전투")
    region_63_battle.geometry("800x600")

    label = tk.Label(region_63_battle, text="서울 전투.")
    label.pack()

    # 초기 아군과 적의 전투력을 표시하는 Label 위젯 생성
    initial_military_label = tk.Label(region_63_battle, text=f"아군 군사력 : {int(military)}")
    initial_military_label.pack()

    initial_combat_power_label = tk.Label(region_63_battle, text=f"적 전투력 : {int(enemy_military)}")
    initial_combat_power_label.pack()

    # 아군 공격 함수 정의
    def perform_ally_attack():
        global enemy_military, region
        enemy_military = max(0, enemy_military - (military * 0.1))
        initial_combat_power_label.config(text=f"적 전투력 : {int(enemy_military)}")

        if enemy_military <= 0:
            region += 1
            result_label = tk.Label(region_63_battle, text="전투에서 승리 했습니다!")
            result_label.pack()
            back_button = tk.Button(region_63_battle, text="돌아가기", command=region_63_battle.destroy)
            back_button.pack()
            button_states["region_64_button"] = "active"
            button_states["region_63_button"] = "disabled"
            region_63_button.config(state=button_states["region_63_button"])

            update_military_label()
            update_combat_power_label()
            update_region_label()
        else:
            # 1.25초 후에 적이 공격하도록 설정
            region_63_battle.after(1250, perform_enemy_attack)

    # 적 공격 함수 정의
    def perform_enemy_attack():
        global military
        military = max(0, military - (enemy_military * 0.1))
        initial_military_label.config(text=f"아군 군사력 : {int(military)}")

        if military <= 0:
            military = 0
            result_label = tk.Label(region_63_battle, text="전투에서 패배 했습니다.")
            result_label.pack()
            back_button = tk.Button(region_63_battle, text="돌아가기", command=region_63_battle.destroy)
            back_button.pack()
            update_military_label()
            update_combat_power_label()
        else:
            # 1.25초 후에 아군이 다시 공격하도록 설정
            region_63_battle.after(1250, perform_ally_attack)

    # 1.25초 후에 아군 공격 시작
    region_63_battle.after(1250, perform_ally_attack)
def prepare_for_battle_gui():
    # Tkinter 윈도우 생성
    prepare_for_battle_window = tk.Toplevel()
    prepare_for_battle_window.title("전투 준비")
    prepare_for_battle_window.geometry("1280x720")

    # 그룹박스 생성
    region_group = tk.LabelFrame(prepare_for_battle_window, text="진출할 지역 선택")
    region_group.pack(fill="both", expand="yes", padx=10, pady=10)

    update_region(region_group, "choice")

    back_button = tk.Button(prepare_for_battle_window, text="뒤로가기", command=prepare_for_battle_window.destroy)
    back_button.pack()

button_states = {
    "region_1_button": "active",
    "region_2_button": "disabled",
    "region_3_button": "disabled",
    "region_4_button": "disabled",
    "region_5_button": "disabled",
    "region_6_button": "disabled",
    "region_7_button": "disabled",
    "region_8_button": "disabled",
    "region_9_button": "disabled",
    "region_10_button": "disabled",
    "region_11_button": "disabled",
    "region_12_button": "disabled",
    "region_13_button": "disabled",
    "region_14_button": "disabled",
    "region_15_button": "disabled",
    "region_16_button": "disabled",
    "region_17_button": "disabled",
    "region_18_button": "disabled",
    "region_19_button": "disabled",
    "region_20_button": "disabled",
    "region_21_button": "disabled",
    "region_22_button": "disabled",
    "region_23_button": "disabled",
    "region_24_button": "disabled",
    "region_25_button": "disabled",
    "region_26_button": "disabled",
    "region_27_button": "disabled",
    "region_28_button": "disabled",
    "region_29_button": "disabled",
    "region_30_button": "disabled",
    "region_31_button": "disabled",
    "region_32_button": "disabled",
    "region_33_button": "disabled",
    "region_34_button": "disabled",
    "region_35_button": "disabled",
    "region_36_button": "disabled",
    "region_37_button": "disabled",
    "region_38_button": "disabled",
    "region_39_button": "disabled",
    "region_40_button": "disabled",
    "region_41_button": "disabled",
    "region_42_button": "disabled",
    "region_43_button": "disabled",
    "region_44_button": "disabled",
    "region_45_button": "disabled",
    "region_46_button": "disabled",
    "region_47_button": "disabled",
    "region_48_button": "disabled",
    "region_49_button": "disabled",
    "region_50_button": "disabled",
    "region_51_button": "disabled",
    "region_52_button": "disabled",
    "region_53_button": "disabled",
    "region_54_button": "disabled",
    "region_55_button": "disabled",
    "region_56_button": "disabled",
    "region_57_button": "disabled",
    "region_58_button": "disabled",
    "region_59_button": "disabled",
    "region_60_button": "disabled",
    "region_61_button": "disabled",
    "region_62_button": "disabled",
    "region_63_button": "disabled",
}

def update_region(region_group, region_type):
    # 기존 버튼들을 삭제
    for widget in region_group.winfo_children():
        widget.destroy()

    # 메인 버튼일 경우
    if region_type == "choice":
        # 각 버튼에 대한 기능 설정
        tax_button = tk.Button(region_group, text="한반도 남부", command=lambda: update_region(region_group, "Sector_A"))
        tax_button.pack(side="left", padx=5, pady=5)

        military_button = tk.Button(region_group, text="한반도 중부", command=lambda: update_region(region_group, "Sector_B"))
        military_button.pack(side="left", padx=5, pady=5)

        research_button = tk.Button(region_group, text="중국", command=lambda: update_region(region_group, "Sector_C"))
        research_button.pack(side="left", padx=5, pady=5)

        facility_button = tk.Button(region_group, text="러시아", command=lambda: update_region(region_group, "Sector_D"))
        facility_button.pack(side="left", padx=5, pady=5)

        battle_button = tk.Button(region_group, text="한반도 북부", command=lambda: update_region(region_group, "Sector_E"))
        battle_button.pack(side="left", padx=5, pady=5)

        battle_button = tk.Button(region_group, text="서울 및 경기도", command=lambda: update_region(region_group, "Sector_F"))
        battle_button.pack(side="left", padx=5, pady=5)

    elif region_type == "Sector_A":
        region_1_button = tk.Button(region_group, text="해남\n전투력 : 200", command=lambda: region_1(region_1_button, region_2_button), state=button_states["region_1_button"])
        region_1_button.grid(row=11,column=1, padx=5, pady=5)
        region_2_button = tk.Button(region_group, text="여수\n전투력 : 500", command=lambda: region_2(region_2_button, region_3_button), state=button_states["region_2_button"])
        region_2_button.grid(row=11,column=2, padx=5, pady=5)
        region_3_button = tk.Button(region_group, text="광주\n전투력 : 1000", command=lambda: region_3(region_3_button, region_4_button), state=button_states["region_3_button"])
        region_3_button.grid(row=9,column=2, padx=5, pady=5)
        region_4_button = tk.Button(region_group, text="남원\n전투력 : 2000", command=lambda: region_4(region_4_button, region_5_button), state=button_states["region_4_button"])
        region_4_button.grid(row=8,column=3, padx=5, pady=5)
        region_5_button = tk.Button(region_group, text="전주\n전투력 : 3200", command=lambda: region_5(region_5_button, region_6_button), state=button_states["region_5_button"])
        region_5_button.grid(row=6,column=2, padx=5, pady=5)
        region_6_button = tk.Button(region_group, text="군산\n전투력 : 4500", command=lambda: region_6(region_6_button, region_7_button), state=button_states["region_6_button"])
        region_6_button.grid(row=7,column=5, padx=5, pady=5)
        region_7_button = tk.Button(region_group, text="진주\n전투력 : 5800", command=lambda: region_7(region_7_button, region_8_button), state=button_states["region_7_button"])
        region_7_button.grid(row=10,column=4, padx=5, pady=5)
        region_8_button = tk.Button(region_group, text="합천\n전투력 : 7000", command=lambda: region_8(region_8_button, region_9_button), state=button_states["region_8_button"])
        region_8_button.grid(row=9,column=4, padx=5, pady=5)
        region_9_button = tk.Button(region_group, text="울산\n전투력 : 9000", command=lambda: region_9(region_9_button, region_10_button), state=button_states["region_9_button"])
        region_9_button.grid(row=7,column=6, padx=5, pady=5)
        region_10_button = tk.Button(region_group, text="부산\n전투력 : 11000", command=lambda: region_10(region_10_button, region_11_button), state=button_states["region_10_button"])
        region_10_button.grid(row=8,column=6, padx=5, pady=5)
        region_11_button = tk.Button(region_group, text="논산\n전투력 : 15000", command=lambda: region_11(region_11_button, region_12_button), state=button_states["region_11_button"])
        region_11_button.grid(row=5,column=2, padx=5, pady=5)
        region_12_button = tk.Button(region_group, text="세종\n전투력 : 20000", command=lambda: region_12(region_12_button, region_13_button), state=button_states["region_12_button"])
        region_12_button.grid(row=4,column=2, padx=5, pady=5)
        region_13_button = tk.Button(region_group, text="포항\n전투력 : 28000", command=lambda: region_13(region_13_button, region_14_button), state=button_states["region_13_button"])
        region_13_button.grid(row=6,column=6, padx=5, pady=5)
        region_14_button = tk.Button(region_group, text="영덕\n전투력 : 40000", command=lambda: region_14(region_14_button, region_15_button), state=button_states["region_14_button"])
        region_14_button.grid(row=5,column=6, padx=5, pady=5)
        region_15_button = tk.Button(region_group, text="안동\n전투력 : 52000", command=lambda: region_15(region_15_button, region_16_button), state=button_states["region_15_button"])
        region_15_button.grid(row=5,column=5, padx=5, pady=5)
        region_16_button = tk.Button(region_group, text="김천\n전투력 : 65000", command=lambda: region_16(region_16_button, region_17_button), state=button_states["region_16_button"])
        region_16_button.grid(row=5,column=4, padx=5, pady=5)
        region_17_button = tk.Button(region_group, text="대구\n전투력 : 80000", command=lambda: region_17(region_17_button, region_18_button), state=button_states["region_17_button"])
        region_17_button.grid(row=4,column=6, padx=5, pady=5)
        region_18_button = tk.Button(region_group, text="청주\n전투력 : 100000", command=lambda: region_18(region_18_button, region_19_button), state=button_states["region_18_button"])
        region_18_button.grid(row=4,column=3, padx=5, pady=5)
        region_19_button = tk.Button(region_group, text="대전\n전투력 : 125000", command=lambda: region_19(region_19_button, region_20_button), state=button_states["region_19_button"])
        region_19_button.grid(row=5,column=3, padx=5, pady=5)
        region_20_button = tk.Button(region_group, text="충주\n전투력 : 150000", command=lambda: region_20(region_20_button, region_21_button), state=button_states["region_20_button"])
        region_20_button.grid(row=2,column=4, padx=5, pady=5)
        region_21_button = tk.Button(region_group, text="원주\n전투력 : 180000", command=lambda: region_21(region_21_button,region_22_button), state=button_states["region_21_button"])
        region_21_button.grid(row=1,column=5, padx=5, pady=5)
        jeju_1_button = tk.Button(region_group, text="제주\n임시 수도",state="disabled")
        jeju_1_button.grid(row=15,column=2, padx=5, pady=5)
        jeju_1_button = tk.Button(region_group, text="서귀포\n점령완료",state="disabled")
        jeju_1_button.grid(row=16,column=2, padx=5, pady=5)
        back_button = tk.Button(region_group, text="돌아가기", command=lambda: update_region(region_group, "choice"))
        back_button.grid(row=19,column=6, padx=5, pady=5)
    elif region_type == "Sector_B":
        region_22_button = tk.Button(region_group, text="평창\n전투력 : 215000", command=lambda: region_22(region_22_button, region_23_button), state=button_states["region_22_button"])
        region_22_button.grid(row=8,column=6, padx=5, pady=5)
        region_23_button = tk.Button(region_group, text="홍천\n전투력 : 250000", command=lambda: region_23(region_23_button, region_24_button), state=button_states["region_23_button"])
        region_23_button.grid(row=7,column=5, padx=5, pady=5)
        region_24_button = tk.Button(region_group, text="춘천\n전투력 : 290000", command=lambda: region_24(region_24_button, region_25_button), state=button_states["region_24_button"])
        region_24_button.grid(row=6,column=5, padx=5, pady=5)
        region_25_button = tk.Button(region_group, text="강릉\n전투력 : 335000", command=lambda: region_25(region_25_button, region_26_button), state=button_states["region_25_button"])
        region_25_button.grid(row=7,column=7, padx=5, pady=5)
        region_26_button = tk.Button(region_group, text="속초\n전투력 : 390000", command=lambda: region_26(region_26_button, region_27_button), state=button_states["region_26_button"])
        region_26_button.grid(row=5,column=7, padx=5, pady=5)
        region_27_button = tk.Button(region_group, text="고성\n전투력 : 450000", command=lambda: region_27(region_27_button, region_28_button), state=button_states["region_27_button"])
        region_27_button.grid(row=4,column=7, padx=5, pady=5)
        region_28_button = tk.Button(region_group, text="철원\n전투력 : 520000", command=lambda: region_28(region_28_button, region_29_button), state=button_states["region_28_button"])
        region_28_button.grid(row=4,column=5, padx=5, pady=5)
        region_29_button = tk.Button(region_group, text="고산\n전투력 : 600000", command=lambda: region_29(region_29_button, region_30_button), state=button_states["region_29_button"])
        region_29_button.grid(row=3,column=6, padx=5, pady=5)
        region_30_button = tk.Button(region_group, text="통천\n전투력 : 690000", command=lambda: region_30(region_30_button, region_31_button), state=button_states["region_30_button"])
        region_30_button.grid(row=3,column=7, padx=5, pady=5)
        region_31_button = tk.Button(region_group, text="원산\n전투력 : 850000", command=lambda: region_31(region_31_button, region_32_button), state=button_states["region_31_button"])
        region_31_button.grid(row=2,column=6, padx=5, pady=5)
        region_32_button = tk.Button(region_group, text="곡산\n전투력 : 950000", command=lambda: region_32(region_32_button, region_33_button), state=button_states["region_32_button"])
        region_32_button.grid(row=2,column=4, padx=5, pady=5)
        region_33_button = tk.Button(region_group, text="연산\n전투력 : 1075000", command=lambda: region_33(region_33_button, region_34_button), state=button_states["region_33_button"])
        region_33_button.grid(row=1,column=4, padx=5, pady=5)
        region_34_button = tk.Button(region_group, text="평양\n전투력 : 1250000", command=lambda: region_34(region_34_button, region_35_button), state=button_states["region_34_button"])
        region_34_button.grid(row=2,column=2, padx=5, pady=5)
        region_35_button = tk.Button(region_group, text="남포\n전투력 : 1400000", command=lambda: region_35(region_35_button, region_36_button), state=button_states["region_35_button"])
        region_35_button.grid(row=3,column=1, padx=5, pady=5)
        region_36_button = tk.Button(region_group, text="순천\n전투력 : 1600000", command=lambda: region_36(region_36_button, region_37_button), state=button_states["region_36_button"])
        region_36_button.grid(row=1,column=2, padx=5, pady=5)
        back_button = tk.Button(region_group, text="돌아가기", command=lambda: update_region(region_group, "choice"))
        back_button.grid(row=11,column=4, padx=5, pady=5)     
    elif region_type == "Sector_C":
        region_37_button = tk.Button(region_group, text="라오산\n전투력 : 1850000", command=lambda: region_37(region_37_button, region_38_button), state=button_states["region_37_button"])
        region_37_button.grid(row=2,column=2, padx=5, pady=5)
        region_38_button = tk.Button(region_group, text="청양\n전투력 : 2100000", command=lambda: region_38(region_38_button, region_39_button), state=button_states["region_38_button"])
        region_38_button.grid(row=1,column=1, padx=5, pady=5)
        region_39_button = tk.Button(region_group, text="리창\n전투력 : 2400000", command=lambda: region_39(region_39_button, region_40_button), state=button_states["region_39_button"])
        region_39_button.grid(row=2,column=1, padx=5, pady=5)
        back_button = tk.Button(region_group, text="돌아가기", command=lambda: update_region(region_group, "choice"))
        back_button.grid(row=4, column=2, padx=5, pady=5)
    elif region_type == "Sector_D":
        region_40_button = tk.Button(region_group, text="나호드카\n전투력 : 2750000", command=lambda: region_40(region_40_button, region_41_button), state=button_states["region_40_button"])
        region_40_button.grid(row=2,column=2, padx=5, pady=5)
        region_41_button = tk.Button(region_group, text="블라디보스토크\n전투력 : 3250000", command=lambda: region_41(region_41_button, region_42_button), state=button_states["region_41_button"])
        region_41_button.grid(row=2,column=1, padx=5, pady=5)
        region_42_button = tk.Button(region_group, text="우수리스크\n전투력 : 3800000", command=lambda: region_42(region_42_button, region_43_button), state=button_states["region_42_button"])
        region_42_button.grid(row=1,column=1, padx=5, pady=5)
        back_button = tk.Button(region_group, text="돌아가기", command=lambda: update_region(region_group, "choice"))
        back_button.grid(row=4,column=2, padx=5, pady=5)
    elif region_type == "Sector_E":
        region_43_button = tk.Button(region_group, text="장진\n전투력 : 4400000", command=lambda: region_43(region_43_button, region_44_button), state=button_states["region_43_button"])
        region_43_button.grid(row=6,column=2, padx=5, pady=5)
        region_44_button = tk.Button(region_group, text="강계\n전투력 : 5000000", command=lambda: region_44(region_44_button, region_45_button), state=button_states["region_44_button"])
        region_44_button.grid(row=5,column=1, padx=5, pady=5)
        region_45_button = tk.Button(region_group, text="낭림\n전투력 : 5700000", command=lambda: region_45(region_45_button, region_46_button), state=button_states["region_45_button"])
        region_45_button.grid(row=5,column=2, padx=5, pady=5)
        region_46_button = tk.Button(region_group, text="자성\n전투력 : 6450000", command=lambda: region_46(region_46_button, region_47_button), state=button_states["region_46_button"])
        region_46_button.grid(row=4,column=1, padx=5, pady=5)
        region_47_button = tk.Button(region_group, text="갑산\n전투력 : 7200000", command=lambda: region_47(region_47_button, region_48_button), state=button_states["region_47_button"])
        region_47_button.grid(row=4,column=3, padx=5, pady=5)
        region_48_button = tk.Button(region_group, text="함흥\n전투력 : 8200000", command=lambda: region_48(region_48_button, region_49_button), state=button_states["region_48_button"])
        region_48_button.grid(row=7,column=3, padx=5, pady=5)
        region_49_button = tk.Button(region_group, text="단천\n전투력 : 9200000", command=lambda: region_49(region_49_button, region_50_button), state=button_states["region_49_button"])
        region_49_button.grid(row=5,column=4, padx=5, pady=5)
        region_50_button = tk.Button(region_group, text="혜산\n전투력 : 10300000", command=lambda: region_50(region_50_button, region_51_button), state=button_states["region_50_button"])
        region_50_button.grid(row=3,column=4, padx=5, pady=5)
        region_51_button = tk.Button(region_group, text="백암\n전투력 : 11500000", command=lambda: region_51(region_51_button, region_52_button), state=button_states["region_51_button"])
        region_51_button.grid(row=3,column=5, padx=5, pady=5)
        region_52_button = tk.Button(region_group, text="삼지연\n전투력 : 12800000", command=lambda: region_52(region_52_button, region_53_button), state=button_states["region_52_button"])
        region_52_button.grid(row=2,column=5, padx=5, pady=5)
        region_53_button = tk.Button(region_group, text="나선\n전투력 : 14300000", command=lambda: region_53(region_53_button, region_54_button), state=button_states["region_53_button"])
        region_53_button.grid(row=1,column=7, padx=5, pady=5)
        region_54_button = tk.Button(region_group, text="청진\n전투력 : 17000000", command=lambda: region_54(region_54_button, region_55_button), state=button_states["region_54_button"])
        region_54_button.grid(row=2,column=7, padx=5, pady=5)
        back_button = tk.Button(region_group, text="돌아가기", command=lambda: update_region(region_group, "choice"))
        back_button.grid(row=10,column=4, padx=5, pady=5)
    elif region_type == "Sector_F":
        region_55_button = tk.Button(region_group, text="사리원\n전투력 : 20000000", command=lambda: region_55(region_55_button, region_56_button), state=button_states["region_55_button"])
        region_55_button.grid(row=1,column=2, padx=5, pady=5)
        region_56_button = tk.Button(region_group, text="해주\n전투력 : 24000000", command=lambda: region_56(region_56_button, region_57_button), state=button_states["region_56_button"])
        region_56_button.grid(row=3,column=2, padx=5, pady=5)
        region_57_button = tk.Button(region_group, text="연천\n전투력 : 29000000", command=lambda: region_57(region_57_button, region_58_button), state=button_states["region_57_button"])
        region_57_button.grid(row=3,column=5, padx=5, pady=5)
        region_58_button = tk.Button(region_group, text="개성\n전투력 : 35000000", command=lambda: region_58(region_58_button, region_59_button), state=button_states["region_58_button"])
        region_58_button.grid(row=4,column=3, padx=5, pady=5)
        region_59_button = tk.Button(region_group, text="이천\n전투력 : 42000000", command=lambda: region_59(region_59_button, region_60_button), state=button_states["region_59_button"])
        region_59_button.grid(row=11,column=4, padx=5, pady=5)
        region_60_button = tk.Button(region_group, text="용인\n전투력 : 50000000", command=lambda: region_60(region_60_button, region_61_button), state=button_states["region_60_button"])
        region_60_button.grid(row=11,column=3, padx=5, pady=5)
        region_61_button = tk.Button(region_group, text="수원\n전투력 : 59000000", command=lambda: region_61(region_61_button, region_62_button), state=button_states["region_61_button"])
        region_61_button.grid(row=10,column=2, padx=5, pady=5)
        region_62_button = tk.Button(region_group, text="인천\n전투력 : 69000000", command=lambda: region_62(region_62_button, region_63_button), state=button_states["region_62_button"])
        region_62_button.grid(row=7,column=1, padx=5, pady=5)
        region_63_button = tk.Button(region_group, text="서울\n전투력 : 90000000", command=lambda: region_63(region_63_button,), state=button_states["region_63_button"])
        region_63_button.grid(row=7,column=3, padx=5, pady=5)
        back_button = tk.Button(region_group, text="돌아가기", command=lambda: update_region(region_group, "choice"))
        back_button.grid(row=15,column=3, padx=5, pady=5)

# 메인 함수
def Lobby():
    global funds_label,military_label,population_label,research_label,population_label,economy_label,region_label,combat_power_label  # funds_label 변수를 전역 변수로 사용
    # Tkinter 윈도우 생성
    Lobby_window = tk.Tk()
    Lobby_window.title("메인 화면")
    Lobby_window.geometry("1280x720")

    # 버튼 그룹박스 생성
    button_group = tk.LabelFrame(Lobby_window, text="기능 버튼")
    button_group.pack(fill="both", expand="yes", padx=10, pady=10)

    # 초기에는 메인 버튼이 나타남
    update_buttons(button_group, "main")

    # 그룹박스 생성
    power_group = tk.LabelFrame(Lobby_window, text="국력")
    power_group.pack(fill="both", expand="yes", padx=10, pady=10)

    # 자원 및 인구 그룹박스에 대한 레이블 생성
    funds_label = tk.Label(power_group, text=f"자금 : {int(funds)}")
    funds_label.grid(row=0, column=0, padx=5, pady=5)

    population_label = tk.Label(power_group, text=f"인구수 : {int(population)}")
    population_label.grid(row=1, column=0, padx=5, pady=5)

    economy_label = tk.Label(power_group, text=f"경제력 : {int(economy)}")
    economy_label.grid(row=2, column=0, padx=5, pady=5)

    research_label = tk.Label(power_group, text=f"연구력 : {int(research)}")
    research_label.grid(row=3, column=0, padx=5, pady=5)

    region_label = tk.Label(power_group, text=f"지역수 : {int(region)}")
    region_label.grid(row=4, column=0, padx=5, pady=5) 
    military_label = tk.Label(power_group, text=f"군사력 : {int(military)}")
    military_label.grid(row=5, column=0, padx=5, pady=5)

    combat_power_label = tk.Label(power_group, text=f"전투력 : {int(military * 0.1)}")
    combat_power_label.grid(row=6, column=0, padx=5, pady=5)

    Lobby_window.mainloop()

# 버튼 업데이트 함수
def update_buttons(button_group, button_type):
    # 기존 버튼들을 삭제
    for widget in button_group.winfo_children():
        widget.destroy()

    # 메인 버튼일 경우
    if button_type == "main":
        # 각 버튼에 대한 기능 설정
        tax_button = tk.Button(button_group, text="세금 징수", command=lambda: update_buttons(button_group, "tax"))
        tax_button.pack(side="left", padx=5, pady=5)

        military_button = tk.Button(button_group, text="군사력 개발", command=lambda: update_buttons(button_group, "military"))
        military_button.pack(side="left", padx=5, pady=5)

        research_button = tk.Button(button_group, text="연구개발", command=lambda: update_buttons(button_group, "research"))
        research_button.pack(side="left", padx=5, pady=5)

        facility_button = tk.Button(button_group, text="시설 개발", command=lambda: update_buttons(button_group, "facility"))
        facility_button.pack(side="left", padx=5, pady=5)

        battle_button = tk.Button(button_group, text="전투 준비", command=prepare_for_battle_gui)
        battle_button.pack(side="left", padx=5, pady=5)

    # 세금 징수 버튼일 경우
    elif button_type == "tax":
        # 각 버튼에 대한 기능 설정
        jeju_button = tk.Button(button_group, text="제주", command=on_jeju_button_click)
        jeju_button.pack(side="left", padx=5, pady=5)

        jeolla_button = tk.Button(button_group, text="전라", command=on_jeolla_button_click)
        jeolla_button.pack(side="left", padx=5, pady=5)

        gyeongsang_button = tk.Button(button_group, text="경상", command=on_gyeongsang_button_click)
        gyeongsang_button.pack(side="left", padx=5, pady=5)

        chungcheong_button = tk.Button(button_group, text="충청", command=on_chungcheong_button_click)
        chungcheong_button.pack(side="left", padx=5, pady=5)

        gangwon_button = tk.Button(button_group, text="강원", command=on_gangwon_button_click)
        gangwon_button.pack(side="left", padx=5, pady=5)

        gyeonggi_button = tk.Button(button_group, text="경기", command=on_gyeonggi_button_click)
        gyeonggi_button.pack(side="left", padx=5, pady=5)

        hwanghae_button = tk.Button(button_group, text="황해", command=on_hwanghae_button_click)
        hwanghae_button.pack(side="left", padx=5, pady=5)

        pyongan_button = tk.Button(button_group, text="평안", command=on_pyongan_button_click)
        pyongan_button.pack(side="left", padx=5, pady=5)

        wonsan_button = tk.Button(button_group, text="원산", command=on_wonsan_button_click)
        wonsan_button.pack(side="left", padx=5, pady=5)

        hamgyong_button = tk.Button(button_group, text="함경", command=on_hamgyong_button_click)
        hamgyong_button.pack(side="left", padx=5, pady=5)

        back_button = tk.Button(button_group, text="돌아가기", command=lambda: update_buttons(button_group, "main"))
        back_button.pack(side="left", padx=5, pady=5)

    elif button_type == "military":
        # 각 버튼에 대한 기능 설정
        soldier_button = tk.Button(button_group, text="보병 생산", command=buy_soldier)
        soldier_button.pack(side="left", padx=5, pady=5)

        Rifle_button = tk.Button(button_group, text="소총 생산", command=buy_Rifle)
        Rifle_button.pack(side="left", padx=5, pady=5)

        RPG_button = tk.Button(button_group, text="대전차포 생산", command=buy_RPG)
        RPG_button.pack(side="left", padx=5, pady=5)

        Artillery_button = tk.Button(button_group, text="야포 생산", command=buy_Artillery)
        Artillery_button.pack(side="left", padx=5, pady=5)

        Tank_button = tk.Button(button_group, text="전차 생산", command=buy_Tank)
        Tank_button.pack(side="left", padx=5, pady=5)

        Fighter_button = tk.Button(button_group, text="전투기 생산", command=buy_Fighter)
        Fighter_button.pack(side="left", padx=5, pady=5)

        back_button = tk.Button(button_group, text="돌아가기", command=lambda: update_buttons(button_group, "main"))
        back_button.pack(side="left", padx=5, pady=5)

    elif button_type == "research":
        # 각 버튼에 대한 기능 설정
        research_1_button = tk.Button(button_group, text="기초 연구", command=research_1)
        research_1_button.pack(side="left", padx=5, pady=5)

        research_2_button = tk.Button(button_group, text="초급 연구", command=research_2)
        research_2_button.pack(side="left", padx=5, pady=5)

        research_3_button = tk.Button(button_group, text="중급 연구", command=research_3)
        research_3_button.pack(side="left", padx=5, pady=5)

        research_4_button = tk.Button(button_group, text="중고급 연구", command=research_4)
        research_4_button.pack(side="left", padx=5, pady=5)

        research_5_button = tk.Button(button_group, text="고급 연구", command=research_5)
        research_5_button.pack(side="left", padx=5, pady=5)

        research_6_button = tk.Button(button_group, text="최고급 연구", command=research_6)
        research_6_button.pack(side="left", padx=5, pady=5)

        back_button = tk.Button(button_group, text="돌아가기", command=lambda: update_buttons(button_group, "main"))
        back_button.pack(side="left", padx=5, pady=5)

    elif button_type == "facility":
        # 각 버튼에 대한 기능 설정
        facility_1_button = tk.Button(button_group, text="주거시설 개발", command=facility_1)
        facility_1_button.pack(side="left", padx=5, pady=5)

        facility_2_button = tk.Button(button_group, text="상업시설 개발", command=facility_2)
        facility_2_button.pack(side="left", padx=5, pady=5)

        facility_3_button = tk.Button(button_group, text="여가시설 개발", command=facility_3)
        facility_3_button.pack(side="left", padx=5, pady=5)

        facility_4_button = tk.Button(button_group, text="교통시설 개발", command=facility_4)
        facility_4_button.pack(side="left", padx=5, pady=5)

        facility_5_button = tk.Button(button_group, text="공업시설 개발", command=facility_5)
        facility_5_button.pack(side="left", padx=5, pady=5)

        facility_6_button = tk.Button(button_group, text="신도시 개발", command=facility_6)
        facility_6_button.pack(side="left", padx=5, pady=5)

        # "돌아가기" 버튼 추가
        back_button = tk.Button(button_group, text="돌아가기", command=lambda: update_buttons(button_group, "main"))
        back_button.pack(side="left", padx=5, pady=5)

name_scene()  # 이름 입력 화면 표시
