# Учебный проект по Проектированию IT-инфраструктуры для интеллектуальных программных систем

# Исполнитель
Студент:  **Исмагилов Айназ**

Группа:   **РИС-24-1м**

# Микросервисное решение для поиска пути c использованием алгоритма A* , предназначенное для интеграции в систему управления мобильными-роботами в рамках роботизированного склада.

Сервис реализован с использованием:
- Python 3.11
- FastAPI
- Docker
- Алгоритм A*

# Сборка и запуск контейнера
docker-compose up --build

Сервис принимает POST-запрос с телом:

{

  "start": [0, 0],
  
  "goal": [2, 2],
  
  "grid": [
  
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
    
  ]
  
}


Клиент получает ответ:
{
  "path": [[0,0],[0,1],[0,2],[1,2],[2,2]]
}
