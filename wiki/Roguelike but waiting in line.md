---
tags: ['#idea', '#task/suspend', '#game', '#wip']
---

# 一維排隊 RPG（MVP完整規格）

---

# 🧠 1. 核心概念

本遊戲是一個：基於同步戰鬥的「一維排隊生存RPG」

核心由2件事構成：
- ⚔️ 戰鬥（決策）
- 🚶 隊列推進（壓力）

---

# 📏 2. 世界結構（一維隊列）

[終點獎品（有限）]
↑
敵人隊列
↑
玩家隊列（含夥伴）
↑
入口

規則：
- 只有最前線進入戰鬥
- 所有單位單向前進
- 玩家永遠在隊列中

# 📏 3. 核心循環


隊列推進
↓
戰鬥
↓
勝利 → 推進 / 獎勵
↓
失敗 → 疲勞 + 插隊風險
↓
夥伴 / 環境改變規則
↓
重複直到終點

---

# ⚔️ 4. 戰鬥系統

## 獲勝方式

將對方角色的HP降至 0 即獲勝

## 配置

### 角色配置

- 一場遊戲有2位角色：玩家角色與敵人角色
- 每位角色
    - 起始生命20
    - 有自己的牌庫(Deck)，包含一副16張卡牌的牌組。實際內容之後說明。
    - 有自己的手牌(Hand)，可從自己的牌庫抽牌移動到手牌，使用卡牌時從手牌移動到展示區(Reveal Area)，上限為7張
    - 有自己的棄牌堆(Discard)，展示區的卡牌使用後移動到棄牌堆，要抽牌時牌庫沒牌就把棄牌堆洗回牌庫再抽一張

## 場地配置

- 場地(Board)共有7格。從左到右編號從1~7
- 玩家角色在2，用藍色方型表示
- 敵人角色在6，用紅色圓形表示
- 雙方初始Range為abs(2-6)=4
- 角色不能站同一格

## 卡牌

卡牌有下列屬性：

- Name : 卡牌名稱
- Speed為此攻擊的速度。速度快的一方會先攻擊。
- Range為此攻擊可以命中的格子，從攻擊來源(通常是你的角色)所在的格子為0開始計算。Range有最小值與最大值兩個數字。當Range僅顯示一個數字時，代表最小值等於最大值。Range為N/A的攻擊無法命中。
- Power : 為此攻擊可以造成多少傷害(damage)，對手的生命會減少與傷害等量的值。Power為N/A的攻擊不會造成傷害(攻擊不會因未造成傷害而變為未命中)。
- Armor : 為此攻擊抵禦傷害的能力，Strike中受到的傷害會減少相當於Armor的值。沒有顯示Armor時，Armor為0。
- Guard : 為此攻擊避免擊暈的能力，Strike中受到的傷害大於Guard值時會被擊暈(stunned)(若你在攻擊前被擊暈，你將無法攻擊)。沒有顯示Guard時，Guard為0。
- Before : 攻擊前發動的效果
- Hit : 命中才發動的效果
- After : 攻擊後發動的效果
- Boost : 卡片被當作Boost時的效果

## 戰鬥流程

- 戰鬥開始
    - 決定先手角色
    - 設置角色到場地上
    - 先手角色從自己牌組抽5張
    - 後手角色從自己牌組抽6張
- 從先手角色開始執行回合流程
    - 抽牌，從自己的牌庫抽2張牌
    - 從3個行動選1個執行
        - 移動行動(Move Action)。實際內容之後說明。
        - 增益行動(Boost Action)。實際內容之後說明。
        - 攻擊行動(Strike Action)。實際內容之後說明。
    - 雙方HP>0
        - 雙方選擇手牌丟棄，直到手牌數量<=上限
        - 輪到對方回合
- 戰鬥結束
    - 結算戰鬥結果

## 移動行動

選擇一個未被佔據的格子作為移動目標，根據距離丟棄對應數量的手牌到棄牌堆移動

## 增益行動

把卡牌移到展示區，結算卡牌上的Boost效果

Boost 有2類：

### Immediate

例如：Draw 2

立刻完成
↓
棄掉

### Continuous

- 留在Reveal區，直到Cleanup或效果要求棄。
- 效果可疊加

## 攻擊行動

- 雙方角色從手牌覆蓋一張卡牌到展示區
- 雙方角色同時翻開卡牌
- 決定先攻方
    - Speed較高的一方為先攻方。Speed相同時，發起方為先攻方
- 先攻方先依以下順序結算攻擊，隨後後攻方依以下順序結算攻擊
    - 如果已被擊暈(Stun)，跳過下列所有步驟
        - 執行Before效果
        - 判斷對方是否於Range內，若是則此攻擊命中
        - 執行Hit效果
        - 造成傷害(總Power減對方的Armor)
        - 最終傷害>=對方的Guard時，造成對方擊暈
    - 執行After效果(即使未命中)
- Cleanup階段
    - 棄置所有Continuous Boost。

## 效果(Effect)

### Close

移到：與對方相鄰。

例如：
A □ □ B
↓
Close
↓
A □ B

### Advance

Advance X：朝對方走X。不能超過對方。

### Retreat

往反方向走。
若牆壁：停止。

### Push

把對方推開。

若撞牆：停止。
不會額外傷害。

### Pull

把對方拉近。

若已經相鄰：不能再拉。

### Move

Move：自己自由選方向。

### Advanc

只能靠近。

### Retreat

只能遠離。

### Ignore Armor

若寫：Ignore Armor

直接：

Power
↓
扣血

Armor 不生效。
Guard 仍正常判定。

### Cannot be Stunned

若效果寫：Cannot be Stunned

即使：Power > Guard

仍可完成攻擊。
傷害照扣。

### Cannot Move

若：
Before：Advance2

但：
Cannot Move
↓
整段移動失效。
其他效果照常。

### Cannot Push

若效果：

Cannot be Pushed

Push：直接無效。

### Critical

攻擊命中時：追加效果。
不同角色定義不同。

### Miss

代表：Range 不成立。

不是：攻擊被取消。

After：通常仍發動。


---

# 💀 5. 玩家系統（疲勞/插隊）

## 核心規則

- 玩家永遠在隊列中
- 戰敗不死亡，而是累積疲勞

---

## 疲勞效果

HP歸零 → 疲勞 +1

疲勞效果：
- 排隊順位下降
- 被NPC插隊
- 支援能力下降（可選）

---

## 插隊機制

- 疲勞越高 → 被插隊機率越高
- 或直接後退1～2格

# 🏁 6. 終點系統

- 終點獎品有限
- 敵人到達會消耗獎品
- 形成競爭壓力

---

# 7. 強化機制

## 設計目標

卡牌強化系統不是單純提升數值，而是逐步改變戰鬥決策。

玩家獲得獎品後，可選擇強化既有卡牌，而非取得更高階版本。

強化應優先影響：

* Speed（節奏）
* Power（傷害）
* Armor（承傷）
* Guard（抗擊暈）
* Range（適用距離）
* 戰鬥規則

避免：

* 單純數值膨脹
* 絕對優勢
* 無腦最佳解

---

## 強化階級

### Tier 1：數值強化

直接修改卡牌數值。

* 輕量化 : Speed +1
* 鋒利 : Power +1
* 厚甲 : Armor +1
* 穩固 : Guard +1
* 靈巧 : Speed +1，Armor -1
* 延伸 : Range擴展一級

---

### Tier 2：特性強化

增加額外效果。

* 穿甲 : 造成傷害時，忽略1點Armor
* 重擊 : 若造成傷害，額外+1傷害
* 防反 : 成功承受攻擊後，反擊1傷害

### Tier 3：條件強化

根據戰況獲得額外收益。

* 追擊 : 若Speed高於對方，Power +2
* 逆轉 : 若Speed低於對方，Power +3
* 精準 : Range完全符合時，Power +2
* 決鬥者 : Speed相同時，造成傷害翻倍
* 壓制 : 對方已受傷時，Power +2

### Tier 4：規則強化

直接改變戰鬥判定。

* 破防 : 造成傷害時，對方Guard視為0
* 霸體 : 每場戰鬥第一次受到Stun，改為無效
* 閃避 : 若Speed差距 ≥ 3，本次受到傷害歸零
* 貫穿 : 造成Stun時，傷害翻倍
* 先制 : 若Speed較高，傷害先結算後再判定反擊

## Tier 5：傳說強化

影響整體戰鬥系統。

* 疾風模組 : 所有卡牌，Speed +2
* 堡壘模組 : 所有卡牌，Armor +2
* 霸王模組 : 所有造成的傷害，無視Guard
* 神射模組 : 遠、中遠牌，Power +3
* 全域延伸 : 所有卡牌，Range +1級


## 強化槽系統

每張卡牌最多擁有：

* 1個數值強化
* 1個特性強化
* 1個條件強化
* 1個規則強化

## 獎品掉落規則

普通獎品：

* Tier 1
* Tier 2

稀有獎品：

* Tier 2
* Tier 3

史詩獎品：

* Tier 3
* Tier 4

傳說獎品：

* Tier 5

## 設計原則

優秀強化應增加：

* 預判深度
* 牌型差異
* 構築方向

不應只增加：

* 傷害
* 血量
* 勝率

## Build範例

### 速度流

核心：

* 輕量化
* 靈巧
* 追擊
* 疾風模組

玩法：

依靠先手造成Stun。


### 坦克流

核心：

* 厚甲
* 堅守
* 霸體
* 堡壘模組

玩法：

承受攻擊後反打。

### 狙擊流

核心：

* 延伸
* 穿甲
* 精準
* 神射模組

玩法：

維持遠距離高傷害輸出。

### 壓制流

核心：

* 重擊
* 壓制
* 破防
* 霸王模組

玩法：

快速造成第一次傷害後滾雪球。


```

# 🤝 7. 夥伴系統

## 本質

> 夥伴 = 改變Yomi規則，而非數值

---

## 能力池（20種）

### 戰鬥型
- 騎士：Block成功反擊
- 狂戰士：平手仍傷害
- 刺客：無視Block
- 獵人：先手
- 守衛：減傷1

---

### 節奏型
- 僧侶：減少疲勞
- 鼓手：推進減緩
- 工程師：降低推進速度
- 時間術士：凍結推進
- 舞者：Support強化

---

### 資訊型
- 斥候：預覽敵人
- 占卜師：提示Yomi
- 間諜：偷看牌
- 記錄者：顯示克制
- 賭徒：高風險高回報

---

### 戰術型
- 鍛造師：穿透攻擊
- 鍊金術士：Support轉傷害
- 弓手：打後排
- 破壞者：Block推進敵人
- 靈媒：免疫疲勞

---

# 🌪️ 8. 環境系統

## 本質

> 改變Yomi規則

---

## 15種環境

### 節奏變化
- 暴風雨：Support削弱
- 黑夜：資訊不完整
- 地震：Block失效
- 大霧：隨機行動
- 乾旱：Support無效

---

### 壓力型
- 崩塌通道：額外推進
- 擁擠隊列：插隊+50%
- 饑荒：每回合疲勞+1
- 瘟疫：全體HP-1
- 混亂：順序打亂

---

### 規則型
- 攻擊強化：Attack +1
- 防禦時代：Block停止推進
- 支援時代：Support強化
- 高速通道：推進減少
- 崩壞秩序：隊列隨機交換

---

# 🧍 11. 玩家死亡規則

HP歸零 → 疲勞 +1 → 排隊順位下降 → 被插隊

本質：
> 玩家不是死亡，而是失去排隊優先權

---

# 🧠 設計核心原則

## ✔ 強化必須做到其中一件：
- 改變勝負結果
- 改變平手行為
- 改變隊列結構
- 改變疲勞機制
- 改變環境規則

## ❌ 禁止：
- 純數值膨脹（無系統影響）
- 永久壓制型效果
- 不影響Yomi決策的buff

```

---

- one dimension rpg
- goal is beating people in the waiting line for prize
- 需要排隊遊戲獨特的挑戰
    - 群落發展
    - 排隊時抵抗環境變化
        - project zomboid
            - [https://pzwiki.net/wiki/Moodles/zh](https://pzwiki.net/wiki/Moodles/zh)
            - [https://playgame.wiki/projectzomboid/gonglue/all](https://playgame.wiki/projectzomboid/gonglue/all)
            - 失血
            - 感冒
            - 負重
            - 過熱
            - 受寒
            - 飢餓 Hunger
            - 受傷 [https://pzwiki.net/wiki/Health#Types_of_Injuries](https://pzwiki.net/wiki/Health#Types_of_Injuries)
            - 生病
            - 口渴 Thirst
            - 淋濕
        - don't starve
            - 機制
                - [https://dontstarve.fandom.com/zh/wiki/生命](https://dontstarve.fandom.com/zh/wiki/%E7%94%9F%E5%91%BD)
                - [https://dontstarve.fandom.com/zh/wiki/理智](https://dontstarve.fandom.com/zh/wiki/%E7%90%86%E6%99%BA)
                - [https://dontstarve.fandom.com/zh/wiki/潮濕](https://dontstarve.fandom.com/zh/wiki/%E6%BD%AE%E6%BF%95)
                - [https://dontstarve.fandom.com/zh/wiki/過熱](https://dontstarve.fandom.com/zh/wiki/%E9%81%8E%E7%86%B1)
                - [https://dontstarve.fandom.com/zh/wiki/寒冷](https://dontstarve.fandom.com/zh/wiki/%E5%AF%92%E5%86%B7)
                - [https://dontstarve.fandom.com/zh/wiki/飢餓](https://dontstarve.fandom.com/zh/wiki/%E9%A3%A2%E9%A4%93)
                - [https://dontstarve.fandom.com/zh/wiki/光源類](https://dontstarve.fandom.com/zh/wiki/%E5%85%89%E6%BA%90%E9%A1%9E)
                - [https://dontstarve.fandom.com/zh/wiki/中毒](https://dontstarve.fandom.com/zh/wiki/%E4%B8%AD%E6%AF%92)
            - 環境
                - [https://dontstarve.fandom.com/zh/wiki/日夜週期](https://dontstarve.fandom.com/zh/wiki/%E6%97%A5%E5%A4%9C%E9%80%B1%E6%9C%9F)
                - [https://dontstarve.fandom.com/zh/wiki/雨天](https://dontstarve.fandom.com/zh/wiki/%E9%9B%A8%E5%A4%A9)
                - [https://dontstarve.fandom.com/zh/wiki/強風](https://dontstarve.fandom.com/zh/wiki/%E5%BC%B7%E9%A2%A8)
                - [https://dontstarve.fandom.com/zh/wiki/閃電](https://dontstarve.fandom.com/zh/wiki/%E9%96%83%E9%9B%BB)
                - [https://dontstarve.fandom.com/zh/wiki/火山](https://dontstarve.fandom.com/zh/wiki/%E7%81%AB%E5%B1%B1)
    - 選定道具，可贈與點到的夥伴，強化他們的抗性
        - 每個夥伴顯示需求按鈕，減少查看操作
    - 狀態影響
        - progress bar ui
        - game control script
        - day and night : sanity
        - item ui
        - 插隊系統
        - rain : stamina
        - ice land and snow : hp
        - desert and heat : hp
        - lightening : hp
        - load : stamina
        - storm : stamina
        - fog : hp
- 可郵購道具ubersheep, 晚上發生插隊事件, 限量
- Reference
    - [pet](https://assetstore.unity.com/packages/3d/characters/animals/animal-pack-deluxe-v2-144071)
    - [define game goal](https://assetstore.unity.com/packages/vfx/shaders/heat-haze-effect-53714)
    - [https://www.youtube.com/watch?v=0jexhkwCGOc&ab_channel=阿津](https://www.youtube.com/watch?v=0jexhkwCGOc&ab_channel=%E9%98%BF%E6%B4%A5)
- iso map
    - [https://blog.unity.com/technology/isometric-2d-environments-with-tilemap](https://blog.unity.com/technology/isometric-2d-environments-with-tilemap)
    - [https://www.youtube.com/watch?v=tW744Zgc1YY&ab_channel=Sykoo](https://www.youtube.com/watch?v=tW744Zgc1YY&ab_channel=Sykoo)
    - [https://www.youtube.com/watch?v=tywt9tOubEY&ab_channel=Unity](https://www.youtube.com/watch?v=tywt9tOubEY&ab_channel=Unity)


# Reference

- [[Yomi]]
- [[Exceed]]
