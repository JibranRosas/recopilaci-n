class personaje():
    def __init__(self,nombre,vida,poder):
        self.nombre=nombre
        self.vida=vida
        self.poder=poder  
    
    def ataque(self,p1):
        print(f'{self.nombre} ha atacado a {p1.nombre}')
        self.btl=p1.vida-self.poder
        p1.vida=self.btl
        print(f'ahora tu contrincante {p1.nombre} tiene {self.btl} puntos de vida\n')
        
        
class habilidad(personaje):
    def __init__(self, nombre, vida, poder,habilidad):
        super().__init__(nombre, vida, poder)    
        self.habilidad=habilidad.lower()
        if self.habilidad == "magia":
            self.poder*=1.5
        elif self.habilidad == "fuerza":
            self.poder*=1.25  
        
holly=habilidad("Holly",100,50,"Magia")
jess=habilidad("Jess",100,45,"Fuerza")


holly.ataque(jess)

jess.ataque(holly)