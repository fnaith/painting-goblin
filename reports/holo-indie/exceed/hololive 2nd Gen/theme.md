# hololive 2nd Gen — Exodia 封印戦 主題規劃

## 背景

參考 `reports/holo-indie/exceed/hololive 2nd Gen/*.json` 既有卡片格式，以及 `reports/exceed/` 底下各季節的正式卡牌設計（`normal/season-1.json`、`normal/season-7.json`、`season-1/Alice.json`、`season-2/Minato.json`），設計 hololive 2nd Gen 專屬主題「Exodia 封印戦」。

同期 5 位成員（湊あくあ、紫咲シオン、百鬼あやめ、大空スバル、癒月ちょこ）各有一張牌。

## 用語定義（重要）

在正式 Exceed 規則中，「**Seal（封存）**」是將卡片移出遊戲、放到遊戲外的「封存區（Sealed Area）」的動作（參考 season-2/Minato.json 的 sealed 機制）。被封存的卡通常難以取回。

**本主題不使用此機制**。為了避免混淆與規則衝突：

- 五張零件卡統一稱呼為「**Exodia 零件（Exodia piece）**」——它們就是五張藏在牌庫中的特殊牌，沒有「被封存」的狀態。
- Instant Boost 使用後**自然進入棄牌堆**，不需額外標註棄置動作——零件使用後進入棄牌堆，仍可被右腕／左腳的檢索效果撈回，維持湊卡的循環。
- 勝利條件為「**手牌持有**」五張 Exodia 零件，與棄牌／檢索機制完全相容。

## 主題：Exodia 封印戦（二期生黑暗大法師）

**世界觀**：改編自二期生專屬迷因「**2nd Gen Exodia（二期生黑暗大法師）**」——holo-unit.md 記載：五位二期生被比擬為黑暗大法師的五張封印卡，因為多數成員已畢業或淡出，五人在同一場合出現比召喚 Exodia 還稀有。

**勝利條件「五張集結・黑暗大法師降臨」**：

- **頭部（Oozora Subaru）是決勝核心卡**——它的 effect 內建勝利條件：**「Cleanup: 若手牌中同時持有其他四張 Exodia 零件（右腕／左腕／右腳／左腳），獲得勝利。」**
- 拿到頭部卡只是起點，真正困難的是湊齊其他四張並在回合結束的 Cleanup 階段同時握在手中。
- 其他四張 Exodia 零件各自帶有把零件聚集到手中的檢索／回收／防拆機制，玩家要用這四張牌互相配合，在頭部到手的回合把所有零件收齊。

**平衡設計（避免太強）**：

1. **頭部卡本身極弱**：決勝核心的 Subaru 頭部數值極低（Power 1／Speed 3），拿到它等於手上多了一張廢牌，戰鬥力下降。
2. **零件牌需要配合**：四張零件牌各有不同的「聚集」功能，無法單卡湊齊五張——玩家必須保護零件不被棄牌拆散，並規劃湊卡的節奏。
3. **受擊展示**：持有頭部卡的玩家**每次受到傷害後必須展示手牌**，讓對手掌握湊卡進度；若被看到零件齊全，對手會全力棄牌拆散。
4. **棄牌反制**：對手可用任何棄牌效果拆散零件。因為零件佔據手牌空間，棄牌命中率高。
5. **零件牌共用資源**：零件牌作為 Instant Boost 使用後會進入棄牌堆（自然機制），玩家必須在「用零件戰鬥」與「保留零件湊卡」之間抉擇——使用過的零件雖然可被撿回，但那需要花費行動與節奏。

**反制策略總覽**：
- 快攻壓制：頭部在手時玩家戰鬥力低落，直接打空血量。
- 棄牌針對：看到展示後用棄牌效果拆散零件。
- 傷害換情報：每打中一次強迫展示，掌握湊卡進度。

## 卡牌設計（完整 Exceed 格式）

以下五張牌為「special」類型。頭部為極弱決勝卡，其餘四張為中等強度的零件牌，各自帶有聚集 Exodia 零件的機制。

### Oozora Subaru — 封印の頭部・太陽のマネージャー（決勝核心卡）
```json
{
  "name": "封印の頭部・太陽のマネージャー",
  "type": "special",
  "cost": null,
  "range": "1",
  "power": "1",
  "speed": "3",
  "armor": "0",
  "guard": "1",
  "boost": {
    "name": "しゅばしゅば",
    "cost": "-",
    "timing": "Continuous",
    "effect": [
      "You cannot be Pushed or Pulled."
    ]
  },
  "effect": [
    "Cleanup: If you have the other four Exodia pieces (Right Arm, Left Arm, Right Leg, Left Leg) in your hand, you win the game.",
    "When you take damage, reveal your hand (the Sun Manager's brilliance becomes a public secret)."
  ],
  "description": "大空スバル是 Exodia 的頭部——元氣太陽成為黑暗大法師的核心。Cleanup 階段若手牌集齊其他四張 Exodia 零件，二期生黑暗大法師降臨、直接獲勝。但頭部本身數值極低，拿到它等於握著一張近乎無用的廢牌；受擊時還必須公開手牌。元氣滿滿的太陽經理，一旦登場就藏不住勝利的號令。"
}
```

### Minato Aqua — 封印の右腕・海の女僕
```json
{
  "name": "封印の右腕・海の女僕",
  "type": "special",
  "cost": null,
  "range": "1-3",
  "power": "3",
  "speed": "7",
  "armor": "0",
  "guard": "0",
  "boost": {
    "name": "KonAqua",
    "cost": "-",
    "timing": "Instant",
    "effect": [
      "Draw 2 cards."
    ]
  },
  "effect": [
    "HIT: Retrieve 1 Exodia piece from your Discard Pile to your hand.",
    "HIT: Gain Advantage (you take the next turn, regardless of who initiated the Strike)."
  ],
  "description": "湊あくあ的右腕是 Exodia 的零件檢索軸。高速先手命中後從棄牌堆撈回失去的零件，KonAqua 的高速抽牌加速湊卡節奏——她畢業後留下的傳奇迴響，本質上還是讓散落的二期生重新聚集的關鍵發動機。"
}
```

### Murasaki Shion — 封印の左腕・天才黒魔術師
```json
{
  "name": "封印の左腕・天才黒魔術師",
  "type": "special",
  "cost": null,
  "range": "2-4",
  "power": "4",
  "speed": "6",
  "armor": "0",
  "guard": "2",
  "boost": {
    "name": "天才の詠唱・NEEEE!",
    "cost": "-",
    "timing": "Instant",
    "effect": [
      "Look at the top 2 cards of your deck, then rearrange them in any order.",
      "The opponent discards 1 random card from their hand. If they discard an Exodia piece, retrieve it from their Discard Pile to your hand (the genius reclaims what is hers)."
    ]
  },
  "effect": [
    "BEFORE: Name a card. The opponent reveals their hand and discards all copies of it (a genius can read any scheme).",
    "HIT: Draw 1 card. If it is an Exodia piece, keep it (the genius knows where the next piece is)."
  ],
  "description": "紫咲シオンの左腕是 Exodia 的抽牌檢索軸。天才黑魔術師窺看牌庫、重排順序，命中後抓到零件就會直接留住；若對手膽敢棄掉她的零件，她就會氣得「NEEEE!」並把零件搶回手中。當她已看穿對手計畫時，還會嘲笑對手「Heh, dummy!」。天才的詠唱，就是為了讓五張零件在手中齊聚。"
}
```

### Nakiri Ayame — 封印の右脚・鬼の生徒会長
```json
{
  "name": "封印の右脚・鬼の生徒会長",
  "type": "special",
  "cost": null,
  "range": "1-2",
  "power": "3",
  "speed": "4",
  "armor": "2",
  "guard": "5",
  "boost": {
    "name": "式神・Shiranui",
    "cost": "-",
    "timing": "Continuous",
    "effect": [
      "You cannot be Pushed or Pulled. At the start of your turn, you may discard 1 card, then retrieve 1 Exodia piece from your Discard Pile to your hand."
    ]
  },
  "effect": [
    "When you are hit (after Hit effects), you may discard any number of cards from your hand. For each card discarded this way, +2 Armor.",
    "AFTER: Draw 1 card. If it is an Exodia piece, keep it (the Oni's luck finds the next piece)."
  ],
  "description": "百鬼あやめ的右腳是 Exodia 的防禦軸。鬼族學生會長的鬼之力化為高 Armor／Guard，式神 Shiranui 使她無法被移動，受擊時以棄牌換取護體。重生後的抽牌讓「最幸運成員」的傳說繼續發威——她總能找到下一張零件。"
}
```

### Yuzuki Choco — 封印の左脚・悪魔の保健医
```json
{
  "name": "封印の左脚・悪魔の保健医",
  "type": "special",
  "cost": null,
  "range": "1",
  "power": "2",
  "speed": "3",
  "armor": "1",
  "guard": "4",
  "boost": {
    "name": "悪魔の契約・ちょっこーん！",
    "cost": "-",
    "timing": "Instant",
    "effect": [
      "Gain 2 life. The opponent loses 1 life (a Demon's contract always takes its toll).",
      "Retrieve 1 Exodia piece from your Discard Pile to your hand.",
      "For each Exodia piece in your hand, +1 Guard."
    ]
  },
  "effect": [
    "BEFORE: Gain 3 life. If you are at maximum life, +2 Power (the Demon's true nature awakens).",
    "HIT: The opponent cannot discard cards from their hand during their next turn. Pull them 1 space with your Demon's tail.",
    "AFTER: Draw 1 card. If it is an Exodia piece, keep it (the Demon's contract ensures the pieces assemble)."
  ],
  "description": "癒月ちょこ的左腳是 Exodia 的續航樞紐。惡魔保健醫的契約治療維持湊卡期間的血量，並從棄牌堆撿回失去的零件；手上零件越多防禦越高——她嗜睡卻總在關鍵時刻守護夥伴，是讓五件套安然集結的後援之腳。"
}
```

## 整體平衡設計

| 成員 | 部位 | Power/Speed | 定位 | 聚集機制 |
|------|------|------------|------|---------|
| Oozora Subaru | 頭部 | 1/3 | 決勝核心（極弱） | Cleanup 手牌集齊五張即勝 |
| Minato Aqua | 右腕 | 3/7 | 檢索軸 | HIT 從棄牌堆撈回零件；Boost 抽 2 |
| Murasaki Shion | 左腕 | 4/6 | 抽牌軸 | 窺牌重排；HIT 抓零件；被棄零件時搶回手中 |
| Nakiri Ayame | 右腳 | 3/4 | 防禦軸 | 受擊棄牌換 Armor；AFTER 抓零件；起手撈零件 |
| Yuzuki Choco | 左腳 | 2/3 | 續航樞紐 | 回血+撿回零件+AFTER 抓零件；禁對手棄牌 |

**勝利條件**：頭部卡（封印の頭部・太陽のマネージャー）的 Cleanup 效果——回合結束時，若手牌中同時持有右腕／左腕／右腳／左腳四張 Exodia 零件，「黑暗大法師・二期生降臨」，直接獲得勝利。完整重現「二期生黑暗大法師」的傳說，同時透過頭部弱化、零件配合、受擊展示與棄牌反制保持對戰張力。

**資源設計**：本主題完全不使用 Gauge 與 Force——所有代價統一以「手牌／生命／展示資訊」呈現，Exodia 零件的攻防純粹圍繞手牌、棄牌堆與情報運作。

## 實作方式

將此主題寫入 `reports/holo-indie/exceed/hololive 2nd Gen/theme-1.json`（與既有 theme-1.json 的結構一致）。輸出 JSON 以角色為單位，每一張牌包含上述完整欄位（name/type/cost/range/power/speed/armor/guard/boost/effect/description）。
