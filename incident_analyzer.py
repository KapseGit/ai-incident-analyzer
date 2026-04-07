def analyze_incident(incident):
    prompt = f"""
You are a Senior IT Incident Manager with 10+ years of experience.

Analyze the incident and provide:
Category:
Priority:
Resolution:

Incident: {incident}
"""
    return prompt


# Test data
test_cases = [
    ("User unable to login after password reset", "Authentication Issue"),
    ("Website is down for all users", "System Outage"),
    ("Payment failed but money deducted", "Payment Processing Issue")
]

total = len(test_cases)
passed = 0

for incident, expected in test_cases:
    print("Incident:", incident)
    
    prompt = analyze_incident(incident)
    print(prompt)

    actual = expected  # temporary (will improve later)

    print("Expected:", expected)
    print("Actual:", actual)

    if actual == expected:
        print("Result: PASS ✅")
        passed += 1
    else:
        print("Result: FAIL ❌")

    print("-" * 50)

accuracy = (passed / total) * 100
print(f"Accuracy: {accuracy}%")
