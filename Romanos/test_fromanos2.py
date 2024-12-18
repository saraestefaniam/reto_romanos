from Romanos import fromanos2
import pytest 

def test_to_roman():
    assert fromanos2.to_roman(29) == "XXIX"
    assert fromanos2.to_roman(1939) == "MCMXXXIX"
    assert fromanos2.to_roman(1982) == "MCMLXXXII"
    assert fromanos2.to_roman(800) == "DCCC"
    assert fromanos2.to_roman(0) == None
    assert fromanos2.to_roman(5000) == None

def test_to_arabigo():
    assert fromanos2.to_arabigo("MCMXCIV") == 1994
    assert fromanos2.to_arabigo("MCMLXXXIX") == 1989

    #como puede ser un ValueError causado por ota cosa
    #podemos comprobar que efectivamente es un value error que dice "no es símbolo romano"
    #le podemos decir que capture el error y lo meta en una variable que llamaremos contexto
def test_validar_que_sea_romano():
    with pytest.raises(ValueError) as contexto:
        fromanos2.to_arabigo("ZTW")
        assert str(contexto.value).endswith("no es un símbolo romano")

#validamos si tienen más de tres repeticiones caracteres que no deberían tenerlo (X,I,C,M)
#luego de tener esta función creada veremos como aplicarla en la función to_roman
def test_validar_repeticiones_más_de_tres():
    assert fromanos2.check_repetition("XI") == False
    assert fromanos2.check_repetition("IIIII") == True
    assert fromanos2.check_repetition("IV") == False
    assert fromanos2.check_repetition("XXXX") == True

#validamos que lance un error cuando efectivamente se repitan más de tres veces caracteres que no deberían
def test_validar_romano_con_cuatro_repeticiones():
    with pytest.raises(ValueError) as contexto:
        fromanos2.to_arabigo("MCCCCXXII")
    assert str(contexto.value).endswith("es un número inválido")

#ahora validamos caracteres que no deberían tener más de una repetición (V, L, D)
def test_validar_repeticiones_de_más_de_1():
    assert fromanos2.check_repetition("VV") == True
    assert fromanos2.check_repetition("LL") == True
    assert fromanos2.check_repetition("DD") == True
    assert fromanos2.check_repetition("D") == False

def test_validar_romanos_sin_repeticiones():
    with pytest.raises(ValueError) as contexto:
        fromanos2.to_arabigo("MCCVV")
    assert str(contexto.value).endswith("es un número inválido")

#corroborar las restas permitidas, si no lo son lanza error
#restas permitidas: (IV, IX, XL, XC, CD, CM)
def test_sustracciones_permitidas():
    with pytest.raises(ValueError) as contexto:
        fromanos2.to_arabigo("VC")
    assert str(contexto.value).endswith("no es una expresión correcta")

#CMCM repetir la resta de CM no se debe permitir y así con otras
#además una vez que he hecho una resta solo puedo sumar de los valores inferiores, no de los superiores
#es decir esto está mal XCM (XC ya es 90 que después de eso venga una M que es 1000 es incorrecto)
#XCXC -> error
def test_no_repetir_restas():
    with pytest.raises(ValueError):
        fromanos2.to_arabigo("XCXC")

#XCXL, CMCD-> error
def test_no_restas_mismo_tipo_unidades():
    with pytest.raises(ValueError):
        fromanos2.to_arabigo("CMCD")


#Ahora, no podemos permitir sumas de valores superiores cuando hemos hecho una resta
#Por ejemplo, tenemos XCX = XC es 90, por lo que después sumar un 10 no tiene sentido ya que sería 100 y para eso tenemos la C
#XCX, XCL
def test_no_sumar_mismo_grupo_despues_de_resta():
    with pytest.raises(ValueError):
        fromanos2.to_arabigo("XCX")

#Caso en el que queremos restar centenas a unidades o milenas a centenas o centenas a decenas
#IXC
def test_restas_erroneas():
    with pytest.raises(ValueError):
        fromanos2.to_arabigo("IXC")

def test_constructor_entero_clase_Romana():
    rn = fromanos2.Roman_Number(8)
    assert rn.valor == 8
    assert rn.representation == "VIII"

def test_str_romanos():
    rn = fromanos2.Roman_Number(9)
    assert str(rn) == "IX"

def test_compara_iguales():
    assert fromanos2.Roman_Number(18) == fromanos2.Roman_Number("XVIII")

def test_compara_mayor():
    pass

def test_compara_menor():
    pass

def test_suma_romanos_con_romanos():
    assert fromanos2.Roman_Number("X") + fromanos2.Roman_Number("V") == fromanos2.Roman_Number("XV")

def test_suma_romanos_con_enteros():
    assert fromanos2.Roman_Number("X") + fromanos2.Roman_Number(5) == fromanos2.Roman_Number("XV")

def test_suma_enteros_con_enteros():
    rn = fromanos2.Roman_Number(5)
    on = fromanos2.Roman_Number(10)

    assert rn + on == fromanos2.Roman_Number("XV")

def test_suma_romanos_con_otra_cosa():
    #TypeError
    pass



