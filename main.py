print("...")

import pygame, time, random, os, turtle	#导入工具箱	
def exit():
	pygame.quit()
	print("exit")
	quit()

pygame.init()	#pygame初始化



#-------新建窗口-------
screen = pygame.display.set_mode((460, 800))	#新建窗口
pygame.display.set_caption("飞机大战 - Pygame")

gameover = pygame.image.load('gameover.png')	#加载图片
gameover = pygame.transform.scale(gameover, (460, 800))

#-------贴背景-------
bg = pygame.image.load('背景.png')	#加载图片
bg = pygame.transform.scale(bg, (460, 800))

#-------贴英雄机 (60, 60)-------
hero1 = pygame.image.load('我方飞机1.png')	#加载英雄机
hero1 = pygame.transform.scale(hero1, (60, 60))	#改变英雄机大小
hero2 = pygame.image.load('我方飞机2.png')
hero2 = pygame.transform.scale(hero2, (60, 60))
hero_down = pygame.image.load('我方飞机爆炸.png')
hero_down = pygame.transform.scale(hero_down, (60, 60))

pygame.mixer.music.load("音乐.wav")

#-------贴小敌机 (42, 36)-------
xdj1 = pygame.image.load('小飞机.png')
xdj1 = pygame.transform.scale(xdj1, (42, 36))
xdj2 = pygame.image.load('小飞机爆炸1.png')
xdj2 = pygame.transform.scale(xdj2, (42, 36))
xdj3 = pygame.image.load('小飞机爆炸2.png')
xdj3 = pygame.transform.scale(xdj3, (42, 36))
xdj4 = pygame.image.load('小飞机爆炸3.png')
xdj4 = pygame.transform.scale(xdj4, (42, 36)) 
xdj1_x = []	#新建小敌机x列表
xdj1_y = []	#新建小敌机y列表
xdj1_blood = [] #新建小敌机血量列表

#-------贴中敌机 (57, 65)-------
zdj1 = pygame.image.load('中飞机.png')
zdj1 = pygame.transform.scale(zdj1, (57, 65))
zdj2 = pygame.image.load('中飞机爆炸1.png')
zdj2 = pygame.transform.scale(zdj2, (57, 65))
zdj3 = pygame.image.load('中飞机爆炸2.png')
zdj3 = pygame.transform.scale(zdj3, (57, 65))
zdj4 = pygame.image.load('中飞机爆炸3.png')
zdj4 = pygame.transform.scale(zdj4, (57, 65))
zdj1_x = []	#新建中敌机x列表
zdj1_y = []	#新建中敌机y列表
zdj1_blood = [] #新建中敌机血量列表

#-------贴大敌机 (66, 92)-------
ddj1 = pygame.image.load('飞船.png')
ddj1 = pygame.transform.scale(ddj1, (66, 92))
ddj2 = pygame.image.load('飞船爆炸1.png')
ddj2 = pygame.transform.scale(ddj2, (66, 92))
ddj3 = pygame.image.load('飞船爆炸2.png')
ddj3 = pygame.transform.scale(ddj3, (66, 92))
ddj4 = pygame.image.load('飞船爆炸3.png')
ddj4 = pygame.transform.scale(ddj4, (66, 92))
ddj1_x = []	#新建大敌机x列表
ddj1_y = []	#新建大敌机y列表
ddj1_blood = [] #新建大敌机血量列表

#-------贴子弹 (8, 17)-------
bullet = pygame.image.load('子弹.png')
bullet = pygame.transform.scale(bullet, (8, 17))
bullet_x = []	#新建子弹x列表
bullet_y = []	#新建子弹y列表


count = 0	#计算执行多少次

#-------标识符-------
flat = 0	#0 - 1 1 - 2 2 - 3

hero_down_display = 0
score = 0
font = pygame.font.Font("simsun.ttc",
                        40)
score1 = font.render("分数:",
                      True,
                      (255, 255, 255))
is_start = 1
print("playing...")
#-------英雄机造型切换-------
while True:
    mouse = pygame.mouse.get_pos()	#获取鼠标位置
    count += 1
    screen.blit(bg, (0, 0))	#贴背景图片
    screen.blit(score1,(0, 0))
    score_display = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_display, (120, 0))
	#-------子弹的出现-------
    if count % 10 == 0 and hero_down_display == 0:
        if flat == 0:
            bullet_x.append(mouse[0])	#添加子弹x坐标
            bullet_y.append(mouse[1])	#添加子弹y坐标
        if flat == 1:
            bullet_x.append(mouse[0]-30)	#添加子弹x坐标
            bullet_y.append(mouse[1])	#添加子弹y坐标

            bullet_x.append(mouse[0]+25)	#添加子弹x坐标
            bullet_y.append(mouse[1])	#添加子弹y坐标
        if flat == 2:
            bullet_x.append(mouse[0]-30)	#添加子弹x坐标
            bullet_y.append(mouse[1])	#添加子弹y坐标

            bullet_x.append(mouse[0])	#添加子弹x坐标
            bullet_y.append(mouse[1])	#添加子弹y坐标

            bullet_x.append(mouse[0]+25)	#添加子弹x坐标
            bullet_y.append(mouse[1])	#添加子弹y坐标
    if is_start == 1:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
            #-------子弹上升-------
        for i in range(len(bullet_x)):	#获取所有的y坐标
            bullet_y[i] -= 5	#让子弹y坐标增加
            screen.blit(bullet, (bullet_x[i], bullet_y[i]))	#贴子弹
            #-------子弹消失-------
        for i in range(len(bullet_x)):
            if bullet_y[i] < 0:
                del bullet_y[i]
                del bullet_x[i]
                break
        if hero_down_display == 0:
            if count % 2 == 0:	#定义规则:奇数贴1,偶数贴2
                screen.blit(hero2, (mouse[0] - 30, mouse[1] - 30))	#贴飞机2
            else:
                screen.blit(hero1, (mouse[0] - 30, mouse[1] - 30))	#贴飞机1
        else:
            screen.blit(hero_down, (mouse[0]-30, mouse[1]-30))
        if hero_down_display == 0:
                #-------小敌机的出现-------
            if count % 100 == 0:
                xdj1_x.append(random.randint(0, 460))	#添加小敌机x坐标
                xdj1_y.append(0)	#添加小敌机y坐标
                xdj1_blood.append(100)	#添加小敌机血量
                time.sleep(0.01)	#等待0.01秒
                #-------小敌机下落-------
            for i in range(len(xdj1_x)):	#获取所有的y坐标
                xdj1_y[i] += 1	#让小敌机y坐标增加
                screen.blit(xdj1, (xdj1_x[i], xdj1_y[i]))	#贴小敌机
                #-------小敌机消失-------
            for i in range(len(xdj1_x)):
                if xdj1_y[i] > 800:
                    del xdj1_y[i]
                    del xdj1_x[i]
                    break
                #-------中敌机的出现-------
            if count % 200 == 0:
                zdj1_x.append(random.randint(0, 460))	#添加中敌机x坐标
                zdj1_y.append(0)	#添加中敌机y坐标
                zdj1_blood.append(100)	#添加中敌机血量
                #-------中敌机下落-------
            for i in range(len(zdj1_x)):	#获取所有的y坐标
                zdj1_y[i] += 1	#让中敌机y坐标增加
                screen.blit(zdj1, (zdj1_x[i], zdj1_y[i]))	#贴小敌机
                #-------中敌机消失-------
            for i in range(len(zdj1_x)):
                if zdj1_y[i] > 800:
                    del zdj1_y[i]
                    del zdj1_x[i]
                    break
                #-------大敌机的出现-------
            if count % 10000 == 0:
                ddj1_x.append(random.randint(0, 460))	#添加大敌机x坐标
                ddj1_y.append(0)	#添加大敌机y坐标
                ddj1_blood.append(100)	#添加大敌机血量
                #-------大敌机下落-------
            for i in range(len(ddj1_x)):	#获取所有的y坐标
                ddj1_y[i] += 1	#让大敌机y坐标增加
                screen.blit(ddj1, (ddj1_x[i], ddj1_y[i]))	#贴大敌机
                #-------大敌机消失-------
            for i in range(len(ddj1_x)):
                if ddj1_y[i] > 800:
                    del ddj1_y[i]
                    del ddj1_x[i]
                    del ddj1_blood[j]
                    break
                #
            for i in range(len(bullet_x)):     #拿到所有的子弹
                for j in range(len(xdj1_x)):   #拿到所有的小敌机
                    if xdj1_x[j] - 8 < bullet_x[i] < xdj1_x[j] + 42:  # 子弹x坐标有没有小敌机x坐标范围内
                        if xdj1_y[j] - 17 < bullet_y[i] < xdj1_y[j] + 36:  # 子弹x坐标有没有小敌机x坐标范围内
                            xdj1_blood[j] -= 10
                            if xdj1_blood[j] <= 0:
                                screen.blit(xdj2, (xdj1_x[j], xdj1_y[j]))
                                screen.blit(xdj3, (xdj1_x[j], xdj1_y[j]))
                                screen.blit(xdj4, (xdj1_x[j], xdj1_y[j]))
                                score += 10
                                del xdj1_y[j]  # 退出循环
                                del xdj1_x[j]
                                break
            # -dj1 _blood
            for i in range(len(bullet_x)):  # 拿到所有的子弹
                for j in range(len(zdj1_x)):  # 拿到所有的小敌机
                    if zdj1_x[j] - 8 < bullet_x[i] < zdj1_x[j] + 57:  # 子弹x坐标有没有小敌机x坐标范围内
                        if zdj1_y[j] - 17 < bullet_y[i] < zdj1_y[j] + 65:  # 子弹x坐标有没有小敌机x坐标范围内
                            zdj1_blood[j] -= 1
                            if zdj1_blood[j] <= 0:
                                screen.blit(zdj2, (zdj1_x[j], zdj1_y[j]))
                                screen.blit(zdj3, (zdj1_x[j], zdj1_y[j]))
                                screen.blit(zdj4, (zdj1_x[j], zdj1_y[j]))
                                score += 100
                                del zdj1_y[j]  # 退出循环
                                del zdj1_x[j]
                                break
            for i in range(len(bullet_x)):  # 拿到所有的子弹
                for j in range(len(ddj1_x)):  # 拿到所有的小敌机
                    if ddj1_x[j] - 8 < bullet_x[i] < ddj1_x[j] + 66:  # 子弹x坐标有没有小敌机x坐标范围内
                        if ddj1_y[j] - 17 < bullet_y[i] < ddj1_y[j] + 92:  # 子弹x坐标有没有小敌机x坐标范围
                            ddj1_blood[j] -= 0.1
                            if ddj1_blood[j] <= 0:
                                screen.blit(ddj2, (ddj1_x[j], ddj1_y[j]))
                                screen.blit(ddj3, (ddj1_x[j], ddj1_y[j]))
                                screen.blit(ddj4, (ddj1_x[j], ddj1_y[j]))
                                score += 1000
                                del ddj1_y[j]  # 退出循环
                                del ddj1_x[j]
                                del ddj1_blood[j]
                                break
            for i in range(len(xdj1_x)):   #拿到所有的小敌机
                if xdj1_x[i] - 8 < mouse[0] < xdj1_x[i] + 42:  # 子弹x坐标有没有小敌机x坐标范围内
                    if xdj1_y[i] - 17 < mouse[1] < xdj1_y[i] + 36:  # 子弹x坐标有没有小敌机x坐标范围内
                        screen.blit(hero_down, (mouse[0]-30, mouse[1]-30))
                        hero_down_display = 1
                        is_start = 2
                        break

            for i in range(len(zdj1_x)):   #拿到所有的小敌机
                if zdj1_x[i] - 8 < mouse[0] < zdj1_x[i] + 42:  # 子弹x坐标有没有小敌机x坐标范围内
                    if zdj1_y[i] - 17 < mouse[1] < zdj1_y[i] + 36:  # 子弹x坐标有没有小敌机x坐标范围内
                        screen.blit(hero_down, (mouse[0]-30, mouse[1]-30))
                        hero_down_display = 1
                        is_start = 2
                        break

            for i in range(len(ddj1_x)):   #拿到所有的小敌机
                if ddj1_x[i] - 8 < mouse[0] < ddj1_x[i] + 42:  # 子弹x坐标有没有小敌机x坐标范围内
                    if ddj1_y[i] - 17 < mouse[1] < ddj1_y[i] + 36:  # 子弹x坐标有没有小敌机x坐标范围内
                        screen.blit(hero_down, (mouse[0]-30, mouse[1]-30))
                        hero_down_display = 1
                        is_start = 2
                        break
    if is_start == 2:
        screen.blit(gameover, (0, 0))
        pygame.mixer.music.stop()
    if is_start == 3:
        score = 0
        xdj1_x = []
        xdj1_y = []
        xdj1_blood = []
        zdj1_x = []
        zdj1_y = []
        zdj1_blood = []
        ddj1_x = []
        ddj1_y = []
        ddj1_blood = []
        bullet_x = []
        bullet_y = []
        hero_down_display = 0
        is_start = 1
            #-------事件-------
    for event in pygame.event.get():	#退出事件
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:	#键盘按下事件
            if event.key == pygame.K_a:	#a键按下
                flat = 0
                print("单弹模式")
            if event.key == pygame.K_b:	#b键按下
                flat = 1
                print("双弹模式")
            if event.key == pygame.K_c:	#c键按下
                flat = 2
                print("三弹模式")
            if event.key == pygame.K_e:
                exit()
            if event.key == pygame.K_SPACE:
                if is_start == 2:
                    is_start = 3

    pygame.display.update()
