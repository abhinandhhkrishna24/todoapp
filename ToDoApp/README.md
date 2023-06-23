Activate virtual environment 
env\Scripts\activate  


pip install -r requirements.txt


python manage.py migrate


python manage.py runserver




API Endpoints
The following API endpoints are available:

List all to-do items: GET /api/todos/
Create a new to-do item: POST /api/todos/create/
Update a to-do item: PUT /api/todos/update/<int:pk>/
Mark a to-do item as completed: PUT /api/todos/complete/<int:pk>/
Delete a to-do item: DELETE /api/todos/delete/<int:pk>/