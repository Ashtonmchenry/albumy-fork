# Calls a pretrained model and parse the result. Everything else below is just Flask/SQLAlchemy plumbing.


import requests
from flask import current_app

def generate_caption_and_tags(image_path):
    endpoint = current_app.config.get('VISION_ENDPOINT')
    key = current_app.config.get('VISION_KEY')
    if not endpoint or not key:
        return None, []

    url = endpoint.rstrip('/') + '/vision/v3.2/analyze?visualFeatures=Description,Tags'
    with open(image_path, 'rb') as f:
        data = f.read()
    resp = requests.post(
        url,
        headers={
            'Ocp-Apim-Subscription-Key': key,
            'Content-Type': 'application/octet-stream'
        },
        data=data,
        timeout=5
    )
    resp.raise_for_status()
    payload = resp.json()
    captions = payload.get('description', {}).get('captions') or []
    alt_text = captions[0]['text'] if captions else None
    tags = [t['name'] for t in payload.get('tags', []) if t.get('confidence', 0) >= 0.6]
    return alt_text, tags
