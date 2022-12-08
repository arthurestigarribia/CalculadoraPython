import math

class Operacoes():
	def __init__(self, a, b):
		self.a = a
		self.b = b

		self.casas_decimais = 10
	
	def operacao_soma(self):
		try:
			return round(self.a + self.b, self.casas_decimais)
		except Exception as e:
			return math.nan

	def operacao_subtracao(self):
		try:
			return round(self.a - self.b, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def operacao_multiplicacao(self):
		try:
			return round(self.a * self.b, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def operacao_divisao(self):
		try:
			return round(self.a / self.b, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def operacao_resto(self):
		try:
			return round(self.a % self.b, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def operacao_potencia(self):
		try:
			return round(self.a ** self.b, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def porcentagem_taxa(self):
		try:
			return round(self.operacao_multiplicacao() / 100, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def porcentagem_aumento(self):
		try:
			return round(self.a + self.porcentagem_taxa(), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def porcentagem_desconto(self):
		try:
			return round(self.a - self.porcentagem_taxa(), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def bhaskara_delta(self):
		try:
			return round(self.a ** 2 - 4 * self.b, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def bhaskara_raiz1(self):
		try:
			return round((- self.a + math.sqrt(self.bhaskara_delta())) / 2, self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def bhaskara_raiz2(self):
		try:
			return round((- self.a - math.sqrt(self.bhaskara_delta())) / 2, self.casas_decimais)
		except Exception as e:
			return math.nan

	def funcao_sqrt(self):
		try:
			return round(math.sqrt(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def funcao_abs(self):
		try:
			return round(math.abs(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def funcao_exp(self):
		try:
			return round(math.exp(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def funcao_loge(self):
		try:
			return round(math.log(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def funcao_log10(self):
		try:
			return round(math.log10(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def trigonometria_sin(self):
		try:
			return round(math.sin(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_cos(self):
		try:
			return round(math.cos(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def trigonometria_tan(self):
		try:
			return round(math.tan(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_sinh(self):
		try:
			return round(math.sinh(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_cosh(self):
		try:
			return round(math.cosh(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def trigonometria_tanh(self):
		try:
			return round(math.tanh(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_asin(self):
		try:
			return round(math.asin(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_acos(self):
		try:
			return round(math.acos(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def trigonometria_atan(self):
		try:
			return round(math.atan(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_asinh(self):
		try:
			return round(math.asinh(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan

	def trigonometria_acosh(self):
		try:
			return round(math.acosh(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def trigonometria_atanh(self):
		try:
			return round(math.atanh(self.a), self.casas_decimais)
		except Exception as e:
			return math.nan
	
	def combinatoria_fatorial(self):
		try:
			if self.a == 0 or self.a == 1:
				return 1
			elif self.a % 1 != 0:
				return math.nan
			
			fat = 1

			for i in range(1, self.a + 1):
				fat = fat * i

			return round(fat, 10)
		except Exception as e:
			return math.nan
	
	def combinatoria_permutacao(self):
		try:
			if (self.a - self.b) < 0:
				return math.nan
			else:
				resp = self.combinatoria_fatorial(self.a) / self.combinatoria_fatorial(self.a - self.b)

				return round(resp, 10)
		except Exception as e:
			return math.nan
	
	def combinatoria_combinacao(self):
		try:
			if (self.a - self.b) < 0:
				return math.nan
			else:
				resp = self.combinatoria_permutacao(self.a) / self.combinatoria_fatorial(self.b)

				return round(resp, 10)
		except Exception as e:
			return math.nan