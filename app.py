from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# In-memory task store
tasks = []
next_id = 1


@app.route("/")
def index():
    filter_by = request.args.get("filter", "all")

    if filter_by == "active":
        filtered = [t for t in tasks if not t["completed"]]
    elif filter_by == "completed":
        filtered = [t for t in tasks if t["completed"]]
    elif filter_by == "high":
        filtered = [t for t in tasks if t["priority"] == "high"]
    else:
        filter_by = "all"
        filtered = list(tasks)

    all_count    = len(tasks)
    active_count = len([t for t in tasks if not t["completed"]])
    done_count   = len([t for t in tasks if t["completed"]])
    high_count   = len([t for t in tasks if t["priority"] == "high" and not t["completed"]])
    pct          = int(done_count / all_count * 100) if all_count else 0

    return render_template(
        "index.html",
        filtered_tasks=filtered,
        filter_by=filter_by,
        all_count=all_count,
        active_count=active_count,
        done_count=done_count,
        high_count=high_count,
        pct=pct,
    )


@app.route("/add", methods=["POST"])
def add():
    global next_id
    title    = request.form.get("title", "").strip()
    priority = request.form.get("priority", "medium")
    if title and priority in ("low", "medium", "high"):
        tasks.append({"id": next_id, "title": title, "completed": False, "priority": priority})
        next_id += 1
    return redirect(url_for("index"))


@app.route("/delete", methods=["POST"])
def delete():
    try:
        task_id = int(request.form.get("task_id", 0))
    except (ValueError, TypeError):
        return redirect(url_for("index"))
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


@app.route("/complete", methods=["POST"])
def complete():
    try:
        task_id = int(request.form.get("task_id", 0))
    except (ValueError, TypeError):
        return redirect(url_for("index"))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
