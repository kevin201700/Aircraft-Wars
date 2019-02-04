#kevin.lee@56tech.wang
import pygame,time,random   #导入pygame,时间，随机数等工具箱,

pygame.init()   #pygame初始化

#-------------新建窗口---------------
sc = pygame.display.set_mode((460,800))       

#-----------贴背景---------------
bg = pygame.image.load('背景.png')      #加载图片

bg = pygame.transform.scale(bg,(460,800))



#----------贴英雄机   大小(60,60)--------
hero1 = pygame.image.load('我方飞机1.png')     #导入英雄机

hero1 = pygame.transform.scale(hero1,(60,60))   #改变英雄机大小

hero2  = pygame.image.load('我方飞机2.png')

hero2 = pygame.transform.scale(hero2,(60,60))

hero_down = pygame.image.load('我方飞机爆炸.png')

hero_down = pygame.transform.scale(hero_down,(60,60))

#------------------------------------------------------------------------------------------------------------------小敌机-------（42,36）

xdj1 =pygame.image.load('小飞机.png')

xdj1 = pygame.transform.scale(xdj1,(42,36))

xdj2 =pygame.image.load('小飞机爆炸1.png')

xdj2 = pygame.transform.scale(xdj2,(42,36))

xdj3 =pygame.image.load('小飞机爆炸2.png')

xdj3 = pygame.transform.scale(xdj3,(42,36))

xdj4 =pygame.image.load('小飞机爆炸3.png')

xdj4 = pygame.transform.scale(xdj4,(42,36))

xdj1_x = []           #新建小敌机x列表

xdj1_y = []           #新建小敌机y列表


#----------------------------------------------------------------------------------------------------------------中低级（57,65）------
#zdj1

#zdj2

#zdj3

#zdj4




#-------------------------------------------------------------------------------------------------------------------大敌机(66,92)----
#ddj1

#ddj2

#ddj3


#ddj4


#------------------------------------------------------导入子弹（8,17）--------------------------------------------------------------------

bullet = pygame.image.load('子弹.png')

bullet = pygame.transform.scale(bullet,(8,17))

bullet_x = []

bullet_y = []



#-----------------------------------------------------------------------------------------------------------------------------------
count = 0        #计算执行多少次


#---------标识符------------
flat = 0           #0  -  1颗子弹     1 -  2颗子弹     2 -----   3颗子弹



#---------------英雄机造型切换----------
while True:
    mouse= pygame.mouse.get_pos()    #获取鼠标位置
    

    sc.blit(bg,(0,0))                   #贴背景图片
    
    time.sleep(0.01)     #等待0.01秒

    count = count + 1



#----------------------------------------------------------子弹飞-----------------------------------------------------------------------------
    if count % 1 ==0:                        #0.5s生成一颗子弹

        if flat ==0:
            bullet_x.append(mouse[0]-30)             #添加子弹的x坐标

            bullet_y.append(mouse[1])             #添加子弹的x坐标

        if flat ==1:

            bullet_x.append(mouse[0]-30)             #添加子弹的x坐标

            bullet_y.append(mouse[1])             #添加子弹的x坐标


            bullet_x.append(mouse[0]+25)             #添加子弹的x坐标

            bullet_y.append(mouse[1])             #添加子弹的x坐标

        if flat ==2:


            
            bullet_x.append(mouse[0]-30)             #添加子弹的x坐标

            bullet_y.append(mouse[1])             #添加子弹的x坐标


            bullet_x.append(mouse[0]+25)             #添加子弹的x坐标

            bullet_y.append(mouse[1])             #添加子弹的x坐标


            bullet_x.append(mouse[0])             #添加子弹的x坐标

            bullet_y.append(mouse[1])             #添加子弹的x坐标



    for i in range(len(bullet_x)):

        bullet_y[i]  -= 5

        sc.blit(bullet,(bullet_x[i],bullet_y[i]))
    

    #子弹消失
    
    for i in range(len(bullet_x)):

        if bullet_y[i] < 0:        #子弹有没有到达窗口最上方

            del bullet_y[i]          #删除对应子弹y坐标

            del bullet_x[i]          #删除对应子弹x坐标

            break    


    


#-----------------------------------------------------英雄机-------------------------------------------------------------------------

    if count % 2 ==0:               #   定义规则： 奇数贴1，偶数贴2

        sc.blit(hero2,(mouse[0]-30,mouse[1]-30))    #贴飞机2
    
    if count % 2 !=0:

        sc.blit(hero1,(mouse[0]-30,mouse[1]-30))    #贴飞机1



        

#------------------------------------------------------------------------小敌机的代码----------------------------------------------------
    #小敌机的出现

    if count % 100 == 0:

        xdj1_x.append(random.randint(0,460))       #添加小敌机x坐标

        xdj1_y.append(0)                       #添加小敌机y坐标

    #敌机下落

    for i in range(len(xdj1_x)):      #获取所有的y
        
        xdj1_y[i] +=  1                   #让小敌机y坐标增加

        sc.blit(xdj1,(xdj1_x[i],xdj1_y[i]))    #贴小敌机

    #小敌机消失
    
    for i in range(len(xdj1_x)):

        if xdj1_y[i] > 800:        #小敌机有没有到达窗口最下方

            del xdj1_y[i]          #删除对应小敌机y坐标

            del xdj1_x[i]          #删除对应小敌机x坐标

            break


#---------------------------------------------------------------------中敌机------------------------------------------------------------





#---------------------------------------------------------------------大敌机-----------------------------------------------------------



#-----------------------------------------------------------------小敌机爆炸-----------------------------------------------------------
    for i in range(len(bullet_x)):     #拿到所有的子弹

        for j in range(len(xdj1_x)):   #拿到所有的小敌机

            if  xdj1_x[j]-8<bullet_x[i]<xdj1_x[j]+42:   #子弹x坐标有没有小敌机x坐标范围内

                if xdj1_y[j]-17 < bullet_y[i]<xdj1_y[j]+ 36:  #子弹x坐标有没有小敌机x坐标范围内

                    sc.blit(xdj2,(xdj1_x[j],xdj1_y[j]))

                    sc.blit(xdj3,(xdj1_x[j],xdj1_y[j]))

                    sc.blit(xdj4,(xdj1_x[j],xdj1_y[j]))

                    del xdj1_y[j]                          #退出循环

                    del xdj1_x[j]

                    break
# -dj1 _blood


#    for i in range(len(bullet_x)):     #拿到所有的子弹

#        for j in range(len(zdj1_x)):   #拿到所有的小敌机

 #           if  zdj1_x[j]-8<bullet_x[i]<zdj1_x[j]+57:   #子弹x坐标有没有小敌机x坐标范围内

  #              if zdj1_y[j]-17 < bullet_y[i]<zdj1_y[j]+ 65:  #子弹x坐标有没有小敌机x坐标范围内

#                    sc.blit(zdj2,(zdj1_x[j],zdj1_y[j]))
#
 #                   sc.blit(zdj3,(zdj1_x[j],zdj1_y[j]))
#
 #                   sc.blit(zdj4,(zdj1_x[j],zdj1_y[j]))
#
   #                 del zdj1_y[j]                          #退出循环

    #                del zdj1_x[j]

     #               break


    #for i in range(len(bullet_x)):     #拿到所有的子弹

     #   for j in range(len(ddj1_x)):   #拿到所有的小敌机

      #      if  ddj1_x[j]-8<bullet_x[i]<ddj1_x[j]+66:   #子弹x坐标有没有小敌机x坐标范围内

       #         if ddj1_y[j]-17 < bullet_y[i]<dzdj1_y[j]+ 92:  #子弹x坐标有没有小敌机x坐标范围内

#                    sc.blit(ddj2,(ddj1_x[j],ddj1_y[j]))
#
 #                   sc.blit(ddj3,(ddj1_x[j],ddj1_y[j]))
#
 #                   sc.blit(ddj4,(ddj1_x[j],ddj1_y[j]))
 
        #            del ddj1_y[j]                          #退出循环

         #           del ddj1_x[j]

          #          break
#---------------------------------------------------------------------------------------------------------事件-------------------------

    for event in pygame.event.get():      #获取所有的事件

        if event.type  == pygame.QUIT:    #退出事件

            pygame.quit()

            exit()           


#---------------------------------------------------------------------------------------------------------键盘事件--------------------        
        if event.type == pygame.KEYDOWN:   #键盘按下事件

            if event.key == pygame.K_q:      #q键按下

                flat = 0

            if event.key == pygame.K_w:      #w键按下

                flat = 1

            if event.key == pygame.K_e:      #e键按下

                flat = 2


            













    pygame.display.update()
