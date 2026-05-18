# [作品标题] — 预测日志

> **本模板由 `/predict` 自动填充**。
> 所有预测都用统一格式（7 组件 + 复盘段）。
> 模板里的示例数据为占位值。

---

**Article ID**: `<12 位 hash>`
**Title**: `<完整标题>`
**Rubric Version**: **`<v0/v1/v2/...>`**
**预测时间**: `<YYYY-MM-DD>`
**Script Path**: `scripts/<YYYY-MM-DD>_<id>_<short>.md`
**Script Hash**: `sha256:<12 位>`
**Target Duration (s)**: `<state.typical_duration_seconds>`
**Actual Script Length**: `<字数>`
**Calibration Samples (at predict time)**: `<state.calibration_samples>`
**Confidence**: `<emoji + 标签>`
**Scored By**: `claude` | `claude+user_override`
**User Override**: `<如有覆盖，列出字段+原值/新值>` | `none`
**预测时数据状态**: **blind**
**BlindScored By**: `cheat-score-blind`
**BlindScore Disagreement**: `<所有维度 delta>`

---

## 输入快照

**分数 (vN)**: `<dim1=X / dim2=X / ...>` → composite=**`<X.XX>`**

**用户改写要点 vs Claude 草稿**（如有）:
- **开头**：[user 砍掉了什么 / 加了什么]
- **砍掉**：[具体段落]
- **保留**：[关键金句]
- **节奏**：比草稿 [紧/松] 约 N%

---

## 预测

> ⚠️ **本段 immutable**——hook 拦截对本段的 Edit。
> 写完不可改。重做请创建 `<本文件名>_redo.md`。

**Bucket**: `<X-Yw>`

**内心概率分布**:
- `<5w` → X%
- `5-30w` → X%
- **`<headline bucket>` → X%**（中枢 ~Xw）
- `>100w` → X%
- `>150w` → X%

> 加起来必须 100%。

**一句话 reason**:
> [核心驱动因素 + 最强反例约束 + 中枢预测]

---

## 推理因素

| 因素 | 方向 | 置信度 | 说明 |
|---|---|---|---|
| `<dim or feature>` | 强+/中+/弱?/强- | 高/中/低 | [≤30字理由] |

---

## 锚点对比

| 对照样本 | composite | 实绩 | 异同 |
|---|---|---|---|
| `<样本名>` | `<X.XX>` | `<Yw>` | [关键差异维度] |

> 校准池不够时：写"校准池只有 N 个样本，无 composite 邻近样本。**锚点对比 N/A**"

---

## 反事实场景（复盘用）

**如果爆 `>X w`**（X% 预期）:
- [验证什么假设]
- [推翻什么假设]

**如果落在 `headline bucket`**（X% 预期）:
- [基准线验证什么]

**如果跌到 `<X w`**（X% 预期）:
- [推翻什么核心判断]

---

## 关键校准假设

[把这次预测当成一次实验，明确写下"如果 X 发生，证明 Y"]

---

## 复盘

> ⚠️ **以下段落由 `/retro` 在 T+3 天后追加**。
> hook 允许追加本段；不允许改预测段任何字符。

（待填——T+3 天后跑 `/retro <对应 video folder>`）
