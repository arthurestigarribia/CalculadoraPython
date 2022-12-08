import tkinter as tk
import operacoes as op

def resposta():
	try:
		a = float(e1.get())
		b = float(e2.get())

		o = op.Operacoes(a, b)

		resultado = {
			'operacao_soma': o.operacao_soma(),
			'operacao_subtracao': o.operacao_subtracao(),
			'operacao_multiplicacao': o.operacao_multiplicacao(),
			'operacao_divisao': o.operacao_divisao(),
			'operacao_resto': o.operacao_resto(),
			'operacao_potencia': o.operacao_potencia(),
			'porcentagem_taxa': o.porcentagem_taxa(),
			'porcentagem_aumento': o.porcentagem_aumento(),
			'porcentagem_desconto': o.porcentagem_desconto(),
			'bhaskara_delta': o.bhaskara_delta(),
			'bhaskara_raiz_1': o.bhaskara_raiz1(),
			'bhaskara_raiz_2': o.bhaskara_raiz2(),
			'funcao_sqrt_a': o.funcao_sqrt(),
			'funcao_abs_a': o.funcao_abs(),
			'funcao_exp_a': o.funcao_exp(),
			'funcao_loge_a': o.funcao_loge(),
			'funcao_log10_a': o.funcao_log10(),
			'trigonometria_sin_a': o.trigonometria_sin(),
			'trigonometria_cos_a': o.trigonometria_cos(),
			'trigonometria_tan_a': o.trigonometria_tan(),
			'trigonometria_asin_a': o.trigonometria_asin(),
			'trigonometria_acos_a': o.trigonometria_acos(),
			'trigonometria_atan_a': o.trigonometria_atan(),
			'trigonometria_sinh_a': o.trigonometria_sinh(),
			'trigonometria_cosh_a': o.trigonometria_cosh(),
			'trigonometria_tanh_a': o.trigonometria_tanh(),
			'trigonometria_asinh_a': o.trigonometria_asinh(),
			'trigonometria_acosh_a': o.trigonometria_acosh(),
			'trigonometria_atanh_a': o.trigonometria_atanh(),
			'combinatoria_fat_a': o.combinatoria_fatorial(),
			'combinatoria_perm': o.combinatoria_permutacao(),
			'combinatoria_comb': o.combinatoria_combinacao(),
		}
		
		t = ''

		for i in resultado:
			try:
				t += str(i) + ' = ' + str(round(resultado[i], 10)) + '\n'
			except ValueError as e:
				t += str(i) + ' = ' + 'erro' + '\n'

		resp['text'] = t
	except Exception as e:
		resp['text'] = 'Entradas inválidas'

app = tk.Tk()
app.title('Calculadora Mágica')

form = tk.Frame(master=app, width=300)

intro = tk.Label(master=form, text='Digite dois números:', width=300)
e1 = tk.Entry(master=form, width=300)
e2 = tk.Entry(master=form, width=300)
calc = tk.Button(master=form, text='Calcular', command=resposta, width=300)
resp = tk.Label(master=form, text='Digite dois números válidos e selecione o botão Calcular.', width=300)

form.pack()

intro.pack()
e1.pack()
e2.pack()
calc.pack()
resp.pack()

app.mainloop()