class church:
    def __init__(self, name, location):
        self.name = name
        self.location = location


dunamis = church("dunamis", "benincity")
lfc = church("livingfaith", "lagos")
rccg = church("redeem", "lagos")

print(rccg.name)