from EmailService import EmailService

def lambda_handler(event, context):
    print(event)
    for record in event['Records']:
        to_email = record['body']
    
        if not to_email:
            return {
                'statusCode': 400,
                'body': 'Email address is required.'
            }
        
        try:
            EmailService.send_welcome_email(to_email)
        except Exception as e:
            print(f"Error: {e}")
            return {
                'statusCode': 500,
                'body': 'Failed to send email.'
            }
    
    return {
        'statusCode': 200,
        'body': 'Welcome emails sent successfully.'
    }
