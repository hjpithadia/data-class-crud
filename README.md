# Project Name

This project is a HelloWorld Python-based REST API service for managing data using Firebase as the backend database. It is a template/starting point for build REST API services using Python and Firebase.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Features

- Provides CRUD (Create, Read, Update, Delete) operations for managing data in Firebase.
- Implements a RESTful API interface for easy integration with other applications.
- Utilizes FastAPI and Firebase Admin SDK for efficient development and database interaction.

## Requirements

- Python 3.7 or higher
- `pip` package manager
- Firebase account and project credentials
- Docker (optional)

## Installation

1. Clone the repository:
   git clone git@github.com:hjpithadia/data-class-crud.git

2. Navigate to the project directory:
   cd data-class-crud

3. Install the required dependencies:
   pip install -r requirements.txt

## Usage

1. Set up your Firebase project and obtain the necessary credentials.

- Create a Firebase project: [Firebase Console](https://console.firebase.google.com/)
- Generate a service account key file: [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk)

2. Create a `.env` file in the project root directory and populate it with your Firebase credentials:
   FIREBASE_API_KEY=<your-api-key>
   FIREBASE_AUTH_DOMAIN=<your-auth-domain>
   FIREBASE_PROJECT_ID=<your-project-id>
   FIREBASE_STORAGE_BUCKET=<your-storage-bucket>
   FIREBASE_MESSAGING_SENDER_ID=<your-messaging-sender-id>
   FIREBASE_APP_ID=<your-app-id>

3. Start the application:
   uvicorn main:app --host 0.0.0.0 --port 8000

4. Access the application in your browser or via API endpoints.

## API Endpoints

- **POST** `/persons`: Create a new persons entry in the Firebase database.
- **GET** `/persons/{id}`: Retrieve a specific persons entry by ID from the Firebase database.
- **PUT** `/persons/{id}`: Update an existing persons entry in the Firebase database.
- **DELETE** `/persons/{id}`: Delete a persons entry from the Firebase database.

## Deployment

To deploy the application to a cloud platform like Google Cloud Run, follow these steps:

1. Build the Docker image:
   docker build -t your-image-name .

2. Push the Docker image to a container registry (e.g., Google Container Registry).

3. Deploy the container image to Google Cloud Run or your preferred cloud platform.

4. Set the necessary environment variables (Firebase credentials) for the deployed application.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
