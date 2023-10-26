import boto3

client = boto3.client(
    service_name="sns",
    region_name="***Regiao do seu serviço***",
    aws_acess_key_id="***Sua acess_key***",
    aws_secret_acess_key="***sua secret_key***"
)

client.publish(
    PhoneNumber="+5599999999999",
    Message="Olá!"
)