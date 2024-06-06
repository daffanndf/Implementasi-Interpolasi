import matplotlib.pyplot as plt

# Data tegangan dan waktu patah
x_data = [5, 10, 15, 20, 25, 30, 35, 40]
y_data = [40, 30, 25, 40, 18, 20, 22, 15]

# Fungsi untuk menghitung nilai interpolasi polinomial Lagrange pada titik x.
def Lagrange(x, x_data, y_data):
    n = len(x_data)
    result = 0.0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

# Fungsi untuk menghitung nilai interpolasi polinomial Newton pada titik x.
def Newton(x, x_data, y_data):
    n = len(x_data)
    divided_diff = [y for y in y_data]

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            divided_diff[j] = (divided_diff[j] - divided_diff[j-1]) / (x_data[j] - x_data[j-i])
    
    result = divided_diff[n-1]
    for i in range(n-2, -1, -1):
        result = result * (x - x_data[i]) + divided_diff[i]
    
    return result

# Rentang untuk interpolasi 5 <= x <= 40
x_interp = [i for i in range(5, 41)]
y_interp_Lagrange = [Lagrange(xi, x_data, y_data) for xi in x_interp]
y_interp_Newton = [Newton(xi, x_data, y_data) for xi in x_interp]

# Plot grafik
plt.plot(x_data, y_data, 'o', label='Data Asli')
plt.plot(x_interp, y_interp_Lagrange, label='Interpolasi Lagrange')
plt.plot(x_interp, y_interp_Newton, label='Interpolasi Newton')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinomial Lagrange dan Newton')
plt.legend()
plt.grid(True)
plt.xlim(5, 40)
plt.show()

