<h1 id="title" align="center">Image Manager REST API</h1>

<p id="description">This application lets users store images. Based on the chosen account type (free, pro, premium), it automatically generates thumbnails and provides expiring links for sharing images securely.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Django admin panel 'http://0.0.0.0:8000/admin/'
*   Listing and creating images 'http://0.0.0.0:8000/api/v1/images'
*   Listing image thumbnails 'http://0.0.0.0:8000/api/v1/images//retrive_thumbnails/
*   Creating thumbnails 'http://0.0.0.0:8000/api/v1/images/create_thumbnails'
*   Generat expiring link 'http://0.0.0.0:8000/api/v1/expiring_links'

<h2>🛠️ Installation Steps:</h2>

<p>1. Requirements</p>

```
-docker
```

```
-docker-compose
```

```
-python 3.11
```

<p>4. Envs</p>

```
rename .env-default => .env 
```

```
fill your .env file with your info
```

<p>6. Run</p>

```
in your terminal run docker-compose up --build 
```

<p>7. Run test</p>

```
docker-compose exec backend pytest
```

<h2>🛡️ License:</h2>

This project is licensed under the Beerware licence
