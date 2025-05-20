# Başlanğıc yaxınlaşma
x = 1.0  
tol = 1e-6  # Tolerans
max_iter = 100

for i in range(max_iter):
    fx = x**5 - x - 2
    dfx = 5 * x**4 - 1
    
    if dfx == 0:
        print("Törəmə sıfır oldu, metod dayandırıldı.")
        break

    x_new = x - fx / dfx
    print(f"x{i+1} = {x_new:.6f}")

    if abs(x_new - x) < tol:
        print(f"\nYakın kök c₀ təxminən: {x_new:.6f}")
        break
    
    x = x_new
