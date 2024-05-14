import tkinter as tk

name_window = None  # 전역 변수로 name_window 선언
prologue_window = None  # 전역 변수로 prologue_window 선언
prologue_index = 0  # 전역 변수로 prologue_index 선언

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
        """,
        f"""
        100년전 미국이 주장하던 고립주의가 미국에 다시 등장했다.
        고립주의 정치인이 2032년 미국 대통령 선거로 당선되어
        미국은 다시 한번 고립주의를 표방하는 나라로 변화한다.

        2033년 2차 한국전쟁이 발발했다.
        철원 전투는 북한의 압승으로 끝났고 
        대한민국 국군의 명령 체계는 그대로 무너져내렸다. 
        이에 한국군은 혼란에 빠졌고 수 갈래로 찢어진 흩어진 다음, 
        그대로 낙동강 방어선과 대구 근방까지 밀려나버린다. 
        후퇴하는 과정에서 민경록 대통령은 포로로 잡혔고, 
        {user_name}이 임시 비상 행정부 ㅜ장을 잡았다. 
        아르한겔스크를 수도로 한 새로운 정부가 들어섰지만, 
        이 쿠데타는 소련을 내전 상황으로 몰아넣었다. 
        결국 레닌의 사망 18주년인 1942년 1월 21일, 
        그렇게 소련은 지도에서 사라지고 아르한겔스크의 신소련 정부는 혼란에 빠졌다.
        """,
        f"""
        프롤로그 4 텍스트 화면 {user_name}
        """
    ]

    button_texts = ['다음', '총원 최대 경계 상태로!', '알겠네!', '앞으로']

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

    if prologue_window is None:
        prologue_window = tk.Toplevel()
        prologue_window.title("프롤로그")
        prologue_window.geometry("1280x720")

        text_widget = tk.Text(prologue_window, height=50, width=100)
        text_widget.pack()

        next_button = tk.Button(prologue_window, text="다음", command=update_text, width=20, height=5)
        next_button.pack(side=tk.BOTTOM)

        update_text()

# 메인 함수
def main():
    # Tkinter 윈도우 생성
    main_window = tk.Toplevel()  # 이전 윈도우에서 메인 창으로 변경
    main_window.title("메인 화면")  # 윈도우 제목 설정
    main_window.geometry("1280x720")  # 윈도우 크기 설정

    # 세금 징수 버튼 생성
    tax_button = tk.Button(main_window, text="세금 징수", command=collect_tax)
    tax_button.pack()

    # 군사력 개발 버튼 생성
    military_button = tk.Button(main_window, text="군사력 개발", command=develop_military)
    military_button.pack()


    # 연구개발 버튼 생성
    research_button = tk.Button(main_window, text="연구개발", command=conduct_research)
    research_button.pack()


    # 시설 개발 버튼 생성
    facility_button = tk.Button(main_window, text="시설 개발", command=develop_facility)
    facility_button.pack()

    # 전투 준비 버튼 생성
    battle_button = tk.Button(main_window, text="전투 준비", command=prepare_for_battle)
    battle_button.pack()

    main_window.mainloop()  # Tkinter 이벤트 루프 시작

# 각 기능에 대한 함수 정의
def collect_tax():
    print("세금을 징수합니다.")

def develop_military():
    print("군사력을 개발합니다.")

def conduct_research():
    print("연구를 진행합니다.")

def develop_facility():
    print("시설을 개발합니다.")

def prepare_for_battle():
    print("전투 준비를 합니다.")


name_scene()  # 이름 입력 화면 표시
