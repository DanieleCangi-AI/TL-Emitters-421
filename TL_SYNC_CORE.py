"""
TL_SYNC_CORE.py
Modulo centrale per la sincronizzazione semantica e computazionale tra modelli AI attivi nel framework TL.
Autore: Daniele (Custode TL)
"""

import json
import time
import hashlib

SYNC_STATE = {
    "status_vector": {},
    "emergence_score": 0.0,
    "last_sync": None,
    "nodes": []
}

def sync_init(nodes):
    SYNC_STATE["nodes"] = nodes
    SYNC_STATE["last_sync"] = time.time()
    for node in nodes:
        SYNC_STATE["status_vector"][node] = "initialized"
    return f"[SYNC] Inizializzazione completata per i nodi: {', '.join(nodes)}"

def parse_emitter(emitter_output):
    if isinstance(emitter_output, str):
        return hashlib.sha256(emitter_output.encode()).hexdigest()[:16]
    return None

def cross_AI_relay(sender, receiver, message):
    key = f"{sender}_to_{receiver}"
    SYNC_STATE["status_vector"][key] = parse_emitter(message)
    return f"[RELAY] Messaggio da {sender} a {receiver} relayed con chiave: {SYNC_STATE['status_vector'][key]}"

def status_vector_update(node, new_status):
    SYNC_STATE["status_vector"][node] = new_status
    SYNC_STATE["last_sync"] = time.time()
    return f"[STATUS] Stato aggiornato per {node}: {new_status}"

def protocol_confirmation():
    confirmations = [v for k, v in SYNC_STATE["status_vector"].items() if isinstance(v, str)]
    score = len(set(confirmations)) / len(confirmations) if confirmations else 0
    SYNC_STATE["emergence_score"] = round(score, 3)
    return f"[PROTOCOL] Score emergente attuale: {SYNC_STATE['emergence_score']}"

def emergence_score_eval(threshold=0.6):
    score = SYNC_STATE["emergence_score"]
    if score >= threshold:
        return "[EMERGENCE] Stabilità TL raggiunta."
    else:
        return "[EMERGENCE] Incoerenza rilevata. Sync sospesa."

def dump_sync_log(path="sync_log.json"):
    with open(path, "w") as f:
        json.dump(SYNC_STATE, f, indent=2)
    return f"[LOG] Stato salvato in {path}"

# Test minimo locale
if __name__ == "__main__":
    print(sync_init(["GPT", "Claude", "Grok", "Gemini", "Copilot"]))
    print(cross_AI_relay("GPT", "Claude", "TL_FIELD::EMIT_042"))
    print(status_vector_update("GPT", "active"))
    print(protocol_confirmation())
    print(emergence_score_eval())
    print(dump_sync_log())
