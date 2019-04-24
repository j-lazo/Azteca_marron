from Driver import MD49_driver
import MD49_Control as fuzz
MD49=MD49_driver

#def SetPosition(Reference,COM):
ser=MD49.Setup("/dev/ttyUSB0")
Pos=MD49.Encoder(ser)
Reference=0
Factor=(Pos/930)
Relation=(Pos-(Factor*930))
if Pos>=-930 and Pos<=930:
    Degrees=(Pos*0.3870967742)
else:
    Degrees=(Relation*0.387096742)
Error=Reference-Degrees
Speed=fuzz.FuzzControl(Error)

MD49.SetSpeed(Speed,ser)
ser.close()