# Cat GIF of the Day

This is a very simple python flask app that gives a random cat gif.

## Docker Deployment

```bash
docker build -t <YOUR NAME>/myfirstapp .
docker run -p 8888:5000 --name myfirstapp <YOUR NAME>/myfirstapp
```