import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        # Function to remove a task
        def remove_task(e):
            task_view.controls.remove(task_container)
            view.update()

        # Create a new task container with a checkbox and a delete button
        task_container = ft.Row(
            controls=[
                ft.Checkbox(label=new_task.value),
                ft.IconButton(icon=ft.icons.DELETE, on_click=remove_task),
            ]
        )
        task_view.controls.append(task_container)
        new_task.value = ""
        view.update()

    new_task = ft.TextField(hint_text="What's needs to be done?")
    task_view = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
                ],
            ),
            task_view,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)
