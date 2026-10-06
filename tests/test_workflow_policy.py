from pathlib import Path


def test_new_commits_do_not_cancel_existing_ci_runs() -> None:
    workflow = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "ci.yml"

    assert "cancel-in-progress: true" not in workflow.read_text(encoding="utf-8")
