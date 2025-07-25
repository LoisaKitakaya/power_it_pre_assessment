# Recipe and Meal Planning Frontend

## Overview

This project is a Next.js-based frontend for a Recipe and Meal Planning App, designed as part of a technical assessment. It integrates with a FastAPI backend to provide a user-friendly interface for submitting recipe queries (e.g., "What can I cook with chicken, rice, and broccoli?") and displaying structured recipe responses generated by Google's Gemini AI. The frontend uses `DaisyUI` for responsive styling, and `react-hot-toast` for notifications, ensuring a modern and interactive user experience.

### Features

- **Responsive UI**: Built with Next.js App Router and DaisyUI (Tailwind CSS) for a modern, mobile-friendly interface.
- **Query Submission**: Users can input queries in a textarea and receive structured recipe responses with ingredients, instructions, tips, and prep time displayed in ordered lists.
- **Loading States**: Visual feedback during API calls using DaisyUI’s loading spinner.
- **Error Handling**: Displays error messages (e.g., empty query, API errors) via `react-hot-toast` notifications.
- **Docker Support**: Containerized setup for consistent deployment with the FastAPI backend.

### Prerequisites

- Node.js 20+ (for local setup)
- Docker (for containerized setup)
- A running FastAPI backend (see [backend README.md](https://github.com/LoisaKitakaya/fastapi_backend/blob/main/README.md))

### Setup Instructions

#### Local Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/LoisaKitakaya/nextjs_frontend.git

   cd nextjs_frontend
   ```

2. **Install Dependencies**:

   ```bash
   npm install
   ```

3. Set Up Environment Variables:

   - Create a .env file in the project

```bash
NEXT_PUBLIC_BACKEND_URL="http://127.0.0.1:8000/api/query"
```

4. **Run the Application**:

   ```bash
   npm run dev
   ```

5. **Access the App**:

   - Open [http://localhost:3000](http://localhost:3000) in a browser.
   - Use the interactive interface to submit queries and view recipes.

#### Docker Setup

1. **Clone the Repository** (if not already done):

   ```bash
   git clone https://github.com/LoisaKitakaya/nextjs_frontend.git

   cd nextjs_frontend
   ```

2. Set Up Environment Variables:

   - Create a .env file in the project

```bash
NEXT_PUBLIC_BACKEND_URL="http://127.0.0.1:8000/api/query"
```

3. **Run with Docker Compose**:

   - From the `nextjs_frontend/` directory:

     ```bash
     docker-compose up -d --build
     ```

   - This starts both the frontend `recipe-frontend` services.

4. **Access the App**:

   - Open [http://localhost:3000](http://localhost:3000) to use the frontend.
   - Verify the backend at [http://localhost:8000/docs](http://localhost:8000/docs).

5. **Stop the Containers**:

   ```bash
   docker-compose down
   ```

#### Usage

- **Submit a Query**:

  - Enter a query in the textarea (e.g., "What can I cook with chicken, rice, and broccoli?").
  - Click "Get Recipe" to fetch a recipe from the backend.
  - Expect:
    - A recipe card with:
      - Recipe name
      - Ordered list of ingredients
      - Ordered list of instructions
      - Ordered list of tips
      - Preparation time
    - Example response:
      ```json
      {
        "answer": "Chicken Broccoli Fried Rice",
        "details": {
          "recipe_name": "Chicken Broccoli Fried Rice",
          "ingredients": [
            "200g chicken breast",
            "1 cup rice",
            "1 cup broccoli"
          ],
          "instructions": ["Cook rice", "Sauté chicken", "Stir-fry broccoli"],
          "tips": ["Add soy sauce for flavor"],
          "prep_time": "30 minutes"
        }
      }
      ```

- **Testing API Directly**:
  - Use curl to test the backend:
    ```bash
    curl -X POST "http://localhost:8000/api/query" -H "Content-Type: application/json" -d '{"query": "What can I cook with chicken, rice, and broccoli?"}'
    ```

## Project Structure

```plain
nextjs_frontend/
├── public/
├── src/
│   ├── app/
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   ├── page.tsx
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── eslint.config.mjs
├── jsconfig.json
├── next.config.mjs
├── package-lock.json
├── package.json
├── postcss.config.js
└── README.md
```
