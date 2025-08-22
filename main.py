from todo import TodoList

def main():
    todo = TodoList()
    todo.load_from_json('tasks.json')

    while True:
        print("\n--- TO DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Edit Task")
        print("4. Remove task")
        print("5. Mark task as complete")
        print("6. Save tasks")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            todo.display_tasks()

        elif choice == '2':
            title = input("Task Title: ").strip()
            if not title:
                print("Task title cannot be empty!")
                continue
            due_date = input("Due date (YYYY-MM-DD, optional): ").strip()
            priority = input("Priority (Low/Normal/High): ").strip()
            
            valid_priorities = ['Low', 'Normal', 'High']
            if priority and priority not in valid_priorities:
                print(f"Invalid priority. Using 'Normal'. Valid options: {', '.join(valid_priorities)}")
                priority = 'Normal'
            
            # Fixed method name - should be add_task, not add_tasks
            todo.add_task(title, due_date or None, priority or 'Normal')
            print("Task added.")

        elif choice == '3':
            todo.display_tasks()
            if not todo.tasks:
                continue
            
            index_str = input("Enter task number to edit: ").strip()
            
            # Check if input is a valid number
            if not index_str.isdigit():
                print("Please enter a valid number.")
                continue
            
            index_num = int(index_str)
            
            # Check if number is in valid range
            if not (1 <= index_num <= len(todo.tasks)):
                print("Invalid task number.")
                continue
            
            try:

                index = index_num - 1
                print("Leave input blank if you don't want to change anything")
                
                new_title = input("New title: ").strip() or None
                new_due_date = input("New due date (YYYY-MM-DD): ").strip() or None
                new_priority = input("New priority (Low/Normal/High): ").strip() or None
                
                # Validate new priority if provided
                valid_priorities = ['Low', 'Normal', 'High']
                if new_priority and new_priority not in valid_priorities:
                    print(f"Invalid priority. Valid options: {', '.join(valid_priorities)}")
                    new_priority = None
                
                # Call the edit_task method
                todo.edit_task(index, new_title, new_due_date, new_priority)
                print("Task updated.")
                
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == '4':
            todo.display_tasks()
            if not todo.tasks: 
                continue
            
            idx_str = input("Enter task number to remove: ").strip()
            
            if not idx_str.isdigit():
                print("Please enter a valid number.")
                continue
            
            idx_num = int(idx_str)
            
            if not (1 <= idx_num <= len(todo.tasks)):
                print("Invalid task number.")
                continue
            
            todo.remove_task(idx_num - 1)
            print("Task removed.")

        elif choice == '5':
            todo.display_tasks()
            if not todo.tasks:  
                continue
            
            idx_str = input("Enter task number to mark as complete: ").strip()
            
            if not idx_str.isdigit():
                print("Please enter a valid number.")
                continue
            
            idx_num = int(idx_str)
            
            if not (1 <= idx_num <= len(todo.tasks)):
                print("Invalid task number.")
                continue
            
            todo.mark_task_complete(idx_num - 1)
            print("Task marked as complete.")

        elif choice == '6':
            todo.save_to_json('tasks.json')
            print("Tasks saved.")

        elif choice == '7':
            todo.save_to_json('tasks.json')
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()