# Introduction
[![Build Status](https://travis-ci.com/ahmedemad3965/TodoAPI.svg??branch=master)](https://travis-ci.com/ahmedemad3965/TodoAPI)

This is a RESTful **API** for a **Todo app**.
The **API** is designed using **Django** and **Postgres** database.
The Project is completely done and the fully documented.
The Project is **open-source** and not used commercially be any means.
The **API** is fully tested with **100% Code coverage** with automated **tests** in a separate folder.
The **docker** and **docker-compose** images configuration files are stored with in the project so that you can use it and test it from anywhere with no problems.
You can freely use, edit and learn from this project.

# Documentation

**Firstly we Create a new user profile:**

    POST www.todo.com/users/signup/
    
    {
        "account": {
            "username": "my_user_name",
            "first_name": "test",
            "last_name": "account",
            "password": "my_super_secret_password"
        }
    }

* note: 
    1. the url domain names used in this docs are NOT real and used only for demonstration.
    2. you can add another field "profile photo", but the request format will be multipart/form-data.



**For retrieving, updating or deleting your profile, you can use:**

    GET, PUT, PATCH, DELETE www.todo.com/users/{username}/


**And For Logging in you can use:**

    POST www.todo.com/users/login/

    {
        "username": "my_user_name",
        "password": "my_super_secret_password"
    }


**And similarly for logging out you use:**

    POST www.todo.com/users/logout/

* no data in the request body.


**Now we have created a user account, we can start by adding new Todo Categories and Items:**

    POST www.todo.com/users/{username}/todo-groups/
    
    {
        "title": "my first todo Category"
    }

    
* note: 
   1. every user can have many todo categories (groups), and each category can contain many todo items.
   
   2. every todo group or todo item will be identified with its sort number which defines its order on the list, it's like a primary key but unique to its own container, the sort is sent in the response, you can specify the sort number only on update not create, the sort number will be used also in ordering the items or groups in the list response.

**To Update a certain todo Category:**

    PUT www.todo.com/users/{username}/todo-groups/{group_sort}/

    {
        "sort": 1,
        "title": "my updated todo Category"
    }
    
**And likewise for deleting a todo Category:**

    DELETE www.todo.com/users/{username}/todo-groups/{group_sort}/


**After We Created a todo Category, Now we can add todo items as follows:**

    POST www.todo.com/users/{username}/todo-groups/{group_sort}/todo-items/
    
    {
        "title": "my first todo item",
        "description": "my first todo item description",
        "status": "U"
    }

* note: the status field can only hold two values U or C which means unchecked or checked, and it indicates whether that todo task is finished or not.

**To List all todo tasks the user has, we use:**

    GET www.todo.com/users/{username}/todo-items/


**To Update a certain todo item:**

    PUT, PATCH www.todo.com/users/{username}/todo-groups/{group_sort}/todo-items/{todo_sort}/

    {
        "sort": 1,
        "title": "my updated and done todo task",
        "description": "my updated and done todo task description",
        "status": "C"
    }


**And likewise for retrieving and deleting a certain todo item:**

    GET, DELETE www.todo.com/users/{username}/todo-groups/{group_sort}/todo-items/{todo_sort}/

**A User might want to add an attachment in a todo item, For this you can do:**

    POST www.todo.com/users/{username}/todo-groups/{group_sort}/todo-items/{todo_sort}/

**And if the user wants to delete the attachment, he can use:**
    
    DELETE www.todo.com/users/{username}/todo-groups/{group_sort}/todo-items/{todo_sort}/attachments/{attachment_sort}/

* note: 
    1. the uploaded file can be of any format, the file can't be any larger than 2 MB.
    2. the request body must contain a field called "file" which contains the attachment's file, the request format must be multipart/form-data.
    3. the sort field is also use with attachment as used with todo categories and items.
