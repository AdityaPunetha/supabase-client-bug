Create a file .env with the following content:
```
SUPABASE_URL =  
SUPABASE_KEY =  
```
Make sure you have relevant permissions in supabase.

Then run:
```
docker build . -t supa-dev
docker run -p 8000:8000 supa-dev
```

Go to http://localhost:8000/docs 

- Execute the auth/google endpoint and it will give you an oauth link.
- Follow that link and login with your google account.
- It will redirect you, copy the access token and refresh from the url.
- On the top right side of the page, click on the Authorize button and paste the access token and refresh token seperated by a space.
- ```access_token_here refresh_token_here```
- Then execute the protected with google endpoint and it will return "You are authorized to access this route".
- Now try stopping the application, it will get stuck.