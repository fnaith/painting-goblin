# hololive GAMERS — TAS-kun 的完美操作 主題規劃

## 參考概念（設計靈感來源）

GAMERS 的同期專屬集體迷因整理（來源：`reports/holo-indie/hololive-talents/holo-unit.md` 與 `reports/holo-member/<id>/report.md`）：

- **官方定位：遊戲專注的次級單位（Gaming-focused sub-unit）**。與其他同期以「世代」凝聚不同，GAMERS 以「遊戲」為紐帶——成員皆因對遊戲的熱愛與羈絆而集結。
- **遊樂場（ゲームセンター）出身的招募史**：Fubuki（遊戲部長）在遊樂場看到小粥與沁音結伴，親自招募兩人入團；Mio 是 Fubuki 加入 hololive 前的遊戲老友。四位成員都透過「遊戲」這條線被聚到一起——這是 GAMERS 獨一無二的故事起點。
- **四獸組合（動物擬態）**：白狐（Fubuki）／黑狼（Mio）／貓又（Okayu）／犬神（Korone）——四頭「會玩遊戲的野獸」組成的狩獵群。
- **單位原創曲「We are GAMERS!!!!」(2024) 與「To Be Continued....」(2025)**：前者是集結號令，後者是續篇——「全員齊聚、一起玩下去」的羈絆意象。
- **內部雙人羈絆 OkaKoro（Okayu × Korone）**：加入 hololive 前就是好友、最知名的組合，被形容「不需言語的默契」。
- **SMOK（Mio／Okayu／Korone／Subaru）**：GAMERS 的子集單位。
- **各成員招牌迷因**：Mio＝「こんばんみぉーん！」／Mio-mama 母性／塔羅占卜／怕恐怖遊戲卻因 GAMERS 責任硬玩／Hatotaurus／愛貓 Taiga。Okayu＝「もぐもぐおかゆ！」／飯糰與 Onigiryaa 監獄／全肯定貓／慵懶卻反射驚人。Korone＝「Yubi Yubi!」／DOOG 鏈鋸／Sonic 大使／TAS-kun 復古玩家／28 小時 Maka Maka 耐久／裏人格 enoroK。

**主題核心：TAS-kun 的完美操作**——GAMERS 熱愛把遊戲玩到完美：Korone 的 TAS-kun、Fubuki 的策士操弄、Mio 的塔羅預知、Okayu 的反射神經。主題圍繞「資訊與精準」——四位成員**各看不同位置的資訊**（對手手牌／牌庫頂／距離時機／棄牌堆），再以窺牌、重排、宣告、讀檔重來把每一次對戰當成一次完美通關。

四個主題零件對應四位可操作成員卡：`shirakami-fubuki`、`ookami-mio`、`nekomata-okayu`、`inugami-korone`（Fubuki 同時屬於 1st Gen，但在此作為 GAMERS 的部長零件）。

---

## 主題：TAS-kun 的完美操作 — 讀檔・Retry

### 核心機制：完美重來（Retry）

- Korone 的 TAS-kun、Mio 的塔羅預知、Okayu 的反射神經、Fubuki 的策士操弄——GAMERS 熱愛「把遊戲玩到完美」。
- **資訊分工（各看各的位置）**：每位成員各自負責「看」場上不同位置的資訊——Fubuki 讀對手的**手牌**、Mio 讀**牌庫頂**、Okayu 讀**距離與時機**、Korone 讀**棄牌堆**。四人合起來，等於同時掌握對局的全部情報。
- 主題零件效果圍繞「資訊與精準」：窺看牌庫、重排順序、宣告對手的行動。核心是 **Retry**：當你的 Strike 被 Guard 或未命中，可付代價（棄 1 手牌）「讀檔」——重排手中卡、重置距離、甚至重抽，重新計畫這一回合。

### 角色對應與各自專屬效果

| 成員 | 稱號 | 資訊位置（看哪裡） | 精準特化 |
|---|---|---|---|
| Shirakami Fubuki | 策士狐・Meme Queen | 對手手牌 | 讀檔時窺看對手手牌並重排自己的牌（Among Us 讀心；Scatman 混淆） |
| Ookami Mio | 塔羅占卜狼 | 牌庫頂 | 窺看並重排牌庫頂、宣告對手出牌類型（BEFORE 預知） |
| Nekomata Okayu | 精準反射貓 | 距離／時機 | 精準掌握距離與反應時機，讀檔時可重抽 1（反射矯正）；命中後 Draw |
| Inugami Korone | TAS 完美犬 | 棄牌堆 | 讀檔回收並重排棄牌堆、+Speed（掌握已耗資源） |

### 平衡設計

1. 讀檔每回合限一次、要代價，不能無限重試。
2. 資訊型效果（窺牌、宣告）不直接造成傷害，靠節奏與預判取勝。
3. 對手可用高速先手壓制，不給讀檔機會。
4. 讀檔不重複觸發同名的 HIT 效果（避免循環）。

### 確保擴展性

- 輔助「檢索」讓讀檔燃料充足。
- 可延伸「Perfect Clear（無傷通關）」終局——連續 3 次命中未被 Guard 時獲得爆發壓制。

---

## 總結

**主推主題**：「TAS-kun 的完美操作」— 讀檔・Retry。

- 貼合 GAMERS 的獨特集體記憶：Korone 的 TAS-kun、Fubuki 的策士操弄、Mio 的塔羅預知、Okayu 的反射神經——四獸都是把遊戲「玩到完美」的玩家。
- 資訊分工：四位成員各看不同位置的資訊（對手手牌／牌庫頂／距離時機／棄牌堆），合起來掌握對局全部情報。
- 機制以既有的手牌／牌庫／棄牌堆／距離運作，不使用額外卡／計數器／Gauge／Force，完全符合技能規範。
- 平衡充分：讀檔每回合限一次、要代價、資訊型效果不直接造成傷害，張力充足。

## 實作方式

依此 theme.md 產出四張成員主題零件，輸出至 `reports/holo-indie/exceed/hololive GAMERS/`（`shirakami-fubuki`／`ookami-mio`／`nekomata-okayu`／`inugami-korone`，與既有 `.json` 的欄位格式一致）。每張零件 Power/Speed 刻意弱化，融入該成員招牌迷因作為 Boost 名稱與效果意象，並附帶抽濾／檢索輔助。
