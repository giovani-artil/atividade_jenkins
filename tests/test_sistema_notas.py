from src.sistema_notas import calcular_media
from src.sistema_notas import verificar_situacao

def test_calcular_media_1():
	assert calcular_media(10,8) == 9

def test_calular_media_2():
	assert calcular_media(2,4) == 6

def test_aprovado():
	assert verificar_situacao(9) == "Aprovado"

def test_reprovado():
	assert verificar_situacao(4) == "Reprovado"
