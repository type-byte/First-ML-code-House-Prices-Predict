import matplotlib.pyplot as plt

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

Xn = []

for i in range(len(X)):
    Xn.append([
        X[i][0] / max_area,
        X[i][1] / max_room
    ])

w1, w2, b = 0, 0, 0
rate = 0.01
epochs = 1000

for epoch in range(epochs):
    dw1, dw2, db = 0, 0, 0
    n = len(Xn)

    for i in range(n):
        predPrice = w1 * Xn[i][0] + w2 * Xn[i][1] + b
        error = predPrice - Y[i]
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
            loss += (w1 * Xn[i][0] + w2 * Xn[i][1] + b - Y[i]) ** 2
        loss /= n
        print(f"Эпоха {epoch}, ошибка {loss:.2f}")


# ===== Визуализация =====

areas_plot = areas
rooms_plot = rooms
prices_plot = Y

area_vals = [min(areas_plot), max(areas_plot)]
room_vals = [min(rooms_plot), max(rooms_plot)]

area_grid = []
room_grid = []
price_grid = []

for a in area_vals:
    for r in room_vals:
        a_n = a / max_area
        r_n = r / max_room
        p_n = w1 * a_n + w2 * r_n + b
        p = p_n

        area_grid.append(a)
        room_grid.append(r)
        price_grid.append(p)

# 3D-график
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(areas_plot, rooms_plot, prices_plot, label="Реальные данные")
ax.plot_trisurf(area_grid, room_grid, price_grid, alpha=0.5)

ax.set_xlabel("Площадь")
ax.set_ylabel("Комнаты")
ax.set_zlabel("Цена")

plt.legend()
plt.show()

# ===== Конец Визуализации =====

newArea, newRoom = map(int, input("Введите площадь и количество комнат интересующей квартиры: \n").split())

newArea_n = newArea / max_area
newRoom_n = newRoom / max_room

priceNewPrediction = w1 * newArea_n + w2 * newRoom_n + b


print(f"Приблизительная стоимость квартиры будет составлять: {priceNewPrediction:.2f}")
