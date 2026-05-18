# nature-writer-ip

> 自然写作IP短视频运营专家 — 基于 cheat-on-content 数据驱动方法论

## 简介

专为"带孩子走进自然、唤醒感受力"的内容创作者设计的短视频IP运营专家 Skill。

融合 cheat-on-content 的预测-校准闭环方法论，针对自然教育领域定制评分体系和工作流。

## 内容形态

- **核心**：带孩子走进自然、唤醒感受力、让文字从心流出
- **人设**：自然里的写作老师 / 感受力唤醒师 / 不教技巧只教感受
- **目标人群**：20-45岁女性（妈妈、教育工作者、关注孩子成长的女性）
- **平台**：视频号 + 抖音

## 核心能力

| 能力 | 说明 |
|------|------|
| IP定位 | 5分钟onboarding完成人设、平台、发布节奏配置 |
| 选题生成 | 基于季节流转和人群痛点生成候选选题池 |
| 脚本创作 | 温暖诗意风格，5套可直接套用的模板 |
| 盲预测 | 发布前评分预测，immutable落盘 |
| 数据复盘 | T+3对比预测vs实绩，偏差分析 |
| Rubric进化 | N≥5后自动检测系统性偏差并升级公式 |

## 安装

### 方式一：直接复制

```bash
cp -r nature-writer-ip ~/.qclaw/skills/
```

### 方式二：Git 克隆

```bash
git clone https://github.com/Patrick-mufeng/nature-writer-ip.git ~/.qclaw/skills/nature-writer-ip
```

## 使用

### 首次使用

```
用户：初始化
Agent：开始5分钟onboarding...
```

### 日常运营

```
找选题 → 写脚本 <选题> → 启动预测 → 拍摄 → 已发布 → T+3复盘
```

### 查看状态

```
用户：状态
Agent：显示buffer/待复盘/校准进度看板
```

## 文件结构

```
nature-writer-ip/
├── SKILL.md                    # 主技能文件
├── scripts/
│   └── init_project.py         # 项目初始化
├── references/
│   ├── starter-rubric.md       # 初始评分维度
│   ├── script-patterns.md      # 风格约束
│   ├── seasonal-calendar.md    # 季节选题
│   └── script-templates.md     # 脚本模板
└── assets/                     # 预留
```

## 依赖

- cheat-init
- cheat-score
- cheat-score-blind
- cheat-shoot
- cheat-bump
- cheat-status

## License

MIT
