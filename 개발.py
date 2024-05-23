#임의변수 나중에 합칠 때 변경
money = 0 
military = 0 #military인지 power attack인지 확인좀
research = 0
economy = 0 
region = 0 #지역 변수명 없는 것 같아서 임의로 씀
population = 0

def print_status(population, economy, money, research, military, region): #현재상태출력함수 필요없으면 날리셈
    print("현재 상태:")
    print("인구 수: ", population)
    print("경제력: ", economy)
    print("예산: ", money)
    print("연구력: ", research)
    print("군사력: ", military)
    print("지역 수: ", region)


# 상태 출력
print_status(population, economy, money, research, military, region)
print(status.print)

#임의변수 나중에 합칠 때 변경2
player_choice = int(input("세금징수(1) 전투준비(2) 군사력 개발(3) 경제력 개발(4) 연구 개발(5)"))

if player_choice == 3 : #3=군사력개발 
    print("보병 - 비용:500 군사력 증가:1")
    buy = input("구매하시겠습니까? (Y/N) 다음 페이지로 (D)")
    if buy == 'Y' or buy == 'y':
        if money>=500 :
            military = military+1
            money = money - 500
            print(status.print) #필요없으면 삭제
        else:
            print("돈이 부족합니다")
    elif buy == 'N' or buy == 'n':
        pass
    elif buy == 'D' or buy == 'd':
        print("총 개발 - 비용:2000 군사력 증가:6 필요 연구력: 20")
        print(status.print) #필요없으면 삭제
        buy = input("구매하시겠습니까? (Y/N)")
        if buy == 'Y' or buy == 'y':
            if money>=2000 and research>=20 :
                military = military+6
                money = money - 2000
                print(status.print) #필요없으면 삭제
            elif money<2000 and research>=20 :
                print("돈이 부족합니다.")
            elif money>=2000 and research<20 :
                print("연구력이 부족합니다.")
        elif buy =='N' or buy == 'n' :
            pass

if player_choice == 4 : #4=경제력개발 
    print("주거시설 개발 - 비용: 2500 경제력 증가:1 인구수 증가:200")
    buy = input("구매하시겠습니까? (Y/N) 다음 페이지로 (D)")
    if buy == 'Y' or buy == 'y':
        if money>=2500 :
            economy = economy+1
            money = money - 2500
            population = population + 200 #이부분 플로우 차트에 없는데 있어야 할 것 같아서 넣음
            print(status.print) #필요없으면 삭제
        else:
            print("돈이 부족합니다")
    elif buy == 'N' or buy == 'n':
        pass
    elif buy == 'D' or buy == 'd':
        print("상업시설 개발 - 비용:10000 경제력:5 인구수 증가:900 필요 지역수: 3개 이상")
        print(status.print) #필요없으면 삭제
        buy = input("구매하시겠습니까? (Y/N)")
        if buy == 'Y' or buy == 'y':
            if money>=10000 and region>=3 :
                economy = economy+5
                money = money - 10000
                population = population + 900 #이부분 플로우 차트에 없는데 있어야 할 것 같아서 넣음2
                print(status.print) #필요없으면 삭제
            elif money<10000 and region>=3 :
                print("돈이 부족합니다.")
            elif money>=10000 and region<3 :
                print("필요 지역수가 부족합니다.")
        elif buy =='N' or buy == 'n' :
            pass
        

if player_choice == 5 : #5=연구개발 
    print("기초 연구 - 비용:5000 연구력 증가:1")
    buy = input("구매하시겠습니까? (Y/N) 다음 페이지로 (D)")
    if buy == 'Y' or buy == 'y':
        if money>=5000 :
            research = research+1
            money = money - 5000
            print(status.print) #필요없으면 삭제
        else:
            print("돈이 부족합니다")
    elif buy == 'N' or buy == 'n':
        pass
    elif buy == 'D' or buy == 'd':
        print("초급 연구 - 비용:10000 연구력 증가:6 필요 경제력: 40")
        print(status.print) #필요없으면 삭제
        buy = input("구매하시겠습니까? (Y/N)")
        if buy == 'Y' or buy == 'y':
            if money>=10000 and economy>=40 :
                research = research + 6
                money = money - 10000
                print(status.print) #필요없으면 삭제
            elif money<10000 and economy>=40 :
                print("돈이 부족합니다.")
            elif money>=10000 and economy<40 :
                print("경제력이 부족합니다.")
        elif buy =='N' or buy == 'n' :
            pass
        


                
    
   
