int_var=10
float_var=6.8
str_var="78"

new_str_var=str(int_var)
new_int_var=int(float(float_var))
new_float_var=float(str_var)

print("new string", new_str_var)
print("net integer", new_int_var)
print("new float", new_float_var)