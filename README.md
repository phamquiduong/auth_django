<img src="src/common/static/favicon/favicon.svg" width=150>

<br>
<br>

# Information about project

| Program Language | Framework | Database |
| ---------------- | --------- | -------- |
| Python 3         | Django 5  | SQLite3  |

<br>
<br>

# Build Project
### Download and install tools
> #### Python3
> - [Official website](https://www.python.org/)
> - [Microsoft store version 3.13](https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=en-us&gl=VN&ocid=pdpshare)

<br>

### Prepair for project
> #### Create .env file
> - Copy file `.env.example` to `.env` in `root` folder
> - Config env variable for project

> #### Create Python virtual environment
> ```bash
> python -m venv .venv
> ```

> #### Active Python virtual environment
> - With Windows OS
>   ```bash
>   .\.venv\Scripts\activate
>   ```
>   - Note: If can not active you can try: Open `Powershell` with `Adminstrator role` and run this command
>     ```bash
>     Set-ExecutionPolicy Unrestricted -Force
>     ```
> - With Linux/ MacOS
>   ```bash
>   source .venv/bin/activate
>   ```

> #### Install Python packages from requirements
> ```bash
> pip install -r requirements.txt
> ```

<br>

### Run Django server
> - Change directory to `src` folder
> - Run server
>   ```
>   python manage.py runserver 0.0.0.0:80
>   ```
>   Note:
>   - `0.0.0.0` is public server to local network, if you don't want to public you can use `127.0.0.1`
>   - `80` is port of server. Default HTTP port `80`, and HTTPS is `443`

<br>
<br>

# Some Django command
>#### Create app
>```bash
> python manage.py startapp [app_name]
>```

>#### Make migrations
>```bash
> python manage.py makemigrations
>```

>#### Run migrate
>```bash
> python manage.py migrate
>```

<br>
<br>

# Thank you so much
