import pandas as pd
import numpy as np


def mbti(vector):
    """Converts the user's vector to mbti.
    Args:
        vector (array): _description_
    result:
        string : mbti
    """
    
    # 딕셔너리로 변경 (가독성)
    E_I_dict = {
        "E":vector[0],
        "I":vector[1]        
          }
    N_S_dict = {
        "N":vector[2],
        "S":vector[3]        
         }
    T_F_dict = {
        "T":vector[4],
        "F":vector[5]        
            }
    P_J_dict = {
        "P":vector[6],
        "J":vector[7]        
         }
    
    
    result1 = sorted(E_I_dict.items(), key = lambda x :- x[1])[0][0]
    result2 = sorted(N_S_dict.items(), key = lambda x :- x[1])[0][0]
    result3 = sorted(T_F_dict.items(), key = lambda x :- x[1])[0][0]
    result4 = sorted(P_J_dict.items(), key = lambda x :- x[1])[0][0]
    mbti = result1+result2+result3+result4
    
    return mbti
