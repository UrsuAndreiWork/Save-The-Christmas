import re
import random


# classes for child gift, and materials


class Child:
    UUID = '1234AV'
    name = 'Alex NewFolder'

    class Adress:
        Country = 'Romania'
        City = 'Galati'
        street = 'Strada Vietii'
        number = '420'

    gifts = []


class Gift:
    def __init__(self, obj, quantity, adjectives, uid):
        self.obj = obj
        self.quantity = quantity
        self.adjectives = adjectives
        self.UID = uid


class Materials:
    plastic = 0
    glass = 0
    textile = 0
    iron = 0
    aluminium = 0
    copper = 0
    gold = 0
    silver = 0
    wood = 0
    porcelain = 0
    rubber = 0
    paper = 0
    groceries = 0


# lists with keywords for searching specific gifts
electronics = ['huawei', 'iphone', 'xiaomi', 'samsung', 'nintendo', 'xbox', 'smartphone', 'console', 'phone', 'tablet',
               'oral-b', 'amd', 'nvidia', 'computer', 'laptop', 'tv', 'monitor', 'keyboard', 'microphone', 'headphones',
               'camera', 'electronic', 'kindle', 'smart', 'robot', 'earphones', 'buds']
food = ['cheese', 'candy', 'fruit', 'chocolate', 'wafers']
textiles = ['pants', 'shirt', 't-shirt', 'dress', 'shorts', 'sandals', 'shoes', 'stiletto', 'wig', 'scarf', 'backpack',
            'handbag', 'pillow', 'blanket', 'slippers', 'hoodie', 'hat', 'sweater', 'jeans', 'plush', 'nike', 'dior',
            'burlon', 'balenciaga', 'adidas', 'versace', 'jordan', 'prada', 'gucci', 'kors', 'chanel', 'lv', 'moschino',
            'zara', 'reserved', 'skirt']
paper = ['poster', 'book', 'giftcard']

# initializing child and materials
MalumaLaurentiu = Child()
MatL = Materials()

# random input for testing the code
MalumaLaurentiu.gifts.append(Gift("zee beez zing toy", "1", "khaki", "1234AV"))
MalumaLaurentiu.gifts.append(Gift("Huawei Media Pad T2 7", "1", "", "1234AV"))
# checking the keywords, first for the object and if that fails for the material -- if that also fails we're making it
# a plastic toy, all values are assigned randomly for variation
for i in MalumaLaurentiu.gifts:
    declassified = 0
    toy = re.split(" ", i.obj)
    for j in toy:
        if j.lower() in electronics:
            declassified = 1
            qtt = random.randrange(10, 18)
            qtt *= int(i.quantity)
            MatL.copper += qtt
            qtt = round(random.uniform(0.01, 1), 2)
            qtt *= int(i.quantity)
            MatL.gold = round(MatL.gold + qtt, 2)
            qtt = round(random.uniform(0.3, 0.6), 2)
            qtt *= int(i.quantity)
            MatL.silver = round(MatL.silver + qtt, 2)
            qtt = random.randrange(100, 500)
            qtt *= int(i.quantity)
            MatL.plastic += qtt
            qtt = random.randrange(10, 50)
            qtt *= int(i.quantity)
            MatL.glass += qtt
            qtt = round(random.uniform(10, 60), 2)
            qtt *= int(i.quantity)
            MatL.iron = round(MatL.iron + qtt, 2)
            break
        elif j.lower() in food:
            declassified = 1
            qtt = random.randrange(500, 2000)
            qtt *= int(i.quantity)
            MatL.groceries += qtt
            break
        elif j.lower() in textiles:
            declassified = 1
            qtt = random.randrange(250, 1000)
            qtt *= int(i.quantity)
            MatL.textile += qtt
            break
        elif j.lower() in paper:
            declassified = 1
            qtt = random.randrange(25, 250)
            qtt *= int(i.quantity)
            MatL.paper += qtt
            break
        elif j.lower() == 'bike' or j.lower() == 'bicycle':
            declassified = 1
            qtt = round(random.uniform(1000, 5000), 2)
            qtt *= int(i.quantity)
            MatL.aluminium = round(MatL.aluminium + qtt, 2)
            qtt = round(random.uniform(500, 750), 2)
            qtt *= int(i.quantity)
            MatL.rubber = round(MatL.rubber + qtt, 2)
            qtt = random.randrange(250, 500)
            qtt *= int(i.quantity)
            MatL.textile += qtt
            break
        elif j.lower() == 'doll':
            declassified = 1
            qtt = random.randrange(10, 20)
            qtt *= int(i.quantity)
            MatL.textile += qtt
            qtt = random.randrange(100, 250)
            qtt *= int(i.quantity)
            MatL.plastic += qtt
            break
        elif j.lower() == 'skateboard' or j.lower() == 'skate':
            declassified = 1
            qtt = random.randrange(450, 900)
            qtt *= int(i.quantity)
            MatL.wood += qtt
            qtt = round(random.uniform(100, 250), 2)
            qtt *= int(i.quantity)
            MatL.iron = round(MatL.iron + qtt, 2)
            qtt = round(random.uniform(100, 150), 2)
            qtt *= int(i.quantity)
            MatL.rubber = round(MatL.rubber + qtt, 2)
            break
    if declassified == 0:
        adj = re.split(" ", i.adjectives)
        for j in adj:
            if j == 'copper':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.copper += qtt
                break
            elif j == 'golden':
                declassified = 1
                qtt = random.randrange(5, 200)
                qtt *= int(i.quantity)
                MatL.gold = round(MatL.gold + qtt, 2)
                break
            elif j == 'silver':
                declassified = 1
                qtt = random.randrange(5, 300)
                qtt *= int(i.quantity)
                MatL.silver = round(MatL.silver + qtt, 2)
                break
            elif j == 'aluminium':
                declassified = 1
                qtt = random.randrange(100, 500)
                qtt *= int(i.quantity)
                MatL.aluminium = round(MatL.aluminium + qtt, 2)
                break
            elif j == 'glass':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.glass = round(MatL.glass + qtt, 2)
                break
            elif j == 'porcelain':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.porcelain = round(MatL.porcelain + qtt, 2)
                break
            elif j == 'rubber':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.rubber = round(MatL.rubber + qtt, 2)
                break
            elif j == 'wooden':
                declassified = 1
                qtt = random.randrange(200, 1000)
                qtt *= int(i.quantity)
                MatL.wood = round(MatL.wood + qtt, 2)
                break
    if declassified == 0:
        qtt = random.randrange(200, 600)
        qtt *= int(i.quantity)
        MatL.plastic += qtt

# random print to check the values
print(MatL.plastic, MatL.glass, MatL.textile, MatL.iron, MatL.aluminium, MatL.copper, MatL.gold, MatL.silver, MatL.wood,
      MatL.porcelain, MatL.rubber, MatL.paper, MatL.groceries)
