def get_score(model_prediction): 
    '''
    model_prediction: The result of model.predict() 
    '''
    y_pred = []
    for pred in [prediction.argmax() for prediction in model_prediction]:
    
        if pred == 0: 
            y_pred.append(7)  #anger 
        
        if pred == 1: 
            y_pred.append(5)  # fear 
        
        if pred == 2: 
            y_pred.append(0) # joy
        
        if pred == 3: 
            y_pred.append(0) # love 
        
        if pred == 4: 
            y_pred.append(10) #sad
        
        if pred == 5: 
            y_pred.append(2) #surprise 
        
    
    return sum(y_pred)/len(y_pred) 



        