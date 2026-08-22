# hololive 4th Gen — holoForce：飛翔する武力（Returning Force）規劃

## 參考概念（設計靈感來源）

4th Gen 是 hololive 官方命名為「**holoForce（ホロフォース）**」的期生，「Force」即「武力／戰力」之意。五位成員全都是超越人類的怪物級存在，組成一支配得上「Force」之名的戰鬥武力：

- **桐生ココ（Kiryu Coco）[R]・指揮官**：**西方龍**。AsaCoco 晨間新聞、紅SC、Meme Review、海外Reddit橋樑，hololive 國際化推手。種族武力＝**龍之息**。稱號**龍の指揮官**。
- **天音かなた（Amane Kanata）[R]・力量擔當**：**天使**。149cm 卻有 50kg 握力的怪力（Kana-Gorilla）、Perfect Pitch 歌姬。種族武力＝**怪力**。稱號**怪力の天使**。
- **常闇トワ（Tokoyami Towa）・狙擊擔當**：**惡魔**。Apex 頂尖狙擊手，TMT（マジ天使）／TMD（マジデビル）雙面性。種族武力＝**暗夜的狙擊**。稱號**暗夜の惡魔**。
- **角巻わため（Tsunomaki Watame）・支援擔當**：**不死羊**。8秒重生、Watame No.1、武道館夢想。種族武力＝**不死的戰歌**。稱號**不死の羊**。
- **姫森ルーナ（Himemori Luna）・突擊擔當**：**戰姫公主**。異世界糖果王國公主、Dark Souls 戰姫、んなーしょい！。種族武力＝**戰姫之劍**。稱號**戰姫の公主**。

### 集體迷因：出擊と飛翔（Returning Force）

「**飛翔する武力（Returning Force）**」是 holoForce 最核心的意象——這支怪物戰隊的戰士**每次出擊後都會飛回戰隊重新整備**，武力永不缺席：龍振翅而歸、天使展翼而返、惡魔匿於暗夜、不死羊無限重生、戰姬凱旋歸陣。holoForce 是一支「打不散、打不退」的武力。

**核心意象：出擊後飛回。** 本主題以「**Strike 後、下回合從棄牌堆飛回 Boost 區**」作為引擎：把 holoForce 的「出擊與歸還」化為**武力卡 Strike 後、下回合飛回 Boost 區的循環**。

---

## 主題設計：出擊と飛翔（Returning Force）— 出擊後飛回

### 核心機制：武力卡（Force Card）

「飛翔する武力」不需額外規則系統——**出擊與歸還直接做成每張主題卡自己的卡片效果**：

- 五位成員各擁有一張**武力卡**（特殊卡，cost null，Power 1-2）。
- **常駐**：以 Boost 使用時正面放入 Boost 區，成為戰隊一員，提供持續武力（依 Boost 區武力卡數量 X 強化）。
- **出擊**：此卡可用作 Strike（出擊攻擊）。
- **飛翔**：**此卡 Strike 後，下回合開始時從棄牌堆飛回 Boost 區**——如同怪物戰士出擊後回到戰隊整備，武力永不缺席，且飛回後立即恢復持續武力。

**每位成員的武力方向不同（非對稱的戰隊分工）：**

| 成員 | 戰隊定位 | 稱號 | 武力（持續 Boost） |
|------|---------|------|--------------------|
| 桐生ココ | 指揮官 | 龍の指揮官 | 你的 attack 獲得 +X Power（龍之威壓） |
| 天音かなた | 力量擔當 | 怪力の天使 | 你的 attack 獲得 +X Speed 或 Push（握力爆發） |
| 常闇トワ | 狙擊擔當 | 暗夜の惡魔 | Strike 時讓對手 Speed -X（Apex 狙擊） |
| 角巻わため | 支援擔當 | 不死の羊 | Strike 時回復 X（不死戰歌） |
| 姫森ルーナ | 突擊擔當 | 戰姫の公主 | Strike 時 +X Armor（戰姫守護） |

（X 為你 Boost 區中武力卡的數量。）

### 勝利條件「Force 全開（Force Awakening）」

**沒有條件勝利**——以武力卡在 Boost 區的持續武力累積優勢，將對手生命打空即獲勝。

- 五張武力卡齊聚 Boost 區時，觸發「**Force 全開**」：戰隊獲得全面壓制（+5 Power／+5 Speed／Strike 時抽 5／Strike 時 +5 Armor）。
- 武力卡 Strike 後飛回 Boost 區，讓持續武力與 Force 全開沒有空窗——這支武力「打不散、打不退」。

### 平衡設計

1. **飛回太強？** → 飛回需「Strike 後下回合」才發生，出擊當下該卡離開 Boost 區（暫時失去其武力），中間有節奏空窗。
2. **Force 全開太強？** → 是**持續壓制**而非直接勝利；武力卡被封印／被棄掉 Boost 區就失去武力（戰隊被拆散）。
3. **單卡弱化** → 武力卡 Power 1-2，價值在循環的持續武力，非單卡戰力。
4. **受擊展示**：達成 Force 全開前受擊需展示手牌，讓對手掌握戰隊集結進度。
5. **既有機制運用** → 只用既有 Boost 區、棄牌堆、封存區，不使用 Gauge／Force／Exceed／Character Cards／Additional Cards、額外計數器／雙面卡／額外卡牌。

### 確保擴展性

- **飛回可循環**：Strike → 棄牌堆 → 下回合飛回 Boost，武力卡幾乎不會真正離場。
- **成員廣度**：holoForce 之外的怪物級成員可加入成為「客座武力」。
- **全開可疊代**：可讓 Force 全開的壓制數值隨卡池成長。

---

## 總結

**主題**：holoForce「飛翔する武力（Returning Force）」——出擊後飛回

- **核心機制**：武力卡（Force Card）——五位成員各一張特殊卡（cost null，Power 1-2）。以 Boost 使用時正面放入 Boost 區成為戰隊一員，提供依「Boost 區武力卡數量 X」等比強化的持續武力；可用作 Strike（出擊）；**Strike 後、下回合開始時從棄牌堆飛回 Boost 區**，讓武力循環不間斷。五位成員武力方向不同（非對稱分工）：ココ 指揮官（attack +X Power）／かなた 力量（attack +X Speed 或 Push）／トワ 狙擊（Strike 讓對手 Speed -X）／わため 支援（Strike 回復 X）／ルーナ 突擊（Strike +X Armor）。五張齊聚觸發「Force 全開」全面壓制。
- **勝利條件**：無條件勝利——以武力卡在 Boost 區的持續武力累積優勢，將對手生命打空即獲勝。

**資源設計**：不使用 Gauge／Force／Exceed／Character Cards／Additional Cards／額外計數器／雙面卡／額外卡牌，純粹以既有 Zones（手牌、棄牌堆、公開區、Boost 區、封存區）與「武力卡正面放入 Boost 區＋Strike 後下回合飛回 Boost 區」運作。卡片效果以既有數值與 Boost 區為核心，不綁卡名（以「武力卡」泛指五張主題卡）。

## 實作方式

將此主題以 5 張「武力卡」（特殊卡）寫入 `reports/holo-indie/exceed/hololive 4th Gen/theme.json`。每張牌以 Boost 使用時可「正面放入 Boost 區」成為戰隊一員，並在其 effect／boost 撰寫「Strike 後，下回合開始時從棄牌堆飛回 Boost 區」；「武力（依 X 等比強化）」撰寫於 boost／effect 欄位。
