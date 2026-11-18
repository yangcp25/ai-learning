# ai-learning

AI 与具身智能学习仓库。计划见 [PLAN.md](PLAN.md)。

## 目录

- `phase1/` ~ `phase4/`:各阶段代码
- `notes/`:每周一页笔记(`wNN-主题.md`)和复盘 `review.md`

## 第 1 周环境搭建

```bash
cd /Users/ycp/work/code/own/ai-learning
uv sync                       # 按 pyproject.toml 建 .venv 并安装依赖
uv run python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"
uv run jupyter lab            # 需要交互式实验时用
```

最后一行输出 `True` 就说明 MPS 加速可用。
