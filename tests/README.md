# Cohen House Concierge - Test Suite

This directory contains the pytest-based test suite for the Cohen House Concierge API.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Shared fixtures and pytest configuration
├── test_main.py         # Main API endpoint tests
└── README.md            # This file
```

## Running Tests

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run All Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=app --cov-report=html
```

### Run Specific Test Categories

```bash
# Unit tests only
pytest -m unit

# Integration tests only
pytest -m integration

# End-to-end tests only
pytest -m e2e

# Fast tests (exclude slow tests)
pytest -m "not slow"
```

### Run Specific Test File

```bash
pytest tests/test_main.py
```

### Run Specific Test

```bash
pytest tests/test_main.py::TestMainEndpoints::test_get_index
```

### Run with Verbose Output

```bash
pytest -v
```

### Run and Stop at First Failure

```bash
pytest -x
```

## Test Markers

Tests are organized using pytest markers:

- `@pytest.mark.unit` - Unit tests for individual functions
- `@pytest.mark.integration` - Integration tests for API endpoints
- `@pytest.mark.e2e` - End-to-end workflow tests
- `@pytest.mark.async` - Tests using async/await
- `@pytest.mark.slow` - Long-running tests
- `@pytest.mark.external` - Tests calling external APIs (should be mocked)

## Fixtures

Common fixtures are defined in `conftest.py`:

- `client` - Synchronous TestClient for FastAPI
- `async_client` - Asynchronous AsyncClient for FastAPI
- `test_app` - FastAPI app instance
- `mock_openai_assistant` - Mocked OpenAI assistant
- `mock_whisper` - Mocked Whisper transcription
- `mock_elevenlabs` - Mocked ElevenLabs TTS
- `mock_spotify` - Mocked Spotify control
- `mock_ring` - Mocked Ring doorbell
- `sample_audio_file` - Sample audio file for testing
- `sample_face_image` - Sample base64 image for testing

## Test Coverage

Target coverage: ≥80%

View coverage report:
```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

## Writing New Tests

### Example: Testing a GET Endpoint

```python
@pytest.mark.integration
def test_my_endpoint(client):
    """Test my endpoint"""
    response = client.get("/my-endpoint")
    assert response.status_code == 200
    assert response.json()["key"] == "value"
```

### Example: Testing a POST Endpoint with Mocking

```python
@pytest.mark.integration
@patch("app.main.some_external_service")
def test_my_post_endpoint(mock_service, client):
    """Test POST endpoint with mocked external service"""
    mock_service.return_value = {"result": "success"}
    
    payload = {"data": "test"}
    response = client.post("/my-endpoint", json=payload)
    
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    mock_service.assert_called_once()
```

### Example: Testing Async Endpoint

```python
@pytest.mark.async
@pytest.mark.integration
async def test_async_endpoint(async_client):
    """Test async endpoint"""
    response = await async_client.get("/async-endpoint")
    assert response.status_code == 200
```

## Best Practices

1. **Use TestClient for FastAPI** - Don't use `requests` library for testing
2. **Mock External APIs** - Use `@patch` or `respx` to mock OpenAI, ElevenLabs, etc.
3. **Test Status Codes** - Always verify response status codes
4. **Test Response Structure** - Verify JSON response structure and content
5. **Use Fixtures** - Reuse common setup through fixtures
6. **Organize with Markers** - Use pytest markers to categorize tests
7. **Aim for High Coverage** - Target ≥80% code coverage
8. **Test Error Cases** - Test both success and failure scenarios
9. **Keep Tests Fast** - Mock slow operations (API calls, file I/O)
10. **Write Descriptive Test Names** - Use clear, descriptive test function names

## CI/CD Integration

Tests are automatically run in CI/CD pipeline on:
- Pull requests
- Commits to main branch

CI configuration checks:
- All tests must pass
- Code coverage must be ≥80%
- No linting errors

## Troubleshooting

### Import Errors

If you see import errors, ensure:
1. You're running tests from the project root
2. The `app` package is importable
3. All dependencies are installed

### Async Test Warnings

If you see warnings about async tests, ensure `pytest-asyncio` is installed:
```bash
pip install pytest-asyncio
```

### Coverage Not Working

Ensure `pytest-cov` is installed:
```bash
pip install pytest-cov
```

## Additional Resources

- [FastAPI Testing Documentation](https://fastapi.tiangolo.com/tutorial/testing/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-asyncio Documentation](https://pytest-asyncio.readthedocs.io/)
