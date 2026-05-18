#!/usr/bin/env python3
"""
nature-writer-ip 项目初始化脚本

用法:
    python init_project.py <项目路径>

功能:
    1. 创建项目目录结构
    2. 写入初始状态文件 (.nature-state.json)
    3. 复制 rubric、pattern、calendar 到项目目录
    4. 创建空的内容池和日历文件
"""

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path


def init_project(project_path: str, skill_dir: Path = None):
    """初始化自然写作IP项目"""
    
    project = Path(project_path).resolve()
    
    # 如果 skill_dir 未提供，尝试推断
    if skill_dir is None:
        # 脚本在 skill/scripts/ 下，skill_dir 是上级目录
        skill_dir = Path(__file__).parent.parent
    
    print(f"🌿 初始化自然写作IP项目: {project}")
    print(f"   Skill 目录: {skill_dir}")
    
    # 创建目录结构
    dirs = [
        project / "scripts",
        project / "predictions",
        project / "videos",
        project / "samples",
        project / "retro",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"   ✅ 创建目录: {d.relative_to(project)}")
    
    # 写入初始状态文件
    state = {
        "project_name": project.name,
        "created_at": datetime.now().isoformat(),
        "content_form": None,  # 待 onboarding 填写
        "platforms": ["视频号", "抖音"],
        "target_publish_cadence_days": None,  # 待 onboarding 填写
        "data_collection": None,  # 待 onboarding 填写
        "benchmark_status": "pending",
        "rubric_version": "v0",
        "calibration_samples": 0,
        "buffer": 0,
        "pending_retros": [],
        "last_action": None,
        "last_action_at": None,
    }
    
    state_file = project / ".nature-state.json"
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"   ✅ 创建状态文件: {state_file.name}")
    
    # 复制参考文件到项目目录
    refs = [
        ("starter-rubric.md", "rubric_notes.md"),
        ("script-patterns.md", "script_patterns.md"),
        ("seasonal-calendar.md", "seasonal_calendar.md"),
        ("script-templates.md", "script_templates.md"),
    ]
    
    ref_dir = skill_dir / "references"
    for src_name, dst_name in refs:
        src = ref_dir / src_name
        dst = project / dst_name
        if src.exists():
            shutil.copy2(src, dst)
            print(f"   ✅ 复制参考: {dst_name}")
        else:
            print(f"   ⚠️  未找到: {src_name}")
    
    # 创建空的内容池
    pool_file = project / "content_pool.md"
    pool_file.write_text("# 候选选题池\n\n> 使用 `/seed` 或说\"找选题\"生成内容\n\n", encoding="utf-8")
    print(f"   ✅ 创建内容池: {pool_file.name}")
    
    # 创建空的日历
    calendar_file = project / "content_calendar.md"
    calendar_file.write_text("# 发布日历\n\n> 使用 `/publish` 或说\"发布计划\"更新\n\n", encoding="utf-8")
    print(f"   ✅ 创建日历: {calendar_file.name}")
    
    # 创建 rubric-memo
    memo_file = project / "rubric-memo.md"
    memo_file.write_text("# Rubric 升级备忘录\n\n", encoding="utf-8")
    print(f"   ✅ 创建备忘录: {memo_file.name}")
    
    # 创建 benchmark
    benchmark_file = project / "benchmark.md"
    benchmark_file.write_text("# 对标账号分析\n\n> 使用 `/learn` 或说\"学对标\"导入\n\n", encoding="utf-8")
    print(f"   ✅ 创建对标分析: {benchmark_file.name}")
    
    print(f"\n✅ 项目初始化完成!")
    print(f"\n下一步:")
    print(f"   1. 运行 onboarding: 回答5个问题完成配置")
    print(f"   2. 说\"找选题\"开始生成内容")
    print(f"   3. 说\"状态\"查看看板")
    
    return project


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python init_project.py <项目路径>")
        print("示例: python init_project.py ./my-nature-ip")
        sys.exit(1)
    
    init_project(sys.argv[1])
