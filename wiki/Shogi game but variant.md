---
tags: ['#idea', '#task/suspend', '#game', '#wip']
---

# OpenSpec Proposal Series
# Project: Scrolling Shogi Roguelite
# Tech Stack: Python + pygame-ce

---

# Overview

## High Concept

將棋 Roguelite 生存遊戲。

玩家控制己方王將，在持續崩壞並向下捲動的棋盤上生存。

每隔固定回合：

- 最底排消失
- 棋盤整體向下推進
- 最上排生成新格子與敵軍

玩家必須：

- 不斷向上推進
- 擊敗敵人
- 收集持駒
- 建立防線
- 獲得升級
- 擊敗 Boss

靈感來源：

- Shotgun King
- Downwell
- Into the Breach
- 將棋

---

# Proposal 001
# Playable Board

## Goal

建立最小可玩的棋盤系統。

## Features

- 9x9 棋盤
- 格子繪製
- 玩家王將
- 游標選取
- 移動王將

## Controls

### Arrow Keys

移動游標

### Space

確認移動

## Files

```text
main.py
board.py
piece.py
renderer.py
```

## Acceptance Criteria

- 顯示 9x9 棋盤
- 王將可移動
- 不可超出邊界

---

# Proposal 002
# Turn System

## Goal

建立回合制架構。

## Features

新增遊戲狀態：

```python
PlayerTurn
EnemyTurn
```

新增：

```python
TurnManager
```

## Turn Flow

```text
Player Turn
↓
Enemy Turn
↓
Turn +1
↓
Player Turn
```

## Files

```text
turn_manager.py
game_state.py
```

## Acceptance Criteria

畫面顯示：

```text
Turn: 1
Player Turn
```

---

# Proposal 003
# Enemy Pawns

## Goal

建立第一種敵人。

## New Piece

```text
Enemy Pawn
```

## Behaviour

每回合：

```text
向下前進一格
```

## Spawn

固定生成於最上排。

## Files

```text
enemy.py
enemy_spawner.py
```

## Acceptance Criteria

敵人持續接近玩家。

---

# Proposal 004
# Capture System

## Goal

實作吃子。

## Rules

移動到敵方格：

```text
吃掉敵方棋子
```

## Features

新增：

```python
capture_piece()
```

## UI

顯示：

```text
Kills: 0
```

## Acceptance Criteria

玩家可消滅敵人。

---

# Proposal 005
# Scrolling Board

## Goal

建立核心玩法。

## Rules

每 5 回合：

### Step 1

刪除最底排

### Step 2

全部棋子往下移動

### Step 3

新增最上排

### Step 4

生成敵軍

## Example

Before

```text
A
B
C
D
```

After

```text
NEW
A
B
C
```

## Failure Condition

玩家被推出棋盤：

```text
Game Over
```

## Files

```text
board_scroll.py
```

## Acceptance Criteria

棋盤持續向下捲動。

---

# Proposal 006
# Wave Generator

## Goal

建立敵人生成系統。

## API

```python
generate_wave(turn)
```

## Difficulty Curve

### Wave 1~10

```text
Pawn
```

### Wave 11~20

```text
Pawn
Lance
```

### Wave 21~30

```text
Pawn
Lance
Knight
```

### Wave 31~50

```text
Pawn
Lance
Knight
Silver
```

## Files

```text
wave_generator.py
```

## Acceptance Criteria

敵軍數量與品質隨時間成長。

---

# Proposal 007
# Shogi Piece Framework

## Goal

導入完整棋種架構。

## Implement

```text
Pawn
Lance
Knight
Silver
Gold
Bishop
Rook
```

## Architecture

```python
MovementPattern
```

## Example

```python
piece.get_valid_moves()
```

## Files

```text
movement.py
piece_factory.py
```

## Acceptance Criteria

所有棋種具備正確走法。

---

# Proposal 008
# Hand Piece System

## Goal

導入持駒。

## Rules

擊敗敵人：

```text
加入持駒
```

例如：

```text
Pawn x2
Knight x1
```

## Controls

### H

開啟持駒介面

### Enter

放置持駒

## UI

```text
Hand:
Pawn x2
Knight x1
```

## Files

```text
hand.py
drop_phase.py
```

## Acceptance Criteria

玩家可打入持駒。

---

# Proposal 009
# Friendly Army

## Goal

建立己方部隊。

## Available Units

```text
Pawn
Lance
Knight
Silver
Gold
```

## AI

### Default Behaviour

```text
優先前進

發現敵人時攻擊
```

## Files

```text
friendly_ai.py
```

## Acceptance Criteria

己方部隊可協助戰鬥。

---

# Proposal 010
# Upgrade Selection

## Goal

建立 Roguelite 成長系統。

## Trigger

每 10 回合。

## UI

三選一。

## Example Upgrades

### Rook Soul

王將獲得飛車走法

### Bishop Soul

王將獲得角行走法

### Reinforcement

獲得持步 x2

### Veteran Army

所有步兵攻擊力增加

### Supply Wagon

持駒容量增加

## Files

```text
upgrade.py
upgrade_pool.py
upgrade_ui.py
```

## Acceptance Criteria

玩家可於每局持續變強。

---

# Proposal 011
# Boss Framework

## Goal

建立 Boss 系統。

## Boss Properties

```python
hp
size
skills
```

## Example Boss

### Giant Rook

```text
HP: 20
Size: 2x2
```

### Fortress

```text
HP: 50
```

持續召喚敵軍。

## Spawn

每 20 Wave。

## Files

```text
boss.py
boss_manager.py
```

## Acceptance Criteria

Boss 戰可正常進行。

---

# Proposal 012
# Complete Roguelite Loop

## Goal

完成 MVP。

## New Systems

### Soul Currency

擊殺獲得：

```text
Soul
```

### Unlock System

解鎖：

```text
新升級
新敵人
新Boss
```

### Statistics

紀錄：

```text
存活回合
擊殺數
Boss擊破數
```

### End Screen

顯示：

```text
Run Summary
```

## Files

```text
meta_progression.py
statistics.py
end_screen.py
```

## Acceptance Criteria

完整流程：

```text
開始遊戲
↓
戰鬥
↓
棋盤捲動
↓
升級
↓
Boss
↓
死亡
↓
結算
↓
重新開始
```

---

# Post-MVP Roadmap

## Proposal 013
Promotion System

### Features

- 成銀
- 成桂
- 成香
- 龍王
- 龍馬

---

## Proposal 014
Elite Enemies

### Examples

#### Bomb Pawn

死亡爆炸

#### Ghost Bishop

無視阻擋

#### Berserker Rook

強制前進

---

## Proposal 015
Relic System

永久被動能力。

### Examples

```text
Double Souls
Auto Promotion
Extra Hand Capacity
```

---

## Proposal 016
Event Rooms

特殊波次。

### Examples

```text
Treasure Wave
Merchant
Shrine
Ambush
```

---

## Proposal 017
Alternative Kings

不同起始職業。

### Examples

#### Warrior King

近戰強化

#### Rook King

飛車移動

#### Summoner King

初始持駒增加

---

## Proposal 018
Loadout System

開局選擇：

```text
起始升級
起始部隊
起始持駒
```

---

## Proposal 019
Daily Challenge

每日固定種子。

排行榜模式。

---

## Proposal 020
Endless Mode

無限生存。

持續生成：

- Elite
- Boss
- Mega Boss

直到死亡。

---

# Milestone Plan

## Milestone A
Core Prototype

```text
001
002
003
004
005
006
```

完成後可驗證：

- 回合制
- 敵軍
- 棋盤捲動

---

## Milestone B
Shogi Identity

```text
007
008
009
```

完成後可驗證：

- 將棋特色
- 持駒
- 部隊戰鬥

---

## Milestone C
Roguelite Identity

```text
010
011
012
```

完成後可驗證：

- 成長
- Boss
- 完整遊戲循環

---

# MVP Definition

完成以下 Proposal 即視為 MVP：

```text
001
002
003
004
005
006
007
008
009
010
011
012
```

最終產出：

「Shotgun King + Downwell + 將棋」
垂直捲軸 Roguelite 生存遊戲。

---

想不到提高中毒性的玩法
[将棋が流行らない理由](https://www.youtube.com/watch?v=Dc_qe-RUJ7Q&ab_channel=%E3%80%90%E5%B0%86%E6%A3%8B%E3%80%91%E5%8F%B3%E5%9B%9B%E9%96%93%E9%A3%9B%E8%BB%8A%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB%E3%81%9D%E3%82%89)

---

- https://www.chessprogramming.org/Main_Page
- https://sebastian.itch.io/tiny-chess-bots
- https://www.youtube.com/watch?v=Ne40a5LkK6A
- https://lishogi.org/
- [Help Make Esports Better: The Good Game Project](https://www.youtube.com/watch?v=iyvkIBA7pNE)
- https://www.youtube.com/watch?v=XSCFrzA3psE
- https://www.youtube.com/watch?v=NotXnKh5F6s
- [【連載】評価関数を作ってみよう！その3 , やねうら王 公式サイト](https://yaneuraou.yaneu.com/2020/11/20/make-evaluate-function-3)
- [コンピュータ将棋の本 ＠将棋 棋書ミシュラン！](https://rocky-and-hopper.sakura.ne.jp/Kisho-Michelin/package/computer.htm)
- [「現代将棋を読み解く７つの理論」あらきっぺさんインタビュー プロ棋士はどんな思考プロセスを踏むのか？ ｜好書好日](https://book.asahi.com/article/14230780)
- [文部科学大臣杯第5回電竜戦は氷彗が初優勝 , コンピュータ将棋協会blog](http://blog.computer-shogi.org/hisui_wins_denryu-sen-5)
- [fairy-stockfish/Fairy-Stockfish: chess variant engine supporting Xiangqi, Shogi, Janggi, Makruk, S-Chess, Crazyhouse, Bughouse, and many more](https://github.com/fairy-stockfish/Fairy-Stockfish)
- [SebLague/Chess-Coding-Adventure: A work-in-progress chess bot written in C#](https://github.com/SebLague/Chess-Coding-Adventure)
- [Chaosus/ModernShogi: Modern Shogi is free, advanced 3D japanese chess client, with AI and multiplayer, made in Godot 3.1](https://github.com/Chaosus/ModernShogi)
- [yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player) , WCSC29 1st winner , educational and USI compliant engine.](https://github.com/yaneurao/YaneuraOu/tree/master)
- [Coding Adventure: Making a Better Chess Bot - YouTube](https://www.youtube.com/watch?v=_vqlIPDR2TU&t=372s)
- [将棋ったー](https://shogitter.com)
- [「将棋」人気ランキング , フリーゲーム投稿サイト unityroom](https://unityroom.com/rankings/tags/121)

- [[Shogi Opening]]
- [[Tsume Shogi]]
- [[Shogi Tool]]
