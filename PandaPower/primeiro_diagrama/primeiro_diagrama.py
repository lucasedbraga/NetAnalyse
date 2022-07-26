import pandapower as pp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando a rede (ambiente)
net = pp.create_empty_network()
# Criando as barras
b1 = pp.create_bus(net, vn_kv=20, name='B1')
b2 = pp.create_bus(net, vn_kv=0.4, name='B2')
b3 = pp.create_bus(net, vn_kv=0.4, name='B3')
b4 = pp.create_bus(net, vn_kv=0.4, name='B4')
b5 = pp.create_bus(net, vn_kv=0.4, name='B5')
# Criar Rede Externa
pp.create_ext_grid(net, bus=b1, vm_pu=1)
# Criando cargas
l1 = pp.create_load(net, bus=b4, p_mw=0.3, q_mvar=0.3)
l2 = pp.create_load(net, bus=b5, p_mw=0.2, q_mvar=0.1)
# Criando Trafos
t1 = pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name='T1')
t2 = pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name='T2')
# Criando as linhas
linha23 = pp.create_line(net, from_bus=b2, to_bus=b3, name="l23", std_type="NAYY 4x50 SE", length_km=0.01)
linha34 = pp.create_line(net, from_bus=b3, to_bus=b4, name="l34", std_type="NAYY 4x50 SE", length_km=0.05)
linha35 = pp.create_line(net, from_bus=b3, to_bus=b5, name="l35", std_type="NAYY 4x50 SE", length_km=0.09)
# Rodando o Power Flow
res = pp.runpp(net)
results = net.res_bus
print(results)
#Verificando Resultados sem Correção
v_pu_limit = 0.92
v_calc = list(results.vm_pu)
plt.figure(figsize=(15,5))
plt.suptitle('Tensões em pu')
plt.subplot(1, 2, 1)
plt.plot(np.ones(len(v_calc))*v_pu_limit, linestyle='dashed', color='red')
plt.plot(v_calc, marker='o', color='blue')
# Corrigindo
cap = pp.create_shunt(net, bus=b3, q_mvar=-1.0)
res_corrigido = pp.runpp(net)
results_corrigido = net.res_bus
v_calc_c = list(results_corrigido.vm_pu)
print(results_corrigido)
plt.subplot(1, 2, 2)
plt.plot(np.ones(len(v_calc_c))*v_pu_limit, linestyle='dashed', color='red')
plt.plot(v_calc_c, marker='o', color='blue')
plt.show()