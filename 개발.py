#���Ǻ��� ���߿� ��ĥ �� ����
money = 0 
military = 0 #military���� power attack���� Ȯ����
research = 0
economy = 0 
region = 0 #���� ������ ���� �� ���Ƽ� ���Ƿ� ��
population = 0

def print_status(population, economy, money, research, military, region): #�����������Լ� �ʿ������ ������
    print("���� ����:")
    print("�α� ��: ", population)
    print("������: ", economy)
    print("����: ", money)
    print("������: ", research)
    print("�����: ", military)
    print("���� ��: ", region)


# ���� ���
print_status(population, economy, money, research, military, region)
print(status.print)

#���Ǻ��� ���߿� ��ĥ �� ����2
player_choice = int(input("����¡��(1) �����غ�(2) ����� ����(3) ������ ����(4) ���� ����(5)"))

if player_choice == 3 : #3=����°��� 
    print("���� - ���:500 ����� ����:1")
    buy = input("�����Ͻðڽ��ϱ�? (Y/N) ���� �������� (D)")
    if buy == 'Y' or buy == 'y':
        if money>=500 :
            military = military+1
            money = money - 500
            print(status.print) #�ʿ������ ����
        else:
            print("���� �����մϴ�")
    elif buy == 'N' or buy == 'n':
        pass
    elif buy == 'D' or buy == 'd':
        print("�� ���� - ���:2000 ����� ����:6 �ʿ� ������: 20")
        print(status.print) #�ʿ������ ����
        buy = input("�����Ͻðڽ��ϱ�? (Y/N)")
        if buy == 'Y' or buy == 'y':
            if money>=2000 and research>=20 :
                military = military+6
                money = money - 2000
                print(status.print) #�ʿ������ ����
            elif money<2000 and research>=20 :
                print("���� �����մϴ�.")
            elif money>=2000 and research<20 :
                print("�������� �����մϴ�.")
        elif buy =='N' or buy == 'n' :
            pass

if player_choice == 4 : #4=�����°��� 
    print("�ְŽü� ���� - ���: 2500 ������ ����:1 �α��� ����:200")
    buy = input("�����Ͻðڽ��ϱ�? (Y/N) ���� �������� (D)")
    if buy == 'Y' or buy == 'y':
        if money>=2500 :
            economy = economy+1
            money = money - 2500
            population = population + 200 #�̺κ� �÷ο� ��Ʈ�� ���µ� �־�� �� �� ���Ƽ� ����
            print(status.print) #�ʿ������ ����
        else:
            print("���� �����մϴ�")
    elif buy == 'N' or buy == 'n':
        pass
    elif buy == 'D' or buy == 'd':
        print("����ü� ���� - ���:10000 ������:5 �α��� ����:900 �ʿ� ������: 3�� �̻�")
        print(status.print) #�ʿ������ ����
        buy = input("�����Ͻðڽ��ϱ�? (Y/N)")
        if buy == 'Y' or buy == 'y':
            if money>=10000 and region>=3 :
                economy = economy+5
                money = money - 10000
                population = population + 900 #�̺κ� �÷ο� ��Ʈ�� ���µ� �־�� �� �� ���Ƽ� ����2
                print(status.print) #�ʿ������ ����
            elif money<10000 and region>=3 :
                print("���� �����մϴ�.")
            elif money>=10000 and region<3 :
                print("�ʿ� �������� �����մϴ�.")
        elif buy =='N' or buy == 'n' :
            pass
        

if player_choice == 5 : #5=�������� 
    print("���� ���� - ���:5000 ������ ����:1")
    buy = input("�����Ͻðڽ��ϱ�? (Y/N) ���� �������� (D)")
    if buy == 'Y' or buy == 'y':
        if money>=5000 :
            research = research+1
            money = money - 5000
            print(status.print) #�ʿ������ ����
        else:
            print("���� �����մϴ�")
    elif buy == 'N' or buy == 'n':
        pass
    elif buy == 'D' or buy == 'd':
        print("�ʱ� ���� - ���:10000 ������ ����:6 �ʿ� ������: 40")
        print(status.print) #�ʿ������ ����
        buy = input("�����Ͻðڽ��ϱ�? (Y/N)")
        if buy == 'Y' or buy == 'y':
            if money>=10000 and economy>=40 :
                research = research + 6
                money = money - 10000
                print(status.print) #�ʿ������ ����
            elif money<10000 and economy>=40 :
                print("���� �����մϴ�.")
            elif money>=10000 and economy<40 :
                print("�������� �����մϴ�.")
        elif buy =='N' or buy == 'n' :
            pass
        


                
    
   
