from llama_cpp import Llama

llm = Llama(
    model_path="./models/Qwen2.5-3B-Instruct-GGUF/qwen2.5-3b-instruct-q4_k_m.gguf",
    n_ctx=8192,
    n_threads=8,      # adjust according to your CPU
    n_gpu_layers=-1,  # offload all layers to GPU (Metal on Apple Silicon)
    verbose=False,
)

output = llm(
    "Write a short poem about artificial intelligence.",
    max_tokens=200,
    temperature=0.7,
)

print(output["choices"][0]["text"])