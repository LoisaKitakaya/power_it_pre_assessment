# Recipe and Meal Planning App

## Overview

This project is a full-stack Recipe and Meal Planning Application developed as part of a technical assessment. It consists of a **FastAPI backend** integrated with Google’s Gemini AI (free tier) to generate structured recipe responses and a **Next.js frontend** with , DaisyUI, and `react-hot-toast` for a responsive, user-friendly interface. The application allows users to submit queries (e.g., "What can I cook with chicken, rice, and broccoli?") and receive detailed recipes with ingredients, instructions, tips, and preparation time.

The project is split into two repositories:

- **Backend**: FastAPI-based API for processing queries and generating recipes.
- **Frontend**: Next.js-based interface for submitting queries and displaying responses.

This repository serves as the entry point for the instructor, providing an overview and links to the backend and frontend repositories, which contain detailed `README.md` files and source code with all the git commits.

## Repositories

- **Backend Repository**: [fastapi_backend](https://github.com/LoisaKitakaya/fastapi_backend)
  - **README**: [README.md](https://github.com/LoisaKitakaya/fastapi_backend/blob/main/README.md)
  - Contains the FastAPI application with, Pydantic models, and Gemini AI integration.
- **Frontend Repository**: [nextjs_frontend](https://github.com/LoisaKitakaya/nextjs_frontend)
  - **README**: [README.md](https://github.com/LoisaKitakaya/nextjs_frontend/blob/main/README.md)
  - Contains the Next.js application with , DaisyUI styling, and `react-hot-toast` for notifications.

**Instructor Note**: Please review the `README.md` files in the backend and frontend repositories for detailed setup instructions, project structure, and usage examples specific to each component.

## Features

- **Backend**:

  - Health check endpoint (`GET /`) to verify API status.
  - Query endpoint (`POST /api/query`) to generate recipes using Gemini AI.
  - Pydantic validation for queries (non-empty).
  - Structured responses with `RecipeResponse` (recipe details) or `ErrorResponse` (errors).
  - CORS support for frontend integration.
  - Dockerized for consistent deployment.

- **Frontend**:
  - Responsive UI with Next.js App Router, and DaisyUI (Tailwind CSS).
  - Query submission form with loading states and error handling via `react-hot-toast`.
  - Displays recipes in a card with ordered lists for ingredients, instructions, and tips.
  - Dockerized for consistent deployment.

## Prompt Engineering

The backend integrates with Google’s Gemini AI to generate recipe responses. The prompt used in fastapi_backend/services/gemini.py is designed to ensure concise, practical, and structured JSON output tailored to the user’s query. Below is the prompt used in the get_gemini_response function:

```python
f"""You are a recipe and meal planning assistant. For the user query: "{query}",
provide a structured recipe in JSON format with the following fields:
- answer: A brief summary of the recipe (string)
- details: An object containing:
  - recipe_name: Name of the recipe (string)
  - ingredients: List of ingredients (array of strings)
  - instructions: List of cooking steps (array of strings)
  - tips: Optional list of cooking tips (array of strings)
  - prep_time: Estimated preparation time (string)
Ensure the response is concise, practical, and tailored to the query."""
```

**Purpose:**

Instructs Gemini AI to return a JSON object with a consistent structure (RecipeResponse) that matches the backend’s Pydantic models, ensuring compatibility with the frontend’s interfaces.

Example Query: "What can I cook with chicken, rice, and broccoli?"

Example Response:

```json
{
  "answer": "Chicken Broccoli Fried Rice",
  "details": {
    "recipe_name": "Chicken Broccoli Fried Rice",
    "ingredients": ["200g chicken breast", "1 cup rice", "1 cup broccoli"],
    "instructions": ["Cook rice", "Sauté chicken", "Stir-fry broccoli"],
    "tips": ["Add soy sauce for flavor"],
    "prep_time": "30 minutes"
  }
}
```

**Notes:**

The prompt uses dynamic insertion of the user’s query (`{query}`) to tailor responses.

The requirement for JSON format ensures parseability by the backend (`json.loads`).

## Prerequisites

- **Docker**: For containerized setup (recommended).
- **Node.js 20+**: For local frontend development.
- **Python 3.10+**: For local backend development.
- **Google Gemini AI API Key**: Free tier, obtained from [Google AI Studio](https://aistudio.google.com).
- **Environment Files**:
  - Backend (`fastapi_backend/.env`):
    ```
    GEMINI_API_KEY=your_api_key
    ```

## Technologies

- **Backend**:

  - FastAPI: API framework
  - Pydantic: Data validation and response modeling
  - Google Gemini AI (`gemini-2.0-flash-001`): Recipe generation
  - python-dotenv: Environment variable management
  - Uvicorn: ASGI server
  - Docker: Containerization

- **Frontend**:
  - Next.js: React framework with App Router
  - DaisyUI: Tailwind CSS component library
  - react-hot-toast: Notifications
  - Docker: Containerization
