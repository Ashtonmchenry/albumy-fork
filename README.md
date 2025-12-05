# Albumy (ML-Enhanced)

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/book/1)*, extended with two small ML-powered features:
>
> 1. **Automatic alt-text generation** for uploaded images  
> 2. **Image search by detected objects** (keywords/tags)

Demo of the original project: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

---

## 1. Installation & Setup

### 1.1. Clone the repository

```bash
git clone https://github.com/Ashtonmchenry/albumy-fork.git
cd albumy-fork
```

 ### 1.2. Create a virtual environment & install dependencies (might require python 3.8)

```bash
python -m venv .venv
# use a python 3.8 .venv incase you run into an
# error while installing requirements
py -3.8 -m venv .venv 
```
Activate environment:
```bash
# Windows PowerShell
.venv/Scripts/Activate
# macOS / Linux
source .venv/bin/activate
```
Install requirements:
```bash
pip install -r requirements.txt
```

### 1.3. Environment configuration (.flaskenv)

Rename `.flaskenv.example` to `.flaskenv`.

### 1.4. Initialize the database and fake data
```bash
flask forge
```
then run:

```bash
flask run
# -> Serving on http://127.0.0.1:5000/
```

### 1.5 Create an account

### 1.6 Confirm your email in the database using flask shell
In another terminal (with `.venv` activated), open python prompt:
```bash
flask shell
```
Then run:
```bash
from albumy.models import User
from albumy.extensions import db
```

Use the email you registered with and run:
```bash
u = User.query.filter_by(email='YOUR_EMAIL_HERE')
u # Must return an object
```
If an object is successfully returned, confirm email:
```bash
u.confirmed = True
db.session.commit()
```

Now exit:
```bash
exit()
```

## 2. Computer Vision API Setup (Azure)

1. Go to the Azure Portal and create a Computer Vision / Cognitive Services resource.
2. After the resource is created, note:
  - The Endpoint URL (e.g. `https://my-vision.cognitiveservices.azure.com`)
  - One of the Keys (Key 1 or Key 2)
3. Put these values into your local `.flaskenv`:

```bash
VISION_ENDPOINT="https://my-vision.cognitiveservices.azure.com"
VISION_KEY="your-key-here"
```

If `VISION_ENDPOINT` or `VISION_KEY` are missing, the app will still run, but the ML features fall back gracefully (no auto alt text/tags).

## 3. Example Usage

1. Click Upload and upload a new image (dog, car, etc.).
2. After upload, navigate to that photo’s detail page:
  - The description under the image should already be filled with a generated caption.
  - Inspect the image element in the browser; its `<img>` tag has `alt="generated caption"`.
  - Below the image, you should see auto-created tags (e.g. `dog`, `car`, `outdoor`).
3. Use the search bar:
  - Type one of the object words (e.g. `dog`) and submit the search.
  - On the results page, click the Tag tab.
  - The photo you just uploaded appears under that tag, even though you never manually added that keyword.

