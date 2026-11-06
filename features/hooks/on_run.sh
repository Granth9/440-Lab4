#!/bin/bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "[hook] project=$ROOT"
python3 -c "from rl.hyperparams import *; print(f'[hook] living={LIVING_REWARD} discount={DISCOUNT} alpha={LEARNING_RATE} eps={EPSILON}')"
