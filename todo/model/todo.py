class Todo:
    def __init__(self, code_id, title, description):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return self.code_id - self.title


class TodoBook:
    def __init__(self):
        self.todos = {}

    def add_todo(self, title: str, description: str):
        generar_id: int = len(self.todos) + 1
        objeto_todo = Todo(generar_id, title, description)
        self.todos[generar_id] = objeto_todo
        return generar_id

    def pending_todos(self):
        pendientes: list = [todos for todos in self.todos.values() if not todos.completed]
        return pendientes

    def completed_todos(self):
        completados: list = [Todo for todos in self.todos.values() if todos.completed]
        return completados

    def tags_todo_count(self):
        tag_count = {}
        for todos in self.todos.values():
            for tag in todos.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count


if __name__ == "__main__":
    por_hacer = TodoBook()
    hacer1 = por_hacer.add_todo("Cosas por realizar el lunes", "Estudiar para algebra lineal.")
    por_hacer.todos[hacer1].add_tag("Estudiar")

    tag_count = por_hacer.tags_todo_count()
    print(tag_count)

    tarea = por_hacer.todos[hacer1]
    titulo = tarea.title
    descripcion = tarea.description
    print(titulo)
    print(descripcion)