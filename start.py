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
    global prologue_window, prologue_index  # prologue_window와 prologue_index를 전역 변수로 사용하겠다고 선언

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

    if prologue_window is None:
        # Tkinter 윈도우 생성
        prologue_window = tk.Toplevel()  # 이전 윈도우에서 새로운 프롤로그 창으로 변경
        prologue_window.title("프롤로그")  # 윈도우 제목 설정
        prologue_window.geometry("1280x720")  # 윈도우 크기 설정

        # 텍스트 위젯 생성
        text_widget = tk.Text(prologue_window, height=50, width=100)
        text_widget.pack()

        # 텍스트 업데이트 함수
        def update_text():
            global prologue_index  # prologue_index를 전역 변수로 사용하겠다고 선언

            if prologue_index < len(prologue_texts):
                text_widget.delete("1.0", tk.END)  # 텍스트 모두 삭제
                text_widget.insert(tk.END, prologue_texts[prologue_index])  # 새로운 텍스트 삽입
                prologue_index += 1
            else:
                prologue_index = 0  # 인덱스 초기화
                prologue_window.destroy()  # 프롤로그 창 닫기
                main()  # 메인 화면 호출

        update_text()  # 초기 텍스트 업데이트

        # 다음 버튼 생성
        next_button = tk.Button(prologue_window, text="다음", command=update_text, width=20, height=5)
        next_button.pack(side=tk.BOTTOM)  # 버튼을 윈도우의 아래쪽에 배치

# 메인 함수
# 이미지를 Tkinter에서 사용하기 위한 모듈 임포트
def main():
    # 메인 윈도우 생성
    main_window = tk.Tk()
    main_window.title("메인 화면")
    main_window.geometry("1280x720")

    # 배경 이미지
    bg_image = tk.PhotoImage(file="main_background.png")  # 배경 이미지로 사용할 PNG 파일을 지정합니다.

    # 배경 이미지를 표시할 라벨 생성
    bg_label = tk.Label(main_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # 배경 이미지를 전체 윈도우에 맞게 배치합니다.

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

    main_window.mainloop()



name_scene()  # 이름 입력 화면 표시
