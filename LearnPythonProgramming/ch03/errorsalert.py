def send_mail(*a):
    print(*a)


alert_system = 'console'  # other value can be 'email'
error_severity = 'critical'  # other values: 'medium' or 'low'
error_message = 'OMG! Something terrible happened!'

if alert_system == 'console':
    print(error_message)  # 1
elif alert_system == 'email':
    if error_severity == 'critical':
        send_mail('admin@example.com', error_message)  # 2
    elif error_severity == 'medium':
        send_mail('support@example.com', error_message)  # 3
    else:
        send_mail('support@example.com', error_message)  # 4
