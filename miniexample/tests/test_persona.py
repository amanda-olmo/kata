# Python libraries
import pytest
import datetime
# Own libraries
from src.persona import Persona

class TestPersona:
    def test_prueba(self):
        assert 0 == 0

    def test_constructor(self):
        persona = Persona(nombre = 'Pepa', edad = 25)
        assert persona.dar_nombre() == 'Pepa'
        assert persona.dar_edad() == 25
    
    def test_asignacion(self):
        persona = Persona(nombre = 'Pepa', edad = 25)
        persona.asignar_edad(33)
        persona.asignar_nombre('Adriana')

        # Comprueba que los datos se han cambiado
        assert persona.dar_nombre() != 'Pepa'
        assert persona.dar_edad() != 25

        assert persona.dar_nombre() == 'Adriana'
        assert persona.dar_edad() == 33
        

    def test_contiene_texto(self):
        persona = Persona(nombre="Maria Alejandra", edad=22)
        assert "Alejandra" in persona.dar_nombre()


    def test_anio_nacimiento(self):
        persona = Persona(nombre="Maria Alejandra", edad=22)
        assert persona.calcular_anio_nacimiento(True) == datetime.datetime.now().year - 22
        assert persona.calcular_anio_nacimiento(False) == datetime.datetime.now().year - 22 + 1