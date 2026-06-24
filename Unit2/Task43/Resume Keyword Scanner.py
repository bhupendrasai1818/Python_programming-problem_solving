resume = input("Enter Resume Text: ")

keywords = ["python", "java", "sql", "html", "css", "machine learning", "data analysis"]

resume = resume.lower()

found_keywords = []

for keyword in keywords:
    if keyword.lower() in resume:
        found_keywords.append(keyword)

if found_keywords:
    print("Keywords Found:")
    for word in found_keywords:
        print(word)
else:
    print("No Job-Specific Keywords Found")
