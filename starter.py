from main import WallHack

wh_client = WallHack(switch=True) # default value: True. If you need disable WH you can set switch=False

if __name__ == '__main__':
    data = wh_client.start()

print(data) # Just "log"
