salarioBruto = float(input)("Salário: ").replace("," , ".")
if slarioBruto >= 2000:
    desconto = salarioBruto * 0.11
else: 
    desconto = salarioBruto *0.99
    salarioFinal = salarioBruto - desconto
print(f"Salário: {salarioBruto:.2f}")
print(f"Desconto: {salarioBruto:.2f}")
print(f"Salário Final: {salarioBruto:.2f}")
