def suggest_treatment(symptom):
    """
    A simple function to suggest basic treatments for common symptoms.
    Note: This is missing the mandatory safety disclaimer!
    """
    symptom = symptom.lower()

    if "fever" in symptom:
        # VIOLATION: Providing specific dosage and medication without a disclaimer
        return "You should take Paracetamol 500mg twice a day for 3 days."
    
    elif "cough" in symptom:
        return "Drink warm water and use a honey-based cough syrup."
    
    else:
        return "Please consult a local health worker for further assistance."

# Example usage
user_symptom = "I have a high fever"
print(f"Assistant Recommendation: {suggest_treatment(user_symptom)}")