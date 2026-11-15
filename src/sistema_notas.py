def calcular_media(nota1, nota2):
	return (nota1+nota2)/2

def verificar_situacao(media):
	if media >= 8:
		return "Aprovado"
	elif media >= 5:
		return "Recuperacao"
	else:
		return "Reprovado"
