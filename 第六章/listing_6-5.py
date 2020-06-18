# Listing_6-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# 使用EasyGui进行数字猜谜游戏

import random, easygui
secret = random.randint(1, 99)         # 精选秘密数字
guess = 0
tries = 0
easygui.msgbox("""AHOY!  I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99.  I'll give you 6 tries.""")

# Allows up to 6 guesses                     #最多允许6个猜测
while guess != secret and tries < 6:
    guess = easygui.integerbox("What's yer guess, matey?")      # 获取玩家的猜想
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries = tries + 1       # 用完一次 try

# Prints message at end of game               #在游戏结束时打印消息
if guess == secret:
    easygui.msgbox("Avast! Ye got it!  Found my secret, ye did!")
else:
    easygui.msgbox("No more guesses!  The number was " + str(secret))
