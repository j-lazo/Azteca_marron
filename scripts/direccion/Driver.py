import serial 
from bitstring import BitStream

class  MD49_driver:
    SYNC="\x00",
    GET_SPEED_1="\x21",
    GET_SPEED_2="\x22",
    GET_ENCODER_1="\x23",
    GET_ENCODER_2="\x24",
    GET_ENCODERS="\x25",
    GET_VOLTS="\x26",
    GET_CURRENT_1="\x27",
    GET_CURRENT_2="\x28",
    GET_VERSION="\x29",
    GET_ACCELERATION="\x2A",
    GET_MODE="\x2B",
    GET_VI="\x2C",
    GET_ERROR="\x2D",
    SET_SPEED_1="\x31",
    SET_SPEED_2="\x32",
    SET_ACCELERATION="\x33",
    SET_MODE="\x34",
    RESET_ENCODERS="\x35",
    DISABLE_REGULATOR="\x36",
    ENABLE_REGULATOR="\x37",
    DISABLE_TIMEOUT="\x38",
    ENABLE_TIMEOUT="\x39"
    
    def Setup(self, COM):
        NAME_PORT= serial.Serial("COM", 9600, timeout = 10)
        return NAME_PORT
    
    def SendCommand(self,Command,NAME_PORT):
        A= self.SYNC + self.Command
        NAME_PORT.write(A)
        
    def ReadAnswer(self,Lenght,NAME_PORT):
        B=NAME_PORT.read(Lenght)
        return B
        
        
    def Encoder(self,NAME_PORT):
        self.SendCommand(self.GET_ENCODER_1)
        X=self.ReadAnswer(4,NAME_PORT)
        Y=X.encode("hex")
        if len(Y) == 8:
            Y=Y
        else:
            Y='0x'+Y
        Value = BitStream(Y)
        return Value
    
    def SetSpeed(self, speed,NAME_PORT):
        Z=self.SET_SPEED_1+ chr(speed)
        self.SendCommand(Z,NAME_PORT)
        
   
