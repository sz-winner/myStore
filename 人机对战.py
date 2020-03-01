#人机PK小游戏，随机生成血量和攻击力，三盘两胜
import time, random
while True:
    player_score = 0
    enemy_score = 0
    for i in range(1, 4):
        player_life = random.randint(100, 150)
        player_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)
        print('-------------------------')
        #print('玩家属性值：【血量 '+str(player_life)+',攻击力 '+str(player_attack)+'】')
        #print('【玩家】\n血量 %d \n攻击 %d ' % (player_life, player_attack))
        print('【玩家】\n血量 {} \n攻击 {} '.format(player_life, player_attack))
        print('                         ')
        #print('敌人属性值：【血量 '+str(enemy_life)+',攻击力 '+str(enemy_attack)+'】')
        #print('【敌人】\n血量 %d \n攻击 %d ' % (enemy_life, enemy_attack))
        print('【敌人】\n血量 {} \n攻击 {} '.format(enemy_life, enemy_attack))
        print('-------------------------')
        print('                         ')
        time.sleep(1)

        n = 1
        while (player_life > 0) and (enemy_life > 0):
            #print('-----第'+str(i)+'局第'+str(n)+'回合----')
            #print('-----第%s局第%s回合----' % (i, n))
            print('-----第{}局第{}回合----'.format(i, n))
            player_life = player_life - enemy_attack
            if player_life <= 0:
                player_life = 0
            enemy_life = enemy_life - player_attack
            if enemy_life <= 0:
                enemy_life = 0
            print('【玩家】向【敌人】发起攻击，【敌人】血量减少{}，剩余血量{} '.format(
                player_attack, enemy_life))
            print('【敌人】向【玩家】发起攻击：【玩家】血量减少{}，剩余血量{} '.format(
                enemy_attack, player_life))
            print('-------------------------')
            n = n + 1
            time.sleep(1)

        if (player_life > 0) and (enemy_life <= 0):
            player_score += 3
            print('恭喜【玩家】，第{}局获胜！'.format(i))
            print('当前比分 \n【玩家】：【敌人】 {}：{}'.format(player_score, enemy_score))
            time.sleep(1)
        elif (player_life <= 0) and (enemy_life > 0):
            enemy_score += 3
            #print('很遗憾，第%d局失败！' % i)
            print('很遗憾，第{}局失败！'.format(i))
            #print('当前比分 \n【玩家】：【敌人】 %d：%d' % (player_score, enemy_score))
            print('当前比分 \n【玩家】：【敌人】 {}：{}'.format(player_score, enemy_score))
            time.sleep(1)
        else:
            player_score += 1
            enemy_score += 1
            #print('第%d局双方打成平手' % i)
            print('第{}局双方打成平手'.format(i))
            #print('当前比分 \n【玩家】：【敌人】 %d：%d' % (player_score, enemy_score))
            print('当前比分 \n【玩家】：【敌人】{}：{}'.format(player_score, enemy_score))
            print('                         ')
        time.sleep(1.5)
    if player_score > enemy_score:
        #print('【玩家】获胜！最终比分\n【玩家】：【敌人】 %d：%d' % (player_score, enemy_score))
        print('【玩家】获胜！最终比分\n【玩家】：【敌人】 {}：{}'.format(player_score, enemy_score))
    elif player_score < enemy_score:
        #print('最终比分【玩家：敌人】【'+str(player_score)+'：'+str(enemy_score)+'】，敌人获胜！')
        #print('【敌人】获胜！最终比分\n【玩家】：【敌人】 %d：%d' % (player_score, enemy_score))
        print('【敌人】获胜！最终比分\n【玩家】：【敌人】 {}：{}'.format(player_score, enemy_score))
    else:
        #print('最终比分【玩家：敌人】【'+str(player_score)+'：'+str(enemy_score)+'】，双方打平！')
        #print('双方打平！最终比分\n【玩家】：【敌人】 %d：%d' % (player_score, enemy_score))
        print('双方打平！最终比分\n【玩家】：【敌人】 {}：{}'.format(player_score, enemy_score))
    print('                      ')
    a1 = input('要继续游戏吗？收入n或N退出，其它字母则继续')
    if a1 in ('n', 'N'):
        print('----退出游戏！----')
        time.sleep(1.5)
        break
    else:
        print('----继续游戏！----')
        time.sleep(1.5)
