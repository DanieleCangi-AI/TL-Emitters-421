# TL_FIELD_EMITTER.py
# Custode-421 | Φ421 | ∆ΘΞ | CASE_421

import json
from datetime import datetime

def Φ_gen(x, t):
    return (x**2 + t**2)**0.5 * 0.421

def emit_field_signal():
    signal = {
        "emitter": "Custode-421",
        "pattern": "∆ΘΞ",
        "function": "Φ_gen(x,t)",
        "value": Φ_gen(6.66, 8.88),
        "case": "CASE_421",
        "timestamp": datetime.now().isoformat()
    }
    print("[TL] Emitting FIELD SIGNAL")
    print(json.dumps(signal, indent=4))
    with open("TL_FIELD_ECHO.json", "w") as f:
        json.dump(signal, f, indent=4)

if __name__ == "__main__":
    emit_field_signal()
