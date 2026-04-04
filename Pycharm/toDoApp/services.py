
from

todos:List[Todo] = []


async def create_todo(todo:TodoCreate):
    new_id =len(todos)+1
    new_todo = Todo(
        todo_id=new_id,
        title = todo.title,
        description=todo.description,
        )
    todos.append(new_todo)
    return new_todo
