import boto3 # type: ignore

# Configuration
s3 = boto3.client(
    's3', 
    key="data/languages_detected/output_240p.mp4_langue.txt")  # Client S3
bucket_name = 'videocloudprojet'  # Remplacez par le nom de votre bucket
file_path = 'data/output_240p.mp4'  # Chemin du fichier local
destination_s3_path = 's3://videocloudprojet/data'  # Chemin du fichier sur S3

# Fonction pour envoyer le fichier
def upload_file_to_s3(file_path, bucket_name, destination_s3_path):
    try:
        # Envoyer le fichier
        s3.upload_file(file_path, bucket_name, destination_s3_path)
        print(f"Le fichier '{file_path}' a été envoyé avec succès sur S3 à l'emplacement '{destination_s3_path}'.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du fichier : {e}")

# Exécution
if __name__ == "__main__":
    upload_file_to_s3(file_path, bucket_name, destination_s3_path)
