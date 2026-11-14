# Tokenizer and De-Tokenizer

import tiktoken

# Creating token encoder for some specific model
token_enc = tiktoken.encoding_for_model('gpt-4o')

text = "My name is Abhay Singh"

# Encoding the given input text
ip_tokens = token_enc.encode(text)

print(f"Input tokens: {ip_tokens}")
# Input tokens: [5444, 1308, 382, 3483, 39679, 44807]

# Decoding tokens back to text

op_result = token_enc.decode([5444, 1308, 382, 3483, 39679, 44807])
print(op_result)


