import boto3
import time
from random import uniform
import json

cliente = boto3.client('kinesis',aws_access_key_id='*****',aws_secret_access_key='*******', region_name='sa-east-1')

while True:

   power_factor = round(uniform(0.7,0.9),2)
   temp_battery = round(uniform(20.00,23.00),2)
   hydraulic_pressure = round(uniform(70.00,76.00),2)

   dados = {'power_factor' : power_factor, 'temp_battery' : temp_battery, 'hydraulic_pressure' : hydraulic_pressure}

   resposta = cliente.put_record(
           StreamName='stream1',
           Data= json.dumps(dados),
           PartitionKey='02'
       )

   print(resposta)
   
   time.sleep(10)