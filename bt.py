import requests, time

class Bt24:
    def __init__(self, dicthonparams, accses_toking):
        self.dicthon = dicthonparams
        self.accses_toking = accses_toking

    def send(self):
        try:
            requests.post(self.accses_toking, json=self.dicthon)
        except requests.ConnectionError as error:
            time.sleep(120)
            self.send()
        except requests.HTTPError as error:
            print('HTTP =>', error)