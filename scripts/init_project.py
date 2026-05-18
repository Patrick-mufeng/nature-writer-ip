#!/usr/bin/env python3
"""
nature-writer-ip 项目初始化脚本 (Schema 1.4)

用法:
    python init_project.py <项目路径>

功能:
    1. 创建项目目录结构（含 .cheat-hooks/）
    2. 写入初始状态文件 (.nature-state.json, schema 1.4)
    3. 复制 rubric、pattern、calendar、workflow 到项目目录
    4. 创建空的内容池、日历、状态看板
    5. 创建 hook 脚本副本
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
        project / ".cheat-cache",
        project / ".cheat-hooks",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"   ✅ 创建目录: {d.relative_to(project)}")
    
    # 写入初始状态文件（schema 1.4）
    now = datetime.now().isoformat()
    state = {
        "schema_version": "1.4",
        "skill_version": "1.0.0",
        "rubric_version": "v0",
        "content_form": None,
        "typical_duration_seconds": 60,
        "target_publish_cadence_days": None,
        "rubric_form_mismatch": False,
        "benchmark_status": "pending",
        "benchmark_name": None,
        "benchmark_sample_count": 0,
        "baseline_plays": None,
        "calibration_samples": 0,
        "calibration_samples_at_last_bump": 0,
        "data_collection": None,
        "pool_status": "markdown",
        "data_layer": "markdown",
        "hooks_installed": True,
        "enabled_trend_sources": ["manual-paste"],
        "enabled_perf_adapters": [],
        "last_bump_at": None,
        "last_bump_self_audited": False,
        "last_published_at": None,
        "last_published_file": None,
        "last_retro_at": None,
        "last_trends_run_at": None,
        "last_trends_added_count": 0,
        "last_prediction_self_scored": False,
        "last_self_scored_at": None,
        "consecutive_directional_errors": [],
        "pending_retros": [],
        "shoots": [],
        "in_progress_session": None,
        "initialized_at": now,
    }
    
    state_file = project / ".nature-state.json"
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"   ✅ 创建状态文件: {state_file.name} (schema 1.4)")
    
    # 复制参考文件到项目目录
    refs = [
        ("starter-rubric.md", "rubric_notes.md"),
        ("script-patterns.md", "script_patterns.md"),
        ("seasonal-calendar.md", "seasonal_calendar.md"),
        ("script-templates.md", "script_templates.md"),
        ("workflow.template.md", "WORKFLOW.md"),
        ("status.template.md", "STATUS.md"),
        ("rubric-memo.template.md", "rubric-memo.md"),
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
    
    # 创建 benchmark
    benchmark_file = project / "benchmark.md"
    benchmark_file.write_text("# 对标账号分析\n\n> 使用 `/learn` 或说\"学对标\"导入\n\n", encoding="utf-8")
    print(f"   ✅ 创建对标分析: {benchmark_file.name}")
    
    # 创建 .gitignore
    gitignore = project / ".gitignore"
    gitignore.write_text(".cheat-cache/\n.cheat-secrets.json\n", encoding="utf-8")
    print(f"   ✅ 创建 .gitignore")
    
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
