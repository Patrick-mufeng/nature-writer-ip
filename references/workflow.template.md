# 工作流速查（nature-writer-ip）

> 这是 `/init` 在你的项目根创建的速查文档。

---

## 一句话流程

```
找选题
  ├─ 没发过历史的 → /seed brainstorm（季节 × 痛点）
  └─ 发过历史的    → /seed brainstorm（季节 × 痛点 × 你过去做过什么）
  ↓
/seed 写 5 个候选到 → content_pool.md
  ↓
用户选选题 → /script 写脚本 → scripts/<日期>_<id>_<short>.md
  ↓
用户改写 scripts/<id>.md
  ↓
/score scripts/<id>.md → 看 rubric 评分（探索）
  ↓
/predict scripts/<id>.md → 写 immutable 预测 v1 到 predictions/
  ↓
拍摄完 → /shoot scripts/<id>.md
   ├─ 建 videos/<id>/ 目录
   ├─ 询问："拍时实际稿子和 scripts/<id>.md 一致吗？"
   │   ├─ 一致 → cp → videos/<id>/script.md，沿用 v1
   │   ├─ 改了 → 要最终稿 → 算 diff
   │   │   ├─ diff ≥30% → 自动 /predict — v2 → predictions/<id>.md append
   │   │   └─ diff <30% → 询问是否 v2，默认沿用 v1
   │   └─ 大改 → 走 _redo 流程
   └─ buffer +1
  ↓
发布 → /publish + URL → buffer -1
  ↓
T+3 天 → /retro videos/<id>/
   ├─ 抓数据 / 用户粘 → 写 videos/<id>/report.md
   ├─ 追加 ## 复盘 段到 predictions/<id>.md
   ├─ diff scripts/<id>.md vs videos/<id>/script.md → 学改稿 pattern
   └─ 把新观察写入 rubric_notes.md
  ↓
累计 ≥3 同向偏差 → /bump（升级 rubric）
```

---

## 五个阶段对应触发词

### ① 选题阶段

| 想做什么 | 触发词 |
|---|---|
| 看 content_pool.md 排序后的推荐 | "找选题" / "下一篇做什么" |
| 看当前状态 | "状态" |

### ② 打分 + 预测

| 想做什么 | 触发词 | 写文件吗 |
|---|---|---|
| 看一份稿子的 rubric 分（探索） | "打分这篇 path/to/draft.md" | 否 |
| 给最终稿写正式 immutable 预测 | "启动预测" / "给这稿子启动预测" | 是（predictions/...md） |

> **score 与 predict 的核心区别**：
> - score 是探索，无副作用，可反复跑
> - predict 是承诺，写完文件被 hook 锁死

### ③ 发布登记

发完后立刻：

```
"已发布 https://..."
```

### ④ 复盘

T+3 天后：

```
"复盘 predictions/2026-05-18_xxx.md"
```

或：

```
"复盘"
```

后者从 `pending_retros` 取最早的一条。

### ⑤ Rubric 升级（罕见）

满足条件才提议：
- 校准池 ≥ 5 篇
- 上次 bump 后又有 ≥ 3 篇新校准
- 检测到连续 ≥ 3 次同向偏差

满足就跑：

```
"升级 rubric --propose 'ER 权重 1.5→2.0'"
```

---

## 三条不可妥协的原则

1. **盲预测**：预测段写在看到任何数据之前，写完不可改
2. **升级 = 全量重打**：bump 必须校准池全量重打分 + 跨模型独立审
3. **rubric 是工作台不是博物馆**：被吸收/被推翻的观察都删掉

---

## 默认配置

| 设置 | 默认 | 何时改 |
|---|---|---|
| `RETRO_WINDOW_DAYS` | 3 | 长文/慢平台改 7 |
| `MIN_SAMPLES_FOR_BUMP` | 5 | 不要降 |
| `CROSS_MODEL_AUDIT` | true | 仅离线时 false |

---

## 看板（status 命令）

任何时候说 "状态"，会输出：
- 当前 mode / rubric 版本 / 校准样本数
- 待办（pending retros + 同向偏差警告）
- buffer 状态（颜色 + 数量）
- 候选池规模
- 健康度
- 下一步建议

---

## 文件结构（你的项目根）

```
<nature-writer-ip-project>/
├── rubric_notes.md          # 评分规则（通用语言，blind 白名单）
├── rubric-memo.md           # 升级 Memo（含实绩，blind 硬禁读）
├── script_patterns.md       # 写作 pattern 沉淀
├── WORKFLOW.md              # 本文件
├── STATUS.md                # 看板（自动维护）
├── content_pool.md          # 候选选题池
├── content_calendar.md      # 发布日历
├── .nature-state.json       # 状态文件
├── .cheat-cache/            # 本地缓存
│   ├── usage.jsonl
│   └── trends-history.jsonl
├── .cheat-hooks/            # hook 脚本
│   ├── prediction-immutability.sh
│   ├── session-start.sh
│   └── log-event.sh
├── scripts/                 # 脚本草稿
├── predictions/             # 预测日志（immutable）
└── videos/                  # 已拍视频
    └── <id>/
        ├── script.md
        └── report.md
```

---

## 卡住了？

- 看 `nature-writer-ip/SKILL.md` 的"必须拒绝的请求"段
- 跑 "状态" 看完整看板
