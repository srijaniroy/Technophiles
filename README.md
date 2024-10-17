# Technophiles

Welcome to the Technophiles Blog! This is a Django-based blogging platform designed for tech enthusiasts to explore the latest blogs on technology.


## Features

- **User Authentication**: Users can sign up and log in to their accounts.
- **Popular Posts**: The home page displays popular blog posts to keep you updated.
- **Search Blogs**: A powerful search function helps users find blog posts by keywords.
- **Dark Mode Switch**: Toggle between light and dark themes for a comfortable reading experience.
- **Read Blog Posts**: Users can read blogs to stay updated.
- **Comment and Reply**: Users can comment on blog posts and reply to existing comments.
- **Contact Us**: A contact form for users to reach out to the blog administrators for inquiries or feedback.
- **Login/Signup**: User authentication system with secure login and signup features.
- **Post Blogs**: Publish blog posts at your convenience (optional for admin users).

  
## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/srijaniroy/Technophiles.git
    cd Technophiles
    ```
    
2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/macOS
    env\Scripts\activate  # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the Blog**:
   Visit `http://127.0.0.1:8000/` in your web browser.


## Usage

- **Homepage**: Displays a selection of popular blog posts.
- **Search**: Use the search bar to find specific blog posts by title or content.
- **Commenting**: Engage with posts by adding comments or replying to existing ones.
- **Dark Mode**: Toggle between light and dark modes by clicking the dark mode switch.
- **Authentication**: Sign up to create an account or log in if you already have one.
- **Contact Us**: Send messages to the blog administrators via the contact form.


## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django