import pytest
from datetime import date, timedelta
import json

def create_test_task(client, title="Test Task", due_date="2024-01-05"):
    """Helper function to create a task for testing."""
    return client.post('/api/tasks',
        json={'title': title, 'due_date': due_date}
    )

class TestTaskAPI:
    """Test cases for the Task API."""

    def test_create_task_success(self, client):
        """Test successful task creation."""
        response = create_test_task(client)
        
        assert response.status_code == 201
        assert response.json['title'] == 'Test Task'
        assert response.json['completed'] == False
        assert 'id' in response.json
        assert 'created_at' in response.json

    def test_create_task_without_title(self, client):
        """Test task creation without title should fail."""
        response = client.post('/api/tasks',
            json={'due_date': '2024-01-05'}
        )
        assert response.status_code == 400

    def test_create_task_invalid_date(self, client):
        """Test task creation with invalid date format."""
        response = client.post('/api/tasks',
            json={'title': 'Test Task', 'due_date': 'invalid-date'}
        )
        assert response.status_code == 400

    def test_get_tasks_empty(self, client):
        """Test getting tasks when none exist."""
        response = client.get('/api/tasks')
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_get_tasks_with_data(self, client):
        """Test getting tasks after creating some."""
        # Create two tasks
        create_test_task(client, "Task 1")
        create_test_task(client, "Task 2")
        
        response = client.get('/api/tasks')
        assert response.status_code == 200
        assert len(response.json) == 2
        assert response.json[0]['title'] in ["Task 1", "Task 2"]

    def test_update_task_success(self, client):
        """Test successful task update."""
        # Create a task first
        create_response = create_test_task(client)
        task_id = create_response.json['id']
        
        # Update the task
        update_response = client.put(f'/api/tasks/{task_id}',
            json={
                'title': 'Updated Task',
                'completed': True
            }
        )
        assert update_response.status_code == 200
        assert update_response.json['title'] == 'Updated Task'
        assert update_response.json['completed'] == True

    def test_update_nonexistent_task(self, client):
        """Test updating a task that doesn't exist."""
        response = client.put('/api/tasks/999',
            json={'title': 'Updated Task'}
        )
        assert response.status_code == 404

    def test_delete_task_success(self, client):
        """Test successful task deletion."""
        # Create a task first
        create_response = create_test_task(client)
        task_id = create_response.json['id']
        
        # Delete the task
        delete_response = client.delete(f'/api/tasks/{task_id}')
        assert delete_response.status_code == 204
        
        # Verify task is deleted
        get_response = client.get('/api/tasks')
        assert len(get_response.json) == 0

    def test_delete_all_tasks(self, client):
        """Test deleting all tasks."""
        # Create multiple tasks
        create_test_task(client, "Task 1")
        create_test_task(client, "Task 2")
        
        # Delete all tasks
        response = client.delete('/api/tasks/clear')
        assert response.status_code == 204
        
        # Verify all tasks are deleted
        get_response = client.get('/api/tasks')
        assert len(get_response.json) == 0

    @pytest.mark.parametrize('task_data,expected_status', [
        ({'title': ''}, 400),
        ({'title': 'A' * 201}, 400),  # Assuming max length is 200
        ({'title': 'Valid Task', 'due_date': 'yesterday'}, 400),
    ])
    def test_create_task_invalid_input(self, client, task_data, expected_status):
        """Test task creation with various invalid inputs."""
        response = client.post('/api/tasks', json=task_data)
        assert response.status_code == expected_status