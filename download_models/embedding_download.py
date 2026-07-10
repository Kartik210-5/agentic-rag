from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="google/embeddinggemma-300m",
    local_dir="./models/google/embeddinggemma-300m"
)

