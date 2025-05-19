from google.cloud import aiplatform

# Initialize Vertex AI with your project ID
aiplatform.init(project='thanhvo15-first-project', location='us-central1')
print("Authentication successful!")