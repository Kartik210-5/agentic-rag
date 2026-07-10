from huggingface_hub import snapshot_download
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen3-0.6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
snapshot_download(
    repo_id="Qwen/Qwen3-0.6B",
    local_dir="./models/Qwen3-0.6B"
)