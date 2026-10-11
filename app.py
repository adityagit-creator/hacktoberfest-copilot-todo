import streamlit as st


st.set_page_config(page_title="To-Do List", page_icon="✅")
st.title("To-Do List")
st.write("Add tasks, keep track of what is done, and remove tasks when you no longer need them.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "next_task_id" not in st.session_state:
    st.session_state.next_task_id = 0


def add_task():
    task_text = st.session_state.new_task.strip()
    if task_text:
        st.session_state.tasks.append(
            {
                "id": st.session_state.next_task_id,
                "text": task_text,
                "completed": False,
            }
        )
        st.session_state.next_task_id += 1
        st.session_state.new_task = ""


def complete_task(task_id):
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break


def delete_task(task_id):
    st.session_state.tasks = [
        task for task in st.session_state.tasks if task["id"] != task_id
    ]


st.text_input("New task", key="new_task", on_change=add_task, placeholder="What needs to get done?")
st.button("Add task", on_click=add_task, type="primary")

pending_tasks = [task for task in st.session_state.tasks if not task["completed"]]
completed_tasks = [task for task in st.session_state.tasks if task["completed"]]

st.subheader(f"Pending ({len(pending_tasks)})")
if pending_tasks:
    for task in pending_tasks:
        task_column, complete_column, delete_column = st.columns([6, 1, 1])
        task_column.write(task["text"])
        complete_column.button(
            "Done",
            key=f"complete_{task['id']}",
            on_click=complete_task,
            args=(task["id"],),
        )
        delete_column.button(
            "Delete",
            key=f"delete_pending_{task['id']}",
            on_click=delete_task,
            args=(task["id"],),
        )
else:
    st.write("No pending tasks.")

st.subheader(f"Completed ({len(completed_tasks)})")
if completed_tasks:
    for task in completed_tasks:
        task_column, delete_column = st.columns([7, 1])
        task_column.write(f"~~{task['text']}~~")
        delete_column.button(
            "Delete",
            key=f"delete_completed_{task['id']}",
            on_click=delete_task,
            args=(task["id"],),
        )
else:
    st.write("No completed tasks yet.")