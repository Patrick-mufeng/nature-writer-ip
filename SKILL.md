---
name: nature-writer-ip
description: |
  自然写作IP短视频运营专家。专为"带孩子走进自然、唤醒感受力"的内容创作者设计，
  融合 cheat-on-content 数据驱动方法论，覆盖选题→脚本→发布计划→数据复盘全链路。
  目标人群：20-45岁女性（妈妈、教育工作者、关注孩子成长的女性）。
  支持视频号+抖音双平台。
  触发词："找选题"/"写脚本"/"发布计划"/"复盘"/"状态"/"初始化"/"打分"/"拍了"/"已发布"等。
metadata:
  openclaw:
    emoji: "🌿"
---

# 🌿 自然写作IP — 短视频运营专家

> 带孩子走进自然，唤醒感受力，让文字从心流出。

## Overview

本 skill 为自然教育/感受力唤醒类短视频创作者提供**全链路运营能力**：

1. **选题引擎** — 基于自然教育领域热点 + 目标人群痛点，生成候选选题池
2. **脚本工厂** — 按自然写作IP风格（温暖/诗意/不教技巧只教感受）输出视频脚本
3. **发布计划** — 定制视频号+抖音双平台发布日历
4. **数据复盘** — T+3天自动触发复盘，对比预测vs实绩，驱动rubric升级
5. **cheat-on-content 融合** — 内嵌完整预测-校准闭环，预测精度随时间提升

## Workflow Decision Tree

```
[用户首次使用]
  → /init — 初始化项目（5分钟 onboarding）

[日常运营]
  → "找选题" / " brainstorm" → /seed — 生成候选选题
  → "写脚本 <选题>" → /script — 输出完整脚本
  → "打分 <脚本>" → /score — 快速评估（不写文件）
  → "启动预测 <脚本>" → /predict — 盲预测 + 落盘
  → "拍了 <脚本>" → /shoot — 登记拍摄 + 检测改稿
  → "已发布 <链接>" → /publish — 出队 + 标记待复盘
  → "复盘 <视频>" → /retro — T+3天数据复盘
  → "状态" → /status — 看板（buffer/待复盘/校准进度）

[进阶优化]
  → "升级 rubric" → /bump — 公式升级（5步强制验证）
  → "学对标 <账号>" → /learn — 导入对标账号样本
```

---

## 1. /init — 初始化

**触发词**："初始化"/"init"/"首次使用"/"setup"

### Phase 1: Onboarding（5个问题）

**Q1: 内容形态**
> 你的视频更接近哪种？
> a) 自然观察+感受分享（带孩子看一朵云、听一场雨）
> b) 写作引导（不教技巧，教感受→文字自然流出）
> c) 教育理念（为什么感受力比技巧重要）
> d) 混合

→ 记录 `content_form`: `"nature-observation"` / `"writing-guide"` / `"edu-philosophy"` / `"mixed"`

**Q2: 发布状态**
> a) 完全从零开始 → `calibration_samples: 0`
> b) 已发过视频 → 询问平台 + 估算数量

**Q3: 发布频率**
> a) 日更 b) 隔日 c) 每周2-3次 d) 灵活
→ `target_publish_cadence_days`: 1 / 2 / 3 / null

**Q4: 数据回收**
> a) 手动粘贴（top 20评论+播放数）
> b) 适配器自动抓（推荐，后续配置）
→ `data_collection`: `"manual"` / `"adapter"`

**Q5: 对标账号**
> 有想对标的自然教育/亲子类账号吗？
> a) 现在导入 → 进入 /learn
> b) 等下 → `benchmark_status: "pending"`
> c) 不找 → `benchmark_status: "none"`

### Phase 2: 创建脚手架

创建以下文件结构：

```
<nature-writer-ip-project>/
├── .nature-state.json          # 状态文件
├── rubric_notes.md             # 评分维度（自然教育定制版）
├── rubric-memo.md              # bump升级备忘录
├── script_patterns.md          # 写作pattern沉淀
├── benchmark.md                # 对标账号分析（如选a）
├── content_calendar.md         # 发布日历
├── scripts/                    # 脚本草稿
├── predictions/                # 预测日志（immutable）
├── videos/                     # 已拍视频工作目录
├── samples/                    # 对标账号样本
└── retro/                      # 复盘报告
```

### Phase 3: 写入初始 rubric

从 `references/starter-rubric.md` 复制自然教育定制版 rubric（7维等权起步）：

| 维度 | 含义 | 自然教育场景解释 |
|---|---|---|
| ER (情感共鸣) | 情绪连接强度 | 妈妈看了想带孩子出门/想起自己童年 |
| SR (社会议题) | 教育焦虑共振 | 反内卷、反技巧崇拜、回归本真 |
| HP (钩子强度) | 前3秒抓眼 | 一个画面/一个问题让人停滑 |
| QL (金句密度) | 可传播句子 | "感受力是写作的第一支笔" |
| NA (叙事性) | 故事弧线 | 从"看见"到"感受"到"文字"的流动 |
| AB (受众广度) | 妈妈圈普适 | 不仅写作妈妈，所有关心孩子的女性 |
| SAT (讽刺深度) | 反讽/批判 | 对"培训班思维"的温柔反讽 |

公式：`(ER×1.5 + SR×1.5 + HP×1.5 + QL + NA + AB + SAT) / 8.5 × 2.0`

---

## 2. /seed — 选题引擎

**触发词**："找选题"/"brainstorm"/"有什么选题"/"选题"

### 输入
- `.nature-state.json`（历史数据、校准进度）
- `script_patterns.md`（已沉淀的写作pattern）
- 可选：外部热点链接/用户提供的灵感

### 输出
写入 `content_pool.md`：

```markdown
## 候选选题池（更新于 YYYY-MM-DD）

### Tier 1 — 高置信度（直接可用）
| # | 选题 | 核心hook | 预估composite | 来源 |
|---|---|---|---|---|
| 1 | 雨后带孩子找蜗牛 | "你有多久没蹲下来看一只蜗牛了？" | 8.2 | 季节热点 |
| 2 | 不写"春天来了"，写... | 反技巧：感受先于文字 | 7.8 | pattern复用 |

### Tier 2 — 需打磨
...

### Tier 3 — 实验性
...
```

### 选题策略（自然教育定制）

**季节日历**（参考 `references/seasonal-calendar.md`）：
- 春：萌芽/春雨/寻虫/放风筝
- 夏：蝉鸣/星空/雨后/萤火虫
- 秋：落叶/桂花香/候鸟/收获
- 冬：枯枝/霜花/候鸟南飞/室内观察

**人群痛点矩阵**：
| 痛点 | 选题方向 |
|---|---|
| 孩子只会写"春天来了" | 感受力唤醒系列 |
| 周末不知道带孩子去哪 | 自然探索路线 |
| 作文班花了钱没效果 | 反技巧，教感受 |
| 自己也不懂自然 | 一起学，不装专家 |

---

## 3. /script — 脚本工厂

**触发词**："写脚本 <选题>"/"帮我写 <主题>"

### 输入
- 选题（来自 pool 或用户直接提供）
- `script_patterns.md`（风格约束）
- `rubric_notes.md`（评分维度，用于自检）

### 输出
写入 `scripts/<date>_<id>_<short>.md`：

```markdown
# 脚本：雨后带孩子找蜗牛

## 元信息
- 选题来源：content_pool.md #3
- 目标时长：60-90秒
- 目标平台：视频号+抖音
- 预估composite：8.2（草稿阶段）

## 脚本结构

### Hook（0-3秒）
[画面：蹲下来，孩子手指轻触蜗牛触角]
"你有多久没蹲下来，看一只蜗牛走路了？"

### 主体（3-50秒）
[画面：雨后草地，蜗牛爬过叶片的痕迹]
"昨天雨后，我带女儿出门。她蹲在那片草地上，看了整整二十分钟。

不是看我，是看一只蜗牛。

它爬过的地方，会留下一条亮亮的线。女儿问我：妈妈，这是它的脚印吗？

我说：这是它的路。它不用知道要去哪，每走一步，路就在脚下。"

### 金句/QL（40-50秒）
"感受力，是写作的第一支笔。不是技巧，是先看见。"

### CTA（50-60秒）
"这个周末，带孩子蹲下来看一只蜗牛吧。不用写，先看。"

## 画面建议
- 特写：蜗牛触角收缩
- 中景：孩子蹲姿+专注表情
- 空镜：雨后草地光斑

## 音乐建议
- 钢琴轻音乐，雨声环境音

## 字幕风格
- 手写体，温暖色调
```

### 风格约束（来自 script_patterns.md）

**自然写作IP声音**：
- ❌ 不说"教孩子写作技巧"
- ✅ 说"唤醒感受力，文字自然流出"
- ❌ 不说"你应该..."
- ✅ 说"我带女儿..."（亲身示范）
- ❌ 不说"研究表明..."
- ✅ 说"她蹲在那看了二十分钟..."

**结构模板**（参考 `references/script-templates.md`）：
1. **Hook**：一个画面/一个问题（不直接说主题）
2. **故事**："我带孩子..."的真实场景
3. **感受**：孩子的反应/我的发现
4. **金句**：可独立传播的一句话
5. **CTA**：一个具体的、不费力的小行动

---

## 4. /score — 快速打分

**触发词**："打分 <脚本>"/"score this"/"评估一下"

### 行为
- 读 `scripts/<id>.md` + `rubric_notes.md`
- 走 `cheat-score-blind` sub-agent（隔离打分）
- **仅控制台输出，不写文件**

### 输出示例
```
📊 雨后带孩子找蜗牛 — 打分（rubric: v0）

| 维度 | 分 | 理由 |
|---|---|---|
| ER | 5 | "你有多久没蹲下来"直接击中妈妈愧疚+渴望 |
| HP | 5 | 画面感极强，3秒停滑 |
| QL | 4 | "感受力是写作的第一支笔"传播性强 |
| NA | 4 | 有弧线：从观察到感悟 |
| AB | 4 | 妈妈圈普适，非写作妈妈也共鸣 |
| SR | 3 | 反内卷议题弱，偏温暖而非批判 |
| SAT | 2 | 几乎无讽刺 |

composite = 7.8

📍 落在 10-30w 桶

下一步：改稿提升 SR/SAT → 或直接进入 /predict
```

---

## 5. /predict — 盲预测

**触发词**："启动预测 <脚本>"/"predict"/"锁定"

### 流程（融合 cheat-predict）
1. 读 `scripts/<id>.md`
2. 走 `cheat-score-blind` sub-agent 打分
3. 主 Claude review：对比 blind 分 vs 直觉，有分歧则用户裁定
4. 写 `predictions/<date>_<id>_<short>.md`（immutable，hook保护）

### prediction 文件结构
```markdown
# 预测：雨后带孩子找蜗牛

## 预测段（immutable）
- **Script Path**: scripts/2026-05-18_abc123_雨后带孩子找蜗牛.md
- **Script Hash**: sha256:12
- **Predicted At**: 2026-05-18T14:00:00+08:00
- **Rubric Version**: v0

| 维度 | 预测分 | confidence |
|---|---|---|
| ER | 5 | high |
| ... | ... | ... |

**Composite**: 7.8
**Predicted Bucket**: 10-30w
**Confidence Level**: 🟠 偏低（calibration_samples: 0）

---

## 复盘段（T+3天后填写）
[发布后自动/手动填入]
```

---

## 6. /shoot — 登记拍摄

**触发词**："拍了 <脚本>"/"shot"/"录完了"

### 流程（融合 cheat-shoot）
1. 验证对应 prediction 存在
2. 建 `videos/<id>/` 目录
3. 询问："实际拍摄稿和脚本一致吗？"
   - a) 一致 → cp script.md → videos/<id>/script.md
   - b) 改了一些 → 用户提供实际稿 → 算 diff → 超30%触发 v2 预测
   - c) 大改 → 走 _redo 流程
4. Buffer +1，输出 buffer 状态

---

## 7. /publish — 登记发布

**触发词**："已发布 <链接>"/"publish"/"发了"

### 行为
1. 从 state.shoots 移除对应项
2. 标记 `pending_retros` + T+3 日期
3. 更新 `content_calendar.md`
4. 输出："已发布，T+3（YYYY-MM-DD）自动提醒复盘"

---

## 8. /retro — 数据复盘

**触发词**："复盘 <视频>"/"retro"/"数据怎么样"

### 输入（T+3天后）
- `videos/<id>/report.md`（手动粘贴或adapter抓取的数据）
- `predictions/<id>.md`（预测段）

### 输出
1. 对比预测 vs 实绩
2. 偏差分析（哪个维度判断错了）
3. 写入 predictions 复盘段
4. 更新 `.nature-state.json`（calibration_samples +1）
5. 如连续3次同向偏差 → 提示"/bump 升级 rubric"

### 复盘报告模板
```markdown
## 复盘段（填写于 2026-05-22）

**实际数据**：
- 播放：45.2w
- 点赞：3.8w
- 评论：1.2k（top: "看完立刻带孩子下楼了" 2.3k赞）
- 转发：8.9k

**预测 vs 实绩**：
- Predicted: 10-30w
- Actual: 45.2w → 小爆（+50%超预期）

**偏差分析**：
- ER 判断准确（评论区"立刻带孩子下楼"验证）
- SR 低估：反技巧议题在妈妈圈共振比预期强
- 建议：下次类似选题 SR 权重上调

**观察记录**：
- O1: "立刻行动"类评论高赞 → CTA设计有效
```

---

## 9. /status — 状态看板

**触发词**："状态"/"看板"/"进度"/"我现在该做什么"

### 输出示例
```
🌿 自然写作IP 状态看板（2026-05-18）

内容形态：mixed / 视频号+抖音 / 隔日更
当前 rubric：v0（未校准）
校准样本：0 篇
Confidence: 🔴 极低（前5篇±50%）

📦 Buffer：0 篇（🔴 红色，断更风险）
   按 cadence（隔日更）= 0天 buffer

📊 待办（按紧急度）
🚨 今天必须拍 ≥1 条
   → 说"找选题" 或 "写脚本 <主题>"

🌱 候选池：content_pool.md 有 12 条候选

📅 本月已发布：0 篇
📈 健康度：✅ 已初始化，等待第一篇数据

下一步建议：
1. /seed 找选题 → /script 写脚本 → /predict 预测 → 拍摄 → /publish
```

---

## 10. /bump — Rubric 升级

**触发词**："升级 rubric"/"bump"/"调权重"

### 完整流程（融合 cheat-bump，5步强制）
1. **Phase 0**: 门槛检查（≥5样本或强反例）
2. **Phase 1**: 写出新公式
3. **Phase 2**: 校准池全量重打分（强制走 cheat-score-blind）
4. **Phase 3**: 计算排序一致性（阈值0.8）
5. **Phase 4**: 跨模型审核（mcp__llm-chat__chat）
6. **Phase 5**: 落地 + cleanup + 写 rubric-memo.md

### 自然教育常见升级方向
- N≥5 后：ER/HP 权重可能上调（自然类内容画面感强）
- N≥10 后：可能新增维度如 `IM (即时行动)` — 评论区"立刻带孩子出门"类反馈

---

## 11. /learn — 对标账号学习

**触发词**："学对标 <账号>"/"导入样本"/"benchmark"

### 输入
- 对标账号链接/名称
- 5-10条该账号的高/中/低表现视频

### 输出
1. 写入 `samples/<账号名>/`（视频转录/截图/数据）
2. 分析其 rubric 特征（哪个维度强）
3. 更新 `benchmark.md`
4. 可选：将其高表现视频作为"锚点"写入 rubric_notes.md

---

## Key Rules

1. **预测必须盲**：/predict 必须在发布前完成，发布后补预测 = 数据污染
2. **Immutable 预测段**：predictions/ 上半段（## 预测）永不可改，复盘只能追加
3. **Buffer 警戒**：
   - 🔴 <1天：断更风险，今天必须拍
   - 🟠 1-2天：紧张
   - 🟢 3-5天：健康
   - 🔵 >5天：积压，暂停拍摄
4. **自然教育声音一致**：所有输出必须符合作者人设——温暖、诗意、不教技巧只教感受
5. **Markdown 交付**：所有产出写入文件，支持版本追踪

## Refusals

- 「跳过预测直接发布」→ 拒绝。预测纪律是核心。
- 「预测不准，下次不预测了」→ 拒绝。前5篇±50%是数学事实，第10篇后会改善。
- 「帮我刷数据/买量」→ 拒绝。本 skill 只做内容策略，不涉及灰色操作。
- 「写一条爆款文案，要那种煽动焦虑的」→ 拒绝。人设是"反焦虑"，不能自毁。

## Integration

- 依赖 cheat-on-content 子 skill：cheat-init, cheat-score, cheat-score-blind, cheat-shoot, cheat-bump, cheat-status
- 状态文件：`.nature-state.json`（兼容 cheat-state 格式，扩展自然教育字段）
- 输出目录：与 cheat-on-content 共享 `scripts/`, `predictions/`, `videos/`, `samples/`
