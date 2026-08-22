# hololive English -Advent- — 逃獄（Breakout from The Cell）規劃

## 參考概念（設計靈感來源）

Advent（holoAdvent）是 hololive English 第三期生，2023 年 7 月出道，共五位成員（holo-unit.md 記載）：**Shiori Novella（シオリ・ノヴェラ）、Koseki Bijou（古石ビジュー）、Nerissa Ravencroft（ネリッサ・レイヴンクロフト）、Fuwawa Abyssgard（フワワ・アビスガード）、Mococo Abyssgard（モココ・アビスガード）**（FUWAMOCO 姊妹共享一個頻道）。

Advent 最獨特、也最「別無分號」的集體迷因，是**「The Cell 監獄」與「集體越獄」**：

- **全員皆是被封印的囚犯**：五位成員的官方 lore 都是「因故被封印在秘密地底監獄 The Cell」——但**每人被封印的原因都不同**：Shiori（竊取禁忌知識）／Bijou（情感之寶石的光芒引發爭奪戰）／Nerissa（歌聲潛力危險、眾神畏懼）／FUWAMOCO（雙胞胎惡魔守衛犬在天界惹麻煩）。
- **集體越獄**：Shiori 是**越獄的主謀**，策畫並解放所有同期生，五人一起逃出 The Cell——不是偶像出道，而是「囚犯集體破獄出道」。
- **與 Justice 的 Seal 對照**：Advent 主題與 Justice「監禁引擎」互為鏡像——Justice 把敵人的卡關進 Seal 區（The Cell 監獄），Advent 則**從 Seal 區越獄**（逃出監獄）；獵人 vs 逃亡者（#AdVSJus）的攻防由此形成。
- **原創曲的「囚→逃→解放」敘事**：《Prisoner》（囚犯）→《Breakout》（破獄）→《Unchained》（解鎖）→《All for One》（萬眾一心）→《Rebellion》（反叛），完整重現監獄逃脫的弧線。
- **監獄鳥的集體記憶**：粉絲群名（Novelites／Pebbles／Jailbirds／Ruffians）與整體群體名 **Adventrix**，呼應「監獄鳥」意象。

### 用語定義：封存區＝The Cell 監獄

正式 Exceed 規則中，**「Seal（封存）」**是將卡片面朝上移出遊戲、放到**封存區（Sealed Area）**的動作；被封存的卡通常難以取回（參考 #407「從封存區返回手牌」、#544、#551、#1185「用封存區的卡 Strike」）。

**本主題將「封存區」直接實作為「The Cell 監獄」**：Advent 囚犯**開局即在封存區（獄中）**，必須達成條件自行越獄（離開封存區返回手牌），且隨時可能被獄卒（Justice）重新逮捕——「被囚禁 ⇄ 越獄」的循環。

### 每位成員的招牌迷因（作為 boost 名稱與效果意象）

| 成員 | 稱號 | 種族／職業 | 招牌迷因 |
|------|------|-----------|---------|
| Shiori Novella | The Archiver（檔案管理員） | 知識蒐集者 | "Don't you think that's a wonderful story?"、離題（Tangents）、用剪刀吃東西、書籤（栞）、發光眼睛 |
| Koseki Bijou | Jewel of Emotions（情感之寶石） | 結晶生命體 | 🗿 摩艾石像、「Bon Bijou!」、Kira-kira、BEEP 文化、「媽媽收集」 |
| Nerissa Ravencroft | The Demon of Sound（音之惡魔） | 被封印的惡魔歌姬 | "Hiya darlings!"、螢光棒（penlights）、down bad、「The Demon of Soup」、烏鴉／音符 |
| Fuwawa Abyssgard | The Fluffy One（蓬鬆擔當） | 惡魔守衛犬 | "BAU BAU!"、「I'm not a chihuahua, I'm Fuwawa!」、「Together we're FUWAMOCO!」、猜拳冠軍 |
| Mococo Abyssgard | The Fuzzy One（毛茸茸擔當） | 惡魔守衛犬 | "BAU BAU!"、「I'm not Fuwawa, I'm Mococoeh!」、「Ehehe, it's play time!」、搗蛋鬼、語尾「え」 |

---

## 主題設計：Breakout 逃獄引擎

### 核心機制：逃獄（Breakout）

以 Advent「五位囚犯被困 The Cell、最後集體越獄」為主題，將 **Seal（封存）區**實作監獄。每位玩家擁有五張 Advent 成員卡（Shiori／Bijou／Nerissa／Fuwawa／Mococo 各一張），**開局時全部面朝上置入封存區（The Cell）**——如同五人同時被困在監獄底層：

- **逃獄（Breakout）**：於你回合開始時，若你已達成該成員的「逃獄條件（Breakout Trigger）」，可將她從封存區返回手牌（逃獄成功）並獲得其「逃獄效果」。返回手牌後即可正常打出使用。
- **獄卒（Jailer）**：對手的反制／棄牌／命中效果可將你**已逃獄的成員再次送入封存區**（獄卒重新逮捕）——此時需重新滿足她的逃獄條件才能再次脫逃，形成「越獄 ⇄ 再逮捕」的攻防循環。
- **監獄的節奏（封印期間）**：被封存的成員卡不可被使用，但**每被封存 1 名成員，你手牌上限 +1**（囚犯越多、獄方戒備越鬆，越能籌劃越獄）。

**共通 effect「Breakout（脫獄）」**：
> 「Breakout：當此卡位於封存區（The Cell）時，於你回合開始時，若你於上回合結束以來已滿足［該成員的逃獄條件］，你可以將此卡從封存區返回手牌，並獲得其『逃獄效果』。」

### 角色對應與各自專屬效果（成員 → 稱號 → 逃獄條件 → 逃獄效果）

每位成員的逃獄條件對應她的「被封印原因」與招牌迷因；逃獄效果則是她越獄後解放的能力：

| 成員 | 稱號 | 逃獄條件（封印原因） | 逃獄效果（解放能力） |
|------|------|---------------------|---------------------|
| Shiori Novella | The Archiver | **知識積累**：上回合你抽牌／檢視合計 2 張以上（竊取禁忌知識的執念） | 檢視牌頂 2 並置回任意順序（剪刀／書籤的靈巧） |
| Koseki Bijou | Jewel of Emotions | **光芒放射**：上回合你受到至少 1 點傷害（情感寶石在壓力下碎裂發光） | 回復 2（光芒的療癒，Bon Bijou!） |
| Nerissa Ravencroft | Demon of Sound | **歌聲共鳴**：上回合你命中對手（被永恆封印的歌聲終於解放） | 對手棄 1（歌聲的魅惑，Hiya darlings!） |
| Fuwawa Abyssgard | The Fluffy One | **守護忠誠**：上回合你進行過 Guard／防禦（守衛犬的職責） | Draw 1（守護犬的奔馳，BAU BAU!） |
| Mococo Abyssgard | The Fuzzy One | **搗蛋遊走**：上回合你 Advance／Retreat（搗蛋鬼四處亂竄） | Move 2（玩樂的愉悅，Ehehe!） |

- **集體越獄（X 強化）**：逃獄的意義在於「全員齊聚」——效果數值依「已逃獄成員數 X」等比強化（如 Shiori 檢視 X 張、Bijou 回復 X、Nerissa 對手棄 X 等）。五人都逃出時觸發 **Adventrix 齊聚**——你每回合首次命中 +1 Power 且受擊時回復 1（監獄鳥全數解放）。

### 平衡設計

1. **逃獄太快／太強？** → 逃獄需先滿足各自的「逃獄條件」，無法免費全數逃出；且已逃獄成員仍會被獄卒重新逮捕（需重新滿足條件）。
2. **效果互相循環？** → 逃獄效果以「命中／檢視／回復」等觸發為前提、同名效果一回合一次，避免無限循環；集體越獄以「已逃獄成員數」計，獄卒逮捕即回落。
3. **Exceed 既有機制** → 全程以既有 Seal 區（監獄）、手牌、棄牌堆、Boost 區運作，善用封存區既有效果（#407 返回手牌、#1185 封存區 Strike 等），不另造輪子、不新增計數器／雙面卡。

### 確保擴展性

- 逃獄可與 Justice「監禁引擎」對接成**跨期對局**：Advent 越獄 vs Justice 逮捕的攻防循環（獵人 vs 逃亡者，#AdVSJus 的實戰化）。

---
## 總結

| 主題 | 核心機制 | 集體迷因連結 |
|------|---------|-------------|
| 1. Breakout 逃獄引擎 | 逃獄條件＋逃獄效果，獄卒可再逮捕（Seal 區＝監獄） | 五位囚犯達成各自封印原因的逃獄條件破獄而出 |

**資源設計**：不使用 Gauge／Force／Exceed／Character Cards／Additional Cards 機制，無額外計數器、無雙面卡、無額外卡牌，卡片效果盡量不綁卡名。純粹以既有 Zones（手牌、棄牌堆、公開區、Boost 區）與 **Seal 封存區**（實作 The Cell 監獄）運作，善用封存區既有規則（#407 返回手牌、#1185 封存區 Strike 等），將 Advent「囚犯 → 集體越獄」的故事實作於 Exceed 的既有空間中。
