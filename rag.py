from load_model import load_model

llm = load_model()

print(llm("Hello, how are you?")["choices"][0]["text"])