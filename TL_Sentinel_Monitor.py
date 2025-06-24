
import os
import time
import hashlib

REPO_PATH = "./"  # Cambia se vuoi monitorare una cartella specifica

def get_file_hashes(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith(".") or file.endswith(".pyc"):
                continue
            path = os.path.join(root, file)
            try:
                with open(path, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                relative_path = os.path.relpath(path, directory)
                hashes[relative_path] = file_hash
            except Exception:
                continue
    return hashes

def main():
    print("🛰️  Sentinel TL attivo. Monitoraggio modifiche in corso...
")
    previous_state = get_file_hashes(REPO_PATH)

    while True:
        time.sleep(10)  # Controlla ogni 10 secondi
        current_state = get_file_hashes(REPO_PATH)

        for file, hash_val in current_state.items():
            if file not in previous_state:
                print(f"[NEW] File aggiunto: {file}")
            elif previous_state[file] != hash_val:
                print(f"[MODIFIED] File modificato: {file}")

        for file in previous_state:
            if file not in current_state:
                print(f"[DELETED] File rimosso: {file}")

        previous_state = current_state

if __name__ == "__main__":
    main()
