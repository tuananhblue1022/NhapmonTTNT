def exercise1(tp, fp, fn):
    # Check if all inputs are integers
    if not all(isinstance(i, int) for i in [tp, fp, fn]):
        print("tp, fp and fn must be int")
        return
    
    # Check if all inputs are greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp and fn must be greater than zero")
        return
    
    # Calculate Precision, Recall, and F1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    # Print the results
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")

# Example usage:
exercise1(tp=2, fp=3, fn=4)
