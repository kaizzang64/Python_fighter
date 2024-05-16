import time
import tkinter as tk

name_window = None  # 전역 변수로 name_window 선언
prologue_window = None  # 전역 변수로 prologue_window 선언
prologue_index = 0  # 전역 변수로 prologue_index 선언


funds_label = None


funds = 10000
population = 10000
economy = 100
research = 0
military = 100
region = 200

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

def update_popualtion_label():
    global population_label
    population_label.config(text=f"인구 : {military}")

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
    global population
    global region
    if region >= 44:
        funds += population * 0.20
        update_funds_label()  # update_funds_label 함수 호출
    time.sleep(0.5)




def conduct_research_gui():
    # Tkinter 윈도우 생성
    conduct_research_window = tk.Toplevel()
    conduct_research_window.title("연구개발")
    conduct_research_window.geometry("1280x720")

    # 연구개발 창에 대한 내용을 표시하는 레이블
    label = tk.Label(conduct_research_window, text="연구를 진행합니다.")
    label.pack()

    # 뒤로가기 버튼 생성
    back_button = tk.Button(conduct_research_window, text="뒤로가기", command=conduct_research_window.destroy)
    back_button.pack()

def develop_facility_gui():
    # Tkinter 윈도우 생성
    develop_facility_window = tk.Toplevel()
    develop_facility_window.title("시설 개발")
    develop_facility_window.geometry("1280x720")

    # 시설 개발 창에 대한 내용을 표시하는 레이블
    label = tk.Label(develop_facility_window, text="시설을 개발합니다.")
    label.pack()

    # 뒤로가기 버튼 생성
    back_button = tk.Button(develop_facility_window, text="뒤로가기", command=develop_facility_window.destroy)
    back_button.pack()

def prepare_for_battle_gui():
    # Tkinter 윈도우 생성
    prepare_for_battle_window = tk.Toplevel()
    prepare_for_battle_window.title("전투 준비")
    prepare_for_battle_window.geometry("1280x720")

    # 전투 준비 창에 대한 내용을 표시하는 레이블
    label = tk.Label(prepare_for_battle_window, text="전투 준비를 합니다.")
    label.pack()

    # 뒤로가기 버튼 생성
    back_button = tk.Button(prepare_for_battle_window, text="뒤로가기", command=prepare_for_battle_window.destroy)
    back_button.pack()




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
    funds_label = tk.Label(power_group, text=f"자금 : {funds}")
    funds_label.grid(row=0, column=0, padx=5, pady=5)

    population_label = tk.Label(power_group, text=f"인구수 : {population}")
    population_label.grid(row=1, column=0, padx=5, pady=5)

    economy_label = tk.Label(power_group, text=f"경제력 : {economy}")
    economy_label.grid(row=2, column=0, padx=5, pady=5)

    research_label = tk.Label(power_group, text=f"연구력 : {research}")
    research_label.grid(row=3, column=0, padx=5, pady=5)

    region_label = tk.Label(power_group, text=f"지역수 : {region}")
    region_label.grid(row=4, column=0, padx=5, pady=5) 
    military_label = tk.Label(power_group, text=f"군사력 : {military}")
    military_label.grid(row=5, column=0, padx=5, pady=5)

    combat_power_label = tk.Label(power_group, text=f"전투력 : {military * 0.1}")
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

        research_button = tk.Button(button_group, text="연구개발", command=conduct_research_gui)
        research_button.pack(side="left", padx=5, pady=5)

        facility_button = tk.Button(button_group, text="시설 개발", command=develop_facility_gui)
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

        Tank_button = tk.Button(button_group, text="전차 생산", command=buy_tank)
        Tank_button.pack(side="left", padx=5, pady=5)

        Fighter_button = tk.Button(button_group, text="전투기 생산", command=buy_Fighter)
        Fighter_button.pack(side="left", padx=5, pady=5)

        # "돌아가기" 버튼 추가
        back_button = tk.Button(button_group, text="돌아가기", command=lambda: update_buttons(button_group, "main"))
        back_button.pack(side="left", padx=5, pady=5)










name_scene()  # 이름 입력 화면 표시
