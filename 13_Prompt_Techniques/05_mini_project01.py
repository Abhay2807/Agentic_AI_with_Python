
import os
from datetime import date
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ConfigDict, ValidationError


# STEP 1: Load API key

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found")


# STEP 2: Create client

client = OpenAI(
    api_key=api_key,
    timeout=30,
    max_retries=2
)


# STEP 3: Define output schema

class TransactionExtraction(BaseModel):

    model_config = ConfigDict(extra="forbid")

    customer_name: str | None
    amount: float | None
    currency: str | None
    transaction_date: date | None

    missing_fields: list[str]

    is_complete: bool


# STEP 4: System prompt

SYSTEM_PROMPT = """
You are a strict financial transaction extraction system.

Extract information ONLY when explicitly available
in the user's input.

STRICT RULES:

1. Never invent or assume missing information.
2. Never assume INR or any default currency.
3. Never calculate or infer a missing amount.
4. If a field is missing, return null.
5. If a date is ambiguous, return null.
6. Do not use examples as information about the
   current transaction.
7. missing_fields must contain all missing or
   ambiguous required fields.
8. is_complete must be true only when all four
   required fields are available and unambiguous.

Required fields:
- customer_name
- amount
- currency
- transaction_date

Examples:

Input:
Rahul paid INR 2500 on 10 November 2026.

Output:
{
  "customer_name": "Rahul",
  "amount": 2500,
  "currency": "INR",
  "transaction_date": "2026-11-10",
  "missing_fields": [],
  "is_complete": true
}

Input:
Priya made a payment on 5 October 2026.

Output:
{
  "customer_name": "Priya",
  "amount": null,
  "currency": null,
  "transaction_date": "2026-10-05",
  "missing_fields": ["amount", "currency"],
  "is_complete": false
}
"""


# STEP 5: User input

transaction_text = """
Rahul paid INR 2500 on 05/06/2026.
"""

# STEP 6: Call LLM

try:

    response = client.chat.completions.parse(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": transaction_text
            }
        ],

        response_format=TransactionExtraction
    )

    message = response.choices[0].message

    if message.refusal:
        print("Model refused:", message.refusal)

    elif message.parsed is None:
        print("No structured response received.")

    else:

        result = message.parsed

        # STEP 7: Application-level validation

        required_fields = {
            "customer_name",
            "amount",
            "currency",
            "transaction_date"
        }

        actual_missing = [
            field
            for field in required_fields
            if getattr(result, field) is None
        ]

        # Verify model's completeness claims
        if set(result.missing_fields) != set(actual_missing):
            print("Rejected: Inconsistent missing-field information.")

        elif result.is_complete != (len(actual_missing) == 0):
            print("Rejected: Inconsistent completeness status.")

        elif actual_missing:

            print("\nINCOMPLETE TRANSACTION")
            print("Missing fields:", actual_missing)
            print("Transaction rejected.")

        else:

            # STEP 8: Business validation

            if result.amount <= 0:
                raise ValueError("Invalid transaction amount")

            print("\nVALID TRANSACTION")
            print(result.model_dump(mode="json"))

except ValidationError as error:
    print("Validation error:", error)

except OpenAIError as error:
    print("OpenAI API error:", error)

except Exception as error:
    print("Unexpected error:", error)
