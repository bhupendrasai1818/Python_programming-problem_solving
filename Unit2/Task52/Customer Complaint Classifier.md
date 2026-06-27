## Customer Complaint Classifier

## 1. Problem Statement

Develop a Python application to categorize customer complaints based on their issue type.

## 2. Algorithm

1. Start the program.
2. Accept the customer complaint description as input.
3. Convert the complaint text into lowercase.
4. Check for keywords related to different complaint categories:
   Delivery issues
   Payment issues
   Product issues
   Service issues
5. Assign the complaint to the appropriate category.
6. Display the complaint category.
7. Stop the program.

## 3. Flowchart 

```Mermaid
flowchart TD
    A([START]) --> B[/Enter Customer Complaint/]
    B --> C[Convert Complaint to Lowercase]
    C --> D{Check Keywords}
    
    D -->|Delivery| E[Category: Delivery Issue]
    D -->|Payment| F[Category: Payment Issue]
    D -->|Product| G[Category: Product Issue]
    D -->|Service| H[Category: Service Issue]
    D -->|None| I[Category: Other Issue]

    E --> J[Display Category]
    F --> J
    G --> J
    H --> J
    I --> J

    J --> K([END])
```

## 4. Python Source Code


complaint = input("Enter customer complaint: ")

complaint = complaint.lower()

if "delivery" in complaint or "late" in complaint:
    category = "Delivery Issue"

elif "payment" in complaint or "transaction" in complaint:
    category = "Payment Issue"

elif "product" in complaint or "damaged" in complaint:
    category = "Product Issue"

elif "service" in complaint or "support" in complaint:
    category = "Service Issue"

else:
    category = "Other Issue"

print("Complaint Category:", category)

## 5. Sample Input
Enter customer complaint:
My delivery is late

## 6. Sample Output
Complaint Category: Delivery Issue

## 7. Screenshot
![alt text](<Screenshot 2026-06-25 095408.png>)