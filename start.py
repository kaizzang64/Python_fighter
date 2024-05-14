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
        f"""
        프롤로그 1 텍스트 화면 {user_name}
        """,
        f"""
        프롤로그 2 텍스트 화면 {user_name}
        """,
        f"""
        프롤로그 3 텍스트 화면 {user_name}
        """,
        f"""
        프롤로그 4 텍스트 화면 {user_name}
        """
    ]

    button_texts = ['모두 전진', '동지들!', '알겠네!', '앞으로']

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
