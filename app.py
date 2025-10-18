from bit_logic import BitFromTron
import numpy as np
import pickle

bit_inst = BitFromTron()

with open( "bit_model_v0000.pkl", "rb") as banana:
    banana_brain = pickle.load(banana)
    print("Model loaded successfully!")
    print(f"Model type: {type(banana_brain)}")
    

def rule_based_answer(question):
    return bit_inst.bit_answer_user(question)

def banana_brain_predicts(question):
    print(f"Function called with: {question}")
    vectorized_question = banana_brain[0].transform([question])
    prediction = banana_brain[1].predict(vectorized_question)
    confidence_level = max(banana_brain[1].predict_proba(vectorized_question)[0])
    
    if confidence_level >= 0.8:
        print(f"[ML BRAIN - Confident: {confidence_level:.2f}]")
        return prediction[0] 
    else:
        print(f"[RULE BASED - Low confidence: {confidence_level:.2f}]")
        back_up = rule_based_answer(question)
        return back_up

try:
    print("Tron Program about to be launched")
    while True:
    
        question = input("BIT IS LISTENING...\n")
        print(banana_brain_predicts(question))

except KeyboardInterrupt:
    print("END OF LINE")
    exit
