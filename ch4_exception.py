# exception handing
'''
try: # 把想捕捉的code區段放入try
    with open('f.txt', 'r') as f: 
        for line in f:
            x = int(line.strip())
except FileNotFoundError as err: 
    print(err)
except ValueError: # try至少接一個except
    print('fail to convert a string to an integer')
else: # 若沒捕捉到error, 會跑到else
    print('no exception caught')
finally: # 不管有無error, 最後一定會執行finally
    print('Must run here')
'''
i = 0
err_count = 0
while True:
    try:
        s = input('enter a number:')
        n = int(s)
        print(f'Good, you entered{n}')
    except ValueError:
        err_count += 1
        if err_count >= 3:
            print('錯誤已經3次')
            break
        print('You should enter a number')
    except KeyboardInterrupt:
        print('Gameover')
        break
    finally:
        i += 1
        print(f'這是第{i}次玩')