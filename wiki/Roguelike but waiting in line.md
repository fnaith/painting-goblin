---
tags: ['#idea', '#task/suspend', '#game', '#wip']
---

# 一維排隊 Yomi RPG（MVP完整規格）

---

# 🧠 1. 核心概念

本遊戲是一個：

> 基於同步戰鬥的「一維排隊生存RPG」

核心由三件事構成：
- ⚔️ 戰鬥（決策）
- 🚶 隊列推進（壓力）
- 🔁 規則變化（環境 + 夥伴）

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

## 🧠 核心概念

本遊戲是一個 1v1 回合制卡牌對戰系統，使用四種核心數值：

-   **Speed**：決定先手順序（節奏）
-   **Power**：決定傷害與壓制能力
-   **Armor**：減少所受傷害
-   **Guard**：決定是否能封鎖對手反擊（Stun）

------------------------------------------------------------------------

## 🃏 卡牌數值表

| 牌   |   Range |   Speed |   Power |   Armor |   Guard |
| ---- | ------- | ------- | ------- | ------- | ------- |
| A    |      近 |       7 |       1 |       2 |       0 |
| B    |      近 |       6 |       3 |       0 |       0 |
| C    |    中近 |       5 |       3 |       2 |       0 |
| D    |    中   |       4 |       4 |       1 |       0 |
| E    |  遠中   |       3 |       5 |       2 |       1 |
| F    |  遠     |       2 |       6 |       2 |       0 |
| G    |  遠     |       1 |       7 |       3 |       2 |

------------------------------------------------------------------------

## ⚔️ 戰鬥階段

### Step 1：選牌

敵我雙方同時秘密選擇一張牌。然後同時展示。

### Step 2：Range判定

敵我雙方展示的卡牌若Range不符合現況則無效。視為Speed=0,Power=0,Armor=0,Guard=0

### Step 3：Damage計算

敵方造成傷害值 = max(0, 敵方卡牌Power - 我方卡牌Armor)
我方造成傷害值 = max(0, 我方卡牌Power - 敵方卡牌Armor)

### Step 4：Stun判定

敵方會不會造成擊暈 = 敵方造成傷害值 > 我方卡牌Guard
我方會不會造成擊暈 = 我方造成傷害值 > 敵方卡牌Guard

### Step 5：Speed判定（先手）

比較敵我雙方展示的卡牌的Speed

### Step 5.1：雙方展示的卡牌的Speed相同時

敵方HP -= 我方造成傷害值
我方HP -= 敵方造成傷害值

### Step 5.2：雙方展示的卡牌的Speed不同時

Speed較高者成為先攻方，另一人成為後攻方。

後攻方HP -= 先攻方造成傷害值

#### Step 5.2.1：先攻方會造成擊暈

結束戰鬥階段

#### Step 5.2.2：先攻方不會造成擊暈

先攻方HP -= 後攻方造成傷害值

結束戰鬥階段


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

# 🃏 卡牌強化系統規格

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

# 強化階級

## Tier 1：數值強化

直接修改卡牌數值。

### 輕量化

* Speed +1

### 鋒利

* Power +1

### 厚甲

* Armor +1

### 穩固

* Guard +1

### 延伸

* Range擴展一級

範例：

近 → 近、中近

中 → 中近、中、遠中

---

## Tier 2：特性強化

增加額外效果。

### 穿甲

造成傷害時：

忽略1點Armor

---

### 重擊

若造成傷害：

額外+1傷害

---

### 防反

成功承受攻擊後：

反擊1傷害

---

### 堅守

Guard +2

Speed -1

---

### 靈巧

Speed +1

Armor -1

---

## Tier 3：條件強化

根據戰況獲得額外收益。

### 追擊

若Speed高於對手：

Power +2

---

### 逆轉

若Speed低於對手：

Power +3

---

### 精準

Range完全符合時：

Power +2

---

### 決鬥者

Speed相同時：

造成傷害翻倍

---

### 壓制

對手已受傷時：

Power +2

---

## Tier 4：規則強化

直接改變戰鬥判定。

### 破防

造成傷害時：

對手Guard視為0

---

### 霸體

每場戰鬥第一次受到Stun：

改為無效

---

### 閃避

若Speed差距 ≥ 3：

本次受到傷害歸零

---

### 貫穿

造成Stun時：

傷害翻倍

---

### 先制

若Speed較高：

傷害先結算後再判定反擊

---

## Tier 5：傳說強化

影響整體戰鬥系統。

### 疾風模組

所有卡牌：

Speed +2

---

### 堡壘模組

所有卡牌：

Armor +2

---

### 霸王模組

所有造成的傷害：

無視Guard

---

### 神射模組

遠、中遠牌：

Power +3

---

### 全域延伸

所有卡牌：

Range +1級

---

# 強化槽系統

每張卡牌最多擁有：

* 1個數值強化
* 1個特性強化
* 1個條件強化
* 1個規則強化

範例：

卡牌E

基礎：

* Speed 3
* Power 5
* Armor 2
* Guard 1

強化：

* 輕量化
* 穿甲
* 精準
* 破防

最終效果：

* Speed 4
* Power 5
* Armor 2
* Guard 1
* 無視1 Armor
* Range符合時 Power +2
* 傷害無視Guard

---

# 獎品掉落規則

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

---

# 設計原則

優秀強化應增加：

* 預判深度
* 牌型差異
* 構築方向

不應只增加：

* 傷害
* 血量
* 勝率

---

# Build範例

## 速度流

核心：

* 輕量化
* 靈巧
* 追擊
* 疾風模組

玩法：

依靠先手造成Stun。

---

## 坦克流

核心：

* 厚甲
* 堅守
* 霸體
* 堡壘模組

玩法：

承受攻擊後反打。

---

## 狙擊流

核心：

* 延伸
* 穿甲
* 精準
* 神射模組

玩法：

維持遠距離高傷害輸出。

---

## 壓制流

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
