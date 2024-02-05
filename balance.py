import smtplib
from email.mime.text import MIMEText
import csv
import os
from datetime import datetime

def process_transactions(file_path):

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        titles = next(csv_reader)      
        credit_transactions = []
        debit_transactions = []
        conteo_meses = {}
          
        for row in csv_reader:
            
            transaction = row[2].strip()
            amount = float(transaction[1:]) 
            transaction_date_str = row[1].strip() 
        
            if transaction[0] == '+':
                credit_transactions.append(amount)
            elif transaction[0] == '-':
                debit_transactions.append(amount)
            
            try:          
                fecha = datetime.strptime(transaction_date_str, '%d/%m/%Y') 
                nombre_mes = fecha.strftime('%B')
                conteo_meses[nombre_mes] = conteo_meses.get(nombre_mes, 0) + 1
            except ValueError:
                print(f'Formatting error in the date: {transaction_date_str}')    
                
    resultado = conteo_meses        

    # Calcula estadísticas
    total_credit = sum(credit_transactions)
    total_debit = sum(debit_transactions)
    average_credit = total_credit / len(credit_transactions) if credit_transactions else 0
    average_debit = total_debit / len(debit_transactions) if debit_transactions else 0
    total_balance = total_credit - total_debit

    send_email(total_balance, average_debit, average_credit, conteo_meses)
    
def send_email(total_balance, average_credit, average_debit, conteo_meses):
    # Configuración del servidor de correo
    smtp_server = 'Your server'
    smtp_port = 587
    sender_email = 'your email'
    sender_password = 'your password'
    receiver_email = 'receiving email'
 
    formatted_meses = ', '.join([f'{mes}: {conteo}' for mes, conteo in conteo_meses.items()])

    message = MIMEText( f'Total balance is: {total_balance:.2f}\n'
                        f'Average credit amount: {average_debit}\n'
                        f'Average debit amount: {average_credit}\n\n'
                        'Number of transactions in:\n' 
                        f'{formatted_meses}\n')

    message['Subject'] = 'Resumen de transacciones'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Enviar el correo electrónico
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Correo electrónico enviado exitosamente.")

if __name__ == "__main__":
    # Ruta al archivo CSV de transacciones
    file_path = 'Your CSV file'

    # Procesar transacciones y enviar resumen por correo electrónico
    process_transactions(file_path)