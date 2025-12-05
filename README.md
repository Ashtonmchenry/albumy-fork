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

 ### 1.2. Create a virtual environment & install dependencies

```bash
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 1.3. Environment configuration (.flaskenv)

Rename `.flaskenv.example` to `.flaskenv`.

```bash
FLASK_APP=albumy
FLASK_ENV=development

# Flask secret key (any random string, do NOT commit real value)
SECRET_KEY="change-me"

# Azure Computer Vision credentials
VISION_ENDPOINT="https://<your-vision-resource>.cognitiveservices.azure.com"
VISION_KEY="<your-vision-key>"
```

### 1.4. Initialize the database and fake data
```bash
# Create tables and generate demo data (users, photos, tags, etc.)
flask forge
```
then run:

```bash
flask run
# -> Serving on http://127.0.0.1:5000/
```

Log in with one of the forged accounts or sign up as a new user.
(If you sign up, you can mark your account as confirmed in the DB using the Flask shell.)

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

1. Start the app:
```bash
flask run
# http://127.0.0.1:5000/
```
2. Log in (or sign up and confirm your account in the DB).
3. Click Upload and upload a new image (dog, car, etc.).
4. After upload, navigate to that photo’s detail page:
  - The description under the image should already be filled with a generated caption.
  - Inspect the image element in the browser; its `<img>` tag has `alt="generated caption"`.
  - Below the image, you should see auto-created tags (e.g. `dog`, `car`, `outdoor`).
5. Use the search bar:
  - Type one of the object words (e.g. `dog`) and submit the search.
  - On the results page, click the Tag tab.
  - The photo you just uploaded appears under that tag, even though you never manually added that keyword.

