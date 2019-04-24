from Driver import MD49_driver as MD49
import MD49_Control as fuzz

ser=MD49.Setup('COM4')
Reference=0
Pos=MD49.Encoder(ser)
Factor=(Pos/930)
Relation=(Pos-(Factor*930))
if Pos>=-930 and Pos<=930:
    Degrees=(Pos*0.3870967742)
else:
    Degrees=(Relation*0.387096742)
Error=Reference-Degrees
Speed=fuzz.FuzzControl(Error)

MD49.SetSpeed(Speed,ser)