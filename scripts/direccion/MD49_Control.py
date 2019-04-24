
import numpy as np
import skfuzzy as fuzz

def FuzzControl(error):

    x_pos = np.arange(-480, 480, 1)
    x_speed = np.arange(0, 255, 1)
    
    
    # Generate fuzzy membership functions
    pos_NB = fuzz.trimf(x_pos, [-480, -360, -240])
    pos_NM = fuzz.trimf(x_pos, [-360, -240, -120])
    pos_NS = fuzz.trimf(x_pos, [-240, -120, 0])
    pos_0 = fuzz.trimf(x_pos, [-120, 0, 120])
    pos_S = fuzz.trimf(x_pos, [0, 120, 240])
    pos_M = fuzz.trimf(x_pos, [120, 240, 360])
    pos_B = fuzz.trimf(x_pos, [240, 360, 480])
    
    speed_NB = fuzz.trimf(x_speed, [0, 0, 43])
    speed_NM = fuzz.trimf(x_speed, [0, 43, 85])
    speed_NS = fuzz.trimf(x_speed, [43, 85, 128])
    speed_0 = fuzz.trimf(x_speed, [85, 128, 171])
    speed_S = fuzz.trimf(x_speed, [128, 171, 213])
    speed_M = fuzz.trimf(x_speed, [171, 213, 255])
    speed_B = fuzz.trimf(x_speed, [213, 255, 255])
    
    """
    Fuzzy rules
    -----------
    
    1. Si Error en pos es NB, entonces la Velocidad es B
    2. Si Error en pos es NM, entonces la Velocidad es M
    3. Si Error en pos es NS, entonces la Velocidad es S
    4. Si Error en pos es 0, entonces la Velocidad es 0
    5. Si Error en pos es S, entonces la Velocidad es NS
    6. Si Error en pos es M, entonces la Velocidad es NM
    7. Si Error en pos es B, entonces la Velocidad es NB.
    """
    
    level_pos_NB = fuzz.interp_membership(x_pos, pos_NB, error)
    level_pos_NM = fuzz.interp_membership(x_pos, pos_NM, error)
    level_pos_NS = fuzz.interp_membership(x_pos, pos_NS, error)
    level_pos_0 = fuzz.interp_membership(x_pos, pos_0, error)
    level_pos_S = fuzz.interp_membership(x_pos, pos_S, error)
    level_pos_M = fuzz.interp_membership(x_pos, pos_M, error)
    level_pos_B = fuzz.interp_membership(x_pos, pos_B, error)
    
    #Regla 1
    SNB = np.fmin(level_pos_NB, speed_B)
    #Regla 2
    SNM = np.fmin(level_pos_NM, speed_M)
    #Regla 3
    SNS = np.fmin(level_pos_NS, speed_S)
    #Regla 4
    S0 = np.fmin(level_pos_0, speed_0)
    #Regla 5
    SS = np.fmin(level_pos_S, speed_NS)
    #Regla 6
    SM = np.fmin(level_pos_M, speed_NM)
    #Regla 7
    SB = np.fmin(level_pos_B, speed_NB)
    
    
    # Aggregate all three output membership functions together
    aggregated= np.fmax(SNB, np.fmax(SNM, np.fmax(SNS, np.fmax(S0, np.fmax(SS, np.fmax(SM, SB))))))
    
    # Calculate defuzzified result
    Speed = fuzz.defuzz(x_speed, aggregated, 'centroid')
    Speedf=int(np.around(Speed, decimals=0))
    
    return Speedf