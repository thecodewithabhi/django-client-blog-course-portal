# 🌀 Django CMS: Clients, Blogs, Courses & Tutorials

A modular and dynamic web application built with Django that allows you to manage **Clients**, **Blogs**, **Courses**, and **Tutorials** in a clean and customizable way.  
Developed by **CodewithAbhi | Abhishek Shakya**, this project is ideal for agencies, educators, developers, and businesses.

---

## 🚀 Features

- ✅ Client Management (with project status, images, URL, and description)
- 📝 Blog Management with CKEditor integration (rich text support)
- 📚 Course & Module Management with duration, description, and module content
- 🌐 Fully dynamic CRUD operations
- 📱 Responsive UI using Bootstrap
- 🔐 Admin panel for content control

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite (default, can be swapped)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Rich Text Editor**: Django CKEditor

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/thecodewithabhi/django-client-blog-course-portal.git
   cd django-client-blog-course-portal
   ```

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   python manage.py migrate
   ```

   ```bash
   python manage.py createsuperuser
   ```

   ```bash
   python manage.py runserver
   ```

   Admin panel: http://localhost:8000/admin
   Client dashboard: http://localhost:8000/clients/
   Client dashboard: http://localhost:8000/blogs/
   Client dashboard: http://localhost:8000/courses/

     project/
   
  ├── member/         # Client model & views
  
  ├── blogs/          # Blog model, CKEditor, views
  
  ├── course/         # Courses & modules
  
  ├── templates/      # Base and module-specific HTML
  
  ├── static/         # CSS/JS assets
  
  └── manage.py

  🙌 Credits
  Developed by CodewithAbhi | Abhishek Shakya
  Connect on [LinkedIn](https://www.linkedin.com/in/abhishekshakyaa/) | [Dev Community](https://dev.to/abhishekshakya)

  📄 License
  This project is open-source and available under the MIT License.
  https://github.com/thecodewithabhi/

![git-work-6](https://github.com/user-attachments/assets/cf8395db-827a-4685-85e9-e7ca99c613fb)
![git-work-5](https://github.com/user-attachments/assets/8cad425d-1f05-4eeb-8c07-d1178c1bd9b5)
![git-work-4](https://github.com/user-attachments/assets/b516e89a-85c8-4123-ba86-33fb02b2a35b)
![git-work-3](https://github.com/user-attachments/assets/28183703-23c7-46ce-9bf9-c09df3d973db)
![git-work-2](https://github.com/user-attachments/assets/f45ca799-684d-474b-bdb8-0ba66ef50da4)
![git-work-1](https://github.com/user-attachments/assets/e9dd32d6-b150-41e8-ac6c-a2a751a2f998)
![git-work](https://github.com/user-attachments/assets/5ee10488-a55a-4e1d-8f7e-9c58551837d5)

  
   
