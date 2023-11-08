import base64

def Base64Encode(x):
  return base64.b64encode(x.encode()).decode()
