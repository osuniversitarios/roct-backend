# roct-backend

## Routes

    base - http://geovanens.pythonanywhere.com/

## Auth - /auth

    POST /auth/login                          - login to the system: {"email": String, "password": String}
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.     eyJpYXQiOjE2MDQwOTE2MDIsIm5iZiI6MTYwNDA5MTYwMiwianRpIjoiYmM4MTFhNzMtN2U1Yy00M2NmLWI0ZWEtYmVmYjQ4ZGQxY2EyIiwiZXhwIjoxNjA0MDkyNTAyLCJpZGVudGl0eSI6e30sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.1XXcquwHJZ0xYOai2NC0NVPA9vMzPM2W4MYct-CdM50"
    }

## Users - /users

    POST /users                                - create new user: {"name": String, "email": String, "cpf": String, "phone": String, "isSalesman": Boolean, "password": String, "avatar": String}
    GET  /users/<id>                           - Get the user that has the id
    PUT  /users/<id>                           - Update the user that has the id
    PUT / users/<id>/changePassword            - Change user password: {"newPassword": String, "oldPassword": String}

## Announcements - /announcements

    GET  /check                                 - check if announcements endpoints live
    POST  /announcements                        - get list of all announcements available -  need body with page(int) and per_page(int)
    GET  /announcements/<uuid>                  - get one announcement, need uiid announcement
    GET  /announcements/search/                 - takes a list of announcement filter by body -  need body with game(string: game name), server(string: server name), item(string: substring for search item by name), type_(options {item, account, gold}),  page(int) and per_page(int)
    POST /announcements/add                     - add new announcement - need body with  image(url), name(string), description(string), price(float), type_({item, account, gold}), salesman_uuid(int)
    GET /announcements/status                   - list status announcements in database
    GET /announcements/types                    - list types announcements in database
    GET /announcements/games                    - list games announcements in database
    GET /announcements/servers                  - list servers announcements in database
    GET /announcements/salesman/<salesman_uuid> - get all announcements wiht salesman_uuid - need body with page(int) and per_page(int)

## Announcements - /purchases
    
    POST /purchases/add                         - body need announcement_uuid, type_card, number_card, cvv, cpf_owner_card, validity_card, name_owner_card, salesman_uuid, buyer_uuid, nick_game
    POST /purchases/update_status               - need body with page(int), per_page(int) and purchase_id(id)(int)
    POST /purchases/sales                       - need body with page(int), per_page(int) and salesman_uuid(id)(int)
    POST /purchases/purchases                   - need body with page(int), per_page(int) and buyer_id(id)(int)
    PUT /purchases/<uuid>/confirmDelivery       - confirm that the item has been delivered
