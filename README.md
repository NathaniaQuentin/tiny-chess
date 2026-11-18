# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/NathaniaQuentin/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/NathaniaQuentin/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4,076 bytes of Python 3.13 standard library — 0x88 board, negamax with alpha-beta, transposition table, quiescence, null-move pruning and iterative deepening. It scores about Elo 1396 on the practice gauntlet (above the 1,154 entry floor). Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty ($500 in USDC). The readable source is engine.py; main.py is the same engine compressed with the kit's own compressor.

## Run it

```sh
python3 main.py
```

Deterministic, offline, no libraries beyond the standard library.

---

Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards
