[![CI Lint (flake8)](https://github.com/realestKMA/openuserdata/actions/workflows/lint.yml/badge.svg)](https://github.com/realestKMA/openuserdata/actions/workflows/lint.yml)
[![CI Test (pytest)](https://github.com/realestKMA/openuserdata/actions/workflows/test.yml/badge.svg)](https://github.com/realestKMA/openuserdata/actions/workflows/test.yml)


# Open Users Data
### Hello There,

Welcome to *Open user data*. This is a part of the Openuser REST API service. Open user data provides dummy user data over [REST API](https://www.redhat.com/en/topics/api/what-is-a-rest-api). It's main purpose is to provide an API endpoint where developers can practice [CRUD](https://www.sumologic.com/glossary/crud/) operations, Authentication/Authorization, and more over REST API.

## Features
- Retrieve all users in the system. **paginated**
  > NOTE: The result is paginated with a default of 50 users returned. this can be change using the **limit/offset** url query parameters to return more or less users, depending on your use case.
- Retrieve a particular user via *username*.
- Retrieve a subset of users via one of [this]() url query parameters.
- Retrieve all users belonging to a creators app instance in the system.
- Retrieve a particular user in a creators app instance via *username*.
- Create a new user in a creators app instance. **(Creators only)**
- Authenticate a user via [*Bearer Authentication*](). uses **JWT**
- Verify a Bearer token. **JWT**
- Refresh a token. **JWT**
- Authenticate a user via [*Session Authetication*]().
- Retrieve data of an authenticated user.
- Update data of an authenticated user.
  > NOTE: User password cannot be updated via REST API, it can only be updated via your creators dashboard. 
- Delete the authenticated user from the system.


## URL Endpoints, Request Methods & Response
#
You are to replace the word *version* with the api version you wish to utilize in the url.cAs of this moment only **v1** is available.

- URL:
  - https://openuserdata.com/
- Methods & Endpoints:

  - **GET**: api/*version*/users/
    
    Retrieve all users in the system.

    Response: 200
    ```JSON
    {
        "count": int,
        "next": url|null,
        "previous": url|null,
        "results": [...]
    }
    ```

  - **GET**: api/*version*/users/*username*/

    Get a specific user by their username. The username should be a valid user username provided by you.

    Response:
    - Success: 200
     
      ```JSON
      {
        "uid": string,
        "username": string,
        "email": string|null,
        "first_name": string|null,
        "last_name": string|null,
        "other_name": string|null,
        "mugshot": url|null,
        "gender": Male|Female|Undefined,
        "dob": string|null,
        "about": string|null
      }
      ```
    - Failure(s): 404
      
      ```JSON
      {
        "detail": "Not found."
      }
      ```

  - **GET**: api/*version*/*cid*/*app_name*/users/

    Retrieve all users belonging to a particular creator's app instance. **cid** should be your creator id, **app_name** should be the app name you want to query. Make sure the app name belongs to the creator.

    Response: 
    - Success: 200

      ```JSON
      {
        "count": int,
        "next": url|null,
        "previous": url|null,
        "results": [...]
      }
      ```
    - Failure(s): 404

      ```JSON
      {
        "detail": "Not found."
      }
      ```
  - **POST**: api/*version*/*cid*/*app_name*/users/app/add/

    Create a new user in a creator's app. Please note the following while creating a new user.
    - the username and email fields should be unique per user as this fields are used to authenticate a user. If an account with the provided username or email address already exist, a 404 response with the appropriate error message will be returned.
    - A password must be provided.
    - Creators have a maximum number of user that can be created per app.

    Request Body:
    > NOTE: Only the username & email fields are required, the rest are optional.
    ```JSON
    {
        "username": string,
        "email": string|null,
        "first_name": string|null,
        "last_name": string|null,
        "other_name": string|null,
        "mugshot": string|null,
        "gender": Male|Female|Undefined,
        "dob": string|null,
        "about": string|null
    }
    ```
    Response:

    - Success: 201
      ```JSON
      {
        "cid": string,
        "app_name": string,
        "uid": string,
        "aid": uuid,
        "username": string,
        "email": string|null,
        "first_name": string|null,
        "last_name": string|null,
        "other_name": string|null,
        "mugshot": string|null,
        "gender": Male|Female|Undefined,
        "dob": string|null,
        "about": string|null
      }
      ```

    - Failure(s): 400
      ```JSON
      {
        "error": "You have reached your open users limit (x)"
      }
      ```
      ```JSON
      {
        "username": ["This username is not available"],
      }
      ```
      ```JSON
      {
        "email": ["This email address belongs to another account"],
      }
      ```
      ```JSON
      {
        "password": ["This field is required."],
      }
      ```
    
  - **GET**: api/*version*/*cid*/*app_name*/users/app/i/

    Retrieve the data of the currently authenticated user.

    Response:
    - Success: 200
      ```JSON
      {
        "cid": string,
        "app_name": string,
        "uid": string,
        "aid": uuid,
        "username": string,
        "email": string|null,
        "first_name": string|null,
        "last_name": string|null,
        "other_name": string|null,
        "mugshot": string|null,
        "gender": Male|Female|Undefined,
        "dob": string|null,
        "about": string|null
      }
      ```
    
    - Failure(s): 401
      ```JSON
      {
        "detail": "User not found",
        "code": "user_not_found"
      }
      ```

      ```JSON
      {
        "detail": "Given token not valid for any token type",
        "code": "token_not_valid",
        "messages": [
            {
                "token_class": "AccessToken",
                "token_type": "access",
                "message": "Token is invalid or expired"
            }
        ]
      }
      ```

  - **PUT**|**PATCH**: api/*version*/*cid*/*app_name*/users/app/i/update/

    Update the data of the currently authenticated user. Supports both **PUT** & **PATCH** request methods.
    > NOTE: You cannot change the password of any user account via this methods, to do that you will need to login to your creators dashboard and update the password for all users in the specified app instance. You can pass only the fields you wish to update in the request body. The fields **app_name**, **cid**, **uid**, **aid**, **app_name** are read only and should not be provided, it will be ignored if found i the request body.

    Request Body:
    ```JSON
    {
        "username": string,
        "email": string|null,
        "first_name": string|null,
        "last_name": string|null,
        "other_name": string|null,
        "mugshot": string|null,
        "gender": Male|Female|Undefined,
        "dob": string|null,
        "about": string|null
    }
    ```

    Response:
    - Success: 202

      ```JSON
      {
        "cid": string,
        "app_name": string,
        "uid": string,
        "aid": uuid,
        "username": string,
        "email": string|null,
        "first_name": string|null,
        "last_name": string|null,
        "other_name": string|null,
        "mugshot": string|null,
        "gender": Male|Female|Undefined,
        "dob": string|null,
        "about": string|null
      }
      ```
    - Failure(s): 400

      ```JSON
      {
        "gender": ["\"Value\" is not a valid choice."]
      }
      ```
      ```JSON
      {
        "username": ["This username is not available"],
      }
      ```
      ```JSON
      {
        "email": ["This email address belongs to another account"],
      }
      ```

  - **DELETE**: api/*version*/*cid*/*app_name*/users/app/i/delete/

    Delete the currently authenticated user from the system permanently.

    Response:

    - Success: 204

      ```JSON
      {
        "uid": string,
        "username": string,
        "app_name": string,
        "email": strimg,
        "detail": "Deleted successfuly"
      }
      ```

    - Failure(s): 401

      ```JSON
      {
        "detail": "User not found",
        "code": "user_not_found"
      }
      ```

      ```JSON
      {
        "detail": "Given token not valid for any token type",
        "code": "token_not_valid",
        "messages": [
            {
                "token_class": "AccessToken",
                "token_type": "access",
                "message": "Token is invalid or expired"
            }
        ]
      }
      ```
  
  
UPDATE: Setting up filter, search and order functionality on the users backend

(13-07-2022) Need to update my undergraduate project.
(20-08-2022) Back to clontinue