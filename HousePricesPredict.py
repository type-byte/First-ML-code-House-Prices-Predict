data = []
with open("housePricesDataset.csv", "r", encoding="utf-8") as f:
    header = f.readline()
    for line in f.readlines():
        row = line.strip().split(",")
        data.append(row)


X, Y = [], []
for row in data:
    area = float(row[0])
    room = float(row[1])
    price = float(row[2])
    X.append([area, room])
    Y.append(price)

areas = [x[0] for x in X]
rooms = [x[1] for x in X]

max_area = max(areas)
max_room = max(rooms)
max_price = max(Y)

Xn = []
Yn = []

for i in range(len(X)):
    Xn.append([
        X[i][0] / max_area,
        X[i][1] / max_room
    ])
    Yn.append(Y[i] / max_price)

w1, w2, b = 0, 0, 0
rate = 0.01
epochs = 1000

for epoch in range(epochs):
    dw1, dw2, db = 0, 0, 0
    n = len(Xn)

    for i in range(n):
        predPrice = w1 * Xn[i][0] + w2 * Xn[i][1] + b
        error = predPrice - Yn[i]
        dw1 += error * Xn[i][0]
        dw2 += error * Xn[i][1]
        db += error

    dw1 /= n
    dw2 /= n
    db /= n

    w1 -= rate * dw1
    w2 -= rate * dw2
    b -= rate * db

    if epoch % 10 == 0:
        loss = 0
        for i in range(n):
            loss += (w1 * Xn[i][0] + w2 * Xn[i][1] + b - Yn[i]) ** 2
        loss /= n
        print(f"Эпоха {epoch}, ошибка {loss:.2f}")

newArea, newRoom = map(int, input("Введите площадь и количество комнат интересующей квартиры: \n").split())

newArea_n = newArea / max_area
newRoom_n = newRoom / max_room

priceNewPrediction = (w1 * newArea_n + w2 * newRoom_n + b) * max_price


print(f"Приблизительная стоимость квартиры будет составлять: {priceNewPrediction:.2f}")