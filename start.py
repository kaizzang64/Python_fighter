import tkinter as tk

# 이름 입력 화면을 생성하는 함수
def name_scene():
    # Tkinter 윈도우 생성
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

# 프롤로그 장면을 생성하는 함수
def prologue_scene(user_name):
    prologue_text = f"""
    프롤로그 텍스트 화면{user_name}
    """

    # Tkinter 윈도우 생성
    prologue_window = tk.Toplevel()
    prologue_window.title("프롤로그")  # 윈도우 제목 설정
    prologue_window.geometry("1280x720")  # 윈도우 크기 설정

    text_widget = tk.Text(prologue_window, height=50, width=100)  # 텍스트 위젯 생성
    text_widget.pack()

    # 텍스트를 한 글자씩 출력하는 함수
    def print_text(index=0):
        if index < len(prologue_text):
            text_widget.insert(tk.END, prologue_text[index])  # 텍스트 위젯에 글자 추가
            index += 1
            prologue_window.after(10, print_text, index)  # 10밀리초 후에 다음 글자 출력
        else:
            next_button = tk.Button(prologue_window, text="다음", command=lambda: [prologue_window.destroy(), prologue_scene_2(user_name)], width=20, height=5)
            next_button.pack(side=tk.BOTTOM)  # 버튼을 윈도우의 아래쪽에 배치

    print_text()  # 텍스트 출력 함수 호출

def prologue_scene_2(user_name):
    prologue_text_2 = f"""
    프롤로그 2 텍스트 화면{user_name}
    """

    # Tkinter 윈도우 생성
    prologue_window_2 = tk.Toplevel()
    prologue_window_2.title("프롤로그 2")  # 윈도우 제목 설정
    prologue_window_2.geometry("1280x720")  # 윈도우 크기 설정

    text_widget_2 = tk.Text(prologue_window_2, height=50, width=100)  # 텍스트 위젯 생성
    text_widget_2.pack()

    # 텍스트를 한 글자씩 출력하는 함수
    def print_text_2(index=0):
        if index < len(prologue_text_2):
            text_widget_2.insert(tk.END, prologue_text_2[index])  # 텍스트 위젯에 글자 추가
            index += 1
            prologue_window_2.after(10, print_text_2, index)  # 10밀리초 후에 다음 글자 출력
        else:
            next_button_2 = tk.Button(prologue_window_2, text="다음", command=lambda: prologue_scene_3(user_name), width=20, height=5)
            next_button_2.pack(side=tk.BOTTOM)  # 버튼을 윈도우의 아래쪽에 배치

    print_text_2()  # 텍스트 출력 함수 호출

# 프롤로그 3 장면을 생성하는 함수
def prologue_scene_3(user_name):
    prologue_text_3 = f"""
    프롤로그 3 텍스트 화면{user_name}
    """

    # Tkinter 윈도우 생성
    prologue_window_3 = tk.Toplevel()
    prologue_window_3.title("프롤로그 3")  # 윈도우 제목 설정
    prologue_window_3.geometry("1280x720")  # 윈도우 크기 설정

    text_widget_3 = tk.Text(prologue_window_3, height=50, width=100)  # 텍스트 위젯 생성
    text_widget_3.pack()

    # 텍스트를 한 글자씩 출력하는 함수
    def print_text_3(index=0):
        if index < len(prologue_text_3):
            text_widget_3.insert(tk.END, prologue_text_3[index])  # 텍스트 위젯에 글자 추가
            index += 1
            prologue_window_3.after(10, print_text_3, index)  # 10밀리초 후에 다음 글자 출력
        else:
            next_button_3 = tk.Button(prologue_window_3, text="다음", command=lambda: prologue_scene_4(user_name), width=20, height=5)
            next_button_3.pack()

    print_text_3()  # 텍스트 출력 함수 호출

# 프롤로그 4 장면을 생성하는 함수
def prologue_scene_4(user_name):
    prologue_text_4 = f"""
    프롤로그 4 텍스트 화면{user_name}
    """

    # Tkinter 윈도우 생성
    prologue_window_4 = tk.Toplevel()
    prologue_window_4.title("프롤로그 4")  # 윈도우 제목 설정
    prologue_window_4.geometry("1280x720")  # 윈도우 크기 설정

    text_widget_4 = tk.Text(prologue_window_4, height=50, width=100)  # 텍스트 위젯 생성
    text_widget_4.pack()

    # 텍스트를 한 글자씩 출력하는 함수
    def print_text_4(index=0):
        if index < len(prologue_text_4):
            text_widget_4.insert(tk.END, prologue_text_4[index])  # 텍스트 위젯에 글자 추가
            index += 1
            prologue_window_4.after(10, print_text_4, index)  # 10밀리초 후에 다음 글자 출력
        else:
            start_main_button = tk.Button(prologue_window_4, text="메인 게임 시작", command=lambda: [prologue_window_4.destroy(), main()], width=20, height=5)
            start_main_button.pack()

            # 텍스트 출력이 끝나면 버튼을 생성하도록 추가
            text_widget_4.after(10, lambda: start_main_button.pack())  

    print_text_4()  # 텍스트 출력 함수 호출

def main():
    # Tkinter 윈도우 생성
    main_window = tk.Tk()
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
