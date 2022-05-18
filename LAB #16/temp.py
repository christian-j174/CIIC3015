class Temperature:
    scales = ['C', 'F', 'K']  # static

    def __init__(self, temp, scale):
        self.temp = temp  # instance
        self.scale = scale  # scale

    def Celcius_to_Fahrenheit(self):
      self.temp = round((9.0/5.0) * self.temp + 32.0, 2)

    def Fahrenheit_to_Celcius(self):
      self.temp = round((5.0/9.0) * (self.temp - 32.0), 2)
#------------------------------------------------------

    def Celcius_to_Kelvin(self):
        self.temp = round(self.temp + 273.16, 2)

    def Celcius_to_Celcius(self):
        self.temp = self.temp

    def Fahrenheit_to_Fahrenheit(self):
        self.temp = self.temp

    def Kelvin_to_Celcius(self):
        self.temp = round(self.temp - 273.16, 2)

    def Kelvin_to_Kelvin(self):
        self.temp = self.temp

    def Kelvin_to_Fahrenheit(self):
        self.temp = round(self.temp - 273.16, 2)
        self.temp = round((9.0/5.0) * self.temp + 32.0, 2)

    def Fahrenheit_to_Kelvin(self):
        self.temp = round( (5.0 / 9.0) * (self.temp - 32.0), 2 )
        self.temp = round(self.temp + 273.16, 2)



def main():

    t = float( input( "Temperature: " ) )
    s = input( 'Scale (C, F, K): ' ).upper()  # current scale of teh temperatur value
    convert = input( 'Convert to  (C, F, K): ' ).upper()  # it receive the desired the scale
    Temp = Temperature( t, s )  # create an instance of the class

    if s == 'C' and convert == 'F':
        print('Converting to Fahrenheit...')
        Temp.Celcius_to_Fahrenheit()
        print(Temp.temp, convert)

    elif s == 'C' and convert == 'K':
        print('Converting to Kelvin...')
        Temp.Celcius_to_Kelvin()
        print( Temp.temp, convert )

    elif s == 'C' and convert == 'C':
        print('Converting to Celcius...')
        Temp.Celcius_to_Celcius()
        print( Temp.temp, convert )

    elif s == 'F' and convert == 'C':
        print('Converting to Celcius...')
        Temp.Fahrenheit_to_Celcius()
        print( Temp.temp, convert )

    elif s == 'F' and convert == 'K':
        print('Converting to Kelvin...')
        Temp.Fahrenheit_to_Kelvin()
        print( Temp.temp, convert )

    elif s == 'F' and convert == 'F':
        print('Converting to Fahrenheit...')
        Temp.Fahrenheit_to_Fahrenheit()
        print( Temp.temp, convert )

    elif s == 'K' and convert == 'C':
        print('Converting to Celcius...')
        Temp.Kelvin_to_Celcius()
        print( Temp.temp, convert )

    elif s == 'K' and convert == 'F':
        print('Converting to Fahrenheit...')
        Temp.Kelvin_to_Fahrenheit()
        print( Temp.temp, convert )

    elif s == 'K' and convert == 'K':
        print('Converting to Kelvin...')
        Temp.Kelvin_to_Kelvin()
        print( Temp.temp, convert )



main()